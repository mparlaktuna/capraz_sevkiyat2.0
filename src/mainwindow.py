import pickle
from random import uniform
from windows.main_window import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from src.data_store import DataStore
from src.data_writer import gams_writer
from src.solver_data import SolverData
from src.solver import Solver
from models.data_set_model import DataSetModel
from models.good_table_model import GoodTableModel
from models.time_table_model import TimeTableModel
from src.sequence_solver import SequenceSolver
from src.enter_sequence import EnterSequenceWidget
from src.sequence import Sequence
from windows.simulation_truck import Ui_simulation_truck


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.data = DataStore()
        self.solver_data = SolverData()
        self.solver = Solver(self.data, self.solver_data)
        self.update_data_table()
        self.setup_data()
        self.value_connections()
        self.connections()
        self.results = {}
        self.combobox_coming_sequence = []
        self.combobox_going_sequence = []
        self.statusBar().showMessage('Ready')
        self.load_generated_data()

        self.showing_result = []
        self.result_times = {}
        self.function_type = "normal"
        self.solution_name = ""
        self.solution_number = 0
        self.sequence_solver = SequenceSolver()
        self.solution_results = dict()
        self.enter_sequence_widget = EnterSequenceWidget(self.data)
        self.current_sequence = Sequence()
        self.load_data()


    def setup_data(self):
        self.data_set_model = DataSetModel(self.data)
        self.datasettable.setModel(self.data_set_model)
        self.inbound_table_model = GoodTableModel(self.data.number_of_inbound_trucks, self.data.number_of_goods, self.data.inbound_goods, 'inbound')
        self.inbound_good_table.setModel(self.inbound_table_model)
        self.outbound_table_model = GoodTableModel(self.data.number_of_outbound_trucks, self.data.number_of_goods, self.data.outbound_goods, 'outbound')
        self.outbound_good_table.setModel(self.outbound_table_model)
        self.compound_coming_table_model = GoodTableModel(self.data.number_of_compound_trucks, self.data.number_of_goods, self.data.compound_coming_goods, 'compound_coming')
        self.compound_coming_good_table.setModel(self.compound_coming_table_model)
        self.compound_going_table_model = GoodTableModel(self.data.number_of_compound_trucks, self.data.number_of_goods, self.data.compound_going_goods, 'compound_going')
        self.compound_going_good_table.setModel(self.compound_going_table_model)
        self.numberOfIterationsLineEdit.setText(str(self.solver_data.number_of_iterations))
        self.tempereature_line_edit.setText(str(self.solver_data.annealing_temperature))
        self.decav_factor_line_edit.setText(str(self.solver_data.annealing_decay_factor))
        self.number_of_tabu_neighbours_line_edit.setText(str(self.solver_data.tabu_number_of_neighbors))
        self.number_of_tabu_line_edit.setText(str(self.solver_data.tabu_number_of_tabu))
        self.data_set_spin_box.setValue(self.solver_data.data_set_number + 1)

    def value_connections(self):
        self.numberOfDataSetsSpinBox.valueChanged.connect(self.set_data_set_table)
        self.loadingTumeLineEdit.textChanged.connect(self.data.set_loading_time)
        self.unloading_time_edit.textChanged.connect(self.data.set_unloading_time)
        self.truckChangeoverTimeLineEdit.textChanged.connect(self.data.set_changeover_time)
        self.effectOfTheArrivalTimesOnMakespanLineEdit.textChanged.connect(self.data.set_makespan_factor)
        self.truckTransferTimeLineEdit.textChanged.connect(self.data.set_truck_transfer_time)
        self.inboundArrivalTimeLineEdit.textChanged.connect(self.data.set_inbound_arrival_time)
        self.outboundArrivalTimeLineEdit.textChanged.connect(self.data.set_outbound_arrival_time)
        self.goodTransferTimeLineEdit.textChanged.connect(self.data.set_good_transfer_time)
        self.numberOfIterationsLineEdit.textChanged.connect(self.set_number_of_iterations)
        self.solverComboBox.currentTextChanged.connect(self.set_solver_algorithm)
        self.tempereature_line_edit.textChanged.connect(self.set_annealing_temperature)
        self.decav_factor_line_edit.textChanged.connect(self.set_annealing_decay)
        self.number_of_tabu_neighbours_line_edit.textChanged.connect(self.set_tabu_neighbor_number)
        self.number_of_tabu_line_edit.textChanged.connect(self.set_tabu_number_tabu)
        self.data_set_spin_box.valueChanged.connect(self.set_data_set_number)

    def set_solver_algorithm(self, value):
        if value:
            self.solver_data.algorithm_name = str(value)

    def set_data_set_number(self, value):
        if value:
            self.solver_data.data_set_number = int(value)

    def set_annealing_temperature(self, value):
        if value:
            self.solver_data.annealing_temperature = float(value)

    def set_annealing_decay(self, value):
        if value:
            self.solver_data.annealing_decay_factor = float(value)

    def set_tabu_neighbor_number(self, value):
        if value:
            self.solver_data.tabu_number_of_neighbors = float(value)

    def set_tabu_number_tabu(self, value):
        if value:
            self.solver_data.tabu_number_of_tabu = float(value)

    def set_data_set_table(self):
        self.data.number_of_data_sets = self.numberOfDataSetsSpinBox.value()
        if self.numberOfDataSetsSpinBox.value() > len(self.data_set_model.data):
            self.data_set_model.insertRows(len(self.data_set_model.data), self.numberOfDataSetsSpinBox.value())
        elif self.numberOfDataSetsSpinBox.value() < len(self.data_set_model.data):
            self.data_set_model.removeRows(len(self.data_set_model.data), self.numberOfDataSetsSpinBox.value())

    def update_number_of_goods(self, amount):
        self.inbound_table_model.change_good_number(amount)
        self.outbound_table_model.change_good_number(amount)
        self.compound_coming_table_model.change_good_number(amount)
        self.compound_going_table_model.change_good_number(amount)
        self.data.number_of_goods = amount

    def set_inbound_truck_number(self, value):
        self.inbound_table_model.truck_number(value)
        self.data.number_of_inbound_trucks = value
        self.data.update_truck_numbers()

    def set_outbound_truck_number(self, value):
        self.outbound_table_model.truck_number(value)
        self.data.number_of_outbound_trucks = value
        self.data.update_truck_numbers()

    def set_compound_truck_number(self, value):
        self.compound_coming_table_model.truck_number(value)
        self.compound_going_table_model.truck_number(value)
        self.data.number_of_compound_trucks = value
        self.data.update_truck_numbers()

    def set_receiving_door_number(self, value):
        self.data.set_receiving_door_number(value)

    def set_shipping_door_number(self, value):
        self.data.set_shipping_door_number(value)

    def set_number_of_iterations(self, value):
        self.solver_data.number_of_iterations = value

    def update_data_table(self):
        """
        update table values
        :return:
        """
        self.loadingTumeLineEdit.setText(str(self.data.loading_time))
        try:
            self.unloading_time_edit.setText(str(self.data.unloading_time))
        except:
            self.unloading_time_edit.setText(str(0))
            self.data.unloading_time = 0
        self.truckChangeoverTimeLineEdit.setText(str(self.data.changeover_time))
        self.effectOfTheArrivalTimesOnMakespanLineEdit.setText(str(self.data.makespan_factor))
        self.truckTransferTimeLineEdit.setText(str(self.data.truck_transfer_time))
        self.inboundArrivalTimeLineEdit.setText(str(self.data.inbound_arrival_time))
        self.outboundArrivalTimeLineEdit.setText(str(self.data.outbound_arrival_time))
        self.goodTransferTimeLineEdit.setText(str(self.data.good_transfer_time))
        self.numberOfInboundTrucksSpinBox.setValue(self.data.number_of_inbound_trucks)
        self.numberOfOutboundTrucksSpinBox.setValue(self.data.number_of_outbound_trucks)
        self.numberOfCompoundTrucksSpinBox.setValue(self.data.number_of_compound_trucks)
        self.numberOfReceivingDoorsSpinBox.setValue(self.data.number_of_receiving_doors)
        self.numberOfShippingDoorsSpinBox.setValue(self.data.number_of_shipping_doors)
        self.numberOfGoodsSpinBox.setValue(self.data.number_of_goods)
        self.numberOfDataSetsSpinBox.setValue(self.data.number_of_data_sets)

    def connections(self):
        """
        create connections from buttons to functions
        :return:
        """
        self.numberOfInboundTrucksSpinBox.valueChanged.connect(self.set_inbound_truck_number)
        self.numberOfOutboundTrucksSpinBox.valueChanged.connect(self.set_outbound_truck_number)
        self.numberOfCompoundTrucksSpinBox.valueChanged.connect(self.set_compound_truck_number)
        self.numberOfCompoundTrucksSpinBox.valueChanged.connect(self.set_compound_truck_number)
        self.numberOfShippingDoorsSpinBox.valueChanged.connect(self.set_shipping_door_number)
        self.numberOfReceivingDoorsSpinBox.valueChanged.connect(self.set_receiving_door_number)
        self.numberOfGoodsSpinBox.valueChanged.connect(self.update_number_of_goods)

        self.print_gams.clicked.connect(self.gams_output)

        self.actionNew_Data.triggered.connect(self.new_data)
        self.actionSave_Data.triggered.connect(self.save_data)
        self.actionLoad_Data.triggered.connect(self.load_data)

        self.generate_times_button.clicked.connect(self.generate_times)
        self.generate_new_boundaries_button.clicked.connect(self.new_generate_times)
        self.solve_data_set_button.clicked.connect(self.solve_data_set)
        self.simulationStartButton.clicked.connect(self.simulation_start)
        self.enter_sequence_button.clicked.connect(self.enter_sequence)
        self.simulationStepForwardButton.clicked.connect(self.simulation_forward)

    def solve_data_set(self):
        pass
        #solve depending on algorithms

    def simulation_start(self):
        pass
        self.solution_name = "simulation_" + self.solver_data.function_type + "_" + str(self.solution_number)
        self.sequence_solver.set_data(self.solver_data, self.data)
        self.current_sequence.print_sequence()
        self.sequence_solver.set_sequence(self.current_sequence)
        self.simulation_set_tables()
        self.simulation_set_trucks()
        self.simulation_add_spacers()
        print(self.sequence_solver.model.time_list)

    def simulation_forward(self):
        print("Simulation Forward")
        self.sequence_solver.step_forward()
        

    def simulation_set_tables(self):
        self.simulation_clear_layouts()
        self.simulationComingTruckList = QVBoxLayout()
        self.simulationReceivingDoorsList = QVBoxLayout()
        self.simulationStation = QVBoxLayout()
        self.simulationCompoundTruckTransferList = QVBoxLayout()
        self.simulationShippingDoorsList = QVBoxLayout()
        self.simulationFinishedList = QVBoxLayout()
        self.simulation_table_list = [self.simulationComingTruckList, self.simulationReceivingDoorsList, self.simulationCompoundTruckTransferList, self.simulationStation, self.simulationShippingDoorsList, self.simulationFinishedList]

        self.simulationGrid.addLayout(self.simulationComingTruckList, 0, 0, 2, 1)
        self.simulationGrid.addLayout(self.simulationReceivingDoorsList, 0, 1, 2, 1)
        self.simulationGrid.addLayout(self.simulationCompoundTruckTransferList, 0, 2, 1, 1)
        self.simulationGrid.addLayout(self.simulationStation, 1, 2, 1, 1)
        self.simulationGrid.addLayout(self.simulationShippingDoorsList, 0, 3, 2, 1)
        self.simulationGrid.addLayout(self.simulationFinishedList, 0, 4, 2, 1)
        title_labels = ["Coming Trucks", "Receiving Doors", "Compound Trucks Transfer List", "Station", "Shipping Doors", "Finished"]

        for i, table_list in enumerate(self.simulation_table_list):
            title = QLabel()
            title.setText(title_labels[i])
            table_list.addWidget(title)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)

            if isinstance(item, QWidgetItem):

                item.widget().close()

            elif isinstance(item, QSpacerItem):
                pass
            else:
                self.clearLayout(item.layout())

            # remove the item from layout
            layout.removeItem(item)

    def simulation_clear_layouts(self):
        try:
            for table_list in self.simulation_table_list:
                self.clear_layout(table_list)
        except:
            print("not cleared")
            pass

    def simulation_add_spacers(self):
        for table_list in self.simulation_table_list:
            spacer = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
            table_list.insertSpacerItem(table_list.count(), spacer)

    def simulation_set_trucks(self):
        for truck in self.sequence_solver.model.all_trucks.values():
            new_truck_widget = QWidget()
            new_truck_element = Ui_simulation_truck()
            new_truck_element.setupUi(new_truck_widget)
            new_truck_element.truckNameLabel.setText(truck.element_name)
            new_truck_element.show_goods_button.clicked.connect(truck.show_goods)
            new_truck_element.show_times_button.clicked.connect(truck.show_times)
            self.simulationComingTruckList.addWidget(new_truck_widget)

    def load_data(self):
        """
        loads prev saved data
        :return:
        """
        # for fast loading data disable after finished and uncomment following
        file_name = "/home/mustafa/Downloads/test202"
        # file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        try:
            self.data = pickle.load(open(file_name, 'rb'))
        except Exception as e:
            pass
        #self.graphicsView.data = self.data
        self.solver.data = self.data
        self.setup_data()
        self.update_data_table()
        self.load_generated_data()
        self.value_connections()

    def save_data(self):
        """
        saves current data
        :return:
        """
        #self.graphicsView.data = self.data
        self.setup_data()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save file', '/home')
        try:
            pickle.dump(self.data,  open(file_name, 'wb'))
        except Exception as e:
            pass

    def enter_sequence(self):
        self.current_sequence = Sequence(self.data)
        self.enter_sequence_widget = EnterSequenceWidget(self.data, self.current_sequence)
        self.enter_sequence_widget.show()

    def gams_output(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save file', '/home')

        gams_writer(file_name, self.data_set_spin_box.value() - 1, self.data)

    def new_data(self):
        self.data = DataStore()
        self.update_data_table()
        self.value_connections()
        self.setup_data()

    def generate_times(self):
        self.data.arrival_times = []
        self.data.lower_boundaries = []
        self.data.upper_boundaries = []
        for k, data_set in enumerate(self.data.data_sets):
            self.data.arrival_times.append({})
            self.data.lower_boundaries.append({})
            self.data.upper_boundaries.append({})

            self.data.calculate_truck_related_data()
            for i in range(self.data.number_of_inbound_trucks):
                name = 'inbound' + str(i)
                two_gdj = self.calculate_2dgj(data_set[2], self.data.coming_mu, self.data.product_per_coming_truck)
                self.data.arrival_times[k][name] = int(uniform(self.data.inbound_arrival_time, two_gdj))

            for i in range(self.data.number_of_outbound_trucks):
                name = 'outbound' + str(i)
                two_gdj = self.calculate_2dgj(data_set[2], self.data.going_mu, self.data.product_per_going_truck)
                gdj = int(uniform(self.data.outbound_arrival_time, two_gdj))
                self.data.arrival_times[k][name] = gdj
                A = gdj + (self.data.going_mu - 1) * self.data.changeover_time + self.data.going_mu * self.data.product_per_going_truck * self.data.loading_time
                self.data.lower_boundaries[k][name] = int(A * data_set[0])
                self.data.upper_boundaries[k][name] = int(A * data_set[1])

            for i in range(self.data.number_of_compound_trucks):
                name = 'compound' + str(i)
                two_gdj = self.calculate_2dgj(data_set[2], self.data.coming_mu, self.data.product_per_coming_truck)
                gdj = int(uniform(self.data.outbound_arrival_time, two_gdj))
                self.data.arrival_times[k][name] = gdj
                #A = gdj + (self.data.going_mu - 1) * self.data.changeover_time + self.data.going_mu * self.data.product_per_going_truck * self.data.loading_time
                A = gdj + (self.data.coming_mu - 1) * self.data.changeover_time + self.data.coming_mu * self.data.product_per_coming_truck * self.data.loading_time + self.data.changeover_time + self.data.truck_transfer_time +(self.data.going_mu - 1) * self.data.changeover_time + self.data.going_mu * self.data.product_per_going_truck * self.data.loading_time
                self.data.lower_boundaries[k][name] = int(A * data_set[0])
                self.data.upper_boundaries[k][name] = int(A * data_set[1])
        self.load_generated_data()

    def new_generate_times(self):
        self.data.arrival_times = []
        self.data.lower_boundaries = []
        self.data.upper_boundaries = []
        for k, data_set in enumerate(self.data.data_sets):
            self.data.arrival_times.append({})
            self.data.lower_boundaries.append({})
            self.data.upper_boundaries.append({})

            self.data.calculate_truck_related_data()
            for i in range(self.data.number_of_inbound_trucks):
                name = 'inbound' + str(i)
                two_gdj = self.calculate_2dgj(data_set[2], self.data.coming_mu, self.data.product_per_coming_truck)
                self.data.arrival_times[k][name] = int(uniform(self.data.inbound_arrival_time, two_gdj))

            for i in range(self.data.number_of_outbound_trucks):
                name = 'outbound' + str(i)
                two_gdj = self.calculate_2dgj(data_set[2], self.data.going_mu, self.data.product_per_going_truck)
                gdj = int(uniform(self.data.outbound_arrival_time, two_gdj))
                self.data.arrival_times[k][name] = gdj
                A = self.data.product_per_coming_truck * self.data.unloading_time + gdj + self.data.product_per_going_truck * self.data.loading_time
                self.data.lower_boundaries[k][name] = int(A * data_set[0])
                self.data.upper_boundaries[k][name] = int(A * data_set[1])

            for i in range(self.data.number_of_compound_trucks):
                name = 'compound' + str(i)
                two_gdj = self.calculate_2dgj(data_set[2], self.data.coming_mu, self.data.product_per_coming_truck)
                gdj = int(uniform(self.data.outbound_arrival_time, two_gdj))
                self.data.arrival_times[k][name] = gdj
                A = self.data.product_per_coming_truck * self.data.unloading_time + gdj + self.data.product_per_going_truck * self.data.loading_time
                self.data.lower_boundaries[k][name] = int(A * data_set[0])
                self.data.upper_boundaries[k][name] = int(A * data_set[1])
        self.load_generated_data()

    def load_generated_data(self):
        self.arrival_time_table_model = TimeTableModel(self.data.arrival_times)
        self.arrival_time_table.setModel(self.arrival_time_table_model)
        self.leaving_lower_table_model = TimeTableModel(self.data.lower_boundaries)
        self.leaving_lower_table.setModel(self.leaving_lower_table_model)
        self.leaving_upper_table_model = TimeTableModel(self.data.upper_boundaries)
        self.leaving_upper_table.setModel(self.leaving_upper_table_model)

    def calculate_2dgj(self, tightness_factor, mu, product_per_truck):
        return (2 * mu * tightness_factor * product_per_truck) / (2 - tightness_factor * mu * self.data.makespan_factor)

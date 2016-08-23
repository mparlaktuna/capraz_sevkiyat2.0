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
from src.annealing_solver import AnnealingSolver
from src.tabu_solver import TabuSolver
from src.enter_sequence import EnterSequenceWidget
from src.sequence import Sequence
from windows.simulation_truck import Ui_simulation_truck
from windows.simulation_door import Ui_simulation_door
from collections import OrderedDict
from src.results import *


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
        self.combobox_coming_sequence = []
        self.combobox_going_sequence = []
        self.statusBar().showMessage('Ready')
        self.load_generated_data()
        self.results = OrderedDict()
        self.shoved_solution_name = ""
        self.shoved_iteration = IterationResults()
        self.shoved_solution = ModelResult()
        self.shoved_iteration_number = 0

        self.continue_solution = True
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

        self.simulationStartButton.setEnabled(False)
        self.simulationStepForwardButton.setEnabled(False)

        self.result_show_best_solution_button.setEnabled(False)
        self.result_show_errors_button.setEnabled(False)
        self.result_show_sequences_button.setEnabled(False)
        self.result_show_trucktimes_button.setEnabled(False)
        self.result_show_truckgoods_button.setEnabled(False)

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
        self.time_limit_edit.textChanged.connect(self.set_time_limit)
        self.numberOfIterationsLineEdit.textChanged.connect(self.set_number_of_iterations)
        self.solverComboBox.currentTextChanged.connect(self.set_solver_algorithm)
        self.tempereature_line_edit.textChanged.connect(self.set_annealing_temperature)
        self.decav_factor_line_edit.textChanged.connect(self.set_annealing_decay)
        self.number_of_tabu_neighbours_line_edit.textChanged.connect(self.set_tabu_neighbor_number)
        self.number_of_tabu_line_edit.textChanged.connect(self.set_tabu_number_tabu)
        self.data_set_spin_box.valueChanged.connect(self.set_data_set_number)
        self.result_solution_name_combo_box.currentTextChanged.connect(self.show_result_update_solution_name)
        self.result_Iteration_number_line_edit.textChanged.connect(self.show_result_update_iteration_number)


    def set_solver_algorithm(self, value):
        if value:
            self.solver_data.algorithm_name = str(value)

    def set_time_limit(self, value):
        if value:
            self.solver_data.time_limit = int(value)

    def set_data_set_number(self, value):
        if value:
            self.solver_data.data_set_number = int(value) - 1

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
        self.solver_data.number_of_iterations = int(value)

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
        self.simulation_reset_button.clicked.connect(self.simulation_reset)

        self.result_show_trucktimes_button.clicked.connect(self.show_result_show_truck_times)
        self.result_show_truckgoods_button.clicked.connect(self.show_result_show_finish_goods)
        self.result_show_errors_button.clicked.connect(self.show_result_show_all_errors)

    def solve_data_set(self):
        if self.solver_data.algorithm_name == "annealing":
            print("Solving for annealing")
            self.solver = AnnealingSolver()
            self.solver_data.function_type = str(self.function_combo_box.currentText())
            self.solution_name = "annealing_" + "_" + self.solver_data.function_type + "_"+str(self.solver_data.data_set_number) + "_" + str(self.solution_number)
            self.solution_number += 1
            self.solver.set_data(self.solver_data, self.data)
            self.sequence_solver.solution_name = self.solution_name
            self.sequence_solver.solution_type = "annealing"
            self.continue_solution = True
            #generate sequence
            #start solving


        elif self.solver_data.algorithm_name == "TS":
            print("Solving for tabu")
            self.solver = TabuSolver()
            self.solver_data.function_type = str(self.function_combo_box.currentText())
            self.solution_name = "tabu_" + "_" + self.solver_data.function_type + "_"+str(self.solver_data.data_set_number) + "_" + str(self.solution_number)
            self.solver.set_data(self.solver_data, self.data)
            self.sequence_solver.solution_name = self.solution_name
            self.sequence_solver.solution_type = "tabu"
            self.continue_solution = True

        while self.continue_solution:
            print("solution start")
            if self.solver.iteration_number < self.solver_data.number_of_iterations:
                self.solver.next_iteration()
            else:
                self.continue_solution = False

        self.results[self.solution_name] = self.solver.iteration_results
        self.update_results()

    def simulation_start(self):
        """
        start a simulation for one solution
        """
        self.solution_name = "simulation_" + str(self.solver_data.data_set_number) + "_" + str(self.solution_number)
        self.solution_number += 1
        self.sequence_solver.set_data(self.solver_data, self.data)
        self.sequence_solver.solution_name = self.solution_name
        self.sequence_solver.solution_type = "simulation"
        self.current_sequence.print_sequence()
        self.sequence_solver.set_sequence(self.current_sequence)
        self.simulation_set_tables()
        self.simulation_set_trucks()
        self.simulation_add_spacers()
        self.enter_sequence_button.setEnabled(False)
        self.simulationStartButton.setEnabled(False)
        self.simulationStepForwardButton.setEnabled(True)

    def simulation_forward(self):
        if self.sequence_solver.step_forward():
            self.simulation_clear_layouts()
            self.simulation_set_tables()
            self.simulation_set_trucks()
            self.simulation_add_spacers()
            self.time.display(self.sequence_solver.model.current_time)
        else:
            self.simulationStepForwardButton.setEnabled(False)
            self.enter_sequence_button.setEnabled(True)
            self.simulationStartButton.setEnabled(False)
            self.results[self.solution_name] = self.sequence_solver.iteration_results
            self.update_results()

    def simulation_reset(self):
        self.enter_sequence_button.setEnabled(True)
        self.simulationStepForwardButton.setEnabled(False)
        self.simulationStartButton.setEnabled(False)

    def update_results(self):
        self.result_solution_name_combo_box.currentTextChanged.disconnect()
        self.result_solution_name_combo_box.clear()
        self.result_solution_name_combo_box.addItems(self.results.keys())
        self.show_result_update_solution_name()
        self.result_solution_name_combo_box.currentTextChanged.connect(self.show_result_update_solution_name)
        self.result_show_best_solution_button.setEnabled(True)
        self.result_show_errors_button.setEnabled(True)
        self.result_show_sequences_button.setEnabled(True)
        self.result_show_trucktimes_button.setEnabled(True)
        self.result_show_truckgoods_button.setEnabled(True)

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
        coming_truck_list = []
        receiving_truck_list = []
        shipping_truck_list = []
        transfer_truck_list = []
        done_truck_list = []
        truck_widget_dict = dict()
        for truck in self.sequence_solver.model.all_trucks.values():
            new_truck_widget = QWidget()
            new_truck_element = Ui_simulation_truck()
            new_truck_element.setupUi(new_truck_widget)
            if truck.state_change:
                new_truck_element.truckNameLabel.setText(truck.element_name+"*")
            else:
                new_truck_element.truckNameLabel.setText(truck.element_name)
            new_truck_element.show_goods_button.clicked.connect(truck.show_goods)
            new_truck_element.show_times_button.clicked.connect(truck.show_times)
            truck_widget_dict[truck.element_name] = new_truck_widget
            if truck.simulation_state == 0:
                # coming truck list
                coming_truck_list.append(truck)
            elif truck.simulation_state == 1:
                # receiving door"
                receiving_truck_list.append(truck)
                if truck.state == 1:
                    new_truck_element.truckNameLabel.setText(truck.element_name+"-w")
                elif truck.state == 2:
                    new_truck_element.truckNameLabel.setText(truck.element_name+"-cin")
                elif truck.state == 3:
                    new_truck_element.truckNameLabel.setText(truck.element_name+"-de")
                elif truck.state == 4:
                    new_truck_element.truckNameLabel.setText(truck.element_name+"-cout")

            elif truck.simulation_state == 2:
                # shipping door
                shipping_truck_list.append(truck)
            elif truck.simulation_state == 3:
                # done
                done_truck_list.append(truck)
            elif truck.simulation_state == 4:
                # transfer
                transfer_truck_list.append(truck)

        for truck in coming_truck_list:
            self.simulationComingTruckList.addWidget(truck_widget_dict[truck.element_name])

        for truck in done_truck_list:
            self.simulationFinishedList.addWidget(truck_widget_dict[truck.element_name])

        for truck in transfer_truck_list:
            self.simulationCompoundTruckTransferList.addWidget(truck_widget_dict[truck.element_name])

        for door in self.sequence_solver.model.receiving_doors.values():
            new_door_widget = QWidget()
            new_door_element = Ui_simulation_door()
            new_door_element.setupUi(new_door_widget)
            new_door_element.door_name.setText(door.element_name)
            new_door_element.show_truck_sequence_button.clicked.connect(door.show_sequence)
            self.simulationReceivingDoorsList.addWidget(new_door_widget)
            for truck in receiving_truck_list:
                if truck.current_door == door:
                    self.simulationReceivingDoorsList.addWidget(truck_widget_dict[truck.element_name])

        for door in self.sequence_solver.model.shipping_doors.values():
            new_door_widget = QWidget()
            new_door_element = Ui_simulation_door()
            new_door_element.setupUi(new_door_widget)
            new_door_element.door_name.setText(door.element_name)
            new_door_element.show_truck_sequence_button.clicked.connect(door.show_sequence)

            self.simulationShippingDoorsList.addWidget(new_door_widget)
            for truck in shipping_truck_list:
                if truck.current_door == door:
                    self.simulationShippingDoorsList.addWidget(truck_widget_dict[truck.element_name])

        new_line_edit = QTextEdit()
        new_line_edit.setText(self.sequence_solver.model.station.good_store.print_goods())
        self.simulationStation.addWidget(new_line_edit)

    def load_data(self):
        """
        loads prev saved data
        :return:
        """
        # for fast loading data disable after finished and uncomment following
        file_name = "C:/Users/mparl/Downloads/test202"
        # file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        try:
            self.data = pickle.load(open(file_name, 'rb'))
        except Exception as e:
            pass
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
        self.simulationStartButton.setEnabled(True)


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

    def show_result_show_all_errors(self):
        error_dialog = QMessageBox()
        error_dialog.setWindowTitle("Solutions of Objective Functions:")
        message = "\n"
        for error_name, errors in self.shoved_solution.errors.items():
            if error_name == "truck_error_times":
                for truck_name, error_list in errors.items():
                    message += truck_name + ":\n"
                    for error_name, error in error_list.items():
                        message += "\t" + error_name + ": " + str(error) + "\n"
            else:
                message += error_name + ": "
                message += str(errors) + "\n"

        error_dialog.setText(message)
        error_dialog.exec_()

    def show_result_show_all_sequences(self):
        pass

    def show_result_show_truck_times(self):
        current_truck = self.result_truck_name_combo_box.currentText()
        time_dialog = QMessageBox()
        time_dialog.setWindowTitle("Times of:" + str(current_truck))
        message = "\n"
        for time_name, times in self.shoved_solution.truck_times[current_truck].items():
            message += time_name + ": "
            message += str(times) + "\n"

        time_dialog.setText(message)
        time_dialog.exec_()

    def show_result_show_finish_goods(self):
        current_truck = self.result_truck_name_combo_box.currentText()
        time_dialog = QMessageBox()
        good_store = self.shoved_solution.final_goods[current_truck]
        time_dialog.setWindowTitle("Goods of " + current_truck)
        message = good_store.print_goods()

        time_dialog.setText(message)
        time_dialog.exec_()

    def show_result_update_truck_list(self):
        self.result_truck_name_combo_box.clear()
        self.result_truck_name_combo_box.addItems(self.shoved_solution.truck_times.keys())

    def show_result_update_iteration_number(self):
        number = self.result_Iteration_number_line_edit.text()
        if not number:
            number = 1
        else:
            try:
                number = int(number)
                self.shoved_iteration_number =  number - 1
                if self.shoved_iteration_number < len(self.shoved_iteration.model_results):
                    print("shoved updated")
                    self.shoved_solution = self.shoved_iteration.model_results[self.shoved_iteration_number]
                    self.show_result_update_truck_list()
            except:
                pass


    def show_result_update_solution_name(self):
        self.shoved_solution_name = self.result_solution_name_combo_box.currentText()
        self.shoved_iteration = self.results[self.shoved_solution_name]
        self.result_Iteration_number_line_edit.setText(str(1))

    def show_result_show_best_solution(self):
        pass
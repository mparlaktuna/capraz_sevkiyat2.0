# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1274, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.enterSequenceButton = QtWidgets.QTabWidget(self.centralwidget)
        self.enterSequenceButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.enterSequenceButton.setTabPosition(QtWidgets.QTabWidget.North)
        self.enterSequenceButton.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.enterSequenceButton.setElideMode(QtCore.Qt.ElideLeft)
        self.enterSequenceButton.setDocumentMode(False)
        self.enterSequenceButton.setTabsClosable(False)
        self.enterSequenceButton.setMovable(False)
        self.enterSequenceButton.setTabBarAutoHide(False)
        self.enterSequenceButton.setObjectName("enterSequenceButton")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setObjectName("formLayout")
        self.numberOfInboundTrucksLabel = QtWidgets.QLabel(self.tab_1)
        self.numberOfInboundTrucksLabel.setObjectName("numberOfInboundTrucksLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.numberOfInboundTrucksLabel)
        self.numberOfInboundTrucksSpinBox = QtWidgets.QSpinBox(self.tab_1)
        self.numberOfInboundTrucksSpinBox.setObjectName("numberOfInboundTrucksSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numberOfInboundTrucksSpinBox)
        self.numberOfOutboundTrucksLabel = QtWidgets.QLabel(self.tab_1)
        self.numberOfOutboundTrucksLabel.setObjectName("numberOfOutboundTrucksLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numberOfOutboundTrucksLabel)
        self.numberOfOutboundTrucksSpinBox = QtWidgets.QSpinBox(self.tab_1)
        self.numberOfOutboundTrucksSpinBox.setObjectName("numberOfOutboundTrucksSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numberOfOutboundTrucksSpinBox)
        self.numberOfCompoundTrucksLabel = QtWidgets.QLabel(self.tab_1)
        self.numberOfCompoundTrucksLabel.setObjectName("numberOfCompoundTrucksLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numberOfCompoundTrucksLabel)
        self.numberOfCompoundTrucksSpinBox = QtWidgets.QSpinBox(self.tab_1)
        self.numberOfCompoundTrucksSpinBox.setObjectName("numberOfCompoundTrucksSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numberOfCompoundTrucksSpinBox)
        self.numberOfReceivingDoorsLabel = QtWidgets.QLabel(self.tab_1)
        self.numberOfReceivingDoorsLabel.setObjectName("numberOfReceivingDoorsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.numberOfReceivingDoorsLabel)
        self.numberOfReceivingDoorsSpinBox = QtWidgets.QSpinBox(self.tab_1)
        self.numberOfReceivingDoorsSpinBox.setObjectName("numberOfReceivingDoorsSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.numberOfReceivingDoorsSpinBox)
        self.numberOfShippingDoorsLabel = QtWidgets.QLabel(self.tab_1)
        self.numberOfShippingDoorsLabel.setObjectName("numberOfShippingDoorsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.numberOfShippingDoorsLabel)
        self.numberOfShippingDoorsSpinBox = QtWidgets.QSpinBox(self.tab_1)
        self.numberOfShippingDoorsSpinBox.setObjectName("numberOfShippingDoorsSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.numberOfShippingDoorsSpinBox)
        self.numberOfGoodsLabel = QtWidgets.QLabel(self.tab_1)
        self.numberOfGoodsLabel.setObjectName("numberOfGoodsLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.numberOfGoodsLabel)
        self.numberOfGoodsSpinBox = QtWidgets.QSpinBox(self.tab_1)
        self.numberOfGoodsSpinBox.setObjectName("numberOfGoodsSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.numberOfGoodsSpinBox)
        self.loadingTumeLabel = QtWidgets.QLabel(self.tab_1)
        self.loadingTumeLabel.setObjectName("loadingTumeLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.loadingTumeLabel)
        self.loadingTumeLineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.loadingTumeLineEdit.setObjectName("loadingTumeLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.loadingTumeLineEdit)
        self.truckChangeoverTimeLabel = QtWidgets.QLabel(self.tab_1)
        self.truckChangeoverTimeLabel.setObjectName("truckChangeoverTimeLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.truckChangeoverTimeLabel)
        self.truckChangeoverTimeLineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.truckChangeoverTimeLineEdit.setObjectName("truckChangeoverTimeLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.truckChangeoverTimeLineEdit)
        self.effectOfTheArrivalTimesOnMakespanLabel = QtWidgets.QLabel(self.tab_1)
        self.effectOfTheArrivalTimesOnMakespanLabel.setObjectName("effectOfTheArrivalTimesOnMakespanLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.effectOfTheArrivalTimesOnMakespanLabel)
        self.effectOfTheArrivalTimesOnMakespanLineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.effectOfTheArrivalTimesOnMakespanLineEdit.setObjectName("effectOfTheArrivalTimesOnMakespanLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.effectOfTheArrivalTimesOnMakespanLineEdit)
        self.truckTransferTimeLabel = QtWidgets.QLabel(self.tab_1)
        self.truckTransferTimeLabel.setObjectName("truckTransferTimeLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.truckTransferTimeLabel)
        self.truckTransferTimeLineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.truckTransferTimeLineEdit.setObjectName("truckTransferTimeLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.truckTransferTimeLineEdit)
        self.inboundArrivalTimeLabel = QtWidgets.QLabel(self.tab_1)
        self.inboundArrivalTimeLabel.setObjectName("inboundArrivalTimeLabel")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.inboundArrivalTimeLabel)
        self.inboundArrivalTimeLineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.inboundArrivalTimeLineEdit.setObjectName("inboundArrivalTimeLineEdit")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.inboundArrivalTimeLineEdit)
        self.outboundArrivalTimeLabel = QtWidgets.QLabel(self.tab_1)
        self.outboundArrivalTimeLabel.setObjectName("outboundArrivalTimeLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.outboundArrivalTimeLabel)
        self.outboundArrivalTimeLineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.outboundArrivalTimeLineEdit.setObjectName("outboundArrivalTimeLineEdit")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.outboundArrivalTimeLineEdit)
        self.goodTransferTimeLabel = QtWidgets.QLabel(self.tab_1)
        self.goodTransferTimeLabel.setObjectName("goodTransferTimeLabel")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.goodTransferTimeLabel)
        self.goodTransferTimeLineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.goodTransferTimeLineEdit.setObjectName("goodTransferTimeLineEdit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.goodTransferTimeLineEdit)
        self.numberOfDataSetsLabel = QtWidgets.QLabel(self.tab_1)
        self.numberOfDataSetsLabel.setObjectName("numberOfDataSetsLabel")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.numberOfDataSetsLabel)
        self.numberOfDataSetsSpinBox = QtWidgets.QSpinBox(self.tab_1)
        self.numberOfDataSetsSpinBox.setMinimum(0)
        self.numberOfDataSetsSpinBox.setProperty("value", 0)
        self.numberOfDataSetsSpinBox.setObjectName("numberOfDataSetsSpinBox")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.numberOfDataSetsSpinBox)
        self.label_20 = QtWidgets.QLabel(self.tab_1)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.unloading_time_edit = QtWidgets.QLineEdit(self.tab_1)
        self.unloading_time_edit.setObjectName("unloading_time_edit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.unloading_time_edit)
        self.verticalLayout.addLayout(self.formLayout)
        self.datasettable = ClipboardTableView(self.tab_1)
        self.datasettable.setAccessibleDescription("")
        self.datasettable.setLineWidth(1)
        self.datasettable.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.datasettable.setTabKeyNavigation(False)
        self.datasettable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.datasettable.setSortingEnabled(True)
        self.datasettable.setObjectName("datasettable")
        self.datasettable.horizontalHeader().setCascadingSectionResizes(True)
        self.datasettable.horizontalHeader().setDefaultSectionSize(70)
        self.verticalLayout.addWidget(self.datasettable)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inbound_good_table = ClipboardTableView(self.tab_1)
        self.inbound_good_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.inbound_good_table.setObjectName("inbound_good_table")
        self.verticalLayout_2.addWidget(self.inbound_good_table)
        self.compound_coming_good_table = ClipboardTableView(self.tab_1)
        self.compound_coming_good_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.compound_coming_good_table.setObjectName("compound_coming_good_table")
        self.verticalLayout_2.addWidget(self.compound_coming_good_table)
        self.outbound_good_table = ClipboardTableView(self.tab_1)
        self.outbound_good_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.outbound_good_table.setObjectName("outbound_good_table")
        self.verticalLayout_2.addWidget(self.outbound_good_table)
        self.compound_going_good_table = ClipboardTableView(self.tab_1)
        self.compound_going_good_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.compound_going_good_table.setObjectName("compound_going_good_table")
        self.verticalLayout_2.addWidget(self.compound_going_good_table)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 5)
        self.enterSequenceButton.addTab(self.tab_1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.leaving_lower_table = ClipboardTableView(self.tab)
        self.leaving_lower_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.leaving_lower_table.setObjectName("leaving_lower_table")
        self.verticalLayout_4.addWidget(self.leaving_lower_table)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 1, 1, 1)
        self.print_gams = QtWidgets.QPushButton(self.tab)
        self.print_gams.setObjectName("print_gams")
        self.gridLayout_2.addWidget(self.print_gams, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.leaving_upper_table = ClipboardTableView(self.tab)
        self.leaving_upper_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.leaving_upper_table.setObjectName("leaving_upper_table")
        self.verticalLayout_5.addWidget(self.leaving_upper_table)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 2, 2, 1, 1)
        self.print_text = QtWidgets.QPushButton(self.tab)
        self.print_text.setObjectName("print_text")
        self.gridLayout_2.addWidget(self.print_text, 0, 2, 1, 1)
        self.generate_times_button = QtWidgets.QPushButton(self.tab)
        self.generate_times_button.setObjectName("generate_times_button")
        self.gridLayout_2.addWidget(self.generate_times_button, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.arrival_time_table = ClipboardTableView(self.tab)
        self.arrival_time_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.arrival_time_table.setObjectName("arrival_time_table")
        self.verticalLayout_3.addWidget(self.arrival_time_table)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.generate_new_boundaries_button = QtWidgets.QPushButton(self.tab)
        self.generate_new_boundaries_button.setObjectName("generate_new_boundaries_button")
        self.gridLayout_2.addWidget(self.generate_new_boundaries_button, 1, 0, 1, 1)
        self.enterSequenceButton.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.solverLabel = QtWidgets.QLabel(self.tab_2)
        self.solverLabel.setObjectName("solverLabel")
        self.horizontalLayout_4.addWidget(self.solverLabel)
        self.solverComboBox = QtWidgets.QComboBox(self.tab_2)
        self.solverComboBox.setObjectName("solverComboBox")
        self.solverComboBox.addItem("")
        self.solverComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.solverComboBox)
        self.numberOfIterationsLabel = QtWidgets.QLabel(self.tab_2)
        self.numberOfIterationsLabel.setObjectName("numberOfIterationsLabel")
        self.horizontalLayout_4.addWidget(self.numberOfIterationsLabel)
        self.numberOfIterationsLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.numberOfIterationsLineEdit.setObjectName("numberOfIterationsLineEdit")
        self.horizontalLayout_4.addWidget(self.numberOfIterationsLineEdit)
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_4.addWidget(self.label_19)
        self.solution_time_label = QtWidgets.QLineEdit(self.tab_2)
        self.solution_time_label.setReadOnly(True)
        self.solution_time_label.setObjectName("solution_time_label")
        self.horizontalLayout_4.addWidget(self.solution_time_label)
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.tempereature_line_edit = QtWidgets.QLineEdit(self.page)
        self.tempereature_line_edit.setObjectName("tempereature_line_edit")
        self.horizontalLayout.addWidget(self.tempereature_line_edit)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.decav_factor_line_edit = QtWidgets.QLineEdit(self.page)
        self.decav_factor_line_edit.setObjectName("decav_factor_line_edit")
        self.horizontalLayout.addWidget(self.decav_factor_line_edit)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.number_of_tabu_neighbours_line_edit = QtWidgets.QLineEdit(self.page_2)
        self.number_of_tabu_neighbours_line_edit.setObjectName("number_of_tabu_neighbours_line_edit")
        self.horizontalLayout_3.addWidget(self.number_of_tabu_neighbours_line_edit)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.number_of_tabu_line_edit = QtWidgets.QLineEdit(self.page_2)
        self.number_of_tabu_line_edit.setObjectName("number_of_tabu_line_edit")
        self.horizontalLayout_3.addWidget(self.number_of_tabu_line_edit)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_4.addWidget(self.label_21)
        self.function_combo_box = QtWidgets.QComboBox(self.tab_2)
        self.function_combo_box.setObjectName("function_combo_box")
        self.function_combo_box.addItem("")
        self.function_combo_box.addItem("")
        self.function_combo_box.addItem("")
        self.function_combo_box.addItem("")
        self.function_combo_box.addItem("")
        self.function_combo_box.addItem("")
        self.function_combo_box.setItemText(5, "")
        self.horizontalLayout_4.addWidget(self.function_combo_box)
        self.time_limit_edit = QtWidgets.QLineEdit(self.tab_2)
        self.time_limit_edit.setObjectName("time_limit_edit")
        self.horizontalLayout_4.addWidget(self.time_limit_edit)
        self.solve_data_set_button = QtWidgets.QPushButton(self.tab_2)
        self.solve_data_set_button.setObjectName("solve_data_set_button")
        self.horizontalLayout_4.addWidget(self.solve_data_set_button)
        self.data_set_spin_box = QtWidgets.QSpinBox(self.tab_2)
        self.data_set_spin_box.setMinimum(1)
        self.data_set_spin_box.setProperty("value", 1)
        self.data_set_spin_box.setObjectName("data_set_spin_box")
        self.horizontalLayout_4.addWidget(self.data_set_spin_box)
        self.stop_data_set_solve_button = QtWidgets.QPushButton(self.tab_2)
        self.stop_data_set_solve_button.setObjectName("stop_data_set_solve_button")
        self.horizontalLayout_4.addWidget(self.stop_data_set_solve_button)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)
        self.generalResultsLayout = QtWidgets.QVBoxLayout()
        self.generalResultsLayout.setObjectName("generalResultsLayout")
        self.gridLayout_7.addLayout(self.generalResultsLayout, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_7.setRowStretch(1, 3)
        self.gridLayout_7.setRowStretch(2, 3)
        self.enterSequenceButton.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.tab_4)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.simulationShippingDoorsList = QtWidgets.QVBoxLayout()
        self.simulationShippingDoorsList.setObjectName("simulationShippingDoorsList")
        self.gridLayout_6.addLayout(self.simulationShippingDoorsList, 0, 3, 1, 1)
        self.simulationStation = QtWidgets.QVBoxLayout()
        self.simulationStation.setObjectName("simulationStation")
        self.gridLayout_6.addLayout(self.simulationStation, 0, 2, 1, 1)
        self.simulationReceivingDoorsList = QtWidgets.QVBoxLayout()
        self.simulationReceivingDoorsList.setObjectName("simulationReceivingDoorsList")
        self.gridLayout_6.addLayout(self.simulationReceivingDoorsList, 0, 1, 1, 1)
        self.simulationFinishedList = QtWidgets.QVBoxLayout()
        self.simulationFinishedList.setObjectName("simulationFinishedList")
        self.gridLayout_6.addLayout(self.simulationFinishedList, 0, 4, 1, 1)
        self.simulationComingTruckList = QtWidgets.QVBoxLayout()
        self.simulationComingTruckList.setObjectName("simulationComingTruckList")
        self.gridLayout_6.addLayout(self.simulationComingTruckList, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.enter_sequence_button = QtWidgets.QPushButton(self.tab_4)
        self.enter_sequence_button.setObjectName("enter_sequence_button")
        self.horizontalLayout_2.addWidget(self.enter_sequence_button)
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.time = QtWidgets.QLCDNumber(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.horizontalLayout_2.addWidget(self.time)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.time_constant = QtWidgets.QLineEdit(self.tab_4)
        self.time_constant.setObjectName("time_constant")
        self.horizontalLayout_2.addWidget(self.time_constant)
        self.simulationStartButton = QtWidgets.QPushButton(self.tab_4)
        self.simulationStartButton.setObjectName("simulationStartButton")
        self.horizontalLayout_2.addWidget(self.simulationStartButton)
        self.simulationStepForwardButton = QtWidgets.QPushButton(self.tab_4)
        self.simulationStepForwardButton.setObjectName("simulationStepForwardButton")
        self.horizontalLayout_2.addWidget(self.simulationStepForwardButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.enterSequenceButton.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.result_names_combo_box = QtWidgets.QComboBox(self.tab_3)
        self.result_names_combo_box.setMinimumSize(QtCore.QSize(300, 0))
        self.result_names_combo_box.setObjectName("result_names_combo_box")
        self.horizontalLayout_5.addWidget(self.result_names_combo_box)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.result_iteration_number_line_edit = QtWidgets.QLineEdit(self.tab_3)
        self.result_iteration_number_line_edit.setObjectName("result_iteration_number_line_edit")
        self.horizontalLayout_5.addWidget(self.result_iteration_number_line_edit)
        self.show_results_button = QtWidgets.QPushButton(self.tab_3)
        self.show_results_button.setObjectName("show_results_button")
        self.horizontalLayout_5.addWidget(self.show_results_button)
        self.multiSolveButton = QtWidgets.QPushButton(self.tab_3)
        self.multiSolveButton.setObjectName("multiSolveButton")
        self.horizontalLayout_5.addWidget(self.multiSolveButton)
        self.multiSolveCombo = QtWidgets.QComboBox(self.tab_3)
        self.multiSolveCombo.setObjectName("multiSolveCombo")
        self.multiSolveCombo.addItem("")
        self.multiSolveCombo.addItem("")
        self.multiSolveCombo.addItem("")
        self.multiSolveCombo.addItem("")
        self.multiSolveCombo.addItem("")
        self.horizontalLayout_5.addWidget(self.multiSolveCombo)
        self.horizontalLayout_5.setStretch(0, 2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_13.addWidget(self.label_17)
        self.sequence_table = ClipboardTableView(self.tab_3)
        self.sequence_table.setMinimumSize(QtCore.QSize(350, 0))
        self.sequence_table.setObjectName("sequence_table")
        self.verticalLayout_13.addWidget(self.sequence_table)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_11.addWidget(self.label_16)
        self.inbound_time_table = ClipboardTableView(self.tab_3)
        self.inbound_time_table.setMinimumSize(QtCore.QSize(350, 0))
        self.inbound_time_table.setObjectName("inbound_time_table")
        self.verticalLayout_11.addWidget(self.inbound_time_table)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_14.addWidget(self.label_18)
        self.good_in_out_table = ClipboardTableView(self.tab_3)
        self.good_in_out_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.good_in_out_table.setObjectName("good_in_out_table")
        self.good_in_out_table.horizontalHeader().setHighlightSections(False)
        self.verticalLayout_14.addWidget(self.good_in_out_table)
        self.horizontalLayout_6.addLayout(self.verticalLayout_14)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_15.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.outbound_time_table = ClipboardTableView(self.tab_3)
        self.outbound_time_table.setMinimumSize(QtCore.QSize(0, 150))
        self.outbound_time_table.setObjectName("outbound_time_table")
        self.verticalLayout_9.addWidget(self.outbound_time_table)
        self.verticalLayout_15.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.compound_time_table = ClipboardTableView(self.tab_3)
        self.compound_time_table.setMinimumSize(QtCore.QSize(0, 150))
        self.compound_time_table.setObjectName("compound_time_table")
        self.verticalLayout_10.addWidget(self.compound_time_table)
        self.verticalLayout_15.addLayout(self.verticalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout_15, 1, 0, 1, 1)
        self.enterSequenceButton.addTab(self.tab_3, "")
        self.gridLayout_9.addWidget(self.enterSequenceButton, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1274, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Data = QtWidgets.QAction(MainWindow)
        self.actionNew_Data.setObjectName("actionNew_Data")
        self.actionLoad_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionSave_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionNew_Data)
        self.menuFile.addAction(self.actionLoad_Data)
        self.menuFile.addAction(self.actionSave_Data)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.enterSequenceButton.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(1)
        self.solverComboBox.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DSS for Cross Docking"))
        self.numberOfInboundTrucksLabel.setText(_translate("MainWindow", "Number of Inbound Trucks"))
        self.numberOfOutboundTrucksLabel.setText(_translate("MainWindow", "Number of Outbound Trucks"))
        self.numberOfCompoundTrucksLabel.setText(_translate("MainWindow", "Number of Compound Trucks"))
        self.numberOfReceivingDoorsLabel.setText(_translate("MainWindow", "Number of Receiving Doors"))
        self.numberOfShippingDoorsLabel.setText(_translate("MainWindow", "Number of Shipping Doors"))
        self.numberOfGoodsLabel.setText(_translate("MainWindow", "Number of Goods"))
        self.loadingTumeLabel.setText(_translate("MainWindow", "Loading Time"))
        self.truckChangeoverTimeLabel.setText(_translate("MainWindow", "Truck Changeover Time"))
        self.effectOfTheArrivalTimesOnMakespanLabel.setText(_translate("MainWindow", "Effect of the arrival times on makespan"))
        self.truckTransferTimeLabel.setText(_translate("MainWindow", "Truck Transfer Time"))
        self.inboundArrivalTimeLabel.setText(_translate("MainWindow", "Inbound Arrival Time"))
        self.outboundArrivalTimeLabel.setText(_translate("MainWindow", "Outbound Arrival Time"))
        self.goodTransferTimeLabel.setText(_translate("MainWindow", "Good Transfer Time"))
        self.numberOfDataSetsLabel.setText(_translate("MainWindow", "Number of Data Sets"))
        self.label_20.setText(_translate("MainWindow", "Unloading Time"))
        self.enterSequenceButton.setTabText(self.enterSequenceButton.indexOf(self.tab_1), _translate("MainWindow", "Data Set"))
        self.label_2.setText(_translate("MainWindow", "Leaving Times Lower Boundary"))
        self.print_gams.setText(_translate("MainWindow", "Gams Output"))
        self.label_3.setText(_translate("MainWindow", "lLeaving Times Upper  Boundary"))
        self.print_text.setText(_translate("MainWindow", "Text Output"))
        self.generate_times_button.setText(_translate("MainWindow", "Generate"))
        self.label.setText(_translate("MainWindow", "Arrival Times"))
        self.generate_new_boundaries_button.setText(_translate("MainWindow", "Generate New Boundaries"))
        self.enterSequenceButton.setTabText(self.enterSequenceButton.indexOf(self.tab), _translate("MainWindow", "AT-TW"))
        self.solverLabel.setText(_translate("MainWindow", "Algorithm"))
        self.solverComboBox.setItemText(0, _translate("MainWindow", "SA"))
        self.solverComboBox.setItemText(1, _translate("MainWindow", "TS"))
        self.numberOfIterationsLabel.setText(_translate("MainWindow", "Number of Iterations"))
        self.numberOfIterationsLineEdit.setText(_translate("MainWindow", "100"))
        self.label_19.setText(_translate("MainWindow", "Solution Time: "))
        self.solution_time_label.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Temperature"))
        self.tempereature_line_edit.setText(_translate("MainWindow", "100"))
        self.label_9.setText(_translate("MainWindow", "Cooling Ratio"))
        self.decav_factor_line_edit.setText(_translate("MainWindow", "0.9"))
        self.label_10.setText(_translate("MainWindow", "# of Neighbours "))
        self.number_of_tabu_neighbours_line_edit.setText(_translate("MainWindow", "5"))
        self.label_11.setText(_translate("MainWindow", "# of Tabu"))
        self.number_of_tabu_line_edit.setText(_translate("MainWindow", "4"))
        self.label_21.setText(_translate("MainWindow", "Objective Function"))
        self.function_combo_box.setItemText(0, _translate("MainWindow", "earliness+tardiness"))
        self.function_combo_box.setItemText(1, _translate("MainWindow", "number_of_goods"))
        self.function_combo_box.setItemText(2, _translate("MainWindow", "total_tardiness"))
        self.function_combo_box.setItemText(3, _translate("MainWindow", "cmax"))
        self.function_combo_box.setItemText(4, _translate("MainWindow", "late_truck"))
        self.solve_data_set_button.setText(_translate("MainWindow", "Run"))
        self.stop_data_set_solve_button.setText(_translate("MainWindow", "Stop"))
        self.enterSequenceButton.setTabText(self.enterSequenceButton.indexOf(self.tab_2), _translate("MainWindow", "Solve Data Set"))
        self.enter_sequence_button.setText(_translate("MainWindow", "Enter Sequence"))
        self.label_8.setText(_translate("MainWindow", "Time"))
        self.label_12.setText(_translate("MainWindow", "One step time"))
        self.time_constant.setText(_translate("MainWindow", "0.1"))
        self.simulationStartButton.setText(_translate("MainWindow", "Start"))
        self.simulationStepForwardButton.setText(_translate("MainWindow", "Step Forward"))
        self.enterSequenceButton.setTabText(self.enterSequenceButton.indexOf(self.tab_4), _translate("MainWindow", "View The Solution"))
        self.label_13.setText(_translate("MainWindow", "Iteration Number"))
        self.result_iteration_number_line_edit.setText(_translate("MainWindow", "1"))
        self.show_results_button.setText(_translate("MainWindow", "Show Results"))
        self.multiSolveButton.setText(_translate("MainWindow", "Solve For"))
        self.multiSolveCombo.setItemText(0, _translate("MainWindow", "earliness+tardiness"))
        self.multiSolveCombo.setItemText(1, _translate("MainWindow", "number_of_goods"))
        self.multiSolveCombo.setItemText(2, _translate("MainWindow", "total_tardiness"))
        self.multiSolveCombo.setItemText(3, _translate("MainWindow", "cmax"))
        self.multiSolveCombo.setItemText(4, _translate("MainWindow", "late_truck"))
        self.label_17.setText(_translate("MainWindow", "Seqeunce Table"))
        self.label_16.setText(_translate("MainWindow", "Inbound Time Table"))
        self.label_18.setText(_translate("MainWindow", "Good Table"))
        self.label_14.setText(_translate("MainWindow", "Outbound Time Table"))
        self.label_15.setText(_translate("MainWindow", "Compound Time Table"))
        self.enterSequenceButton.setTabText(self.enterSequenceButton.indexOf(self.tab_3), _translate("MainWindow", "Show Results"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionNew_Data.setText(_translate("MainWindow", "&New Data"))
        self.actionLoad_Data.setText(_translate("MainWindow", "&Load Data"))
        self.actionSave_Data.setText(_translate("MainWindow", "&Save Data"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))

from src.clipboard_table_view import ClipboardTableView

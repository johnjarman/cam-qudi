# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PulsedMainGui.ui'
#
# Created: Mon Jun 29 17:32:31 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(947, 771)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.current_sequence_ComboBox = QtGui.QComboBox(self.tab)
        self.current_sequence_ComboBox.setObjectName(_fromUtf8("current_sequence_ComboBox"))
        self.gridLayout_4.addWidget(self.current_sequence_ComboBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.fastcounter_bin_ComboBox = QtGui.QComboBox(self.tab)
        self.fastcounter_bin_ComboBox.setObjectName(_fromUtf8("fastcounter_bin_ComboBox"))
        self.gridLayout_4.addWidget(self.fastcounter_bin_ComboBox, 1, 4, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 1, 3, 1, 1)
        self.idle_RadioButton = QtGui.QRadioButton(self.tab)
        self.idle_RadioButton.setObjectName(_fromUtf8("idle_RadioButton"))
        self.gridLayout_4.addWidget(self.idle_RadioButton, 0, 0, 1, 1)
        self.run_RadioButton = QtGui.QRadioButton(self.tab)
        self.run_RadioButton.setObjectName(_fromUtf8("run_RadioButton"))
        self.gridLayout_4.addWidget(self.run_RadioButton, 0, 1, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_4.addWidget(self.graphicsView, 2, 0, 1, 6)
        self.graphicsView_2 = QtGui.QGraphicsView(self.tab)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.gridLayout_4.addWidget(self.graphicsView_2, 3, 0, 1, 6)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.laser_channel_ComboBox = QtGui.QComboBox(self.tab_2)
        self.laser_channel_ComboBox.setObjectName(_fromUtf8("laser_channel_ComboBox"))
        self.gridLayout_10.addWidget(self.laser_channel_ComboBox, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_10.addWidget(self.label_6, 1, 0, 1, 1)
        self.sampling_freq_DoubleSpinBox = QtGui.QDoubleSpinBox(self.tab_2)
        self.sampling_freq_DoubleSpinBox.setObjectName(_fromUtf8("sampling_freq_DoubleSpinBox"))
        self.gridLayout_10.addWidget(self.sampling_freq_DoubleSpinBox, 1, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_10, 0, 2, 1, 1)
        self.gridLayout_17 = QtGui.QGridLayout()
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        spacerItem1 = QtGui.QSpacerItem(20, 150, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem1, 0, 1, 1, 1)
        self.repeat_block_TableWidget = QtGui.QTableWidget(self.tab_2)
        self.repeat_block_TableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.repeat_block_TableWidget.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.repeat_block_TableWidget.setRowCount(6)
        self.repeat_block_TableWidget.setColumnCount(16)
        self.repeat_block_TableWidget.setObjectName(_fromUtf8("repeat_block_TableWidget"))
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.repeat_block_TableWidget.setHorizontalHeaderItem(15, item)
        self.gridLayout_17.addWidget(self.repeat_block_TableWidget, 0, 0, 5, 1)
        self.clear_repeat_table_PushButton = QtGui.QPushButton(self.tab_2)
        self.clear_repeat_table_PushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.clear_repeat_table_PushButton.setObjectName(_fromUtf8("clear_repeat_table_PushButton"))
        self.gridLayout_17.addWidget(self.clear_repeat_table_PushButton, 3, 1, 1, 1)
        self.del_row_repeat_PushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_row_repeat_PushButton.sizePolicy().hasHeightForWidth())
        self.del_row_repeat_PushButton.setSizePolicy(sizePolicy)
        self.del_row_repeat_PushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.del_row_repeat_PushButton.setObjectName(_fromUtf8("del_row_repeat_PushButton"))
        self.gridLayout_17.addWidget(self.del_row_repeat_PushButton, 2, 1, 1, 1)
        self.add_row_repeat_PushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_row_repeat_PushButton.sizePolicy().hasHeightForWidth())
        self.add_row_repeat_PushButton.setSizePolicy(sizePolicy)
        self.add_row_repeat_PushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.add_row_repeat_PushButton.setObjectName(_fromUtf8("add_row_repeat_PushButton"))
        self.gridLayout_17.addWidget(self.add_row_repeat_PushButton, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem2, 4, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_17, 2, 0, 1, 4)
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.clear_init_table_PushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_init_table_PushButton.sizePolicy().hasHeightForWidth())
        self.clear_init_table_PushButton.setSizePolicy(sizePolicy)
        self.clear_init_table_PushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.clear_init_table_PushButton.setObjectName(_fromUtf8("clear_init_table_PushButton"))
        self.gridLayout_11.addWidget(self.clear_init_table_PushButton, 4, 1, 1, 1)
        self.add_row_init_PushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_row_init_PushButton.sizePolicy().hasHeightForWidth())
        self.add_row_init_PushButton.setSizePolicy(sizePolicy)
        self.add_row_init_PushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.add_row_init_PushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.add_row_init_PushButton.setBaseSize(QtCore.QSize(40, 0))
        self.add_row_init_PushButton.setToolTip(_fromUtf8(""))
        self.add_row_init_PushButton.setObjectName(_fromUtf8("add_row_init_PushButton"))
        self.gridLayout_11.addWidget(self.add_row_init_PushButton, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 150, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem3, 0, 1, 1, 1)
        self.init_block_TableWidget = QtGui.QTableWidget(self.tab_2)
        self.init_block_TableWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.init_block_TableWidget.sizePolicy().hasHeightForWidth())
        self.init_block_TableWidget.setSizePolicy(sizePolicy)
        self.init_block_TableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.init_block_TableWidget.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.init_block_TableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.init_block_TableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.init_block_TableWidget.setRowCount(6)
        self.init_block_TableWidget.setColumnCount(16)
        self.init_block_TableWidget.setObjectName(_fromUtf8("init_block_TableWidget"))
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.init_block_TableWidget.setHorizontalHeaderItem(15, item)
        self.gridLayout_11.addWidget(self.init_block_TableWidget, 0, 0, 6, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem4, 5, 1, 1, 1)
        self.delete_row_init_PushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_row_init_PushButton.sizePolicy().hasHeightForWidth())
        self.delete_row_init_PushButton.setSizePolicy(sizePolicy)
        self.delete_row_init_PushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.delete_row_init_PushButton.setObjectName(_fromUtf8("delete_row_init_PushButton"))
        self.gridLayout_11.addWidget(self.delete_row_init_PushButton, 3, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_11, 1, 0, 1, 4)
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_14 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_13.addWidget(self.label_8, 1, 0, 1, 1)
        self.block_length_bin_SpinBox = QtGui.QSpinBox(self.groupBox)
        self.block_length_bin_SpinBox.setMaximumSize(QtCore.QSize(16777215, 18))
        self.block_length_bin_SpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.block_length_bin_SpinBox.setReadOnly(True)
        self.block_length_bin_SpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.block_length_bin_SpinBox.setMaximum(99999999)
        self.block_length_bin_SpinBox.setObjectName(_fromUtf8("block_length_bin_SpinBox"))
        self.gridLayout_13.addWidget(self.block_length_bin_SpinBox, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_13.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_13.addWidget(self.label_9, 2, 0, 1, 1)
        self.block_size_DoubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.block_size_DoubleSpinBox.setMaximumSize(QtCore.QSize(16777215, 18))
        self.block_size_DoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.block_size_DoubleSpinBox.setReadOnly(True)
        self.block_size_DoubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.block_size_DoubleSpinBox.setDecimals(6)
        self.block_size_DoubleSpinBox.setObjectName(_fromUtf8("block_size_DoubleSpinBox"))
        self.gridLayout_13.addWidget(self.block_size_DoubleSpinBox, 2, 1, 1, 1)
        self.laser_pulses_SpinBox = QtGui.QSpinBox(self.groupBox)
        self.laser_pulses_SpinBox.setMaximumSize(QtCore.QSize(16777215, 18))
        self.laser_pulses_SpinBox.setWrapping(False)
        self.laser_pulses_SpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.laser_pulses_SpinBox.setReadOnly(True)
        self.laser_pulses_SpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.laser_pulses_SpinBox.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.laser_pulses_SpinBox.setMaximum(99999999)
        self.laser_pulses_SpinBox.setProperty("value", 0)
        self.laser_pulses_SpinBox.setObjectName(_fromUtf8("laser_pulses_SpinBox"))
        self.gridLayout_13.addWidget(self.laser_pulses_SpinBox, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_13.addWidget(self.label_10, 3, 0, 1, 1)
        self.block_length_ms_DoubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.block_length_ms_DoubleSpinBox.setMaximumSize(QtCore.QSize(16777215, 18))
        self.block_length_ms_DoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.block_length_ms_DoubleSpinBox.setReadOnly(True)
        self.block_length_ms_DoubleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.block_length_ms_DoubleSpinBox.setSuffix(_fromUtf8(""))
        self.block_length_ms_DoubleSpinBox.setDecimals(5)
        self.block_length_ms_DoubleSpinBox.setMaximum(10000.0)
        self.block_length_ms_DoubleSpinBox.setProperty("value", 0.0)
        self.block_length_ms_DoubleSpinBox.setObjectName(_fromUtf8("block_length_ms_DoubleSpinBox"))
        self.gridLayout_13.addWidget(self.block_length_ms_DoubleSpinBox, 0, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 0, 3, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_9.setHorizontalSpacing(24)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_9.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 1)
        self.block_list_ComboBox = QtGui.QComboBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.block_list_ComboBox.sizePolicy().hasHeightForWidth())
        self.block_list_ComboBox.setSizePolicy(sizePolicy)
        self.block_list_ComboBox.setObjectName(_fromUtf8("block_list_ComboBox"))
        self.gridLayout_9.addWidget(self.block_list_ComboBox, 0, 1, 1, 1)
        self.clear_table_PushButton = QtGui.QPushButton(self.tab_2)
        self.clear_table_PushButton.setObjectName(_fromUtf8("clear_table_PushButton"))
        self.gridLayout_9.addWidget(self.clear_table_PushButton, 2, 2, 1, 1)
        self.save_block_PushButton = QtGui.QPushButton(self.tab_2)
        self.save_block_PushButton.setObjectName(_fromUtf8("save_block_PushButton"))
        self.gridLayout_9.addWidget(self.save_block_PushButton, 1, 2, 1, 1)
        self.current_block_LineEdit = QtGui.QLineEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_block_LineEdit.sizePolicy().hasHeightForWidth())
        self.current_block_LineEdit.setSizePolicy(sizePolicy)
        self.current_block_LineEdit.setObjectName(_fromUtf8("current_block_LineEdit"))
        self.gridLayout_9.addWidget(self.current_block_LineEdit, 1, 1, 1, 1)
        self.delete_block_PushButton = QtGui.QPushButton(self.tab_2)
        self.delete_block_PushButton.setObjectName(_fromUtf8("delete_block_PushButton"))
        self.gridLayout_9.addWidget(self.delete_block_PushButton, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.tab_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 899, 662))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_16 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_15 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.gridLayout_15.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings_Sequence = QtGui.QAction(MainWindow)
        self.actionSettings_Sequence.setObjectName(_fromUtf8("actionSettings_Sequence"))
        self.actionSettings_Block_Generation = QtGui.QAction(MainWindow)
        self.actionSettings_Block_Generation.setObjectName(_fromUtf8("actionSettings_Block_Generation"))
        self.actionSettings_Sequence_Editor = QtGui.QAction(MainWindow)
        self.actionSettings_Sequence_Editor.setObjectName(_fromUtf8("actionSettings_Sequence_Editor"))
        self.menuSettings.addAction(self.actionSettings_Sequence)
        self.menuSettings.addAction(self.actionSettings_Block_Generation)
        self.menuSettings.addAction(self.actionSettings_Sequence_Editor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Pulse Sequence to run:", None))
        self.label.setText(_translate("MainWindow", "FastCounter binning", None))
        self.idle_RadioButton.setText(_translate("MainWindow", "Idle", None))
        self.run_RadioButton.setText(_translate("MainWindow", "Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Analysis", None))
        self.label_5.setText(_translate("MainWindow", "LaserChannel:", None))
        self.label_6.setText(_translate("MainWindow", "Sampling Freq. (MHz)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ACh0\n"
"Function", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ACh0\n"
"Freq. (GHz)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ACh0\n"
"Ampl. (V)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ACh0\n"
"Phase (°)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DCh0", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DCh1", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ACh1\n"
"Function", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ACh1\n"
"Freq. (GHz)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ACh1\n"
"Ampl. (V)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "ACh1\n"
"Phase (°)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "DCh2", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "DCh3", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Length (ns)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Inc. (ns)", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Repeat?", None))
        item = self.repeat_block_TableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Use as tau?", None))
        self.clear_repeat_table_PushButton.setText(_translate("MainWindow", "Clear", None))
        self.del_row_repeat_PushButton.setText(_translate("MainWindow", "Del.", None))
        self.add_row_repeat_PushButton.setText(_translate("MainWindow", "Add", None))
        self.clear_init_table_PushButton.setText(_translate("MainWindow", "Clear", None))
        self.add_row_init_PushButton.setText(_translate("MainWindow", "Add", None))
        self.init_block_TableWidget.setSortingEnabled(False)
        item = self.init_block_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ACh0\n"
"Function", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ACh0\n"
"Freq. (GHz)", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ACh0\n"
"Ampl. (V)", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ACh0\n"
"Phase (°)", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DCh0", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DCh1", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ACh1\n"
"Function", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ACh1\n"
"Freq. (GHz)", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ACh1\n"
"Ampl. (V)", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "ACh1\n"
"Phase (°)", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "DCh2", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "DCh3", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Length (ns)", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Inc. (ns)", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Repeat?", None))
        item = self.init_block_TableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Use as tau?", None))
        self.delete_row_init_PushButton.setText(_translate("MainWindow", "Del.", None))
        self.groupBox.setTitle(_translate("MainWindow", "Current Block Information", None))
        self.label_8.setText(_translate("MainWindow", "Length (bins):", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Length (μs):</p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "Size (MB)", None))
        self.label_10.setText(_translate("MainWindow", "# of Laserpulses:", None))
        self.label_12.setText(_translate("MainWindow", "Current Block:", None))
        self.label_11.setText(_translate("MainWindow", "Choose Block:", None))
        self.clear_table_PushButton.setText(_translate("MainWindow", "Clear Table", None))
        self.save_block_PushButton.setText(_translate("MainWindow", "Save Block", None))
        self.delete_block_PushButton.setText(_translate("MainWindow", "Delete Block", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Block Generator", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Sequence Editor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "PulseExtraction", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.actionSettings_Sequence.setText(_translate("MainWindow", "Settings: Analysis", None))
        self.actionSettings_Block_Generation.setText(_translate("MainWindow", "Settings: Block Generation", None))
        self.actionSettings_Sequence_Editor.setText(_translate("MainWindow", "Settings: Sequence Editor", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelemGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(836, 600))
        MainWindow.setMaximumSize(QtCore.QSize(836, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 290, 592, 104))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.AircraftBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.AircraftBox.setContentsMargins(0, 0, 0, 0)
        self.AircraftBox.setObjectName("AircraftBox")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.AircraftBox.addWidget(self.label_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.alt_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alt_label.sizePolicy().hasHeightForWidth())
        self.alt_label.setSizePolicy(sizePolicy)
        self.alt_label.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label.setBaseSize(QtCore.QSize(0, 0))
        self.alt_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.alt_label.setObjectName("alt_label")
        self.gridLayout_3.addWidget(self.alt_label, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.aoa_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aoa_number.sizePolicy().hasHeightForWidth())
        self.aoa_number.setSizePolicy(sizePolicy)
        self.aoa_number.setMinimumSize(QtCore.QSize(150, 40))
        self.aoa_number.setDigitCount(7)
        self.aoa_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.aoa_number.setObjectName("aoa_number")
        self.gridLayout_3.addWidget(self.aoa_number, 1, 3, 1, 1)
        self.alt_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alt_number.sizePolicy().hasHeightForWidth())
        self.alt_number.setSizePolicy(sizePolicy)
        self.alt_number.setMinimumSize(QtCore.QSize(150, 40))
        self.alt_number.setDigitCount(7)
        self.alt_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.alt_number.setObjectName("alt_number")
        self.gridLayout_3.addWidget(self.alt_number, 1, 2, 1, 1)
        self.ias_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ias_number.sizePolicy().hasHeightForWidth())
        self.ias_number.setSizePolicy(sizePolicy)
        self.ias_number.setMinimumSize(QtCore.QSize(120, 40))
        self.ias_number.setDigitCount(6)
        self.ias_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ias_number.setObjectName("ias_number")
        self.gridLayout_3.addWidget(self.ias_number, 1, 1, 1, 1)
        self.ias_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ias_label.sizePolicy().hasHeightForWidth())
        self.ias_label.setSizePolicy(sizePolicy)
        self.ias_label.setMinimumSize(QtCore.QSize(0, 0))
        self.ias_label.setBaseSize(QtCore.QSize(0, 0))
        self.ias_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.ias_label.setObjectName("ias_label")
        self.gridLayout_3.addWidget(self.ias_label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.aoa_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aoa_label.sizePolicy().hasHeightForWidth())
        self.aoa_label.setSizePolicy(sizePolicy)
        self.aoa_label.setMinimumSize(QtCore.QSize(0, 0))
        self.aoa_label.setBaseSize(QtCore.QSize(0, 0))
        self.aoa_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.aoa_label.setObjectName("aoa_label")
        self.gridLayout_3.addWidget(self.aoa_label, 0, 3, 1, 1)
        self.tplus_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tplus_label.sizePolicy().hasHeightForWidth())
        self.tplus_label.setSizePolicy(sizePolicy)
        self.tplus_label.setMinimumSize(QtCore.QSize(0, 0))
        self.tplus_label.setBaseSize(QtCore.QSize(0, 0))
        self.tplus_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.tplus_label.setObjectName("tplus_label")
        self.gridLayout_3.addWidget(self.tplus_label, 0, 0, 1, 1)
        self.tplus_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.tplus_number.setMinimumSize(QtCore.QSize(100, 0))
        self.tplus_number.setDigitCount(7)
        self.tplus_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.tplus_number.setObjectName("tplus_number")
        self.gridLayout_3.addWidget(self.tplus_number, 1, 0, 1, 1)
        self.AircraftBox.addLayout(self.gridLayout_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 20, 778, 233))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.EngineBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.EngineBox.setContentsMargins(0, 0, 0, 0)
        self.EngineBox.setObjectName("EngineBox")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.EngineBox.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.rpm_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rpm_label.sizePolicy().hasHeightForWidth())
        self.rpm_label.setSizePolicy(sizePolicy)
        self.rpm_label.setMinimumSize(QtCore.QSize(63, 0))
        self.rpm_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.rpm_label.setObjectName("rpm_label")
        self.gridLayout_5.addWidget(self.rpm_label, 0, 0, 1, 1)
        self.bat_voltage_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bat_voltage_label.sizePolicy().hasHeightForWidth())
        self.bat_voltage_label.setSizePolicy(sizePolicy)
        self.bat_voltage_label.setMinimumSize(QtCore.QSize(63, 0))
        self.bat_voltage_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.bat_voltage_label.setObjectName("bat_voltage_label")
        self.gridLayout_5.addWidget(self.bat_voltage_label, 0, 3, 1, 1)
        self.rpm_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rpm_number.sizePolicy().hasHeightForWidth())
        self.rpm_number.setSizePolicy(sizePolicy)
        self.rpm_number.setMinimumSize(QtCore.QSize(150, 40))
        self.rpm_number.setDigitCount(7)
        self.rpm_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.rpm_number.setObjectName("rpm_number")
        self.gridLayout_5.addWidget(self.rpm_number, 1, 0, 1, 1)
        self.pump_power_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pump_power_number.sizePolicy().hasHeightForWidth())
        self.pump_power_number.setSizePolicy(sizePolicy)
        self.pump_power_number.setMinimumSize(QtCore.QSize(100, 40))
        self.pump_power_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.pump_power_number.setObjectName("pump_power_number")
        self.gridLayout_5.addWidget(self.pump_power_number, 1, 2, 1, 1)
        self.egt_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.egt_label.sizePolicy().hasHeightForWidth())
        self.egt_label.setSizePolicy(sizePolicy)
        self.egt_label.setMinimumSize(QtCore.QSize(63, 0))
        self.egt_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.egt_label.setObjectName("egt_label")
        self.gridLayout_5.addWidget(self.egt_label, 0, 1, 1, 1)
        self.bat_voltage_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bat_voltage_number.sizePolicy().hasHeightForWidth())
        self.bat_voltage_number.setSizePolicy(sizePolicy)
        self.bat_voltage_number.setMinimumSize(QtCore.QSize(100, 40))
        self.bat_voltage_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bat_voltage_number.setObjectName("bat_voltage_number")
        self.gridLayout_5.addWidget(self.bat_voltage_number, 1, 3, 1, 1)
        self.egt_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.egt_number.sizePolicy().hasHeightForWidth())
        self.egt_number.setSizePolicy(sizePolicy)
        self.egt_number.setMinimumSize(QtCore.QSize(150, 40))
        self.egt_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.egt_number.setObjectName("egt_number")
        self.gridLayout_5.addWidget(self.egt_number, 1, 1, 1, 1)
        self.pump_power_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pump_power_label.sizePolicy().hasHeightForWidth())
        self.pump_power_label.setSizePolicy(sizePolicy)
        self.pump_power_label.setMinimumSize(QtCore.QSize(150, 0))
        self.pump_power_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pump_power_label.setObjectName("pump_power_label")
        self.gridLayout_5.addWidget(self.pump_power_label, 0, 2, 1, 1)
        self.throttle_pct_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.throttle_pct_label.sizePolicy().hasHeightForWidth())
        self.throttle_pct_label.setSizePolicy(sizePolicy)
        self.throttle_pct_label.setMinimumSize(QtCore.QSize(150, 0))
        self.throttle_pct_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.throttle_pct_label.setObjectName("throttle_pct_label")
        self.gridLayout_5.addWidget(self.throttle_pct_label, 2, 0, 1, 1)
        self.throttle_pct_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.throttle_pct_number.sizePolicy().hasHeightForWidth())
        self.throttle_pct_number.setSizePolicy(sizePolicy)
        self.throttle_pct_number.setMinimumSize(QtCore.QSize(100, 40))
        self.throttle_pct_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.throttle_pct_number.setObjectName("throttle_pct_number")
        self.gridLayout_5.addWidget(self.throttle_pct_number, 3, 0, 1, 1)
        self.fuel_pct_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fuel_pct_label.sizePolicy().hasHeightForWidth())
        self.fuel_pct_label.setSizePolicy(sizePolicy)
        self.fuel_pct_label.setMinimumSize(QtCore.QSize(63, 0))
        self.fuel_pct_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.fuel_pct_label.setObjectName("fuel_pct_label")
        self.gridLayout_5.addWidget(self.fuel_pct_label, 2, 1, 1, 1)
        self.fuel_pct_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fuel_pct_number.sizePolicy().hasHeightForWidth())
        self.fuel_pct_number.setSizePolicy(sizePolicy)
        self.fuel_pct_number.setMinimumSize(QtCore.QSize(100, 40))
        self.fuel_pct_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.fuel_pct_number.setObjectName("fuel_pct_number")
        self.gridLayout_5.addWidget(self.fuel_pct_number, 3, 1, 1, 1)
        self.load_cell_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_cell_label.sizePolicy().hasHeightForWidth())
        self.load_cell_label.setSizePolicy(sizePolicy)
        self.load_cell_label.setMinimumSize(QtCore.QSize(63, 0))
        self.load_cell_label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.load_cell_label.setObjectName("load_cell_label")
        self.gridLayout_5.addWidget(self.load_cell_label, 2, 2, 1, 1)
        self.load_cell_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_cell_number.sizePolicy().hasHeightForWidth())
        self.load_cell_number.setSizePolicy(sizePolicy)
        self.load_cell_number.setMinimumSize(QtCore.QSize(100, 40))
        self.load_cell_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.load_cell_number.setObjectName("load_cell_number")
        self.gridLayout_5.addWidget(self.load_cell_number, 3, 2, 1, 1)
        self.EngineBox.addLayout(self.gridLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.eng_status_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.eng_status_label.setObjectName("eng_status_label")
        self.horizontalLayout_2.addWidget(self.eng_status_label, 0, QtCore.Qt.AlignVCenter)
        self.eng_status_box = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.eng_status_box.setMaximumSize(QtCore.QSize(16777215, 40))
        self.eng_status_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.eng_status_box.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(172, 172, 172);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgb(122, 122, 122);")
        self.eng_status_box.setObjectName("eng_status_box")
        self.horizontalLayout_2.addWidget(self.eng_status_box, 0, QtCore.Qt.AlignVCenter)
        self.EngineBox.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(130, 440, 592, 104))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.AircraftBox_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.AircraftBox_2.setContentsMargins(0, 0, 0, 0)
        self.AircraftBox_2.setObjectName("AircraftBox_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.AircraftBox_2.addWidget(self.label_4)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.packet_loss_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packet_loss_number.sizePolicy().hasHeightForWidth())
        self.packet_loss_number.setSizePolicy(sizePolicy)
        self.packet_loss_number.setMinimumSize(QtCore.QSize(150, 40))
        self.packet_loss_number.setDigitCount(7)
        self.packet_loss_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.packet_loss_number.setObjectName("packet_loss_number")
        self.gridLayout_4.addWidget(self.packet_loss_number, 1, 2, 1, 1)
        self.alt_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alt_label_2.sizePolicy().hasHeightForWidth())
        self.alt_label_2.setSizePolicy(sizePolicy)
        self.alt_label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label_2.setBaseSize(QtCore.QSize(0, 0))
        self.alt_label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.alt_label_2.setObjectName("alt_label_2")
        self.gridLayout_4.addWidget(self.alt_label_2, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.rssi_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rssi_number.sizePolicy().hasHeightForWidth())
        self.rssi_number.setSizePolicy(sizePolicy)
        self.rssi_number.setMinimumSize(QtCore.QSize(120, 40))
        self.rssi_number.setDigitCount(6)
        self.rssi_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.rssi_number.setObjectName("rssi_number")
        self.gridLayout_4.addWidget(self.rssi_number, 1, 1, 1, 1)
        self.ias_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ias_label_2.sizePolicy().hasHeightForWidth())
        self.ias_label_2.setSizePolicy(sizePolicy)
        self.ias_label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.ias_label_2.setBaseSize(QtCore.QSize(0, 0))
        self.ias_label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.ias_label_2.setObjectName("ias_label_2")
        self.gridLayout_4.addWidget(self.ias_label_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.bat_voltage_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bat_voltage_label_2.sizePolicy().hasHeightForWidth())
        self.bat_voltage_label_2.setSizePolicy(sizePolicy)
        self.bat_voltage_label_2.setMinimumSize(QtCore.QSize(63, 0))
        self.bat_voltage_label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.bat_voltage_label_2.setObjectName("bat_voltage_label_2")
        self.gridLayout_4.addWidget(self.bat_voltage_label_2, 0, 0, 1, 1)
        self.px_bat_voltage_number = QtWidgets.QLCDNumber(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.px_bat_voltage_number.sizePolicy().hasHeightForWidth())
        self.px_bat_voltage_number.setSizePolicy(sizePolicy)
        self.px_bat_voltage_number.setMinimumSize(QtCore.QSize(100, 40))
        self.px_bat_voltage_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.px_bat_voltage_number.setObjectName("px_bat_voltage_number")
        self.gridLayout_4.addWidget(self.px_bat_voltage_number, 1, 0, 1, 1)
        self.AircraftBox_2.addLayout(self.gridLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RAPTA Telemetry"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Aircraft Data</span></p></body></html>"))
        self.alt_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Altitude</p></body></html>"))
        self.ias_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">IAS</p></body></html>"))
        self.aoa_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">AoA</p></body></html>"))
        self.tplus_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">T+</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Engine Data</span></p></body></html>"))
        self.rpm_label.setText(_translate("MainWindow", "<p align=\"center\">RPM</p>"))
        self.bat_voltage_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Bat V</p></body></html>"))
        self.egt_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">EGT</p></body></html>"))
        self.pump_power_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Pump Power</p></body></html>"))
        self.throttle_pct_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Throttle %</p></body></html>"))
        self.fuel_pct_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Fuel %</p></body></html>"))
        self.load_cell_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Load Cell</p></body></html>"))
        self.eng_status_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Status</span></p></body></html>"))
        self.eng_status_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Aircraft Status</span></p></body></html>"))
        self.alt_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Packet Loss %</p></body></html>"))
        self.ias_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">RSSI %</p></body></html>"))
        self.bat_voltage_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Bat V</p></body></html>"))

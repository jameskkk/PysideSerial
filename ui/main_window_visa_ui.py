# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_visa.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(666, 545))
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 641, 518))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.com_label = QLabel(self.verticalLayoutWidget)
        self.com_label.setObjectName(u"com_label")
        sizePolicy.setHeightForWidth(self.com_label.sizePolicy().hasHeightForWidth())
        self.com_label.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.com_label)

        self.com_combo = QComboBox(self.verticalLayoutWidget)
        self.com_combo.setObjectName(u"com_combo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.com_combo.sizePolicy().hasHeightForWidth())
        self.com_combo.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.com_combo)

        self.baudrate_label = QLabel(self.verticalLayoutWidget)
        self.baudrate_label.setObjectName(u"baudrate_label")
        sizePolicy.setHeightForWidth(self.baudrate_label.sizePolicy().hasHeightForWidth())
        self.baudrate_label.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.baudrate_label)

        self.baudrate_spinbox = QSpinBox(self.verticalLayoutWidget)
        self.baudrate_spinbox.setObjectName(u"baudrate_spinbox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.baudrate_spinbox.sizePolicy().hasHeightForWidth())
        self.baudrate_spinbox.setSizePolicy(sizePolicy3)
        self.baudrate_spinbox.setMinimum(9600)
        self.baudrate_spinbox.setMaximum(115200)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.baudrate_spinbox)

        self.data_bits_label = QLabel(self.verticalLayoutWidget)
        self.data_bits_label.setObjectName(u"data_bits_label")
        sizePolicy.setHeightForWidth(self.data_bits_label.sizePolicy().hasHeightForWidth())
        self.data_bits_label.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.data_bits_label)

        self.data_bits_combo = QComboBox(self.verticalLayoutWidget)
        self.data_bits_combo.setObjectName(u"data_bits_combo")
        sizePolicy3.setHeightForWidth(self.data_bits_combo.sizePolicy().hasHeightForWidth())
        self.data_bits_combo.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.data_bits_combo)

        self.stop_bits_label = QLabel(self.verticalLayoutWidget)
        self.stop_bits_label.setObjectName(u"stop_bits_label")
        sizePolicy.setHeightForWidth(self.stop_bits_label.sizePolicy().hasHeightForWidth())
        self.stop_bits_label.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.stop_bits_label)

        self.stop_bits_combo = QComboBox(self.verticalLayoutWidget)
        self.stop_bits_combo.setObjectName(u"stop_bits_combo")
        sizePolicy3.setHeightForWidth(self.stop_bits_combo.sizePolicy().hasHeightForWidth())
        self.stop_bits_combo.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.stop_bits_combo)

        self.command_label = QLabel(self.verticalLayoutWidget)
        self.command_label.setObjectName(u"command_label")
        sizePolicy.setHeightForWidth(self.command_label.sizePolicy().hasHeightForWidth())
        self.command_label.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.command_label)

        self.command_edit = QLineEdit(self.verticalLayoutWidget)
        self.command_edit.setObjectName(u"command_edit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.command_edit)

        self.receiver_label = QLabel(self.verticalLayoutWidget)
        self.receiver_label.setObjectName(u"receiver_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.receiver_label)

        self.receiver_text = QTextEdit(self.verticalLayoutWidget)
        self.receiver_text.setObjectName(u"receiver_text")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.receiver_text)

        self.connect_button = QPushButton(self.verticalLayoutWidget)
        self.connect_button.setObjectName(u"connect_button")
        sizePolicy3.setHeightForWidth(self.connect_button.sizePolicy().hasHeightForWidth())
        self.connect_button.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.connect_button)

        self.disconnect_button = QPushButton(self.verticalLayoutWidget)
        self.disconnect_button.setObjectName(u"disconnect_button")
        self.disconnect_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.disconnect_button.sizePolicy().hasHeightForWidth())
        self.disconnect_button.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.disconnect_button)

        self.refresh_button = QPushButton(self.verticalLayoutWidget)
        self.refresh_button.setObjectName(u"refresh_button")
        sizePolicy3.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.refresh_button)

        self.send_button = QPushButton(self.verticalLayoutWidget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.send_button)

        self.status_label = QLabel(self.verticalLayoutWidget)
        self.status_label.setObjectName(u"status_label")
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.status_label)

        self.clear_button = QPushButton(self.verticalLayoutWidget)
        self.clear_button.setObjectName(u"clear_button")
        sizePolicy3.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.clear_button)

        self.check_visa = QCheckBox(self.verticalLayoutWidget)
        self.check_visa.setObjectName(u"check_visa")
        self.check_visa.setChecked(True)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.check_visa)


        self.verticalLayout.addLayout(self.formLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Serial Port Tool", None))
        self.com_label.setText(QCoreApplication.translate("MainWindow", u"Select COM Port:", None))
        self.baudrate_label.setText(QCoreApplication.translate("MainWindow", u"Baudrate:", None))
        self.data_bits_label.setText(QCoreApplication.translate("MainWindow", u"Data Bits:", None))
        self.stop_bits_label.setText(QCoreApplication.translate("MainWindow", u"Stop Bits:", None))
        self.command_label.setText(QCoreApplication.translate("MainWindow", u"Send Command:", None))
        self.receiver_label.setText(QCoreApplication.translate("MainWindow", u"Receiver:", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnect_button.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh Ports", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send Command", None))
#if QT_CONFIG(shortcut)
        self.send_button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.check_visa.setText(QCoreApplication.translate("MainWindow", u"Visa Mode", None))
    # retranslateUi


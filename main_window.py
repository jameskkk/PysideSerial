import sys
import os
import serial
import serial.tools.list_ports
from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtCore import QThread, Signal
from main_window_ui import Ui_MainWindow
from password_dialog import PasswordDialog
import resources_rc


class SerialThread(QThread):
    data_received = Signal(str)

    def __init__(self, serial_port: serial.Serial):
        super().__init__()
        self.serial_port = serial_port
        self.running = True

    def run(self):
        while self.running:
            if self.serial_port and self.serial_port.is_open and self.serial_port.in_waiting > 0:
                received = self.serial_port.readline()
                data = received.decode("utf-8").strip()
                self.data_received.emit(data)

    def stop(self):
        self.running = False


class SerialTool(QMainWindow):
    def closeEvent(self, event: QCloseEvent):
        if self.serial_thread:
            self.serial_thread.stop()
        event.accept()
        # Make sure Application exit
        QApplication.instance().quit()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(640, 510)  # Fixed Windows size
        # self.setWindowIcon(QIcon("nkg.ico"))  # Set Windows ICON
        resources_rc.qInitResources()
        self.setWindowIcon(QIcon(":/nkg.ico"))  # Set icon from resource

        # Initialize COM Port
        self.populate_com_ports()

        # Initialize data bits
        self.ui.data_bits_combo.addItems(["5", "6", "7", "8"])
        self.ui.data_bits_combo.setCurrentIndex(3)  # Default 8 data bits

        # Initialize stop bits
        self.ui.stop_bits_combo.addItems(["1", "1.5", "2"])
        self.ui.stop_bits_combo.setCurrentIndex(0)  # Defaul set 1 stop bit

        # bind button clicked event
        self.ui.connect_button.clicked.connect(self.connect_serial)
        self.ui.disconnect_button.clicked.connect(self.disconnect_serial)
        self.ui.clear_button.clicked.connect(self.clear_message)
        self.ui.refresh_button.clicked.connect(self.refresh_ports)
        self.ui.send_button.clicked.connect(self.send_data)

        self.serial_port = None
        self.serial_thread = None

    def populate_com_ports(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                if "USB" in port.description.upper() or "USB" in port.hwid.upper():
                    self.ui.com_combo.addItem(port.device)
                    if not os.access(port.device, os.R_OK) or not os.access(port.device, os.W_OK):
                        dialog = PasswordDialog(device=port.device)
                        dialog.exec()
            else:
                self.ui.com_combo.addItem(port.device)

    def connect_serial(self):
        """Connect to selection COM Port"""
        com_port = self.ui.com_combo.currentText()
        baudrate = self.ui.baudrate_spinbox.value()
        data_bits = int(self.ui.data_bits_combo.currentText())
        try:
            if com_port != "":
                self.serial_port = serial.Serial(com_port, baudrate, data_bits, timeout=1)
                self.ui.send_button.setEnabled(True)
                self.ui.connect_button.setEnabled(False)
                self.ui.disconnect_button.setEnabled(True)
                self.ui.status_label.setText("Connected")

                self.serial_thread = SerialThread(self.serial_port)
                self.serial_thread.data_received.connect(self.receive_data)
                self.serial_thread.start()
            else:
                self.ui.status_label.setText("Please select COM port!")
        except Exception as e:
            self.ui.status_label.setText(f"Error: {e}")

    def disconnect_serial(self):
        """Disconnect COM Port"""
        try:
            if self.serial_port and self.serial_port.is_open:
                self.ui.send_button.setEnabled(False)
                self.ui.connect_button.setEnabled(True)
                self.ui.disconnect_button.setEnabled(False)
                if self.serial_thread:
                    self.serial_thread.stop()
                self.serial_port.close()
                self.ui.status_label.setText("Disconnected")
        except Exception as e:
            self.ui.status_label.setText(f"Error: {e}")

    def clear_message(self):
        self.ui.receiver_text.clear()

    def refresh_ports(self):
        """Reflash available COM Port list"""
        self.ui.com_combo.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.com_combo.addItem(port.device)

    def send_data(self):
        """Send serial command"""
        data = self.ui.command_edit.text()
        if self.serial_port and self.serial_port.is_open and data != "":
            self.serial_port.write(data.encode())
            self.ui.receiver_text.append("Send: " + data)

    def receive_data(self, data: str):
        """Receive serial message"""
        self.ui.receiver_text.append(f"Received: {data}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialTool()
    window.show()
    sys.exit(app.exec())

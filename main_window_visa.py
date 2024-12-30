import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtCore import QThread, Signal
from ui.main_window_visa_ui import Ui_MainWindow
from password_dialog import PasswordDialog
import resources_rc
import pyvisa


class SerialThread(QThread):
    data_received = Signal(str)

    def __init__(self, serial_port: pyvisa.Resource):
        super().__init__()
        self.serial_port = serial_port
        self.running = True

    def run(self):
        while self.running:
            if self.serial_port:
                received = self.serial_port.read()
                data = received.strip()
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
        self.resource_manager = None

    def populate_com_ports(self):
        self.ui.com_combo.clear()
        # 建立 Resource Manager
        self.resource_manager = pyvisa.ResourceManager("@py")
        # 列出所有可用資源
        ports = self.resource_manager.list_resources()
        for port in ports:
            if "USB" in port or "ASRL" in port:
                if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
                    if "/dev/ttyACM" in port:  # ASRL/dev/ttyACM0::INSTR
                        dev = port.split("::")[0].replace("ASRL", "")
                        self.ui.com_combo.addItem(port)
                        if not os.access(dev, os.R_OK) or not os.access(dev, os.W_OK):
                            dialog = PasswordDialog(device=dev)
                            dialog.exec()
                else:
                    self.ui.com_combo.addItem(port)

    def initialize_visa(self, com_port: str, baudrate: int, data_bits: int):
        try:
            self.resource_manager = pyvisa.ResourceManager("@py")
            self.serial_port = self.resource_manager.open_resource(com_port)
            self.serial_port.baud_rate = baudrate  # 設置與 Arduino 一致的波特率
            self.serial_port.data_bits = data_bits
            self.serial_port.parity = pyvisa.constants.Parity.none
            self.serial_port.stop_bits = pyvisa.constants.StopBits.one
            self.serial_port.timeout = 5000  # 設置逾時為 5 秒
            return True
        except Exception as e:
            print("Error:", e)
        return False

    def connect_serial(self):
        """Connect to selection COM Port"""
        com_port = self.ui.com_combo.currentText()
        baudrate = self.ui.baudrate_spinbox.value()
        data_bits = int(self.ui.data_bits_combo.currentText())
        try:
            if com_port != "" and self.initialize_visa(com_port, baudrate, data_bits):
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
            if self.serial_port:
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
        self.populate_com_ports()

    def send_data(self):
        """Send serial command"""
        data = self.ui.command_edit.text()
        if self.serial_port and data != "":
            self.serial_port.write(data)
            self.ui.receiver_text.append("Send: " + data)

    def receive_data(self, data: str):
        """Receive serial message"""
        self.ui.receiver_text.append(f"Received: {data}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialTool()
    window.show()
    sys.exit(app.exec())

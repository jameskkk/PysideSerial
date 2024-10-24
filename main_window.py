import sys
import serial
import serial.tools.list_ports
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window_ui import Ui_MainWindow

class SerialTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(640, 500) #固定視窗大小
        
        # Initialize COM Port
        self.populate_com_ports()

        # Initialize data bits
        self.ui.data_bits_combo.addItems(["5", "6", "7", "8"])
        self.ui.data_bits_combo.setCurrentIndex(3)  # 預設為8個資料位

        # Initialize stop bits
        self.ui.stop_bits_combo.addItems(["1", "1.5", "2"])
        self.ui.stop_bits_combo.setCurrentIndex(0)  # 預設為1個停止位

        # bind button clicked event
        self.ui.connect_button.clicked.connect(self.connect_serial)
        self.ui.disconnect_button.clicked.connect(self.disconnect_serial)
        self.ui.refresh_button.clicked.connect(self.refresh_ports)
        self.ui.send_button.clicked.connect(self.send_data)

        self.serial_port = None

    def populate_com_ports(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.com_combo.addItem(port.device)

    def connect_serial(self):
        """Connect to selection COM Port"""
        com_port = self.ui.com_combo.currentText()
        baudrate = self.ui.baudrate_spinbox.value()
        try:
            if com_port != "":
                self.serial_port = serial.Serial(com_port, baudrate)
                self.ui.send_button.setEnabled(True)
                self.ui.connect_button.setEnabled(False)
                self.ui.disconnect_button.setEnabled(True)
                self.ui.status_label.setText("Connected")
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
                self.serial_port.close()
                self.ui.status_label.setText("Disconnected")
        except Exception as e:
            self.ui.status_label.setText(f"Error: {e}")

    def refresh_ports(self):
        """Reflash available COM Port list"""
        self.ui.com_combo.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.com_combo.addItem(port.device)

    def send_data(self):
        """Send serial command"""
        if self.serial_port and self.serial_port.is_open:
            data = self.ui.command_edit.text().encode()
            self.serial_port.write(data)

    def receive_data(self):
        """Receive serial message"""
        if self.serial_port and self.serial_port.is_open:
            data = self.serial_port.read_all().decode()
            self.ui.receiver_text.append(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialTool()
    window.show()
    sys.exit(app.exec())

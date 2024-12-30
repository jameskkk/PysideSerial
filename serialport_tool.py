"""Serial port tool example"""
import serial
import serial.tools.list_ports
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QFormLayout, QSpinBox, QHBoxLayout


class SerialPortTool(QWidget):
    """SerialPortTool main class"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Port Tool")
        self.init_layout()

        self.serial_connection = None

    def init_layout(self):
        """Initialize UI layout"""
        # 介面布局
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # COM Port選擇
        self.com_label = QLabel("Select COM Port:")
        self.com_combo = QComboBox()
        self.refresh_ports()

        form_layout.addRow(self.com_label, self.com_combo)

        # 基本參數設置
        self.baudrate_label = QLabel("Baudrate:")
        self.baudrate_spinbox = QSpinBox()
        self.baudrate_spinbox.setRange(9600, 115200)
        self.baudrate_spinbox.setValue(9600)

        form_layout.addRow(self.baudrate_label, self.baudrate_spinbox)

        self.data_bits_label = QLabel("Data Bits:")
        self.data_bits_combo = QComboBox()
        self.data_bits_combo.addItems(["5", "6", "7", "8"])
        self.data_bits_combo.setCurrentIndex(3)  # 預設為8個資料位

        form_layout.addRow(self.data_bits_label, self.data_bits_combo)

        self.stop_bits_label = QLabel("Stop Bits:")
        self.stop_bits_combo = QComboBox()
        self.stop_bits_combo.addItems(["1", "1.5", "2"])
        self.stop_bits_combo.setCurrentIndex(0)  # 預設為1個停止位

        form_layout.addRow(self.stop_bits_label, self.stop_bits_combo)

        # 按鈕
        button_layout = QHBoxLayout()
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_serial)

        self.refresh_button = QPushButton("Refresh Ports")
        self.refresh_button.clicked.connect(self.refresh_ports)

        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.refresh_button)

        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def refresh_ports(self):
        """刷新可用的COM Port列表"""
        self.com_combo.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.com_combo.addItem(port.device)

    def connect_serial(self):
        """連接到選定的COM Port"""
        com_port = self.com_combo.currentText()
        baudrate = self.baudrate_spinbox.value()
        data_bits = int(self.data_bits_combo.currentText())
        stop_bits = float(self.stop_bits_combo.currentText())

        try:
            self.serial_connection = serial.Serial(port=com_port, baudrate=baudrate, bytesize=data_bits,
                                                   stopbits=stop_bits, timeout=1)
            print(f"Connected to {com_port} with baudrate {baudrate}")
        except Exception as e:
            print(f"Error connecting to {com_port}: {e}")

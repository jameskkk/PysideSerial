# import sys
import subprocess
from PySide6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QDialog, QLabel


class PasswordDialog(QDialog):
    def __init__(self, device=""):
        super().__init__()
        self.device = device
        self.setWindowTitle("Enter Admin Password")
        self.layout = QVBoxLayout()

        self.label = QLabel("Please enter the admin password:")
        self.layout.addWidget(self.label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_password)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def submit_password(self):
        password = self.password_input.text()
        self.run_chmod(password, self.device)
        self.accept()

    def run_chmod(self, password: str, device: str):
        # Example chmod command with sudo
        command = f"echo {password} | sudo -S chmod 666 {device}"
        try:
            # os.chmod(device, 0o666) 
            subprocess.run(command, shell=True, check=True)
            self.label.setText("Permission changed successfully!")
        except subprocess.CalledProcessError:
            self.label.setText("Failed to change permission.")
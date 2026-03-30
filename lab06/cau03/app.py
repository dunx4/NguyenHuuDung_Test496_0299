import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.Railfence import Ui_MainWindow
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "message": self.ui.txtPlaintext.toPlainText(),
            "key": int(self.ui.txtKey.text())  # thêm ô nhập key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtCiphertext.setText(data["encrypted_message"])

                QMessageBox.information(self, "Info", "Encrypted Successfully")
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "ciphertext": self.ui.txtCiphertext.toPlainText(),
            "key": int(self.ui.txtKey.text())
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtPlaintext.setText(data["decrypted_message"])

                QMessageBox.information(self, "Info", "Decrypted Successfully")
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
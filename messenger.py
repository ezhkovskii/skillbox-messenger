from PyQt5 import QtWidgets, QtCore
import clientui
import requests
from datetime import datetime


class MessengerWindow(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self, server_url):
        super().__init__()
        self.setupUi(self)
        self.server_url = server_url
        self.send.pressed.connect(self.send_message)
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load_messages)
        self.timer.start(1000)

    def pretty_message(self, message):
        dt = datetime.fromtimestamp(message['time'])
        dt_str = dt.strftime('%H:%M:%S')
        self.messages.append(message['name'] + ' ' + dt_str)
        self.messages.append(message['text'])
        self.messages.append('')
        self.messages.repaint()

    def load_messages(self):
        try:
            data = requests.get(self.server_url + '/messages',
                                params={'after': self.after}).json()
        except:
            return

        for message in data['messages']:
            self.pretty_message(message)
            self.after = message['time']

    def send_message(self):
        name = self.name.text()
        text = self.text.toPlainText()

        data = {'name': name, 'text': text}
        try:
            response = requests.post(self.server_url + '/send',
                                     json=data)
        except:
            self.messages.append('Сервер недоступен. Попробуйте позже.\n')
            self.messages.repaint()
            return

        if response.status_code != 200:
            self.messages.append('Неправильные данные\n')
            self.messages.repaint()
            return

        self.text.setText('')
        self.text.repaint()


app = QtWidgets.QApplication([])
window = MessengerWindow('http://127.0.0.1:5000')
window.show()
app.exec_()

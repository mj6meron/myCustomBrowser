from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton

app = QApplication([])

window = QWidget()
window.setWindowTitle('My Browser')

view = QWebEngineView(window)

url_bar = QLineEdit(window)

layout = QVBoxLayout()

# create a horizontal layout for the buttons
button_layout = QHBoxLayout()

# create the back button
back_button = QPushButton('Back')
back_button.clicked.connect(view.back)
button_layout.addWidget(back_button)

# create the forward button
forward_button = QPushButton('Forward')
forward_button.clicked.connect(view.forward)
button_layout.addWidget(forward_button)

# create the refresh button
refresh_button = QPushButton('Refresh')
refresh_button.clicked.connect(view.reload)
button_layout.addWidget(refresh_button)

# create the go button
go_button = QPushButton('Go')
go_button.clicked.connect(load_url)
button_layout.addWidget(go_button)

# add the URL bar and the buttons to the vertical layout
layout.addWidget(url_bar)
layout.addLayout(button_layout)
layout.addWidget(view)

# set the layout of the main window
window.setLayout(layout)

def load_url():
    url = url_bar.text()
    if not url.startswith('http'):
        url = 'http://' + url
    view.load(QUrl(url))

# set the OpenAI Chatbot page as the home page
view.load(QUrl('https://beta.openai.com/docs/models/gpt-3'))

window.show()

app.exec_()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение БД")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.query_input = QLineEdit()
        self.layout.addWidget(self.query_input)

        self.execute_button = QPushButton("Выполнить")
        self.execute_button.clicked.connect(self.execute_query)
        self.layout.addWidget(self.execute_button)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.create_database()

    def create_database(self):
        conn = sqlite3.connect("original.db")
        c = conn.cursor()

        # Создание таблиц
        c.execute("CREATE TABLE IF NOT EXISTS rang1 (name TEXT PRIMARY KEY, renewal_plus TEXT, renewal_multiply TEXT, renewal_super TEXT, code TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS rang2 (name TEXT PRIMARY KEY, renewal_plus TEXT, renewal_multiply TEXT, renewal_super TEXT, code TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS rang3 (name TEXT PRIMARY KEY, renewal_plus TEXT, renewal_multiply TEXT, renewal_super TEXT, code TEXT)")

        conn.commit()
        conn.close()

    def execute_query(self):
        query = self.query_input.text()

        if query:
            conn = sqlite3.connect(r"..\ItemDatabase\original.db")
            c = conn.cursor()

            c.execute(query)
            result = c.fetchall()

            self.table.setRowCount(len(result))
            self.table.setColumnCount(len(result[0]))

            for i, row in enumerate(result):
                for j, val in enumerate(row):
                    item = QTableWidgetItem(str(val))
                    self.table.setItem(i, j, item)

            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

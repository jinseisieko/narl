import sqlite3
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QDialog, \
    QHBoxLayout, QListWidget, QMessageBox, QSplitter
import json
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QDialog, \
    QHBoxLayout, QListWidget, QMessageBox, QSplitter

string_readonly_code_textedit = """
x

y

size_x

size_y

hp

vx

vy

max_velocity

slowdown

acceleration

max_hp

armor

delay

armor_piercing

bullet_size_x

bullet_size_y

bullet_damage

critical_coefficient

critical_chance

scatter

bullet_life_time

bullet_velocity

damage_delay"""


class NewItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New")

        self.item_name_label = QLabel("STRING:")
        self.item_name_lineedit = QLineEdit()
        self.item_name_button = QPushButton("OK")
        self.item_name_button.clicked.connect(self.accept)

        layout = QHBoxLayout()
        layout.addWidget(self.item_name_label)
        layout.addWidget(self.item_name_lineedit)
        layout.addWidget(self.item_name_button)
        self.setLayout(layout)

    def get_item_name(self):
        return self.item_name_lineedit.text()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Creator Items")

        self.name_label = QLabel("Name:")
        self.name_lineedit = QLineEdit()

        self.renewal_plus_label = QLabel("renewal_plus:")
        self.renewal_plus_list = QListWidget()

        self.renewal_multiply_label = QLabel("renewal_multiply:")
        self.renewal_multiply_list = QListWidget()

        self.renewal_super_label = QLabel("renewal_super:")
        self.renewal_super_list = QListWidget()

        self.renewal_plus_button = QPushButton("Add")
        self.renewal_plus_button.clicked.connect(self.renewal_plus)
        self.renewal_multiply_button = QPushButton("Add")
        self.renewal_multiply_button.clicked.connect(self.renewal_multiply)
        self.renewal_super_button = QPushButton("Add")
        self.renewal_super_button.clicked.connect(self.renewal_super)

        self.code_label = QLabel("code:")
        self.code_textedit = QTextEdit()

        self.press_button_button = QPushButton("Compile")
        self.press_button_button.clicked.connect(self.press_button)

        self.renewal_plus_list.itemClicked.connect(self.remove_item)
        self.renewal_multiply_list.itemClicked.connect(self.remove_item)
        self.renewal_super_list.itemClicked.connect(self.remove_item)

        self.readonly_code_label = QLabel("readonly")
        self.readonly_code_textedit = QTextEdit()
        self.readonly_code_textedit.setReadOnly(True)
        self.readonly_code_textedit.setText(string_readonly_code_textedit)

        main_layout = QHBoxLayout()

        general_layout = QVBoxLayout()
        general_layout.addWidget(self.name_label)
        general_layout.addWidget(self.name_lineedit)
        general_layout.addWidget(self.renewal_plus_label)
        general_layout.addWidget(self.renewal_plus_list)
        general_layout.addWidget(self.renewal_plus_button)
        general_layout.addWidget(self.renewal_multiply_label)
        general_layout.addWidget(self.renewal_multiply_list)
        general_layout.addWidget(self.renewal_multiply_button)
        general_layout.addWidget(self.renewal_super_label)
        general_layout.addWidget(self.renewal_super_list)
        general_layout.addWidget(self.renewal_super_button)
        general_layout.addWidget(self.press_button_button)

        code_layout = QVBoxLayout()
        code_layout.addWidget(self.code_label)
        code_layout.addWidget(self.code_textedit)

        readonly_layout = QVBoxLayout()
        readonly_layout.addWidget(self.readonly_code_label)
        readonly_layout.addWidget(self.readonly_code_textedit)

        splitter = QSplitter()
        general_widget = QWidget()
        general_widget.setLayout(general_layout)
        code_widget = QWidget()
        code_widget.setLayout(code_layout)
        readonly_widget = QWidget()
        readonly_widget.setLayout(readonly_layout)
        splitter.addWidget(readonly_widget)
        splitter.addWidget(general_widget)
        splitter.addWidget(code_widget)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        splitter.setStretchFactor(2, 2)

        main_layout.addWidget(splitter)

        self.setLayout(main_layout)

        self.resize(1300, 900)

    def remove_item(self, item):
        list_widget = self.sender()
        if isinstance(list_widget, QListWidget):
            row = list_widget.row(item)
            answer = QMessageBox.question(self, 'Удаление',
                                          f"Вы уверены, что хотите удалить элемент '{item.text()}'?",
                                          QMessageBox.Yes | QMessageBox.No)
            if answer == QMessageBox.Yes:
                list_widget.takeItem(row)

    def renewal_plus(self):
        dialog = NewItemDialog(self)
        if dialog.exec():
            item_name = dialog.get_item_name()
            self.renewal_plus_list.addItem(item_name)

    def renewal_multiply(self):
        dialog = NewItemDialog(self)
        if dialog.exec():
            item_name = dialog.get_item_name()
            self.renewal_multiply_list.addItem(item_name)

    def renewal_super(self):
        dialog = NewItemDialog(self)
        if dialog.exec():
            item_name = dialog.get_item_name()
            self.renewal_super_list.addItem(item_name)

    def get_name(self):
        return self.name_lineedit.text()

    def get_items(self):
        item1_items = [self.renewal_plus_list.item(i).text() for i in range(self.renewal_plus_list.count())]
        item2_items = [self.renewal_multiply_list.item(i).text() for i in range(self.renewal_multiply_list.count())]
        item3_items = [self.renewal_super_list.item(i).text() for i in range(self.renewal_super_list.count())]

        return item1_items, item2_items, item3_items

    def get_code(self):
        return self.code_textedit.toPlainText()

    def press_button(self):
        def convert_array_to_dict_int(array):
            result_dict = {}
            for item in array:
                key, value = item.split(" ")
                result_dict[key] = int(value)
            return result_dict

        def convert_array_to_dict_str(array):
            result_dict = {}
            for item in array:
                key, value = item.split(" ")
                result_dict[key] = value
            return result_dict

        name = self.get_name()
        code = self.get_code()
        renewal_plus, renewal_multiply, renewal_super = self.get_items()
        renewal_plus = json.dumps(convert_array_to_dict_int(renewal_plus))
        renewal_multiply = json.dumps(convert_array_to_dict_int(renewal_multiply))
        renewal_super = json.dumps(convert_array_to_dict_str(renewal_super))

        result = f"('{name}', '{renewal_plus}', '{renewal_multiply}', '{renewal_super}', '{code}')\n"
        with open(r"..\ItemDatabase\all.txt", "a", encoding="utf-8") as file:
            file.write("Insert: " + result)

        con = sqlite3.connect(r"..\ItemDatabase\original.db")
        cur = con.cursor()
        cur.execute(f"INSERT INTO items VALUES {result}")
        con.commit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())

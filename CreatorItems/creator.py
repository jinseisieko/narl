import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QDialog, \
    QHBoxLayout, QListWidget, QMessageBox, QSplitter


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

        self.press_button_button = QPushButton("Press Button")
        self.press_button_button.clicked.connect(self.press_button)

        self.renewal_plus_list.itemClicked.connect(self.remove_item)
        self.renewal_multiply_list.itemClicked.connect(self.remove_item)
        self.renewal_super_list.itemClicked.connect(self.remove_item)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.name_label)
        left_layout.addWidget(self.name_lineedit)
        left_layout.addWidget(self.renewal_plus_label)
        left_layout.addWidget(self.renewal_plus_list)
        left_layout.addWidget(self.renewal_plus_button)
        left_layout.addWidget(self.renewal_multiply_label)
        left_layout.addWidget(self.renewal_multiply_list)
        left_layout.addWidget(self.renewal_multiply_button)
        left_layout.addWidget(self.renewal_super_label)
        left_layout.addWidget(self.renewal_super_list)
        left_layout.addWidget(self.renewal_super_button)
        left_layout.addWidget(self.press_button_button)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.code_label)
        right_layout.addWidget(self.code_textedit)

        splitter = QSplitter()
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)

        main_layout.addWidget(splitter)

        self.setLayout(main_layout)

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

        return {
            "renewal_plus": item1_items,
            "renewal_multiply": item2_items,
            "renewal_super": item3_items
        }

    def get_code(self):
        return self.code_textedit.toPlainText()

    def press_button(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())

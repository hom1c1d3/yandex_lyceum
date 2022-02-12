import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxSchools = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSchools.sizePolicy().hasHeightForWidth())
        self.comboBoxSchools.setSizePolicy(sizePolicy)
        self.comboBoxSchools.setObjectName("comboBoxSchools")
        self.gridLayout.addWidget(self.comboBoxSchools, 0, 0, 1, 1)
        self.comboBoxForms = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxForms.sizePolicy().hasHeightForWidth())
        self.comboBoxForms.setSizePolicy(sizePolicy)
        self.comboBoxForms.setObjectName("comboBoxForms")
        self.gridLayout.addWidget(self.comboBoxForms, 0, 1, 1, 1)
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSubmit.sizePolicy().hasHeightForWidth())
        self.btnSubmit.setSizePolicy(sizePolicy)
        self.btnSubmit.setObjectName("btnSubmit")
        self.gridLayout.addWidget(self.btnSubmit, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Результат олимпиады: фильтрация"))
        self.btnSubmit.setText(_translate("MainWindow", "Узнать результаты"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.olimpiad_results = self.load_olimpiad_results('rez.csv')
        self.setupUi(self)

    @staticmethod
    def load_olimpiad_results(file_path):
        with open(file_path, encoding='utf8') as fd:
            olimpiad_results = csv.DictReader(fd, delimiter=',', quotechar='"')
            olimpiad_results = list(olimpiad_results)
        return olimpiad_results

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.display_table(self.olimpiad_results)
        self.set_filters()
        self.comboBoxSchools.currentTextChanged.connect(self.update_filters_forms)
        self.comboBoxSchools.currentTextChanged.emit(self.comboBoxSchools.currentText())
        self.btnSubmit.clicked.connect(self.apply_filters)

    def set_filters(self):
        forms_numbers = {row['login'].split('-')[-2] for row in self.olimpiad_results}
        self.comboBoxForms.clear()
        self.comboBoxForms.addItem('Все')
        self.comboBoxForms.addItems(sorted(forms_numbers))
        school_numbers = {row['login'].split('-')[-3] for row in self.olimpiad_results}
        self.comboBoxSchools.clear()
        self.comboBoxSchools.addItem('Все')
        self.comboBoxSchools.addItems(sorted(school_numbers))

    def update_filters_forms(self, school_filter):
        filter_func = (lambda row, ftr: row['login'].split('-')[-3] == ftr)
        forms_numbers = {row['login'].split('-')[-2] for row in self.olimpiad_results
                         if filter_func(row, row['login'].split('-')[-3]
                         if school_filter == 'Все' else school_filter)}
        self.comboBoxForms.clear()
        self.comboBoxForms.addItem('Все')
        self.comboBoxForms.addItems(sorted(forms_numbers))

    def display_table(self, olimpiad_results):
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['Фамилия', "Результат"])
        data = sorted(((row['user_name'].split()[-2], row['Score']) for row in olimpiad_results),
                      key=lambda x: float(x[1]), reverse=True)
        for row_ind, row in enumerate(data):
            self.tableWidget.setRowCount(row_ind + 1)
            for item_ind, item in enumerate(row):
                self.tableWidget.setItem(row_ind, item_ind, QtWidgets.QTableWidgetItem(item))

    def apply_filters(self):
        school_filter = self.comboBoxSchools.currentText()
        if school_filter == 'Все':
            olimpiad_results = self.olimpiad_results
        else:
            olimpiad_results = (row for row in self.olimpiad_results
                                if row['login'].split('-')[-3] == school_filter)
        forms_filter = self.comboBoxForms.currentText()
        if forms_filter == 'Все':
            olimpiad_results = olimpiad_results
        else:
            olimpiad_results = (row for row in olimpiad_results
                                if row['login'].split('-')[-2] == forms_filter)
        self.display_table(olimpiad_results)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

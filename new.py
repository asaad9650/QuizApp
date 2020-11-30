from PyQt5 import QtCore,QtGui , QtWidgets,uic
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import pyqtSlot,QTimer
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from socket import *
import socket


class Client(QDialog):
    #count = 0


    def __init__(self):
        length = 0
        self.count = 1
        super(Client,self).__init__()
        loadUi('Window.ui' , self)
        self.setWindowTitle('Quiz Application')
        self.setWindowIcon(QIcon('logooo.jpg'))

        self.btn_enter.clicked.connect(self.login_Btn)
        self.btn_next.clicked.connect(self.submit_Btn)
        self.frame_2.setEnabled(False)
        self.textEdit_question.setReadOnly(True)

        self.serverName = "192.168.1.108"
        self.serverPort = 10000
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((self.serverName, self.serverPort))

    @pyqtSlot()
    def login_Btn(self):
        #self.btn_enter.setEnabled(True)
        self.clientSocket.send(str(self.edit_name.text()).encode())
        self.clientSocket.send((str(self.edit_password.text)).encode())
        print(self.edit_name.text())
        print(self.edit_password.text())
        var = self.clientSocket.recv(1024).decode()
        print(var)
        self.frame.setEnabled(False)
        self.frame_2.setEnabled(True)
        length = self.clientSocket.recv(1024).decode()
        print('Total number of Questions: ' + str(length) + '\n')
        question = self.clientSocket.recv(1024).decode()
        self.textEdit_question.setText(question)
        #self.textEdit_question.setText("********* WELCOME TO QUIZ *********\n\nTotal number of questions "
        #                              + str(length)
        #                             + "\n" + "Click next to begin the QUIZ\n")
        #self.textEdit_question.setText("Total number of questions " + str(length) + "\n")


        #print(qustion.decode())

        #length = self.clientSocket.recv(1024)
        #print("Number of questions " + length + "\n")
        #length = int(length.decode())
        #self.textEdit_question.setText("Number of questions " + length + "\n")

        #count = 0
    @pyqtSlot()
    def submit_Btn(self):
        if(self.count <= 10):
            check = str(self.textEdit_answer.toPlainText())
            if(check == 'true' or check == 'false'):
                self.clientSocket.send(check.encode())
                self.textEdit_answer.setText('')
                print('Answer sent successfully.')
                self.count = self.count +1
                next_quest = self.clientSocket.recv(1024).decode()

                if self.count<=10:
                    self.textEdit_question.setText(next_quest)
                    print(self.count)
                    print(next_quest)
                else:
                    self.textEdit_question.setText("***** Summary of Quiz *****\n\n"
                                                   + str(next_quest)
                                                   + '\n\nYour Attendance is marked successfully.. !!'
                                                   + '\n*** Quiz End ***')
                    self.textEdit_answer.setReadOnly(True)
                    self.btn_next.setEnabled(False)
                    self.clientSocket.close()
            else:
                print('Answer not sent, Try Again.')

        #else:
            #self.textEdit_answer.setReadOnly(True)
            #print('10+')
            #result = self.clientSocket.recv(1024).decode()
            #self.textEdit_question.setText("***** Summary of Quiz *****\n"
                                   #+str(result)
                                   #+'\nYour Attendance is marked successfully.. !!'
                                   #+'\n*** Quiz End ***' )

        #self.btn_next.setEnabled(True)
        #question = self.clientSocket.recv(1024).decode()
        #if str(question)!="Question":
        #self.textEdit_question.setText(question)
        #check = str(self.textEdit_answer.toPlainText())
        #self.btn_next.setEnabled(False)

        #check = str(self.textEdit_answer.toPlainText())
        #while(self.textEdit_answer.toPlainText() != 'true'):
        #   check = str(self.textEdit_answer.toPlainText())
        #if check == 'true' or check == 'false':
        #print('Submit')
        #if (check == '' or check == ' '):
        #self.btn_next.setEnabled(False)
        #print('Dis')
        #else:
        #self.btn_next.setEnabled(True)
        #print('En')


if __name__ == "__main__":
    import sys


    app = QApplication(sys.argv)

    ui = Client()

    ui.show()
    sys.exit(app.exec())

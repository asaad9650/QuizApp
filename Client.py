from socket import *
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


serverName = "192.168.1.108"
serverPort = 10000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

message = clientSocket.recv(1024)  # for welcome and authentication info
msg=message.decode()
print (msg)
ans=input('Confirm Connecttion: ').encode()
clientSocket.send(ans)
#Name
msg1=clientSocket.recv(1024)
name=input(msg1.decode())
clientSocket.send(name.encode())
#Pass
pas=clientSocket.recv(1024)
paas=input(pas.decode())
clientSocket.send(paas.encode())
#Authantication
auth=clientSocket.recv(1024)
print(auth.decode())
#Question
qustion=clientSocket.recv(1024)
print(qustion.decode())
length = clientSocket.recv(1024)
length = int(length.decode())
print('Total Questions : ' , length )
i=1
print('\nWrite all your answers in lower case like: true/false\n')

while i<=length:
    Questions=clientSocket.recv(1024)
    print(Questions.decode())
    ans1=input('Enter Answer: ')
    con=input('Is Your answer is Conform [Y/N]: ')
    if con=='Y' or con=='y':
        clientSocket.send(ans1.encode())
    else:
        ans2=input('Enter Your New Answer: ')
        clientSocket.send(ans2.encode())
    i=i+1
    cls()
print('\n\n')
print('************** Summary of quiz **************')
score=clientSocket.recv(1024)
print(score.decode())
print('Your Attendance is marked successfully')
clientSocket.close()
exit(0)
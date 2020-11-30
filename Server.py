from socket import *
import threading
import time

global i
i = 0

class ThreadedServer():
    def listenToClient(self, client, addr):
        global i
        while True:
            string="Welcome to Quiz".encode()

            client.send(string) #Send first message to client
            authentication = client.recv(1024) #Get authentication input
            print(authentication)
            str1='Name <space> Surname: '.encode()

            client.send(str1)
            m1 = client.recv(1024) #Get name-surname data from user

            name, surname = na.split() #Split input and keep them in parameters

            str2 = 'Input Your Password: '.encode()
            client.send(str2)
            password = client.recv(1024) #Get password value
            pas=password.decode()
            na = name.decode()
            su=surname.decode()
            print ("Username: ", na)
            print ("Password: ", pas)

            file = open("students.txt", "r") #Open students txt file
            str_file = file.read() #Keep it in string.

            if (str_file.find(na[i]) != -1 and str_file.find(pas[i])): #if you can find username
                 #if you can find password
                arr6="Successfuly Authenticated!.\n".encode()
                client.send(arr6)
                file2 = open("attendance.txt", "w")	#open the authentication txt file
                file2.write(na) #write username
                file2.write(": yes") #if user successfuly authenticated, insert it to attendance txt file
                file2.close() #close file

                localtime1 = time.localtime(time.time())[4] #get local minute
                print ("Time->", time.localtime(time.time())[3], ":", time.localtime(time.time())[4] )#display time.

                #Open questions
                questionFile = open("questions.txt", "r")
                questions = questionFile.read()
                questions = [y for y in (x.strip() for x in questions.splitlines()) if y]
                questionFile.close()

                #Open answers
                answerFile = open("answers.txt","r")
                answers = answerFile.read()
                answers = [y for y in (x.strip() for x in answers.splitlines()) if y]
                answerFile.close()

                #Give +10 scores for each true answers
                client.send('Question\n'.encode())
                le=('\n'+str(len(questions))+'\n').encode()
                client.send(le)
                score = 0
                for number in range(0, len(questions)):

                    var = ('\n'+str(questions[number])).encode()
                    client.send(var)
                    answer = client.recv(1024).decode()

                    if answer.lower() == answers[number]:
                        score = score + 10
                    
	            #get localtime minute value again.
                localtime2 = time.localtime(time.time())[4]
                #subtract times.
                timestamp = localtime2 - localtime1
                #if>30 time is up.
                if timestamp > 30:
                    print ("Your time is up!\n")
                    client.close()
                    #display total score
                scr = na, su, "score", str(score), "bonus", str(10 / (timestamp + 1)), "total Score:", str(score + 10 / (timestamp + 1))
                print (scr)
                client.send(str(scr).encode())

        else:
            client.send("Authentication cannot be completed.\n")

        i = i + 1
        file.close()

        client.close()
    def __init__(self, serverPort, serverName):
        try:
            serverSocket = socket(AF_INET, SOCK_STREAM)
        except:
            print ("Socket cannot be created")
            exit(1)
            #Sockets are the endpoints of a bidirectional communications channel.
        print ("Socket is created")
        try:
            serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
            print ("Socket cannot be used")
            exit(1)
        print ("Socket is being used")
        try:
            serverSocket.bind(('', serverPort))

        except:
            print ("Binding cannot de done")
            exit(1)
        print ("Binding is done")
        try:
            serverSocket.listen(45)
        except:
            print ("Server cannot listen!")
            exit(1)
        print ("Server is ready to receive")

        while True:
            connectionSocket, addr = serverSocket.accept()

            threading.Thread(target=self.listenToClient, args=(connectionSocket, addr)).start()

if __name__ == "__main__":
    serverName = "192.168.1.108"
    serverPort = 10000
    ThreadedServer(serverPort, serverName)


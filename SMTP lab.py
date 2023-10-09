from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

mailserver = "smtp.freesmtpservers.com"
port = 25

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print ('220 reply not received from server.') 

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("After helo command: " + recv1)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

mailFrom = "MAIL FROM: <junkit.wong@sjsu.edu> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: " + recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

rcptTo = "RCPT TO: <rando@gmail.com>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: " + recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

    
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: " + recv4)
if recv4[:3] != '354':
    print('250 reply not received from server.')

subject = "Subject: SMTP TEST. \r\n\r\n"
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024).decode()
print("Response after sending message body:" + recv_msg)
if recv_msg[:3] != '250':
    print('250 reply not received from server.')

clientSocket.send("QUIT\r\n".encode())
message = clientSocket.recv(1024).decode()
print(message)
clientSocket.close()
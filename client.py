import socket
import threading
import time

SERVER = ('192.168.0.100', 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.connect(SERVER)

login = input('Введите свой логин: ')  # в логине нельзя использовать |, в логине и в сообщениях
# служебнные слова connecting, exit

message = login + 'connecting'
s.sendto(message.encode('utf-8'), SERVER)  # даем серверу знать о себе
del message


def get_message():  # принимаем сообщения
    while True:
        data = s.recv(1024)
        print(time.ctime(), data.decode('utf-8'))  # добавить время отправки с помощью модуля time


get_mess = threading.Thread(target=get_message)
get_mess.start()

try:
    print('Команда для выхода - [exit]')
    while True:  # отправляем сообщения
        opponent = input('Введите логин адресата: ')
        data = input('Введите сообщение:')
        message = opponent + '|' + '[{0}]: {1}'.format(login, data)  # шифруем сообщение:
        # (логин адресата)|[логин отправителя]: сообщение,
        # на сервере логин адресата будет обработан отдельно
        s.sendto(message.encode('utf-8'), SERVER)  # сообщение в формате
        print(message)
        del message

except opponent == 'exit' or data == 'exit':
    message = login + '|' + 'exit'
    s.sendto(message.encode('utf-8'), SERVER)  # уведомляем сервер о выходе
    exit()  # завершаем программу

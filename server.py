import socket

SERVER = ('192.168.0.100', 8080)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.connect(SERVER)
s.listen(5)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('', 0))
ss.connect(SERVER)
ss.listen(5)

users_online = {}


def message_operation(name, message, address):
    if name.decode('utf-8') in users_online.keys():
        ss.sendto(message, users_online[name.decode('utf-8')])
        print('message has been sent to', name.decode('utf-8'))
    else:
        ss.sendto('Пользователь не онлайн'.encode('utf-8'), address)
        print('user is not online')
    return 0


while True:
    data, address = s.recvfrom(1024)
    decoded_data = data.decode('utf-8')

    if decoded_data.find('connecting') != -1:  # переводим байты в строку
        name, connecting = decoded_data.split('|')  # в дальнейшем думаю использовать
        # функцию data.partition('|')
        print('connecting user', name)
        users_online.update({name: address})  # добавляем пользователя в список онлайн
        print('user connected')

    elif decoded_data.find('exit') != -1:
        name, exitt = decoded_data.split('|')
        del users_online[name]
    else:
        name, message = decoded_data.split('|')
        message_operation(name, message, address)

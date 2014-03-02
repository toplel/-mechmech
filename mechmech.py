import socket
import botconfig
import botSkills

def answer(x):
    global currentNick
    print ('>>>' + x) #DEBUG
    if x[:4] == 'PING':
        ret = ['PONG' + x[4:len(x)]]
    else:
        ret = []
        if ('PRIVMSG ' + botconfig.channel + ' :' in x) or ('PRIVMSG ' + currentNick + ' :' in x):
            rret = botSkills.shellInterpreter(x)
            for r in rret:
                ret.append('PRIVMSG ' + r[0] +' :' + r[1] + '\n')
                print('<<<' + r[1]) #DEBUG
    return ret

if __name__ == '__main__':
    currentNick = botconfig.nickList[0]
    sox = socket.socket()
    sox.connect((botconfig.host, botconfig.port))
    try:
        sox.recv(botconfig.buffer_size)
        sox.send(bytes('USER mecha mecha mecha :Mechabot\n', botconfig.charset))
        sox.send(bytes('NICK ' + currentNick + '\n', botconfig.charset))
        ping = str(sox.recv(botconfig.buffer_size), botconfig.charset)
        sox.send(bytes('PONG' + ping[4:len(ping)] + '\n', botconfig.charset))
        sox.send(bytes('JOIN ' + botconfig.channel + '\n', botconfig.charset))
        botSkills.initializeShellCommands()
        while True:
            try:
                incoming = str(sox.recv(botconfig.buffer_size), botconfig.charset)
                outgoing = answer(incoming)
                for x in outgoing:
                    sox.send(bytes(x, botconfig.charset))
            except:
                pass
    except KeyboardInterrupt:
        sox.close()
        print('Exiting by KeyboardInterrupt (Ctrl+C).')

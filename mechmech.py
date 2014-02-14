import socket
import botconfig
import botSkills

def answer(x):
    global currentNick
    print (">>>" + x)
    if x[:4] == "PING":
        ret = ["PONG" + x[4:len(x)]]
    else:
        ret = []
        if ("PRIVMSG #2d :" in x) or ("PRIVMSG " + currentNick + " :" in x):
            rret = botSkills.shellInterpreter(x)
            for r in rret:
                ret.append("PRIVMSG #2d :" + r + "\n")
                print("<<<" + r)
    return ret

if __name__ == "__main__":
    currentNick = "MechaBot2"
    sox = socket.socket()
    sox.connect((botconfig.host, botconfig.port))
    try:
        sox.recv(512)
        sox.send(bytes("USER mecha mecha mecha :Mechabot\n", botconfig.charset))
        sox.send(bytes("NICK " + currentNick + "\n", botconfig.charset))
        ping = str(sox.recv(512), botconfig.charset)
        sox.send(bytes("PONG" + ping[4:len(ping)] + "\n", botconfig.charset))
        sox.send(bytes("JOIN " + botconfig.channel + "\n", botconfig.charset))
        while True:
            incoming = str(sox.recv(1024), botconfig.charset)
            outgoing = answer(incoming)
            for x in outgoing:
                sox.send(bytes(x, botconfig.charset))
    except KeyboardInterrupt:
        sox.close()
        print("Exiting by KeyboardInterrupt (Ctrl+C).")

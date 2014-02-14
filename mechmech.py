import socket
import botconfig
import botSkills
def answer(x):
    global currentNick
    if x[:4] == "PING":
        ret = "PONG" + x[4:len(x)]
    else:
        if ("PRIVMSG #2d :" in x) or ("PRIVMSG " + currentNick + " :" in x):
            ret = botSkills.dealWithIt(x)
            ret = "PRIVMSG " + botconfig.channel + " :" + ret + "\n"
        else:
            ret = ""
    print (">>>" + x)
    print ("<<<" + ret)
    return ret

if __name__ == "__main__":
    currentNick = "MechaBot"
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
            if outgoing != "":
                sox.send(bytes(outgoing, botconfig.charset))
    except KeyboardInterrupt:
        sox.close()
        print("Exiting by KeyboardInterrupt (Ctrl+C).")

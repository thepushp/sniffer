from datetime import datetime

host_list = ["testsite"]
login_time = ["12"]
logout_time = ["34"]


def store_data(host):
    if host not in host_list:
        now = datetime.now().time()
        host_list.append(host)
        login_time.append(str(now))
        logout_time.append(str(now))
    else:
        now = datetime.now().time()
        logout_time[host_list.index(host)] = str(now)
    # print(*host_list, login_time, logout_time)

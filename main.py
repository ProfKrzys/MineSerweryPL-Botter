import threading, json
from API import signUp, comment
from API.Style import Style
import ctypes

lock = threading.Lock()
accs = 0
comments = 0

def creator(serverid, message, positive):
    global accs, comments
    
    response = signUp.signup()
    if response != False:
        with open("accounts.txt", "a") as file:
            file.write(f"{response[0]}:{response[1]}:{response[2]}:{response[3]}\n")
        Style.print(f"[+] Created account token: {response[3][:5]}***")
        
        with lock:
            accs += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"MineSerwery Gen | Accounts: {accs} | Comments: {comments}")
        
        resp = comment.comment(response[0], response[3], serverid, message, positive)
        if resp != False:
            Style.print(f"[+] Commented on {serverid}")
            
            with lock:
                comments += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"MineSerwery Gen | Accounts: {accs} | Comments: {comments}")
        else:
            if resp == "Comment too short":
                Style.print(f"[-] Couldn't comment on {serverid}! Error code: Comment too short")
            else:
                Style.print(f"[-] Couldn't comment on {serverid}!")
    else:
        Style.print("[-] Couldn't create token!")

def start_creator_threads(serverid, message, positive):
    threads = []
    while True:
        thread = threading.Thread(target=creator, args=(serverid, message, positive))
        threads.append(thread)
        thread.start()


with open("config.json", "r") as file:
    config = json.load(file)

serverid = config["server"]
message = config["text"]
positive = config["positive"]

start_creator_threads(serverid, message, positive)

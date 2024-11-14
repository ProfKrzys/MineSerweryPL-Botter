import requests

def comment(name, token, serverid, message, positive):
    if positive == True:
        positive = "true"
    else:
        positive = "false"

    query = {"login":name,"token":token,"mark":positive,"text":message,"server":str(serverid)}
    try:
        response = requests.get("https://api.mineserwery.pl/server.sendComment", params=query)
        if response.status_code == 200 and response.json()["type"] == "success":
            return True
        elif response.status_code == 200 and response.json()["error"] == 14:
            return "Comment to short"
        return False
    except:
        return False

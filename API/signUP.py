import random, string, requests

def signup():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = name + "@gmail.com"
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    query = {"name":name, "email":email, "password":password}
    try:
        response = requests.get("https://api.mineserwery.pl/account.register", params=query)
        if response.status_code == 200 and response.json()["type"] == "success":
            token = response.json()["token"]
            return name, email, password, token
        return False
    except:
        return False

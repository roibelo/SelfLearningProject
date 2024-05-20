import requests


def do_post_request(user_id):
    try:
        url = "http://127.0.0.1:5000/users/" + str(user_id)
        res = requests.post(url, json={"user_name": "belo"})
        if res.ok:
            data = res.json()
            print("<H1 id='user'>" + data["user_added"] + "</H1>")
        else:
            print("<H1 id='error'>id already exists " + str(user_id) + "</H1>")
            print(res.json())
    except Exception as ex:
        print("<H1 id='error'>error: " + ex.__str__() + "</H1>")


def do_get_request(user_id):
    try:
        url = "http://127.0.0.1:5000/users/" + str(user_id)
        res = requests.get(url)
        if res.ok and res.status_code == 200:
            data = res.json()
            if data["user_name"] == "belo":
                print("<H1 id='user'>" + data["user_name"] + "</H1>")
            else:
                print("the value from the api is different from 'belo'")
        else:
            print("<H1 id='error'>no such user " + str(user_id) + "</H1>")
    except Exception as ex:
        print("<H1 id='error'>error: " + ex.__str__() + "</H1>")


#do_post_request(1)
#do_get_request(3)
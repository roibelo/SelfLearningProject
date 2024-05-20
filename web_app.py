from flask import Flask, request

app = Flask(__name__)

# supported methods
@app.route('/users/get_user_data/<user_id>')
def get_user_data(user_id):
    try:
        #user_name = db_connector.get_user_name(user_id)
        user_name = "";
        if user_id == "1":
            user_name = "roi"
        elif user_id == "2":
            user_name = "belo"

        if user_name != "":
            return "<H1 id='user'>" + user_name + "</H1>"
        else:
            return "<H1 id='error'>no such user " + user_id + "</H1>"
    except Exception as ex:
        return "<H1 id='error'>error: " + ex.__str__() + "</H1>"

app.run(host='127.0.0.1', debug=True, port=5001)
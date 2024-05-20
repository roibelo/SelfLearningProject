from flask import Flask, request

app = Flask(__name__)

# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        if user_id == "1":
            return {"status": "ok", "user_name": "roi"}, 200
        elif user_id == "2":
            return {"status": "ok", "user_name": "belo"}, 200
        else:
            return {"status": "error", "reason": "no such id"}, 500

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        if user_name == "roi":
            return {"status": "ok", "user_added": user_name}, 200
        elif user_name == "belo":
            return {"status": "ok", "user_added": user_name}, 200
        else:
            return {"status": "error", "reason": "id already exist"}, 500

    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        if user_name == "roi":
            return {"status": "ok", "user_change": "belo"}, 200
        elif user_name == "belo":
            return {"status": "ok", "user_change": "roi"}, 200
        else:
            return {"status": "error", "reason": "user not exist"}, 500

    elif request.method == 'DELETE':
        if user_id == "1":
            return {"status": "ok", "user_deleted": "1"}, 200
        elif user_id == "2":
            return {"status": "ok", "user_deleted": "2"}, 200
        else:
            return {"status": "error", "reason": "no such id"}, 500

app.run(host='127.0.0.1', debug=True, port=5000)
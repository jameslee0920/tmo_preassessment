from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    num = request.args.get("num", None)
    # For debugging
    print(f"got number {num}")

    response = {}

    # Check if user sent a eq at all
    if not num:
        response["ERROR"] = "no number found, please send a number after '/square/?num='."
    elif not str(num).isdigit():
        response["ERROR"] = "Input has to be numeric"
    else:
        response["MESSAGE"] = f"Square of {num} is: {int(num)**2}!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('num')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Square of {num} is: {int(num)**2}!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no number found, please send a number after '/square/?num='."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome! Let's square a number.</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
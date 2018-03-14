from flask import Flask, url_for, request, jsonify
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def api_root():
    print(request.headers)
    if request.method == 'GET' and request.headers['Accept'] == 'application/json':
        return jsonify(message="Good Morning")
    elif request.method == 'GET':
        return "Hello World"
    elif request.method == 'POST':
        return request.data

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == '__main__':
    app.run(debug=True)

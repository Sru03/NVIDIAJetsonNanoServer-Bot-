from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()





# from flask import Flask, jsonify
# import json

# app = Flask(__name__)

# @app.route('/data', methods = ['GET'])
# def get_data():
#     data_list = read_from_file()
#     return jsonify(data_list)

# if __name__ == '__main__':
#     app.run(host = '0.0.0.0', port=5000)
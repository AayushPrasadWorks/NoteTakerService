import pymongo
from flask import Flask
from flask import request
from flask import render_template
from Server import Server

app = Flask(__name__)

myclient = pymongo.MongoClient('127.0.0.1', 27017)

@app.route('/', methods=['GET'])
def forms():
    print(request.data)
    if request.method == 'get':
        name = request.form['Name']
        ser = Server()
        ser.getPersonMessage(name,myclient)
        return render_template("text.html")
    return 'OK'

@app.route('/', methods=['POST'])
def form_insert():
    print(request.data)
    if request.method == 'POST':
       name = request.form['Name']
       message = request.form['Message']
       date = request.form['Date']
       ser = Server()
       ser.add(name, message, date,myclient)
       return render_template("text.html")
    return 'OK'

@app.route('/', methods=['PUT'])
def form_update():
    print(request.data)
    if request.method == 'PUT':
       name = request.form['Name']
       new_message = request.form['Message']
       new_date = request.form['Date']
       ser = Server()
       ser.update(name,new_message,new_date,myclient)
       return render_template("text.html")
    return 'Success'

@app.route('/', methods=['DELETE'])
def form_delete():
    print(request.data)
    if request.method == 'DELETE':
        name = request.form['Name']
        ser = Server()
        ser.delete(name,myclient)
        return render_template("text.html")
    return 'OK'


if __name__ == "__main__":
    app.run()
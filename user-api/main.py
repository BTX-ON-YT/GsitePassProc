from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from pysondb import db


app = Flask(__name__)
api = Api(app)


a=db.getDb("users")




@app.route('/', methods=['GET'])
def home():
    return "Nothing to see here... also you can't see me..<a href=""https://www.youtube.com/watch?v=dQw4w9WgXcQ"">.</a> <br> <br> <br> Tor Soon.TM"
@app.route('/emailsend', methods=['GET', 'POST'])
def emailsend():
    return "Done"




if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app
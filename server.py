'''
Archivo donde correra el objeto json
'''
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/index')
def index():
    persona = {
            "dui":"4567894-7",
            "Nombre":"Alejandro Aragon",
            "carnet":"ar17092",
            "educacion":{
                "insa":{
                    "basica":["2011","2012","2013"],
                    "bachillerato":["2014","2015","2016"]
                }
            }
    }
    return jsonify(persona)


if __name__ == '__main__':
    app.run(debug= True, port=8080)

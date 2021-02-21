from flask import Flask,jsonify, request
import subprocess
import requests
import json
from subprocess import call

app = Flask(__name__)


@app.route("/bashcall", methods = ["POST"])

def runCommand():
   str = request.json['command']
   console = open("output.txt",'w+')
   subprocess.call(str, shell=True, stdout=console)
   console.close()
   text = open("output.txt",'r').read()
   return text

if __name__ == '__main__':
   app.run(port=5000)

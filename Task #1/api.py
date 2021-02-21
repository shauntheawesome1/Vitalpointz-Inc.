from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

accounts = [
	{'name': "Shaun", 'ID': 185188},
	{'name': "Shanelle", 'ID': 216424}
  ]

@app.route("/accounts", methods=["GET"])

def getAccounts():
	return jsonify(accounts)

@app.route("/account/<an>", methods=["GET"])

def getAccount(an):
	accountNumber = int(an)-1
	return jsonify(accounts[accountNumber])

@app.route("/account", methods=["POST"])

def addAccount():
	name = request.json['name']
	id = request.json['ID']
	data = {'name': name, 'ID': id}
	accounts.append(data)
	return jsonify(data)

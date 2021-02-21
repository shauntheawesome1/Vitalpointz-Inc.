$ curl http://127.0.0.1:5000/accounts
$ curl http://127.0.0.1:5000/account/1
$ curl http://127.0.0.1:5000/account/2

$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Shovon", "balance": 100}' http://127.0.0.1:8080/account


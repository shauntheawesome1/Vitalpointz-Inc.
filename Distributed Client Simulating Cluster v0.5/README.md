Note: For a Full description including test code, please click on the "DCSC v0.5 README" pdf file.
Actual code is located in "src.py". 


This product is a REST API that, upon being called, will execute a bash command given by a client. There are two sides to this API: a server side and a client side. Upon starting the program, the server side listens for any calls from clients. Furthermore, many security assets including token-based authentication, access control list, etc allow for a more established and secure session between the client and server. Finally, all calls made to the server (whether authorized or unauthorized) are recorded in their respective log files.


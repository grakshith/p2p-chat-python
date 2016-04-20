# P2P Chat App
#### A simple to use chat program that uses sockets and multi-threading

This is a p2p chat program written in python. The traditional client server based chat is also supported
## 1. Getting started
Start the server using 
```sh
$ python Server.py
````
The clients can connect to the server through client.py
```sh
$ python Client.py
````
---
The p2p version can be started using the command
```sh
$ python p2p.py
````
----
Alternatively, it can be run from the terminal itself. 
####1. Make the files executable
```sh
$chmod u+x Server.py Client.py p2p.py
````
####2. Run the program
````sh
$ ./Server.py
````
````sh
$ ./Client.py
````
````sh
$ ./p2p.py
````
----
The client asks for the hostname and the port on which the server is listening. Then an attempt is made to connect to the server. If everything is all right, the client should prompt you to start typing your messages. Else an exception is thrown.

##2. Things to be implemented yet
- General exception handling
- Some more polishing
- Build a gui ;)

##3. General
Feel free to report bugs. Or shoot an e-mail to hehaichi@gmail.com

##4. License

This work is licensed with the MIT license

####The MIT License (MIT)
Copyright (c) 2015 Rakshith G

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

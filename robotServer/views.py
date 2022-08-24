from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import socket
import sys
import json

# Create your views here.

def index(request):
    return render(request, "robotServer/index.html")

def toRover(request):
    HOST, PORT = "localhost", 3000

    m ='{"hearbeat": 2}'
    jsonObj = json.loads(m)

    data = jsonObj

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(jsonObj)

        # Receive data from the server and shut down
        received = sock.recv(5000)
    finally:
        sock.close()

    print "Sent:     {}".format(data)
    print "Received: {}".format(received)

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

def drive(request):
    HOST, PORT = "localhost", 5000

    m ="{ hearbeat_count: 0,\n is_operational: 0,\n wheel_shift: 0,\n drive_mode: 'D',\n speed: 0,\n angle: 0 }"

  {\n"
    "  \"heartbeat_count\": %d,\n"
    "  \"is  _operational\": %d,\n"
    "  \"wheel_shift\": %d,\n"
    "  \"drive_mode\": \"%c\",\n"
    "  \"speed\": %d,\n"
    "  \"angle\": %d\n"
    "}
    jsonObj = json.loads(m)

    data = jsonObj

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if request.method == "POST":
        try:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(jsonObj) #or sendall

        finally:
            sock.close()

        print "Sent:     {}".format(data)
    else:
        try:
            # Receive data from the server and shut down
            received = sock.recv(5000)
        finally:
            sock.close()
        return data

        print "Received: {}".format(received)
        
        

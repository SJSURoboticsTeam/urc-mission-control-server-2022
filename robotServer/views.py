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
    
    """
    Format:
  {\n"
    "  \"heartbeat_count\": %d,\n"
    "  \"is  _operational\": %d,\n"
    "  \"wheel_shift\": %d,\n"
    "  \"drive_mode\": \"%c\",\n"
    "  \"speed\": %d,\n"
    "  \"angle\": %d\n"
    "}
    """

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
            print "Received: {}".format(received)
        return data

        

def arm(request):
    HOST, PORT = "localhost", 5000
    arm_info = """
    { heartbeat_count: 0,\n is_operational: 1,\n arm_mode: A,\n hand_mode: H,
    \n arm_speed: 0, \n battery: 0,\n rotunda_angle: 0,\n shoulder_angle: 0,
    \n elbow_angle: 0,\n wrist_roll: 0,\n wrist_pitch: 0,\n pinky_angle: 0,\n
    ring_angle: 0,\n middle_angle: 0,\n pointer_angle: 0,\n thumb_angle: 0}
    """
        
    """
    Format:
    {\n" 
    "   \"heartbeat_count\": %d, \n"
    "   \"is_operational\": %d, \n"
    "   \"arm_mode\": \"%c\", \n"
    "   \"hand_mode\": \"%c\", \n"
    "   \"arm_speed\": %d, \n"
    "   \"battery\": %d, \n"
    "   \"rotunda_angle\": %d, \n"
    "   \"shoulder_angle\": %d, \n"
    "   \"elbow_angle\": %d, \n"
    "   \"wrist_roll\": %d, \n"
    "   \"wrist_pitch\": %d, \n"
    "   \"pinky_angle\": %d, \n"
    "   \"ring_angle\": %d, \n"
    "   \"middle_angle\": %d, \n"
    "   \"pointer_angle\": %d, \n"
    "   \"thumb_angle\": %d, \n"

    "}
    """

    jsonObj = json.loads(arm_info)

    data = jsonObj

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if request.method == "POST":
        try:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.send(data) #or sendall

        finally:
            sock.close()

        print "Sent:     {}".format(data)
    else:
        try:
            # Receive data from the server and shut down
            received = sock.recv(5000)
        finally:
            sock.close()
            print "Received: {}".format(received)
        return data






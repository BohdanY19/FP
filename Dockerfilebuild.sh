#!/bin/bash

sudo docker build -t my_flask_app:v0.1 /home/bohdan/simple-python-application/RandomApi/
sudo docker run -d -p 8040:8040 7de9833778e1

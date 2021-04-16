#!/bin/bash
#takes in URL and display all HTTP methods accepted
curl -si $1 | grep Allow | cut -d ":" -f 2 | cut -c -2

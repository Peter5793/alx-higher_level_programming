#!/bin/bash
#takes in URL and display all HTTP methods accepted
curl -si OPTIONS $1

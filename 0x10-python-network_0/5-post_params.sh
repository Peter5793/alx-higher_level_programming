#!/bin/bash
# sends a PPOST request to the passed URL
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"

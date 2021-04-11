#!/bin/bash
# sends a PPOST request to the passed URL
curl -s -X POST -d "email=hr@holbertonschool.com&subjectI will always be here for PLD" "$1"

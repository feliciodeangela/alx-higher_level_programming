#!/bin/bash
# POST body
curl -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -s "$1"

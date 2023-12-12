#!/bin/bash
# Size of the response body
curl -s "$1" | wc -c

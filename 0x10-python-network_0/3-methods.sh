#!/bin/bash
# Display available methods
curl -sI "$1" | tail -n 2 | head -n 1 | cut -c 8-

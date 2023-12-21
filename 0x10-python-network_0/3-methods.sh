#!/bin/bash
# Display available methods
curl -sI "$1" | grep '^Allow: ' | cut -c 8-

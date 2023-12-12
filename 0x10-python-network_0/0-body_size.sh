#!/bin/bash
# Size of the response body
curl -w '%{size_download}\n' "$1"

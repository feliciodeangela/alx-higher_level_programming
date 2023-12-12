#!/bin/bash
# Size of the response body
curl -wp '%{size_download}\n' "$1"

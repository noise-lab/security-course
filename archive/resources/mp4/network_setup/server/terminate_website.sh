#!/bin/bash
if [ "$(id -u)" = "0" ]; then
    echo "don't use sudo for this"
    exit 1
fi

kill -9 $(pgrep -f "launch_website.py")
kill -9 $(pgrep -f "coffee app.coffee")

#!/bin/bash

# Run first Python script in the background and redirect output to script1.log
python script1.py > script1.log &

# Run second Python script in the background and redirect output to script2.log
python script2.py > script2.log &

# Wait for both scripts to finish
wait
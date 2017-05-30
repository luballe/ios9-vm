#!/bin/bash

for run in {1..5}
do
  # Redirect the stdout to /dev/null 
  python 1-CargarMapa.py > /dev/null 2>&1 &
done

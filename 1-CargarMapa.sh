#!/bin/bash

cd python selenium_phantom

for run in {1..5}
do
  python 1-CargarMapa.py &
done

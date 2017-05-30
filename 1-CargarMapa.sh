#!/bin/bash

cd selenium_phantom

for run in {1..5}
do
  python 1-CargarMapa.py &
done
cd ..

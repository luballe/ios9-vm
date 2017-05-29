#!/bin/bash

for run in {1..5}
do
  python 1-CargarMapa.py >> 1-CargarMapa.txt &
done

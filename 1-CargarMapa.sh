#!/bin/bash

for run in {1..5}
do
  python 1-CargarMapa.py & > /dev/null
done

#!/bin/bash

for run in {1..5}
do
  python selenium_phantom/1-CargarMapa.py &
done

#!/usr/bin/env bash

awk -F',' 'BEGIN{print "ArrDelay,Origin"; OFS=","} $17=="SFO" {print $15,$17}' 2007.csv | head -4 -> first_sfo3.csv

echo "Chandy"

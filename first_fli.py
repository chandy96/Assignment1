#!/usr/bin/env python3

import pandas as pd
import numpy as np

firstflight= pd.read_csv("2007.csv")

first_flight = firstflight[firstflight["Origin"]=="SFO"].loc[:,('ArrDelay','Origin')].head(3)

first_flight.to_csv('first3fli.csv', index=False)


print("Chandy")

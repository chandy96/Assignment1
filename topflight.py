#!/usr/bin/env python3

import pandas as pd
impoprt pandas as np


top3 = pd.read_csv("2007.csv")

top3fli = top3.groupby('Dest').count().rest.index().sort_values(by="Year",ascending=False).loc[;Desr;,'Year')].head(3)

top3fli.columns=['Dest'.'Count']

top3fli.to_csv('top3fli.csv',index=False)
 
 
 print("Chandy")

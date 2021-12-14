import pandas as pd
import csv

df = pd.read_csv("star_with_gravity.csv")

distanceStars = []

for data in df.Distance:
    if(data<=100):
        distanceStars.append(True)
    else:
        distanceStars.append(False)
        
isDistance = pd.Series(distanceStars)

starDisctance = df[isDistance]
starDisctance.reset_index(inplace=True,drop=True)

gravityStars = []
for data in starDisctance.Gravity:
    if(data>=150 and data<=350):
        gravityStars.append(True)
    else:
        gravityStars.append(False)

isGravity = pd.Series(gravityStars)
finalStars = starDisctance[isGravity]
finalStars.reset_index(inplace=True,drop=True)
 
finalStars.to_csv("filteresStars.csv")                        
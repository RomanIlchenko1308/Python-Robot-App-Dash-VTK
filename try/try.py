import pandas as pd

txtoutput = """RIGHT,3,3,-90
LEFT,3,3,0
PLACE,3,3,0
HOME,1,1,0
RIGHT,1,1,-90
LEFT,1,1,0
LEFT,1,1,90
LEFT,1,1,180
LEFT,1,1,270
LEFT,1,1,0
LEFT,1,1,90
LEFT,1,1,180
PLACE,1,1,180
PLACE,3,5,180
PLACE,3,5,360
HOME,1,1,0
"""
txtoutput1 = txtoutput.split("\n")
print(txtoutput1)

# ---
df = pd.DataFrame(txtoutput1, columns =['Commands'])
print("-----------------------------------------")
print(df)

# split column and add new columns to df
df[['Commands', 'Coord: X', 'Coord: Y', "Vector: F"]] = df['Commands'].str.split(',', expand=True)
# display the dataframe
print("++++++++++++++++++++++++++++++++++++++++++")
print(df)
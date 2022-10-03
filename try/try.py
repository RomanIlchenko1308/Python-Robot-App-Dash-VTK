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
"""
         Commands
0   RIGHT,3,3,-90
1      LEFT,3,3,0
2     PLACE,3,3,0
3      HOME,1,1,0
4   RIGHT,1,1,-90
5      LEFT,1,1,0
6     LEFT,1,1,90
7    LEFT,1,1,180
8    LEFT,1,1,270
9      LEFT,1,1,0
10    LEFT,1,1,90
11   LEFT,1,1,180
12  PLACE,1,1,180
13  PLACE,3,5,180
14  PLACE,3,5,360
15     HOME,1,1,0
16               
"""


# ---
df = pd.DataFrame(txtoutput1, columns =['Commands'])
print("-----------------------------------------")
print(df)

# split column and add new columns to df
df[['Commands', 'Coord: X', 'Coord: Y', "Vector: F"]] = df['Commands'].str.split(',', expand=True)
# display the dataframe
print("++++++++++++++++++++++++++++++++++++++++++")
print(df)
"""
++++++++++++++++++++++++++++++++++++++++++
   Commands Coord: X Coord: Y Vector: F
0     RIGHT        3        3       -90
1      LEFT        3        3         0
2     PLACE        3        3         0
3      HOME        1        1         0
4     RIGHT        1        1       -90
5      LEFT        1        1         0
6      LEFT        1        1        90
7      LEFT        1        1       180
8      LEFT        1        1       270
9      LEFT        1        1         0
10     LEFT        1        1        90
11     LEFT        1        1       180
12    PLACE        1        1       180
13    PLACE        3        5       180
14    PLACE        3        5       360
15     HOME        1        1         0
16              None     None      None
"""
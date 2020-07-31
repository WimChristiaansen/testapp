#import external library pandas
import pandas as pd

#read the csv as a dataframe and make data accessible
boundaries = pd.read_csv("bounds_full.csv", index_col=0)

boundaries.columns = ["Left", "Bottom", "Right", "Top"]

boundaries["Left"] = boundaries["Left"].apply(lambda x: x[1:])
boundaries["Left"] = boundaries["Left"].astype(float)

boundaries["Bottom"] = boundaries["Bottom"].astype(float)

boundaries["Right"] = boundaries["Right"].astype(float)

boundaries["Top"] = boundaries["Top"].apply(lambda x: x[:-1])
boundaries["Top"] = boundaries["Top"].astype(float)

#definition to check which tile the coordinates given (x, y) are in
def check_bounds(x, y):

    x = float(x)
    y = float(y)
    for i in range(0, 39294):
        left = boundaries.iloc[i]["Left"]
        right = boundaries.iloc[i]["Right"]
        bottom = boundaries.iloc[i]["Bottom"]
        top = boundaries.iloc[i]["Top"]

        if (left < x < right) and (bottom < y < top):
                print(left, right, bottom, top)
                return i+2
        else:
            continue
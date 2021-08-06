import pandas as pd
import numpy as np
df=pd.read_csv("MOCK_DATA.csv")
df2=df["email"]
i=0
def split(word):
    return [char for char in word]
while i<1000:
    x=split(df2[i])
    y=df2[i]
    if "0"  in x:
        df2.at[i]=np.nan
        i=i+1
    elif "1"  in x:
        df2.at[i]=np.nan
        i=i+1
    elif "2" in x:
        df2.at[i] = np.nan
        i = i + 1
    elif "3" in x:
        df2.at[i] = np.nan
        i = i + 1
    elif "4" in x:
        df2.at[i] = np.nan
        i = i + 1
    elif "5" in x:
        df2.at[i] = np.nan
        i = i + 1
    elif "6" in x:
        df2.at[i] = np.nan
        i = i + 1
    elif "7" in x:
        df2.at[i] = np.nan
        i = i + 1
    elif "8" in x:
        df2.at[i] = np.nan
        i = i + 1
    elif "9" in x:
        df2.at[i] = np.nan
        i = i + 1

    else:
        i=i+1
print(df2)
df["email"]=df2
df.to_json("final.json")
df.to_csv("FINAL_FORM.csv")
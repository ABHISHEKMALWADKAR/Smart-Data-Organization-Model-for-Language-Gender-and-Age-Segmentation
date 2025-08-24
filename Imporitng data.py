import pandas as pd

with open("D:\\PYTHON\\Final project\\Languages.txt", "r") as logfile, \
     open("output.txt", "w", encoding="utf-8") as outfile:
    for line in logfile:
        outfile.write(line)

# Read the tab-separated text file into a DataFrame
df = pd.read_csv("D:\\PYTHON\\Final project\\Languages.txt", sep="\t")

# Write the DataFrame to an Excel file
df.to_csv("D:\\PYTHON\\Final project\\Languages_output.csv", index=False)
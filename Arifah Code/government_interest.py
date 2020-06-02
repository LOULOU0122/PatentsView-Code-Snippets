#Read-in script for Raw government interest statements on all patents (where available)

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")
file_name = "government_interest.tsv.zip"
f_name = "government_interest.tsv"
# Selecting the zip file.
zf = zip.ZipFile(file_name)
# Reading the selected file in the zip.
df = pd.read_csv(zf.open(f_name), delimiter="\t")
# Print first five observations
print(df.head())
# Print summary of data: number of columns, observations, and each variable data type
print(len(df))
df.info()


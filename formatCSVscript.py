import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import warnings

warnings.filterwarnings('ignore')

# load dataset from input directory
df = pd.read_csv("C:/Users/evanj/Desktop/Senior/Spring/4424 MCL/Final_project/cv-valid-train.csv") 
df[df['age'].notna()].head()

#we extract the columns that we think useful are
df = df[['filename','age','gender']]
#To clean the data we remove the sample with NaN attribute values.
data = df[df['age'].notna() & df['gender'].notna()]
data.reset_index(inplace=True, drop=True)
print(data.head())

data.to_csv("../Final_project/out.csv")
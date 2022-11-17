
import pandas as pd
import glob
import os

input_loc = "C:\\Users\\User\\Desktop\\wamboh\\Agricultural"
output_loc = "C:\\Users\\User\\Desktop\\wamboh\\Agricultural"

import pandas as pd
import glob
import os

# merging the files
files_joined = os.path.join(input_loc, "salesdata*.csv")

# Return a list of all joined files
list_files = glob.glob(files_joined)

print("** Merging multiple csv files into a single pandas dataframe **")
# Merge files by joining all files
dataframe = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
print(dataframe)
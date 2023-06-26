# Args:
#     Path - The path to the excel sheet to be sorted
#     Gene - The gene to sort the data by

# Imports
import pandas as pd
import sys

# Check if parameters are valid
if (len(sys.argv) != 4):
    print(f'ERROR: Incorrect number of parameters. Example: {sys.argv[0]} <excel_path> <rows_to_skip> <gene>')
    sys.exit()

# Create dataframe from excel path
excel_path = sys.argv[1]
rows_to_skip = int(sys.argv[2])
gene = sys.argv[3]

df = pd.read_excel(excel_path, skiprows=rows_to_skip)

print(df)

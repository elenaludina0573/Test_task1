import json
import pandas
import pandas as pd
import os


# Read excel document
excel_data_df = pandas.read_excel(io=os.path.abspath('files\\Прайс-лист AGC 2024.03.04 Опт.xlsx'),
                                  sheet_name='Автостекло. Аксессуары. Клей')

# Define structure for json
thisisjson_dict_1 = [
    {
        "art": "",
        "eurocode": "",
        "oldcode": "",
        "name": "",
        "catalog": "",
        "category": "",
        "price": ""
    }
]

# Iterate over rows in the dataframe
for index, row in excel_data_df.iterrows():
    # Add data to the list
    thisisjson_dict_1.append({
        "art": row['AGC'],
        "eurocode": row['Unnamed: 0'],
        "oldcode": row['Unnamed: 2'],
        "name": row['Unnamed: 3'],
        "category": row['AGC'],
        "price": row['Unnamed: 7']
    })

    # Check if we have reached the end of the file
    if index == len(excel_data_df) - 1:
        break

# Define file to write to and 'w' for write option -> json.dump()
# defining the list to write from and file to write to
with open('data_1.json', 'w', encoding=" UTF-8") as json_file:
    chunks = pd.read_json('data_1.json', lines=True, chunksize=10)
    for i, c in enumerate(chunks):
        c.to_json('chunk_{}.json'.format(i))
    json.dump(thisisjson_dict_1, json_file)

# Read excel document
excel_data_df = pandas.read_excel(io=os.path.abspath('files\\Прайс-лист AGC 2024.03.04 Опт.xlsx'),
                                  sheet_name='Российский автопром')

# Define structure for json
thisisjson_dict_2 = [
    {
        "art": "",
        "eurocode": "",
        "oldcode": "",
        "name": "",
        "catalog": "",
        "category": "",
        "price": ""
    }
]

# Iterate over rows in the dataframe
for index, row in excel_data_df.iterrows():
    # Add data to the list
    thisisjson_dict_2.append({
        "art": row['Unnamed: 1'],
        "eurocode": row['Unnamed: 0'],
        "oldcode": row['Unnamed: 2'],
        "name": row['Unnamed: 3'],
        "category": row['Unnamed: 0'],
        "price": row['Unnamed: 7']
    })

    # Check if we have reached the end of the file
    if index == len(excel_data_df) - 1:
        break

# Define file to write to and 'w' for write option -> json.dump()
with open('data_2.json', 'w', encoding="utf-8") as json_file:
    json.dump(thisisjson_dict_2, json_file)

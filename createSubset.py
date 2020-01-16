import json

# Open the created json file with data only on Iraq
with open("Iraq.json", 'r', encoding = 'utf-16' ) as file:
    contentIraq = json.load(file)
# print(contentIraq)


# Creating a CSV file
with open("IraqCSV.csv", 'w') as file:
    # Writing the header containing the names of the columns
    file.write(f'ID, Year, Best_est_deaths\n')
    # loop over all dictionairies in the data file and add them as entries to the csv file
    for entry in contentIraq:
        file.write(f'{entry["id"]}, {entry["year"]}, {entry["best"]}\n')





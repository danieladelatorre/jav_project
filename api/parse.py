import csv
from .views import add_entry

def parse_info():
    with open('datasets_596958_1073629_Placement_Data_Full_Class (1).csv', 'r') as csv_file:
        #reads the csv file and stores the values in a dictionary
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            add_entry(line)

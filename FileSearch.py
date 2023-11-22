from csv import reader
from DatabaseRecord import DatabaseRecord

def determine_if_collectibleId_in_ManualCollection_csv(collectibleId):
    manual_association_csv = open('ManualAssociation.csv', 'r')
    datareader = reader(manual_association_csv)
    for row in datareader:
        if collectibleId in row:
            return True
    return False

def fetch_associated_database_record(databaseId):
    # Open file
    database_file = open('Database.csv', 'r')
    # Read data from file
    database_file_data = database_file.read()
    # Split into lines
    split_database_file_data = database_file_data.splitlines()

    for line in split_database_file_data:
        split_line = line.split(',')
        if split_line[0] == databaseId:
            return DatabaseRecord(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6],
                                            split_line[7], split_line[8], split_line[9], split_line[10], split_line[16])

    return None
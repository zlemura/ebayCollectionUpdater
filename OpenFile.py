from CollectionRecord import CollectionRecord
from DatabaseRecord import DatabaseRecord

def open_collection_file():
    # Open file
    collection_file = open('Collection.csv', 'r')
    # Read data from file
    collection_file_data = collection_file.read()
    # Split into lines
    split_collection_file_data = collection_file_data.splitlines()

    collection_list = []

    for line in split_collection_file_data:
        split_line = line.split(',')
        if split_line[0] == 'CollectibleId':
            continue
        collection_list.append(CollectionRecord(split_line[0], split_line[1], split_line[5], split_line[6], split_line[7],
                                                split_line[9], split_line[11], split_line[12]))

    return collection_list

def open_database_file():
    # Open file
    database_file = open('Database.csv', 'r')
    # Read data from file
    database_file_data = database_file.read()
    # Split into lines
    split_database_file_data = database_file_data.splitlines()

    database_list = []

    for line in split_database_file_data:
        split_line = line.split(',')
        if split_line[0] == 'Player':
            continue
        database_list.append(DatabaseRecord(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6],
                                            split_line[7], split_line[8], split_line[9], split_line[15]))

    return database_list
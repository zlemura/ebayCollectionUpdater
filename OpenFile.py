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
                                            split_line[7], split_line[8], split_line[9], split_line[10], split_line[16]))

    return database_list

def open_manual_association_file():
    manual_association_records = {}
    manual_association_file = open('ManualAssociation.csv', 'r')
    manual_association_file_data = manual_association_file.read()
    split_manual_association_file_data = manual_association_file_data.splitlines()

    database_list = open_database_file()
    collection_list = open_collection_file()

    for row in split_manual_association_file_data:
        matched_database_record = None
        matched_collection_record = None
        row_split = row.split(',')
        if row_split[0] == 'CollectibleId':
            continue
        else:
            # Fetch DatabaseRecord.
            for database_record in database_list:
                if database_record.id == row_split[1]:
                    matched_database_record = database_record
            # Fetch CollectionRecord.
            for collection_record in collection_list:
                if collection_record.collectibleId == row_split[0]:
                    matched_collection_record = collection_record
        if matched_database_record != None and matched_collection_record != None:
            manual_association_records[matched_collection_record] = matched_database_record

    '''
    for key in manual_association_records.keys():
        print("Key = " + str(key.__dict__))
        print("Value = " + str(manual_association_records[key].__dict__))
    '''
    return manual_association_records

def open_exclusions_file():
    exclusions_file = open('Exclusions.csv', 'r')
    exclusions_file_data = exclusions_file.read()
    split_exclusions_file_data = exclusions_file_data.splitlines()

    exclusions_list = []

    for line in split_exclusions_file_data:
        if line == 'collectibleId':
            continue
        else:
            exclusions_list.append(line)

    return exclusions_list

def open_final_association_file():
    final_association_file = open('FinalAssociation.csv', 'r')
    final_association_file_data = final_association_file.read()
    split_final_association_file_data = final_association_file_data.splitlines()

    final_association_dict = {}

    for line in split_final_association_file_data:
        split_line = line.split(',')
        if split_line[0] == 'collectibleId':
            continue
        else:
            final_association_dict[split_line[0]] = split_line[1]

    return final_association_dict

def fetch_collectible_record_by_collectibleId(collectibleId):
    # Open file
    collection_file = open('Collection.csv', 'r')
    # Read data from file
    collection_file_data = collection_file.read()
    # Split into lines
    split_collection_file_data = collection_file_data.splitlines()

    for line in split_collection_file_data:
        split_line = line.split(',')
        if split_line[0] == 'CollectibleId':
            continue
        if split_line[0] == collectibleId:
            print("Matched record!")
            print(split_line[0])
            return CollectionRecord(split_line[0], split_line[1], split_line[5], split_line[6], split_line[7],
                             split_line[9], split_line[11], split_line[12])

    return None

def fetch_database_record_by_databaseId(databaseId):
    # Open file
    database_file = open('Database.csv', 'r')
    # Read data from file
    database_file_data = database_file.read()
    # Split into lines
    split_database_file_data = database_file_data.splitlines()

    for line in split_database_file_data:
        split_line = line.split(',')
        if split_line[0] == 'Player':
            continue
        if split_line[0] == databaseId:
            return DatabaseRecord(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5],
                           split_line[6],
                           split_line[7], split_line[8], split_line[9], split_line[10], split_line[16])

    return None

def determine_if_collectibleId_in_CollectibleUpdateLog_csv(collectibleId):
    # Open file
    collectible_update_log = open('CollectibleUpdateLog.csv', 'r')
    # Read data from file
    collectible_update_log_file_data = collectible_update_log.read()
    # Split into lines
    split_collection_update_log_data = collectible_update_log_file_data.splitlines()

    for line in split_collection_update_log_data:
        split_line = line.split(',')
        if split_line[0] == 'CollectibleId':
            continue
        if split_line[0] == collectibleId:
            return True

    return False
import CollectionDatabaseMatcher
import OpenFile


# TODO
# Open FinalAssociation.csv and extract dictionary - collectible, databaseRecord.
# Create new title for collection record.
# Update attributes - if applicable.
# Open eBay.
# Loop through collection.
# Match record from collection record collectibleId and update to new title.
# Update collection record attributes (if applicable).
# Save changes to collection record.
# Add validation logic - take collection, match record, verify title is correct format.
# Add manual association logic - loop through collectibles not matched, input database record ID to associte too.
import UpdateFile


def main():
    #Open database file.
    database_list = OpenFile.open_database_file()
    #Open collection file.
    collection_list = OpenFile.open_collection_file()
    collection_list_to_process = []
    #Exclude results in FinalAssociation.csv
    print("Prior to processing final associations there are " + str(len(collection_list)) + " records to be processed.")
    final_association_dict = OpenFile.open_final_association_file()
    for record in collection_list:
        collectibleId_matched = False
        for key in final_association_dict.keys():
            if record.collectibleId == key and len(key) > 0:
                collectibleId_matched = True
                print("Final association found!")
                print("Matched the key " + str(key) + " to record.collectibleId " + str(record.collectibleId))
                break
            else:
                continue
        if collectibleId_matched == False:
            collection_list_to_process.append(record)
    print("After processing final associations there are " + str(len(collection_list_to_process)) + " records to be processed.")

    #Exclude results in ManualAssociation.csv
    manual_association_records = OpenFile.open_manual_association_file()
    loop_collection_list_to_process = collection_list_to_process
    print("Prior to processing manual associations there are " + str(len(collection_list_to_process)) + " records to be processed.")
    for record in loop_collection_list_to_process:
        collectibleId_matched = False
        for key in manual_association_records.keys():
            if record.collectibleId == key and len(key) > 0:
                collectibleId_matched = True
                print("Manual association found!")
                print("Matched the key " + str(key) + " to record.collectibleId " + str(record.collectibleId))
                break
            else:
                continue
        if collectibleId_matched == True:
            collection_list_to_process.remove(record)
    print("After processing manual associations there are " + str(len(collection_list_to_process)) + " records to be processed.")

    #Exclude results in Exclusions.csv
    exclusions_list = OpenFile.open_exclusions_file()
    loop_collection_list_to_process = collection_list_to_process
    print("Prior to processing exclusions there are " + str(len(collection_list_to_process)) + " records to be processed.")
    for record in loop_collection_list_to_process:
        collectibleId_matched = False
        for key in manual_association_records.keys():
            if record.collectibleId == key and len(key) > 0:
                collectibleId_matched = True
                print("Exclusion found!")
                print("Matched the key " + str(key) + " to record.collectibleId " + str(record.collectibleId))
                break
            else:
                continue
        if collectibleId_matched == True:
            collection_list_to_process.remove(record)
    print("After processing exclusions there are " + str(len(collection_list_to_process)) + " records to be processed.")

    if input() != 'y':
        SystemExit.code(0)

    #Match collection records to database.
    collection_matched_database_dict, collection_could_not_be_matched_list = \
        CollectionDatabaseMatcher.match_collection_records_to_database_record(collection_list_to_process, database_list)
    #Add results to FinalAssociation.csv.
    for key in collection_matched_database_dict.keys():
        UpdateFile.add_record_to_FinalAssociation_csv(key.collectibleId, collection_matched_database_dict[key].id)
    #Add results to ManualAssociations.csv.
    if len(collection_could_not_be_matched_list) > 0:
        if input("Proceed with manually associating unmatched records? (Type 'y')") == 'y':
            CollectionDatabaseMatcher.manually_associate_unmatched_records(collection_could_not_be_matched_list,
                                                                           database_list)

    # Add results to FinalAssociation.csv.
    manual_associated_records = OpenFile.open_manual_association_file()
    for key in manual_associated_records.keys():
        UpdateFile.add_record_to_FinalAssociation_csv(key.collectibleId, manual_associated_records[key].id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


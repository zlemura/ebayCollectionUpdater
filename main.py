import CollectionDatabaseMatcher
import EbayUpdater
import OpenFile
import Selenium


# TODO
# Open FinalAssociations.csv.
# Print each record to update.
# Print URL to update.
# Print new title.
# Print parrallel.
# Confirm update made.
# Save to update made file.
import UpdateFile


def main():
    '''
    #Open database file.
    database_list = OpenFile.open_database_file()
    #Open collection file.
    collection_list = OpenFile.open_collection_file()
    collection_list_to_process = []
    #Exclude results in FinalAssociation.csv
    #print("Prior to processing final associations there are " + str(len(collection_list)) + " records to be processed.")
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
    #print("After processing final associations there are " + str(len(collection_list_to_process)) + " records to be processed.")

    #Exclude results in ManualAssociation.csv
    manual_association_records = OpenFile.open_manual_association_file()
    loop_collection_list_to_process = collection_list_to_process
    #print("Prior to processing manual associations there are " + str(len(collection_list_to_process)) + " records to be processed.")
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
    #print("After processing manual associations there are " + str(len(collection_list_to_process)) + " records to be processed.")

    #Exclude results in Exclusions.csv
    exclusions_list = OpenFile.open_exclusions_file()
    loop_collection_list_to_process = collection_list_to_process
    print("Prior to processing exclusions there are " + str(len(collection_list_to_process)) + " records to be processed.")
    for record in loop_collection_list_to_process:
        collectibleId_matched = False
        for key in exclusions_list:
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

    '''
    final_association_dict = OpenFile.open_final_association_file()

    for key in final_association_dict.keys():
        #Check if collectibleId in CollectibleUpdateLog.csv.
        if OpenFile.determine_if_collectibleId_in_CollectibleUpdateLog_csv(str(key)) == False:
            record_updated = False
            while record_updated == False:
                collectible_record = OpenFile.fetch_collectible_record_by_collectibleId(str(key))
                database_record = OpenFile.fetch_database_record_by_databaseId(final_association_dict[key])
                url = "https://www.ebay.com/collection/collectible?notionalTypeId=Soccer&period=1Y&collectibleId=" + str(
                    key)
                print(url)
                print("Database ID = " + str(database_record.id))
                #print("Current title = " + str(collectible_record.title))
                # Title format = Player + Set or Season + Manufacturer + Card number + Variant + Grader + Grade
                formatted_title = str(database_record.player) + " " + str(database_record.set) + " #" + str(
                    database_record.card_number)

                if len(database_record.variant) > 0 and database_record.variant != 'Base':
                    formatted_title = formatted_title + " " + str(database_record.variant)
                if len(database_record.numbered) > 0:
                    formatted_title = formatted_title + " " + str(database_record.numbered)
                if len(database_record.grader) > 0:
                    formatted_title = formatted_title + " " + str(database_record.grader) + " " + str(
                        database_record.grade)
                print("Formatted title = " + formatted_title)

                if len(database_record.variant) > 0 or len(database_record.numbered) > 0:
                    if database_record.variant == 'Base':
                        if len(database_record.numbered) > 0:
                            print("Parrallel = " + str(database_record.numbered))
                    else:
                        if len(database_record.numbered) > 0:
                            print("Parrallel = " + str(database_record.variant) + " " + str(database_record.numbered))
                        else:
                            print("Parrallel = " + str(database_record.variant))
                else:
                    print("No parrallel data found")

                if input("Collectible updated?") == 'y':
                    record_updated = True
                    UpdateFile.add_record_to_CollectibleUpdateLog_csv(collectible_record.collectibleId,
                                                                      database_record.id)
                else:
                    print("Please update collectible and confirm.")
        else:
            continue

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


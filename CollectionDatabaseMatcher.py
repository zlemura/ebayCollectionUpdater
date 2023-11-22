import FileSearch
import UpdateFile
from CollectionRecord import  CollectionRecord
from DatabaseRecord import DatabaseRecord

# TODO
# Add logic to check if collectionId is in FinalAssociation.csv.

def match_collection_records_to_database_record(collection_list, database_list):
    collection_matched_database_dict = {}
    collection_could_not_be_matched_list = []

    for collection_record in collection_list:
        collection_record_matched = False
        if len(collection_record.player) > 0:
            for database_record in database_list:
                if collection_record.player == database_record.player:
                    add_player_list = True
                    print(collection_record.player, database_record.player)
                    print(database_record.variant, collection_record.title)
                    if len(database_record.variant) > 0 and database_record.variant != 'Base':
                        if database_record.variant not in collection_record.title:
                            add_player_list = False
                        print("Matched variant!")
                    print(database_record.numbered, collection_record.title)
                    if len(database_record.numbered) > 0:
                        if database_record.numbered not in collection_record.title:
                            add_player_list = False
                        print("Matched numbered!")
                    print(database_record.is_autograph, collection_record.title)
                    if database_record.is_autograph == 'Y':
                        if 'Auto' not in collection_record.title:
                            add_player_list = False
                        print("Matched auto!")
                    print(database_record.grader, collection_record.title)
                    if len(database_record.grader) > 0:
                        if database_record.grader not in collection_record.title:
                            add_player_list = False
                        print("Matched grader!")
                    print(database_record.grade, collection_record.title)
                    if len(database_record.grade) > 0:
                        if database_record.grade not in collection_record.title:
                            add_player_list = False
                            print("Matched grade!")
                    print(database_record.card_number, collection_record.title)
                    if database_record.card_number not in collection_record.title:
                        add_player_list = False
                    print("Matched card number!")
                    print(database_record.set, collection_record.title)
                    if database_record.set not in collection_record.title:
                        add_player_list = False
                    print("Matched set!")

                    if add_player_list == False:
                        print("Collection record could not be matched.")
                    else:
                        collection_matched_database_dict[collection_record] = database_record
                        collection_record_matched = True
                        print("Collection record matched!")
        if collection_record_matched == False:
            collection_could_not_be_matched_list.append(collection_record)

    return collection_matched_database_dict, collection_could_not_be_matched_list

def manually_associate_unmatched_records(collection_could_not_be_matched_list, database_list):
    counter = 0

    manually_associated_unmatched_records = {}
    manually_associated_unmatched_records_added_to_dict = []
    skipped_records = []
    excluded_records = []
    player_name_collection_could_not_be_matched_list = []

    #Find records with player name's.
    for record in collection_could_not_be_matched_list:
        if len(record.player) > 0:
            player_name_collection_could_not_be_matched_list.append(record)
        else:
            manually_associated_unmatched_records_added_to_dict.append(record)

    #Find records with collectibleId not in ManualAssociation.csv.
    final_unmatched_records_list = []

    for record in player_name_collection_could_not_be_matched_list:
        if FileSearch.determine_if_collectibleId_in_ManualCollection_csv(record.collectibleId) == True:
            print(record.collectibleId + " removed from list.")
        else:
            final_unmatched_records_list.append(record)
            print(record.collectibleId + " kept in list.")

    print("You are about to proceed with the manual association of " + str(
        len(final_unmatched_records_list)) + " records. Do you wish to proceed?")
    if input("Proceed? (Type 'y')") != 'y':
        return None

    for unmatched_record in final_unmatched_records_list:
        counter += 1
        print("Processing unmatched record " + str(counter) + " of " + str(len(final_unmatched_records_list)))
        print(unmatched_record.title)
        print(unmatched_record.collectibleId)
        valid_input = False
        while valid_input == False:
            database_id_to_associate = input("Type database ID, 's' to skip, 'e' to exclude or 'd' for summary.")
            if len(database_id_to_associate) > 0:
                if database_id_to_associate == 's':
                    skipped_records.append(unmatched_record)
                    valid_input = True
                elif database_id_to_associate == 'e':
                    excluded_records.append(unmatched_record)
                    valid_input = True
                elif database_id_to_associate == 'd':
                    for key in manually_associated_unmatched_records.keys():
                        print(key.__dict__)
                        print(manually_associated_unmatched_records[key])
                else:
                    if int(database_id_to_associate) < len(database_list):
                        manually_associated_unmatched_records[unmatched_record] = database_id_to_associate
                        UpdateFile.add_record_to_ManualAssociation_csv(unmatched_record.collectibleId, database_id_to_associate)
                        valid_input = True
                    else:
                        print("Please enter an ID between 1 and " + str(len(database_list)))
            else:
                print("Please enter an ID")
from CollectionRecord import  CollectionRecord
from DatabaseRecord import DatabaseRecord

# TODO
# Add ID's to Database records - can be used for manual association.
# Add manual association logic - loop through collectibles not matched, input database record ID to associte too.

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

    count = 0
    for record in collection_could_not_be_matched_list:
        if len(record.player) > 0:
            print(record.__dict__)
            count += 1

    print(count)

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
    #Match collection records to database.
    collection_matched_database_dict, collection_could_not_be_matched_list = \
        CollectionDatabaseMatcher.match_collection_records_to_database_record(collection_list, database_list)
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

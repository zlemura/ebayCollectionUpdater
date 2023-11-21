import CollectionDatabaseMatcher
import OpenFile


# TODO
# Add ID's to Database records - can be used for manual association.
# Loop through collection file.
# Determine record from database record from collection record title - extracing collectibleId.
# Create new title for collection record.
# Update attributes - if applicable.
# Open eBay.
# Loop through collection.
# Match record from collection record collectibleId and update to new title.
# Update collection record attributes (if applicable).
# Save changes to collection record.
# Add validation logic - take collection, match record, verify title is correct format.
# Add manual association logic - loop through collectibles not matched, input database record ID to associte too.

def main():
    collection_list = OpenFile.open_collection_file()
    database_list = OpenFile.open_database_file()
    CollectionDatabaseMatcher.match_collection_records_to_database_record(collection_list, database_list)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

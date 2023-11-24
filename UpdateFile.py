from csv import writer, reader

def add_record_to_ManualAssociation_csv(collectibleId, databaseId):
    manual_association_csv = open('ManualAssociation.csv', 'r')
    datareader = reader(manual_association_csv)

    for row in datareader:
        collectibleId_found = False
        if collectibleId in row:
            collectibleId_found = True
            break

    if collectibleId_found == False:
        manual_association_csv = open('ManualAssociation.csv', 'a', newline='')
        writer_object = writer(manual_association_csv)
        List = [collectibleId, databaseId]
        writer_object.writerow(List)
        manual_association_csv.close()
        print("ManualAssociation.csv updated successfully!")
    else:
        print("CollectibleId found in ManualAssociation.csv. File not updated!")

def add_record_to_FinalAssociation_csv(collectibleId, databaseId):
    manual_association_csv = open('FinalAssociation.csv', 'r')
    datareader = reader(manual_association_csv)

    for row in datareader:
        collectibleId_found = False
        if collectibleId in row:
            collectibleId_found = True
            break

    if collectibleId_found == False:
        final_association_csv = open('FinalAssociation.csv', 'a', newline='')
        writer_object = writer(final_association_csv)
        List = [collectibleId, databaseId]
        writer_object.writerow(List)
        final_association_csv.close()
        print("FinalAssociation.csv updated successfully!")
    else:
        print("CollectibleId found in FinalAssociation.csv. File not updated!")

def add_record_to_Exclusions_csv(collectibleId):
    exclusions_csv = open('Exclusions.csv.csv', 'r')
    datareader = reader(exclusions_csv)

    for row in datareader:
        collectibleId_found = False
        if collectibleId in row:
            collectibleId_found = True
            break

    if collectibleId_found == False:
        exclusions_csv = open('Exclusions.csv.csv', 'a', newline='')
        writer_object = writer(exclusions_csv)
        List = [collectibleId]
        writer_object.writerow(List)
        exclusions_csv.close()
        print("Exclusions.csv updated successfully!")
    else:
        print("CollectibleId found in Exclusion.csv. File not updated!")

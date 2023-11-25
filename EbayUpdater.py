import OpenFile
import Selenium


def update_collectible_record(driver, collectibleId, databaseId):
    collection_record = OpenFile.fetch_collectible_record_by_collectibleId(collectibleId)
    database_record = OpenFile.fetch_database_record_by_databaseId(databaseId)

    #Open URL - https://www.ebay.com/collection/collectible?notionalTypeId=Soccer&period=1Y&collectibleId={collectibleId}
    driver = Selenium.open_collectible_page(driver, collectibleId)

    #Find update button.

    #Click update button.

    #Find title element.

    #Update to formatted title - Player + Set or Season + Manufacturer + Card number + Variant + Grader + Grade

    #Find 'Show More' button.

    #Click 'Show More' button.

    #Find Parrallel field.

    #Update Parrallel field.

    #Find 'Save Changes' button.

    #Click 'Save Changes' button.

    #Log change to file.

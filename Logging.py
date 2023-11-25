import logging

def log_update_to_collection(collectibleId, databaseId):
    logging.basicConfig(filename="collection_updates.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("CollectibleId - " + str(collectibleId) + " updated with reference to databaseId - " + str(databaseId))
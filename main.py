from sensor.configuration.mongo_db_connection import MongoDBClient

if __name__ ==' __main__' :
    mongoclient = MongoDBClient()
    print('collection_name:', mongoclient.database.list_collection_names())

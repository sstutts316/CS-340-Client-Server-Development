#Example Python Code to Insert a Document

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passwd, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = passwd
        HOST = host
        PORT = port
        DB = database
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                #Attempt to insert a document into the collection
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise ValueError("Nothing to save because the data parameter is empty")
        
# Read method to implement the R in CRUD.
    def read(self, query):        
        try:
            #Attempt to query documents from the collection
            result = self.collection.find(query)
            return result
        except Exception as e:
            print(f"Error querying documents: {e}")
            return False
        
# Update method to implement the U in CRUD.
    def update(self, query, data):
        """Update method to modify document(s) in the collection."""
        try:
            # Use update_many to update multiple documents, update_one for a single document
            result = self.collection.update_many(query, {"$set": data})
            return result.modified_count
        except Exception as e:
            print(f"Error updating documents: {e}")
            return 0

# Delete method to implement the D in CRUD.
    def delete(self, query):
        """Delete method to remove document(s) from the collection."""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting documents: {e}")
            return 0
from pymongo.mongo_client import MongoClient

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://root:1234@cluster0.zv4whxp.mongodb.net/?retryWrites=true&w=majority"

# Set the Stable API version when creating a new client
conn = MongoClient(uri)
                          
# Send a ping to confirm a successful connection
try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
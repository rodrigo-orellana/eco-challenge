import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
# "mongodb://rodrigoesteban:r0k4FCFHDNGJKnlh@123.45.67.89:27017/MiBaseDatos")  # defaults to port 27017mongodb+srv://rodrigoesteban:<password>@cluster0-qazzt.mongodb.net/test?retryWrites=true&w=majority
db = client.sample_airbnb
my_collection = db.listingsAndReviews
# print the number of documents in a collection
print(my_collection.count_documents({}))

# direccion = "mongodb://127.0.0.1:27017/MiBaseDatos"
#direccion = "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/MiBaseDatos?retryWrites=true&w=majority"
#direccion = "mongodb+srv://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net/MiBaseDatos?ssl=true&ssl_cert_reqs=CERT_NONE"
#direccion = "mongodb://rodrigoesteban:r0k4FCFHDNGJKnlh@cluster0-qazzt.mongodb.net:27017"

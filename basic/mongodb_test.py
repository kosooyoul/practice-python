from pymongo import MongoClient

print('# Start')

mongo = MongoClient('mongodb://localhost:27017/')
db = mongo.blog

print(db.posts.insert({'title': 'hello', 'content': 'hmmmm'}))
print(db.posts.count())

# Read 1 document
# print(db.posts.find_one())

# Read all documents
posts = db.posts.find()
for item in posts: print(item)

mongo.close()

print('# End')
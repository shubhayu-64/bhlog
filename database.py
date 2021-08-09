from datetime import datetime
import pymongo
from pymongo import MongoClient
from schemas import Bhlog_DB

cluster = MongoClient(
    "mongodb+srv://admin:admin@bhlogdb.tgscv.mongodb.net/Bhlog_DB?retryWrites=true&w=majority")

db = cluster["Bhlog_DB"]
collection = db["Bhlog_data"]


async def set_id():
    data = collection.find({})
    id = len(list(data)) + 1
    return id


async def ifBhlogExists(id: int):
    exist_check = str(collection.find_one({"_id": id}))
    if exist_check == "None":
        return False
    return True


async def getAllBhlogs():
    data = collection.find({})
    bhlogs = list(data)
    return bhlogs


async def getBhlog(_id: int):
    bhlog: Bhlog_DB = {}
    data = collection.find_one({"_id": _id})
    return data


async def add_new_bhlog(bhlog: Bhlog_DB):
    post = {'_id': bhlog.id,
            'title': bhlog.title,
            'content': bhlog.content,
            'feature_image': bhlog.feature_image,
            'tags': bhlog.tags,
            'created_at': bhlog.created_at,
            'updated_at': bhlog.updated_at}
    collection.insert_one(post)
    return post


async def updateBhlog(bhlog: Bhlog_DB):
    data = bhlog.dict()
    print(data)
    collection.update_one({"_id": data['id']}, {
                          "$set": {"title": data["title"],
                                   "content": data["content"],
                                   "feature_image": data["feature_image"],
                                   "tags": data["tags"], "updated_at": datetime.now()}})

    return await getBhlog(data["id"])


async def deleteBhlog(id: int):
    collection.delete_one({'_id': id})
    return "Bhlog deleted successfully"

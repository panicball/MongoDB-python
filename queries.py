import pymongo
from bson.code import Code

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["cinema"]
mycol = mydb["film"]
mycol1 = mydb["movie_screening"]


def menu():
    print (" ")
    print ("  MongoDB queries ")
    print ("-----------------------------")
    print ("1. Retrieve embedded entities ")
    print ("2. Retrieve aggregating querie ")
    print ("3. Retrieve aggregating querie with map-reduce ")
    print ("4. Retrieve embedded entities 2")
    print ("5. Retrieve aggregating querie 2")
    print ("6. Retrieve aggregating querie with map-reduce 2")
    print ("7. Exit ")
    print (" ")
    return int(input ("Choose your option: "))


def embedded_entities():
    x = []
    p = mydb.film.find({ "review": {"$exists": "true"}}, { "_id": 0, "id": 0, "genre": 0, "director": 0, "budget": 0} )
    for i in p:
        x.append(i)
        print(i)


def aggregating_querie():
    agg_result =  mydb.film.aggregate( [
        { "$match": { "genre" : "Adventure" } },
        { "$group": { "_id": "$director", "total": { "$sum": "$budget" } } }
        ] )

    for i in agg_result: 
        print(i)


def aggregating_querie_map_reduce():
    map = Code("function () {"
            "     emit(this.director, this.budget);"
            "}")

    reduce = Code("function (key, value) {"
                "    return Array.sum(value);"
                "}")

    result = mycol.map_reduce(map, reduce, "myresults", query = {"genre":"Adventure"})
    for doc in result.find():
        print(doc)


def embedded_entities2():
    x = []
    p = mydb.film.find({ "director": {"$exists": "true"}}, { "_id": 0, "director": 1} ).distinct("director")
    for i in p:
        x.append(i)
        print(i)


def aggregating_querie2():
    agg_result =  mydb.film.aggregate( [
        { "$group": { "_id": "$director", "film_number": { "$sum": 1 } } }
        ] )

    for i in agg_result: 
        print(i)


def aggregating_querie_map_reduce2():
    map = Code("function () {"
            "     emit(this.director, 1);"
            "}")

    reduce = Code("function (key, value) {"
                "    return Array.sum(value);"
                "}")

    result = mycol.map_reduce(map, reduce, "myresults2")
    for doc in result.find():
        print(doc)


print ("")
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    print (" ")
    if choice == 1:
        embedded_entities()
    elif choice == 2:
        aggregating_querie()
    elif choice == 3:
        aggregating_querie_map_reduce()
    elif choice == 4:
            embedded_entities2()
    elif choice == 5:
            aggregating_querie2()
    elif choice == 6:
        aggregating_querie_map_reduce2()
    elif choice == 7:
        loop = 0

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["cinema"]
mycol = mydb["film"]

film = [
    { 
        "id": 0,
        "title": "Ratatouille", 
        "genre": "Fantasy",
        "review": [{
            "stars": 5,
            "comment": "comment_0_0"
        }, {
            "stars": 4,
            "comment": "comment_0_1"
        }],

        "director": {
            "name": "Brad",
            "surname": "Bird"
        },

        "budget": 150
    },
#--------------------------------------
    { 
        "id": 1,
        "title": "Shrek", 
        "genre": "Comedy",
        "review": [{
            "stars": 5,
            "comment": "comment_1_0"
        }, {
            "stars": 5,
            "comment": "comment_1_1"
        }, {
            "stars": 5,
            "comment": "comment_1_2"
        }],

        "director": {
            "name": "Andrew",
            "surname": "Adamson"
        },

        "budget": 125
    },
#--------------------------------------
    { 
        "id": 2,
        "title": "Dumbo", 
        "genre": "Adventure",
        "review": [{
            "stars": 2,
            "comment": "comment_2_0"
        }],

        "director": {
            "name": "Ben",
            "surname": "Sharpsteen"
        },

        "budget": 1.3
    },
#--------------------------------------
    { 
        "id": 3,
        "title": "The Incredibles", 
        "genre": "Adventure",
        "review": [{
            "stars": 5,
            "comment": "comment_3_0"
        }, {
            "stars": 4,
            "comment": "comment_3_1"
        }, {
            "stars": 5,
            "comment": "comment_3_2"
        }],

        "director": {
            "name": "Brad",
            "surname": "Bird"
        },

        "budget": 92
    },
#--------------------------------------
    { 
        "id": 4,
        "title": "Coco", 
        "genre": "Adventure",
        "review": [{
            "stars": 5,
            "comment": "comment_4_0"
        }, {
            "stars": 2,
            "comment": "comment_4_1"
        }, {
            "stars": 1,
            "comment": "comment_4_2"
        }, {
            "stars": 2,
            "comment": "comment_4_3"
        }, {
            "stars": 3,
            "comment": "comment_4_4"
        }],

        "director": {
            "name": "Lee",
            "surname": "Unkrich"
        },

        "budget": 175
    },
#--------------------------------------
    { 
        "id": 5,
        "title": "The Incredibles 2", 
        "genre": "Adventure",
        "review": [{
            "stars": 5,
            "comment": "comment_5_0"
        }, {
            "stars": 4,
            "comment": "comment_5_1"
        }, {
            "stars": 3,
            "comment": "comment_5_2"
        }],

        "director": {
            "name": "Brad",
            "surname": "Bird"
        },

        "budget": 200
    },
#--------------------------------------
    { 
        "id": 5,
        "title": "Toy story", 
        "genre": "Adventure",
        "review": [{
            "stars": 2,
            "comment": "comment_6_0"
        }, {
            "stars": 4,
            "comment": "comment_6_1"
        }],

        "director": {
            "name": "Lee",
            "surname": "Unkrich"
        },

        "budget": 30
    }
]

x = mycol.insert_many(film)

mycol1 = mydb["movie_screening"]

movie_screening = [
    { 
            "id": 0,
            "film_id":0,
            "time": "12:45",
            "cost": 10
     },
#--------------------------------------     
    { 
            "id": 1,
            "film_id":1,
            "time": "17:00",
            "cost": 12
     },
#--------------------------------------     
    { 
            "id": 2,
            "film_id":1,
            "time": "23:25",
            "cost": 15
     },
#--------------------------------------
    { 
            "id": 3,
            "film_id":2,
            "time": "9:30",
            "cost": 6
     },
#--------------------------------------
    { 
            "id": 4,
            "film_id":2,
            "time": "14:35",
            "cost": 6
     },
#--------------------------------------     
    { 
            "id": 5,
            "film_id":3,
            "time": "7:00",
            "cost": 9
     },
#--------------------------------------     
    { 
            "id": 6,
            "film_id":4,
            "time": "20:50",
            "cost": 13
     },
#--------------------------------------
    { 
            "id": 7,
            "film_id":4,
            "time": "19:35",
            "cost": 5
     },
#--------------------------------------
    { 
            "id": 8,
            "film_id":5,
            "time": "4:35",
            "cost": 16
     }
]

x = mycol1.insert_many(movie_screening)


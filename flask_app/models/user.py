# import the function that will return the instance of a connection

from flask_app.config.mysqlconnection import connectToMySQL

#model the class after the user table  from our databse 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.email= data['email']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']


    # Use class methods to query the database 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # call the connectToMySQL function with the schema you are targeting 

        users_db = connectToMySQL('users').query_db(query)

        # create an empty list to append our instances of users
        users = []
        # iterate over the db results and create instances of users with cls 
        for user in users_db:
            users.append(cls(user))
        return users

    # class method to save a user to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s,%(lname)s, %(email)s, now(), now() );"

        return connectToMySQL('users').query_db(query, data)


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users').query_db(query, data)

        this_user = cls(results[0])
        return this_user

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s,email = %(email)s WHERE id = %(id)s;"
        results = connectToMySQL('users').query_db(query, data)
        return results
        

    
    
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.__init__ import DATABASE

class Ninjas: 
    def __init__( self , data ): 
        self.id = data['id']   
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


# READ ALL
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM ninjas;
        """
        results = connectToMySQL(DATABASE).query_db(query)

        ninja_list = []

        for row in results:
            new_ninja = cls(row)
            ninja_list.append(new_ninja)

        return ninja_list

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name,last_name,age) VALUES (%(first_name)s,%(last_name)s,%(age)s);"

        result = connectToMySQL(DATABASE).query_db(query,data)
        return result


    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])


    #UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


    #DELETE
    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
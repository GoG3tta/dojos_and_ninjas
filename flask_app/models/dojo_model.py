from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.__init__ import DATABASE

class Dojos: 
    def __init__( self , data ): 
        self.id = data['id']   
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM dojos;
        """
        results = connectToMySQL(DATABASE).query_db(query)

        dojo_list = []

        for row in results:
            new_dojo = cls(row)
            dojo_list.append(new_dojo)

        return dojo_list

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s,%(created_at)s,%(Updated_at)s);"

        result = connectToMySQL(DATABASE).query_db(query,data)
        return result


    # @classmethod
    # def get_one(cls,data):
    #     query  = "SELECT * FROM dojos WHERE id = %(id)s";
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     return cls(result[0])


    # #UPDATE
    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE dojos SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s,updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query,data)


    # #DELETE
    # @classmethod
    # def destroy(cls,data):
    #     query  = "DELETE FROM dojos WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query,data)
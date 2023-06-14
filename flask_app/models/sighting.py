from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Sighting:
    db_name = 'python_exam_db'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.location = db_data['location']
        self.what_happened = db_data['what_happened']
        self.date = db_data['date']
        self.num_of_Saquatches = db_data['num_of_Saquatches']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO sightings (location, what_happened, date, num_of_Saquatches, user_id) VALUES (%(location)s,%(what_happened)s,%(date)s,%(num_of_Saquatches)s,%(user_id)s);"
        return connectToMySQL('python_exam_db').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings;"
        results =  connectToMySQL('python_exam_db').query_db(query)
        all_sightings = []
        for row in results:
            
            all_sightings.append( cls(row) )
        return all_sightings
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        results = connectToMySQL('python_exam_db').query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE sightings SET location=%(location)s, what_happened=%(what_happened)s, date=%(date)s, num_of_Saquatches=%(num_of_Saquatches)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('python_exam_db').query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL('python_exam_db').query_db(query,data)
    
    
    @staticmethod
    def validate_sighting(sighting):
        is_valid = True
        if len(sighting['location']) < 2:
            is_valid = False
            flash("Name must be at least 2 characters","sighting")

        if len(sighting['what_happened']) < 3:
            is_valid = False
        
            flash("What must be at least 3 characters","sighting")
    
        if sighting['date'] == "":
            is_valid = False
            flash("Please enter a date","sighting")
        
        # if str(sighting['num_of_Saquatches']) > 0:
        #     is_valid = False
        #     flash("number must be at least filled","sighting")
        return is_valid
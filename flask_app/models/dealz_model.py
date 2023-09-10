from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user_model
from flask import flash


# Creating the class for dealz
class Dealz:
    def __init__(self, data):
        self.id = data["id"]
        self.price = data["price"]
        self.model = data["model"]
        self.make = data["make"]
        self.year = data["year"]
        self.city = data["city"]
        self.state = data["state"]
        self.zipcode = data["zipcode"]
        self.photoLink = data["photoLink"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    # Setting up the create method for the data creation
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO car_dealz (price, model, make, year, city, state, zipcode, photoLink, description, user_id)
            VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(city)s, %(state)s, %(zipcode)s, %(photoLink)s, %(description)s, %(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    # Gets all of the information when joining both tables
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM car_dealz
            JOIN users 
            WHERE users.id = car_dealz.user_id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        list_of_dealz = []
        for elements in results:
            this_deal = cls(elements)
            user_data = {
                **elements,
                "id": elements["users.id"],
                "created_at": elements["created_at"],
                "updated_at": elements["updated_at"],
            }
            this_deal.seller = user_model.User(user_data)
            list_of_dealz.append(this_deal)
        return list_of_dealz

    @classmethod
    def get_by_id(cls, id):
        data = {"id": id}
        query = """
                SELECT * FROM car_dealz
                JOIN users 
                ON users.id = car_dealz.user_id
                WHERE car_dealz.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        if results:
            this_deal = cls(results[0])
            each_data = results[0]
            user_data = {
                **each_data,
                "id": each_data["users.id"],
                "updated_at": each_data["updated_at"],
                "updated_at": each_data["updated_at"],
            }
            this_user = user_model.User(user_data)
            this_deal.seller = this_user
            return this_deal
        return False

    @classmethod
    def update(cls, data):
        query = """
                UPDATE car_dealz 
                SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, city = %(city)s, state = %(state)s, zipcode = %(zipcode)s, photoLink = %(photoLink)s, description = %(description)s
                WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    # Deleting from our database and our rendered page
    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM car_dealz 
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    # Creating a validator to ensure user is inputting the required length of each user input
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["price"]) < 1:
            is_valid = False
            flash("Enter a price greater than 0.")
        if len(data["model"]) < 1:
            is_valid = False
            flash("Model name must not be empty.")
        if len(data["make"]) < 1:
            is_valid = False
            flash("Make name must not be empty.")
        if len(data["year"]) < 1:
            is_valid = False
            flash("Year must not be empty.")
        if len(data["city"]) < 1:
            is_valid = False
            flash("City must not be empty.")
        if len(data["state"]) < 1:
            is_valid = False
            flash("State must not be empty.")
        if len(data["zipcode"]) < 1:
            is_valid = False
            flash("Zipcode must not be empty.")
        if len(data["description"]) < 1:
            is_valid = False
            flash("Description must not be empty.")

        return is_valid

# Gabe Conner
# Assignment 7.2

import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Establish connection
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()

     # Query 1: Select all fields for the studio table
    print("\n-- DISPLAYING Studio RECORDS --")
    query1 = "SELECT * FROM studio"
    cursor.execute(query1)
    studios = cursor.fetchall()
    for studio_id, studio_name in studios:
        print(f"Studio ID: {studio_id}")
        print(f"Studio Name: {studio_name}\n")
    
    # Query 2: Select all fields for the genre table
    print("\n-- DISPLAYING Genre RECORDS --")
    query2 = "SELECT * FROM genre"
    cursor.execute(query2)
    genres = cursor.fetchall()
    for genre_id, genre_name in genres:
        print(f"Genre ID: {genre_id}")
        print(f"Genre Name: {genre_name}\n")

    # Query 3: Select movie names with a runtime of less than 2 hours
    print("\n-- DISPLAYING Short Film RECORDS --")
    query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    cursor.execute(query3)
    films = cursor.fetchall()
    for film_name, film_runtime in films:
        print(f"Film Name: {film_name}")
        print(f"Runtime: {film_runtime}\n")

    # Query 4: List of film names and directors grouped by director
    print("\n-- DISPLAYING Director RECORDS in Order --")
    query4 = """
        SELECT film_name, film_director 
        FROM film
        ORDER BY film_director
    """
    cursor.execute(query4)
    film_directors = cursor.fetchall()
    for film_name, film_director in film_directors:
        print(f"Film Name: {film_name}")
        print(f"Director: {film_director}\n")

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The specified database does not exist.")
    else:
        print(err)

        db.close()
    

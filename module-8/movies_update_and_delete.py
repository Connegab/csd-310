# Gabe Conner
# Assignment 8.2

import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost", 
    user="movies_user", 
    password="popcorn",
    database="movies" 
)

cursor = db.cursor()  # Create a cursor object

def show_films(cursor, title):
    """Display films in specific format"""
    print("\n-- {} --".format(title))
    
    # Query with INNER JOIN to fetch genre and studio names
    query = """
    SELECT film.film_name AS 'Name', 
           film.film_director AS 'Director', 
           genre.genre_name AS 'Genre', 
           studio.studio_name AS 'Studio'
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)  # Execute the query
    films = cursor.fetchall()  # Fetch all results
    
    # Iterate over results and print in a structured format
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre Name: {film[2]}")
        print(f"Studio Name: {film[3]}\n")


# Step 1: Display initial films
show_films(cursor, "DISPLAYING FILMS")

# Step 2: Insert a new record into the film table
insert_query = """
INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
VALUES (%s, %s, %s, %s, %s, %s);
"""
cursor.execute(insert_query, ("The Matrix", "1999", 94, "Lana Wachowski", 1, 2))  # Update IDs based on your schema
db.commit()

# Step 3: Display films after insertion
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Step 4: Update the film "Alien" to the Horror genre
update_query = """
UPDATE film 
SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') 
WHERE film_name = 'Alien';
"""
cursor.execute(update_query)
db.commit()

# Step 5: Display films after the update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

# Step 6: Delete the film "Gladiator"
delete_query = "DELETE FROM film WHERE film_name = 'Gladiator';"
cursor.execute(delete_query)
db.commit()

# Step 7: Display films after deletion
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close the database connection
cursor.close()
db.close()

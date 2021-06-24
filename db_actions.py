import mysql.connector as mysql

host = None
database = None
user = None
password = None

class Database:

    def connect():
        global host
        global database
        global user
        global password

        if host == None:
            with open("db_data.txt","r") as f:
                lines = f.readlines()
                host = lines[0]
                database = lines[1]
                user = lines[2]
                password = lines[3]

        global db_connection
        global cursor
        db_connection = mysql.connect(host=host, database=database, user=user, password=password)
        cursor = db_connection.cursor()

    def disconnect():
        db_connection.close()
        cursor.close()


    def add_elo_user(user_id, ign):
        Database.connect()

        insert_query = "INSERT INTO elos (user_id, ign, elo) VALUES (%s, %s, %s);"
        cursor.execute(insert_query, (int(user_id), str(ign), int(0),))
        db_connection.commit()

        Database.disconnect()
    
    def remove_elo_user(user_id):
        Database.connect()

        delete_query = "DELETE FROM elos WHERE user_id = %s;"
        cursor.execute(delete_query, (int(user_id),))
        db_connection.commit()

        Database.disconnect()

    def find_elo(user_id):
        Database.connect()

        find_query = "SELECT elo from elos where user_id = %s;"
        cursor.execute(find_query, (int(user_id),))
        data = cursor.fetchone()

        Database.disconnect()

        try:
            return data[0]
        except:
            return None

    def get_global_leaderboard():
        Database.connect()

        get_query = "Select * from elos;"
        cursor.execute(get_query)
        data = cursor.fetchall()

        data.sort(key=lambda x: x[2])
        data.reverse()

        return data
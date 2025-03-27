import sqlite3
import json

def database(file_path):  
    try:
        con = sqlite3.connect("Bike_Data_Base.sqlite3")
        cur = con.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS BIKE_INFORMATIONS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Bike_Name VARCHAR,
                bike_model_year VARCHAR,
                Bike_Currency VARCHAR,
                Bike_Price FLOAT,
                bike_power_cc INTEGER,
                bike_power_watt INTEGER,
                bike_type VARCHAR,
                bike_distance VARCHAR,
                condition VARCHAR
            )
        """)
        
        with open(file_path, 'r') as file:
            bike_datas = json.load(file)
        
        for bike_data in bike_datas:
            cur.execute("""
                INSERT INTO BIKE_INFORMATIONS (Bike_Name,bike_model_year,Bike_Price, Bike_Currency, bike_power_cc,bike_power_watt,bike_type,bike_distance,condition) 
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (bike_data['Bike Name'], bike_data['Bike Year'], bike_data['Bike Price'], bike_data['Bike Currency'],bike_data['Bike Power CC'],bike_data['Bike Power Watt'],bike_data['Type Of Bike'],bike_data['Bike Total Travel Distance'],bike_data['Condition Of Bike']))

        con.commit() 
        print("Data inserted successfully.")
    except Exception as e:
        print("ERROR:", e)
    finally:
        con.close()

database("bikes.json")

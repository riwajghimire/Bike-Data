import sqlite3
import csv

conn= sqlite3.Connection('Bike_Data_Base.sqlite3')


cursor = conn.cursor()
cursor.execute("select * from BIKE_INFORMATIONS")
with open("bike_data.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)


import mysql.connector
from server.models.Manufacturer import Manufacturer
config = {
'user':'testuser',
'password':'password1',
'host': '10.20.0.211',
'database': 'equipment_db'
}

cnx = mysql.connector.connect(**config)

def getManufacturers():
    manufacturers = []
    cursor = cnx.cursor()
    query = ("SELECT pkey, name  FROM manufacturer")
    cursor.execute(query)
    for (pkey, name) in cursor:
        temp = Manufacturer(pkey, name)
        manufacturers.append(temp)
    cursor.close()
    cnx.close()
    return manufacturers

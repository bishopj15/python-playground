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
    query = ("SELECT pkey, description  FROM equipment_type")
    cursor.execute(query)
    for (pkey, description) in cursor:
        temp = Manufacturer(pkey, description)
        manufacturers.append(temp)
    cursor.close()
    cnx.close()
    return manufacturers

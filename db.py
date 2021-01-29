import mysql.connector 
import csv

from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': '12345',
    'host': '35.228.178.37',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': './ssl/server-ca.pem',
    'ssl_cert': './ssl/client-cert.pem',
    'ssl_key': './ssl/client-key.pem'
}

config['database']='falcon_app'
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()
# cursor.execute("SELECT * FROM space_missions")
# cursor.execute("INSERT INTO users (username, password) VALUES ('admin','admin')")
# myresult = cursor.fetchall()


# for x in myresult:
#   print(x)

class MysqlConnection:
    
    # def recordToDict(self, list):
    #     record = {'id': list[0][0] ,
    #               'company_name': list[0][1] ,
    #               'location': list[0][2],
    #               'date': list[0][3],
    #               'detail': list[0][4],
    #               'rocket_status': list[0][5],
    #               'rocket': list[0][6],
    #               'mission_status': list[0][7],
    #               'isdel': list[0][8]}
    #     return record

    def listAll(self, limit):
        query = "SELECT id, company_name, location, date, detail, rocket_status, rocket, mission_status FROM space_missions WHERE isdel='false' LIMIT " + str(limit)
        cursor.execute(query)
        return cursor.fetchall()
    
    def getById(self, id):
        query = "SELECT id, company_name, location, date, detail, rocket_status, rocket, mission_status FROM space_missions WHERE id=" + str(id)
        cursor.execute(query)
        list = cursor.fetchall()
        record = {'id': list[0][0] ,
                  'company_name': list[0][1] ,
                  'location': list[0][2],
                  'date': list[0][3],
                  'detail': list[0][4],
                  'rocket_status': list[0][5],
                  'rocket': list[0][6],
                  'mission_status': list[0][7]}
        return record
    
    def loginGetByUsername(self, username):
        query = "SELECT username, password FROM users WHERE username=" + str(username)
        cursor.execute(query)
        list = cursor.fetchall()
        # record = {'username': list[0][0] ,
        #           'password': list[0][1]}
        return list
    
    def deleteById(self, id):
        query1 = "UPDATE space_missions SET isdel='true' WHERE id=" + str(id)
        cursor.execute(query1)
        query2 = "SELECT detail FROM space_missions WHERE id=" + str(id)
        cursor.execute(query2)
        return cursor.fetchall()

    def updateById(self, id, company_name, location, date, detail, rocket_status, rocket, mission_status):
        cursor.execute("UPDATE space_missions SET" +
                       " company_name='" + str(company_name) + "'" +
                       ", location='" + str(location) + "'" +
                       ", date='" + str(date) + "'" +
                       ", detail='" + str(detail) + "'" +
                       ", rocket_status='" + str(rocket_status) + "'" +
                       ", rocket='" + str(rocket) + "'" +
                       ", mission_status='" + str(mission_status) + "'" +
                       " WHERE id='" + str(id) + "'")
        cnxn.commit()
        return "Rekord zostal zaaktualizowany."

###DATABASE SSL###
#  mysql -uroot -p -h 35.228.178.37 \
#     --ssl-ca=server-ca.pem --ssl-cert=client-cert.pem \
#     --ssl-key=client-key.pem

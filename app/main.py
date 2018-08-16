# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from flask import Flask
import pymysql.cursors
import json

app = Flask(__name__)
listOfDevs = [{
                    'name':'ravi',
                    'skill':'gcp',
                    'team':'gcp'
                },
                {
                    'name':'ravi1',
                    'skill':'gcp1',
                    'team':'gcp1'
                }
            ]

@app.route('/developers/pushdata', methods=['GET'])
def pushSampleData():
    connection = createDBConnection()
    try:
        with connection.cursor() as cursor:
            for developer in listOfDevs:
                # Read a single record
                createsql = 'CREATE TABLE IF NOT EXISTS TEST ( id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), skill VARCHAR(30), team VARCHAR(50) )'
                cursor.execute(createsql)
                sql = "INSERT INTO TEST (name,skill,team) VALUES ("+"'" + developer['name'] + "'" + ',' + "'" + developer['skill'] + "'" + ',' + "'" +developer['team'] +"'"+ ')'
                print (sql)
                cursor.execute(sql)
                print ('SQL push successful' + developer['name'])
        connection.commit()
    finally:
        connection.close()
    return 'Data Inserted'

@app.route('/developers', methods=['GET'])
def getDevelopers():
    connection = createDBConnection()
    return json.dumps(getDevelopers(connection))

def createDBConnection ():
    connection = pymysql.connect(host=DB_HOST_NAME,
                                 user='root',
                                 password='DB_PASSWORD',
                                 db='developers',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def getDevelopers(connection):
    print('LOG: DB Request')
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * from TEST"
            cursor.execute(sql)
            result = cursor.fetchall()
            print('LOG: DB Response')
    finally:
        connection.close()
    return result

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

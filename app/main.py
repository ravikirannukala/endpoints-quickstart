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
from flaskext.mysql import MySQL
import json

app = Flask(__name__)

@app.route('/airportName', methods=['GET'])
def airportName():
    return json.dumps(getDBData())


def getDBData():
    mysql = MySQL()

    # MySQL configurations
    print ('BEFORE DB')
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
    app.config['MYSQL_DATABASE_DB'] = 'mysql'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    print('BEFORE DB - init')
    mysql.init_app(app)
    print('BEFORE DB-connect')
    conn = mysql.connect()
    print('BEFORE DB- after connect')
    cursor = conn.cursor()
    print('BEFORE DB-cursor')
    cursor.execute("select * from mysql.TEST")
    print('BEFORE DB - after query')
    outputList = []
    for row in cursor.fetchall():
        output={}
        output['id'] = row[0]
        output['name'] = row[1]
        output['skill'] = row[2]
        output['team'] = row[3]
        outputList.append(output)
    cursor.close()
    return outputList

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


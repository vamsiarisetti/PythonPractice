import mysql.connector



def dbConn():
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'admin',
                'database': 'vsearchlogDB', }
    conn = mysql.connector.connect(**dbconfig)
    _SQL = """insert into log
     (phrase, letters, ip, browser_string, results)
     values
     (%s,%s,%s,%s,%s)"""
    cursor = conn.cursor()
    cursor.execute(_SQL, ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}"))
    conn.commit()

    if(cursor.close()):
        conn.close()
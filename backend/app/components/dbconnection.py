from app import mysql


def selectResearches():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM researches")
    if result > 0:
        return cur.fetchall()
    else:
        return False


def insertResearches(params):
    cur = mysql.connection.cursor()
    sql = "INSERT INTO researches (ip_address, site, type, query, result) VALUES(%s, %s, %s, %s, %s)"
    cur.execute(sql, params)
    mysql.connection.commit()
    cur.close()
    return True




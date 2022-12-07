import MySQLdb as mdb
from bottle import FormsDict
from hashlib import md5

# connection to database project2
def connect():
    return mdb.connect(host="localhost",
                       user="project2",
                       passwd=open("dbrw.secret").read().strip(),
                       db="project2");

#creates a row in table named user
def createUser(username, password):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("INSERT INTO users (username, password, passwordhash) VALUES(%s, %s, %s)",
                (username, password, md5(password).digest()))
    db_rw.commit()

#validates if username,password pair provided by user is correct or not
def validateUser(username, password):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("SELECT id FROM users WHERE username=%s AND password=%s", [username, password])
    if cur.rowcount < 1:
        return False
    return True

#checks if there exists username in table users
#if user exists return (id, username) pair
def fetchUser(username):
    db_rw = connect()
    cur = db_rw.cursor(mdb.cursors.DictCursor)
    print username
    cur.execute("SELECT id, username FROM users WHERE username=%s" , [username])
    if cur.rowcount < 1:
        return None
    return FormsDict(cur.fetchone())

#adds a query from user with id=user_id into table named history
def addHistory(user_id, query):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("INSERT INTO history (user_id, query) VALUES(%s, %s)", [user_id, query])
    db_rw.commit()

#grabs last 15 queries made by user with id=user_id from table named history
def getHistory(user_id):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("SELECT DISTINCT query FROM history WHERE user_id = %s ORDER BY id DESC LIMIT 15", [user_id])
    rows = cur.fetchall();
    return [row[0] for row in rows]

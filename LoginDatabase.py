import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("./HomeProject.db")
        self.c = self.conn.cursor()

    def close():
        self.conn.close()

    def sign_up(self, username, password, email):
        self.c.execute(''' INSERT INTO users
            VALUES ('{}', '{}', '{}') '''.format(
                username, password, email))
        self.conn.commit()

    def login(self, username, password):
        user = self.c.execute(''' SELECT name, email FROM users WHERE
            name='{}' and password='{}' '''.format(username, password)).fetchone()

        return user
import sqlite3
from sqlite3 import Error

class Main:
    def execute_query(self, query_list, commit=False, fetchAll=False, fetchOne=False):
        try:
            conn = sqlite3.connect("learnKorean.db")
            c = conn.cursor()
            result = None
            if type(query_list) == str:
                c.execute(query_list)
            else:
                for query in query_list:
                    c.execute(query)
            if commit:
                conn.commit()
            if fetchAll:
                result = [row for row in c.fetchall()]
            if fetchOne:
                result = c.fetchone()
        except Error as e:
            print(e)
        finally:
            c.close()
            conn.close()
            return result

    def read_database(self, db_name):
        data = self.execute_query(query_list="SELECT * FROM " + db_name + "", fetchAll=True)
        print(data)

class User(Main):
    def __init__(self, username_arg, password_arg, remember_me_arg):
        self.username = username_arg
        self.password = password_arg
        self.remember_me = remember_me_arg

    def to_string(self):
        return self.username + ", " + self.password + ", " + str(self.remember_me)+ "."

    def add_user(self):
        query1 ="""CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, password TEXT NOT NULL, remember_me INTEGER NOT NULL)"""
        query2 = "INSERT INTO user (name, password, remember_me) VALUES (?,?,?)", (self.username, self.password, self.remember_me)

    def del_user(self, name):
        self.execute_query(query_list='DELETE FROM user WHERE name = ' + name + '', commit=True)

    def check_user(self):
        query = "SELECT * FROM user WHERE name = '" + self.username + "'"
        exec_query = self.execute_query(query_list=query, fetchOne=True)
        if exec_query == None:
            return False
        else:
            query_list = [x for x in exec_query]
            if query_list[1] == self.username and query_list[2] == self.password:
                return True
            else:
                return False
class Topics(Main):
    def add_topic(self, title, description, rule1, example1, topic, rule2="", rule3="", rule4="", rule5="", rule6="", rule7="", rule8="", example2="", example3="", example4="", example5="", example6="", example7="", example8=""):
        values = (topic, title, description,
                  rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
                  example1, example2, example3, example4, example5, example6, example7, example8)
        query2 = 'INSERT INTO topics VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        try:
            conn = sqlite3.connect("learnKorean.db")
            c = conn.cursor()
            c.execute(query2, values)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            c.close()
            conn.close()

    def update_topic(self, id, title, description, rule1, example1, topic, rule2, rule3, rule4, rule5, rule6, rule7, rule8, example2, example3, example4, example5, example6, example7, example8):
        values = (id, topic, title, description,
                  rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
                  example1, example2, example3, example4, example5, example6, example7, example8)
        query2 = "UPDATE topics SET topic = ? , title = ? , description = ?  WHERE id = ?"

        try:
            conn = sqlite3.connect("learnKorean.db")
            c = conn.cursor()
            c.execute(query2, values)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            c.close()
            conn.close()
    def del_topic(self, id):
        self.execute_query(query_list='DELETE FROM topics WHERE id = ' + id + '', commit=True)

    def check_topic(self):
        #Check columns
        #query = "PRAGMA table_info(topics)"
        query = "SELECT * FROM topics"
        exec_query = self.execute_query(query_list=query, fetchAll=True)
        if exec_query == None:
            return False
        else:
            return exec_query
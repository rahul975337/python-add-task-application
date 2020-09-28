import sqlite3 as lite
# functionality goes here
class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY AUTOINCREMENT,name TEXT,description TEXT,price TEXT,is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB!")
    def insert_data(self, data):
        try:
            with con:
                cur=con.cursor()
                cur.execute(
                    "INSERT INTO course(name,description,price,is_private) VALUES (?,?,?,?)", data
                    )
        except Exception:
            return False
# ////////////////////////////////
    def fetch_data(self):
        try:
            with con:
                cur=con.cursor()
                cur.execute(
                    "SELECT * FROM course"
                    )
                return cur.fetchall()
        except Exception:
            return False
# //////////////////////////////////
    def delete_data(self, id):
        try:
            with con:
                cur=con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(
                   sql,[id]
                    )
        except Exception:
            return False

#  provide interface to user
def main():
    print("*"*40)
    print("\n::COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()
    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)
    print('\nPress 1. Insert a new Course\n')
    print('\nPress 2. Show all Courses\n')
    print('\nPress 3. Delete a Course (NEED ID OF COURSE)\n')
    print("#"*40)
    print("\n")
    choice  = input("\n Enter a choice: ")
    if choice == "1":

        name = input("\n ENTER course name: ")
        description = input("\n ENTER course description: ")
        price = input("\n ENTER course price: ")
        private = input("\n Is this course private (0/1): ")
        if db.insert_data([name,description,price,private]):

            print("Course was inserted successfully")
        else:
            print("Oops !! Something went wrong")






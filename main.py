import mysql.connector as connector


class DBHelper:
    """
    Created class for performing curd operations on sql queries
    """

    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='Shubham@123',
                                     database='pythontest')

    def user_table(self):
        """
        This function is for creating a table
        """
        query = 'create table if not exists user(userID int primary key,userName varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self, userid, username, phone):
        """
        This function is for inserting data in the table
        """
        query = "insert into user(userid,userName,phone) values(%d,'%s','%s')" % (userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    def delete_user(self, userid):
        """
        this function is for deleting the user by referring his user id
        """
        query2 = "delete from user where userid={}" % userid
        print(query2)
        cur = self.con.cursor()
        cur.execute(query2)
        self.con.commit()
        print("deleted")

    def update_user(self, userid, newname):
        """
        this function is for updating the users information
        """
        query3 = "update user set userName='{}' where userid={}" % (newname, userid)
        cur = self.con.cursor()
        cur.execute(query3)
        self.con.commit()

    def address(self):
        """
        In this function new table is created and fetched with the existing table by using foreign key
        """
        query = 'create table user_address(userID int, city varchar(15),zip varchar(6), ' \
                ' FOREIGN KEY (userID) REFERENCES user(userID))'
        cur = self.con.cursor()
        cur.execute(query)
        print("executed second table query")

    def insert_into_address(self, userid, city, zipcode):
        """
        In this function inserting a users address info
        """
        query = "insert into user_address(userID,city,zip) values(%d,'%s', '%s')" % (userid, city, zipcode)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


helper = DBHelper()
helper.user_table()
helper.insert_user(3333, "Pankaj", "876543")
helper.insert_user(2324, "Onkar", "666666")
helper.insert_user(4447, "Aditya", "757575")
helper.delete_user()
helper.update_user(2324, 'Raju')
helper.address()
helper.insert_into_address(1436, "pune", '422610')

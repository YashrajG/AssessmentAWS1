import pymysql
import sys

connection = pymysql.connect(
    host='yrdbinstance.csaruqlxxway.us-east-1.rds.amazonaws.com',
    user=sys.argv[1],
    password=sys.argv[2],
    db='yrdb',
)
my_database = connection.cursor()

choice = 0
while(choice != '5'):
    choice = input("Choose an action number:\n1. Insert record\n2. Read Table\n3. Update a value\n4. Delete a record\n5. Exit\nChoice : ")
    if choice == '1':
        gid = input("Enter new ID:")
        gname = input("Enter new name:")
        publisher = input("Enter new publisher:")
        rating = input("Enter new rating:")
        
        sql_statement = "INSERT INTO games (gid,gname,publisher,rating) values(%s,%s,%s,%s)"
        values = (gid,gname,publisher,rating)
        my_database.execute(sql_statement,values)
        connection.commit()
    elif choice == '2':
        sql_statement = "SELECT * FROM games"
        my_database.execute(sql_statement)
        output = my_database.fetchall()
        for x in output:
          print(x)
    elif choice == '3':
        updationChoice = input("Choose a column name to update:\n1. gid\n2. gname\n3. publisher\n4. rating\nChoice : ")
        
        #TODO automate
        if updationChoice not in {'gid', 'gname', 'publisher', 'rating'}:
            print('invalid column name')
            continue
        newValue = input("New value : ")
        gid = input("where gid = ")
        sql_statement = "UPDATE games SET " + updationChoice + "='" + newValue + "' where gid='" + gid + "'"
        my_database.execute(sql_statement)
        connection.commit()
    elif choice == '4':
        gid = input("where gid = ")
        sql_query = "DELETE FROM games where gid='" + gid + "'"
        my_database.execute(sql_query)
        connection.commit()
        print("Row(s) deleted successfully!!!!")

#TODO handle injection
#TODO handle multiple tables

'''
ubuntu@ip-172-31-92-62:~$ python3 Problem8.py yashrajgangal yashyashyash
Choose an action number:
1. Insert record
2. Read Table
3. Update a value
4. Delete a record
5. Exit
Choice : 2
(1, 'fortnite', 'epicgames', 4)
(2, 'FIFA19', 'easports', 5)
(3, 'CS:CZ', 'steam', 4)
(4, 'CS:GO', 'steam', 9)
(5, 'Age of Emp', 'Ensemble', 8)
Choose an action number:
1. Insert record
2. Read Table
3. Update a value
4. Delete a record
5. Exit
Choice : 1
Enter new ID:6
Enter new name:AgeOfMytho
Enter new publisher:ensemble
Enter new rating:9
Choose an action number:
1. Insert record
2. Read Table
3. Update a value
4. Delete a record
5. Exit
Choice : 2
(1, 'fortnite', 'epicgames', 4)
(2, 'FIFA19', 'easports', 5)
(3, 'CS:CZ', 'steam', 4)
(4, 'CS:GO', 'steam', 9)
(5, 'Age of Emp', 'Ensemble', 8)
(6, 'AgeOfMytho', 'ensemble', 9)
# Choose an action number:
# 1. Insert record
# 2. Read Table
# 3. Update a value
# 4. Delete a record
# 5. Exit
# Choice : 3
# Choose a column name to update:
# 1. gid
# 2. gname
# 3. publisher
# 4. rating
# Choice : publisher
# New value : ea
# where gid = 2
# Choose an action number:
# 1. Insert record
# 2. Read Table
# 3. Update a value
# 4. Delete a record
# 5. Exit
# Choice : 2
# (1, 'fortnite', 'epicgames', 4)
# (2, 'FIFA19', 'ea', 5)
# (3, 'CS:CZ', 'steam', 4)
# (4, 'CS:GO', 'steam', 9)
# (5, 'Age of Emp', 'Ensemble', 8)
# (6, 'AgeOfMytho', 'ensemble', 9)
# Choose an action number:
# 1. Insert record
# 2. Read Table
# 3. Update a value
# 4. Delete a record
# 5. Exit
# Choice : 4
# where gid = 1
# Row(s) deleted successfully!!!!
# Choose an action number:
# 1. Insert record
# 2. Read Table
# 3. Update a value
# 4. Delete a record
# 5. Exit
# Choice : 2
# (2, 'FIFA19', 'ea', 5)
# (3, 'CS:CZ', 'steam', 4)
# (4, 'CS:GO', 'steam', 9)
# (5, 'Age of Emp', 'Ensemble', 8)
# (6, 'AgeOfMytho', 'ensemble', 9)
# Choose an action number:
# 1. Insert record
# 2. Read Table
# 3. Update a value
# 4. Delete a record
# 5. Exit
Choice : 5
'''

import mysql.connector
import random

fortune= random.sample(range(156), 156)
random.shuffle(fortune,random.random)
random.shuffle(fortune,random.random)
random.shuffle(fortune,random.random)

past= fortune[0]
present= fortune[1]
future= fortune[2]

cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='python')
cursor = cnx.cursor()
selectPast = "select name,general from tarot where id =%s"%past
cursor.execute(selectPast)
a=cursor.fetchall()

for i in a:
    print "Your Past:"
    print "+++++++++++++++++++++++++++++"
    print "Card: "+i[0]
    print "+++++++++++++++++++++++++++++"
    print i[1]
    print "+++++++++++++++++++++++++++++"
    
cnx.commit()
cursor.close()
cnx.close()

cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='python')
cursor = cnx.cursor()
selectPresent = "select name,general from tarot where id =%s"%present
cursor.execute(selectPresent)
a=cursor.fetchall()

for i in a:
    print "Your Present:"
    print "+++++++++++++++++++++++++++++"
    print "Card: "+i[0]
    print "+++++++++++++++++++++++++++++"
    print i[1]
    print "+++++++++++++++++++++++++++++"
    
cnx.commit()
cursor.close()
cnx.close()

cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='python')
cursor = cnx.cursor()
selectFuture = "select name,general from tarot where id =%s"%future
cursor.execute(selectFuture)
a=cursor.fetchall()

for i in a:
    print "Your Future:"
    print "+++++++++++++++++++++++++++++"
    print "Card: "+i[0]
    print "+++++++++++++++++++++++++++++"
    print i[1]
    print "+++++++++++++++++++++++++++++"
    
cnx.commit()
cursor.close()
cnx.close()




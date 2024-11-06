import mysql.connector as mc
db = mc.connect(host='127.0.0.1',user='root',passwd='123456', database='sanjai')
if db.is_connected():
    print('Connection successful!')
curobj = db.cursor()
def view():
    curobj.execute("select * from anime;")
def insert():
    while True:
        a = int(input("Enter anime id: "))
        b = input("Enter anime name: ")
        c = input("Enter date of anime release: ")
        d = input("Enter genre: ")
        curobj.execute(f"insert into anime values({a},'{b}','{c}','{d}')")
        ch = input('Do you want to enter more records?(Y/N): ')
        if ch.lower()=='n':
            break
    db.commit()
    print('Records added...')
    
def create():
    curobj.execute('create table anime(id integer primary key,anime_name varchar(20),date_of_release date,genre varchar(15));')
    db.commit()
    
def searchall():
    curobj.execute('select * from anime')
    data=curobj.fetchall()
    print(data)
    
def searcho():
    curobj.execute('select * from anime')
    data=curobj.fetchall()
    for x in data:
        print(data)
        
def updatename():
    a=input('enter anime name to be changed')
    b=input('enter id what to change')
    tu="UPDATE anime SET anime_name='{x}' WHERE id={y}".format(y=b,x=a)
    curobj.execute(tu)
    db.commit()
    

def updatedate():
    a=input('enter date to be changed')
    b=input('enter id what to change')
    tu="UPDATE anime SET date_of_release='{x}' WHERE id={y}".format(y=b,x=a)
    curobj.execute(tu)
    db.commit()
    
def updategenre():
    a=input('enter genre to be changed')
    b=input('enter id what to change')
    tu="UPDATE anime SET genre='{x}' WHERE id={y}".format(y=b,x=a)
    curobj.execute(tu)
    db.commit()
    
def deleteid():
    deno=int(input("Enter id of whose rec u want to delete"))
    q="delete from anime where id=%s"
    curobj.execute(q,(deno,))
    db.commit()
    
def deletename():
    deno=input("Enter name of whose rec u want to delete")
    q="delete from anime where anime_name='%s'"
    curobj.execute(q,(deno,))
    db.commit()

def deletedate():
    deno=input("Enter date of whose rec u want to delete")
    q="delete from anime where date_of_release='%s'"
    curobj.execute(q,(deno,))
    db.commit()
    
def deletegenre():
    deno=input("Enter genre of whose rec u want to delete")
    q="delete from anime where genre='%s'"
    curobj.execute(q,(deno,))
    db.commit()

def searchid():
    curobj.execute('select * from anime')
    data=curobj.fetchall()
    x=input('enter id you want to see')
    for y in data:
        if y[0]==x:
            print(data)

def searchname():
    curobj.execute('select * from anime')
    data=curobj.fetchall()
    x=input('enter name record you want to see')
    for y in data:
        if y[1].lower()==x.lower():
            print(y)
            
def searchgenre():
    curobj.execute('select * from anime')
    data=curobj.fetchall()
    x=input('enter genre record you want to see')
    for y in data:
        if y[1].lower()==x.lower():
            print(y)
            

while True:
    print('1.DISPLAY')
    print('2.CREATE')
    print('3.DELETE')
    print('4.INSERT')
    print('5.SEARCH')
    print('6.UPDATE')
    print('7.EXIT')
    k=int(input('enter what you want between(1-7) '))
    if k==1:
        searchall()
            
    elif k==2:
        create()

    elif k==3:
        print('1.ID')
        print('2.NAME')
        print('3.DATE')
        print('4.GENRE')
        j=int(input('enter what you want to see'))
        if j==1:
            deleteid()
        if j==2:
            deletename()
        if j==3:
            deletedate()
        if j==4:
            deletegenre()
        else:
            print('GIVE VALUE BETWEEN (1-4)')
    elif k==4:
        insert()

    elif k==5:
        print('1.GENRE')
        print('2.NAME')
        print('3.SEARCH ONE BY ONE')
        print('4.ID')
        j=int(input('enter what you want to see'))
        if j==1:
            searchgenre()
        elif j==2:
            searchname()
        elif j==3:
            searcho()
        elif j==4:
            searchid()
        
        else:
            print('GIVE VALUE BETWEEN (1-4)')
    elif k==6:
        print('1.GENRE')
        print('2.NAME')
        print('3.DATE')
        j=int(input('enter what you want to see'))
        if j==1:
            updategenre()
        elif j==2:
            updatename()
        else:
            updatedate()
    elif k==7:
        break
    else:
        print('GIVE VALUE BETWEEN (1-7)')

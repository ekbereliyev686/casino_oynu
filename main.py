import sqlite3
import random

# Bazada olacaq :

#     login
#     password
#     cash

# Proqram soruşur :

   

#        Secim edin  (1) Qeydiyyatdan kecin (2) Oyuna basla (3) İstifadəçini bazadan silin (4) Balansi yoxla (5) Cixish

# Qeyd:
   
#     Qazandıqda pulun üzərinə 10 azn gəlsin
#     Uduzduqda puldan 5 azn çıxsın
#     Loginin bazada olub olmamağını yoxlayın
#     Balansın mənfiyə getməyinin qarşısını alın
#     Əgər kifayət qədər balans yoxdursa -  (2) oyuna başla düyməsi basıldıqda error qaytarsın

db=sqlite3.connect("data.db")
sql=db.cursor()

sql.execute(""" CREATE TABLE IF NOT EXISTS casino(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login VARCHAR(50),
            password INTEGER,
            cash INTEGER
) """)
while True:
    choise=(input(""" Secim edin  
    (1) Qeydiyyatdan kecin
    (2) Oyuna basla 
    (3) İstifadəçini bazadan silin
    (4) Balansi yoxla
    (5) Cixish
    :  """))
    if choise=="1":
        login=input("Loginizi daxil edin :")
        password=input("Paroluzu daxil edin :")
        cash=int(input("Maxsimum gire bileceyiniz mebleg 5:   Oynamaq isdediyiniz meblegi daxil edin :"))
        if cash<5:
            print("5 azn asagi mebleg daxil ede bilmersiz")
            break
        else:
            sql.execute(f"INSERT INTO casino(login,password,cash) VALUES('{login}','{password}','{cash}')")
            db.commit()
    elif choise=="2":
        game=["alma",'armud']
        prize=(random.choice(game))
        b=sql.execute("SELECT cash FROM casino ")
        cash=int(''.join(map(str,b.fetchone())))
        if cash<=0:
            print("Oynamaq ucun kifayet qeder balansiniz yoxdur")
            balance=int(input("Balansiniz artirmaq isdeyirsiniz ? (1) He  (2) Yox: "))
            if balance==1:
                income=int(input("Meblegi daxil edin: "))
                sql.execute(f"UPDATE casino SET cash=cash+{income} ")
                db.commit()
                budget=cash+income
                print(f"Sizin balansiniz {budget}")
                break
            else:
                break
        if prize=='alma':
            cash+=10
            print(f"Tebrikler siz uddunuz.Balans {cash}")
            
            sql.execute("UPDATE casino SET cash=cash+10 ")
            db.commit()
            break
        elif prize=="armud":
            if cash-5<0:
                break 
            else:
                cash-=5
                print(f"Siz uduzdunuz.Balans {cash}")
                sql.execute("UPDATE casino SET cash=cash-5 ")
                db.commit()
                break
    elif choise=="3":
        delete=input("Silmek isdediyiniz istifadecini girin: ")
        b=sql.execute("SELECT login FROM casino ")
        b=''.join(map(str,b.fetchone()))

        if delete == b:
            sql.execute(f"DELETE FROM casino WHERE login = '{delete}' ")
            db.commit()
            print("Ugurla silindi")
            break
        else:
            print("Bele istifadeci yoxdur")
            break

    elif choise=="4":
        b=sql.execute("SELECT cash FROM casino ")
        a=''
        print(f"Sizin balansiniz {a.join(map(str,b.fetchone()))}")
        break
    elif choise=="5":
        break
    
    else:
        print("Proqram Ugurla islemesi ucun bir reqem daxil edin. ")
        break
import csv
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from datetime import datetime

current_time = datetime.now()
def date():
    c = str(current_time)
    return (c[0:10])


'''Files'''
afile = "admin.csv"
cfile = "client.csv"
tfile="transaction.csv"

'''MENU'''
#login menu
def lmenu():
    print("""                  LOGIN
                ---------
         CHOICE    :    FUNCTION
        --------       ----------
            1      :    ADMIN
            2      :    CLIENT   
            3      :    EXIT PROGRAM""" )
    print("        --------------------------")
    print("\n")
      
#admin menu
def amenu():
        print("""                  MENU
                ---------
         CHOICE    :    FUNCTION
        --------       ----------
            1      :    Display records
            2      :    Search records
            3      :    Insert a record
            4      :    Delete a record
            5      :    Edit a record
            6      :    Logout""")
        print("        --------------------------")
        print("\n")

def aemenu():
    print("""                  MENU
                ---------
         CHOICE    :    FUNCTION
        --------       ----------
            1      :    Edit E-Mail
            2      :    Edit Name
            3      :    Edit Login Password
            4      :    Edit Phone No.
            5      :    Edit State
            6      :    Edit Transaction pin 
            7      :    Edit Balance
            8      :    Edit Account Type
            9      :    Exit """)
    print("        --------------------------")
    print("\n")



#client menu
def acmenu():
   print("\n")
   print("""
 ------------------------------------------          
        ACCOUNT TYPE    :    INTRESET
 ------------------------------------------     
    Recurring deposit   :    5
    Forward deposit     :    7
        Savings         :    6""")
   
   print("------------------------------------------ ")
   print("\n")    

def cmenu():
    print("""                  MENU
                ---------
         CHOICE    :    FUNCTION
        --------       ----------
            1      :    View account details
            2      :    Transaction
            3      :    Edit account details
            4      :    Printable passbook pdf        
            5      :    Logout      """)

    print("        --------------------------")
    print("\n")    

def tmenu():
    print("\n")
    print("""                  MENU
                ---------
         CHOICE    :    FUNCTION
        --------       ----------
            1      :    Deposit
            2      :    Withdraw
            3      :    Exit      """)
    print("        --------------------------")
    print("\n")        

def cemenu():
    print("""                  MENU
                ---------
         CHOICE    :    FUNCTION
        --------       ----------
            1      :    Edit E-Mail
            2      :    Edit Name
            3      :    Edit Login Password
            4      :    Edit Phone No.
            5      :    Edit State
            6      :    Edit Transaction pin 
            7      :    Edit Account Type
            8      :    Exit """)
    print("        --------------------------")
    print("\n")    

'''ADMIN FUNCTIONS'''
#admin main
def amain(afile):
    aid = input("Enter admin id :").strip()
    pas = input("Enter password :")

    x=0

    f = open(afile, "r")
    rec = csv.reader(f)
    list1 = []

    for i in rec:
        if i != []:
            list1.append(i)

    f.close()

    for i in list1:
        if i[0] == aid and i[1] == pas:
            x=1
      
    return x

#sub admin function
def adisplay(file):
    f = open(file, "r")
    rec = csv.reader(f)
    list1 = []

    for i in rec:
        if i != []:
            list1.append(i)

    f.close()

    ind=[] #index

    email=[]
    pas=[]
    name=[]
    no=[]
    state=[]
    pin=[]
    bal=[]
    actype=[]
    irate=[]

    for i in range(len(list1)):
        email.append(list1[i][0])
        pas.append(list1[i][1])
        name.append(list1[i][2])
        no.append(list1[i][3])
        state.append(list1[i][4])
        pin.append(list1[i][5])
        bal.append(list1[i][6])
        actype.append(list1[i][7])
        irate.append(list1[i][8])

    for j in range(1,len(list1)+1):
        ind.append(j)
        
    data = {"E-MAIL":email,"PASSWORD":pas,"NAME":name,"PHONE NO.":no,"STATE":state,"PIN":pin,"BALANCE":bal,"Account Type":actype,"Intreset":irate}
    df=pd.DataFrame(data, index=ind)
    print("------------------------------------------------------------------------------------------------------")
    print(df)
    print("------------------------------------------------------------------------------------------------------\n")

def asearch(file):
    c=0
    f = open(cfile, "r")
    rec = csv.reader(f)
    list1 = []

    for i in rec:
        if i != []:
            list1.append(i)

    f.close()


    email = input("Enter your email :").strip()
    for i in range(len(list1)):
        if list1[i][0]==email:
            rec = list1[i]
            c=1

    if c==1:
        data = {"E-MAIL":[rec[0]],"PASSWORD":[rec[1]],"NAME":[rec[2]],"PHONE NO.":[rec[3]],"STATE":[rec[4]],"PIN":[rec[5]],"BALANCE":[rec[6]],"Account Type":[rec[7]],"Intereset":[rec[8]]}
        df=pd.DataFrame(data,index=[1])
        print("------------------------------------------------------------------------------------------------------")
        print(df)
        print("------------------------------------------------------------------------------------------------------\n")

    elif c==0:
        print("E-mail not found!")

def ainsert(file):
    f = open(file, "a")
    rec = csv.writer(f, delimiter=",")
    while True:
        email=input("Enter E-Mail:").strip()
        pas=input("Enter password:")
        name=input("Enter Name :")
        no=int(input("Enter Phone No. :"))
        state=input("Enter State :")
        pin=int(input("Enter pin :"))
        bal=int(input("Enter balance :"))
        actype=input("Enter actype(fd/rd/savings) :").lower().strip()
        irate=0
        if actype=="fd":
            irate=7

        elif actype=="rd":
            irate=5

        elif actype=="savings":
            irate=8

        rec.writerow([email,pas,name,no,state,pin,bal,actype,irate])

        print("\n")
        ch = input("Do you want to continue (y/n) :").lower()
        print("\n")
        
        if ch =="y":
            continue

        else:
            f.close()
            break
            

def adel(file):
    c=0
    f = open(file, "r")
    rec = csv.reader(f)
    list1 = []

    for i in rec:
        if i != []:
            list1.append(i)

    f.close()


    email = input("Enter your email :").strip()
    for i in range(len(list1)):
        if list1[i][0]==email:
            rec = list1[i]
            c=1

    if c==1:
        print(rec)
        print("-------------------------\n")
        dchoice=input("Do you want to delete the record(Y/N) ?").lower()
        
        if dchoice=='y':
            f1 = open(file,"w")
            rec = csv.writer(f1, delimiter=",")

            for j in range(len(list1)):
                if list1[j][0]!=email:
                    rec.writerow(list1[j])

                    
            f1.close()
            print("Deleted successfully!")
            
    elif c==0:
        print("E-mail not found!")

def aedit(file):
    f = open(file, "r")
    rec = csv.reader(f)
    list1 = []
    for i in rec:
        if i != []:
            list1.append(i)

    f.close()
    irate=0
    c=0
    email=input("Enter old email :").strip()

    for i in range(len(list1)):
        if list1[i][0]==email:
            x=i
            c=1

    if c==1:
        while True:
            print("\n")
            aemenu()

            choice = int(input("Enter your choice :"))
            if choice==1:
                email1=input("Enter new email :").strip()
                list1[x][0]=email1

            elif choice==2:
                name = input("Enter new name :")
                list1[x][1]=name


            elif choice==3:
                pas = input("Enter new passowrd :")
                list1[x][2]=pas

            elif choice==4:
                no= input("Enter new Phone NO. :")
                list1[x][3]=no


            elif choice==5:
                state = input("Enter new State :")
                list1[x][4] = state


            elif choice==6:
                pin=int(input("Enter New pin :"))
                list1[x][5] = pin


            elif choice==7:
                bal=int(input("Enter new Balance :"))
                list1[x][6] = bal

            elif choice==8:
                actype = input("Enter new acoount type :").lower().strip()
                list1[x][7]=actype
                if actype=="fd":
                    irate=7

                elif actype=="rd":
                    irate=5

                elif actype=="savings":
                    irate=8   

                list1[x][8]=irate

            elif choice==9:
                f1 = open(file, "w")
                rec = csv.writer(f1, delimiter=",")
                for i in range(len(list1)):
                    rec.writerow(list1[i])

                f1.close()
                break
            

    elif c==0:
        print("E-mail not found!")

#main admin function
def admin():
    a = amain(afile) #admin verification

    if a==1:
        while True:
            print("\n")
            amenu()
            choice2=int(input("Enter your choice :"))
            if choice2==1:
                adisplay(cfile)

            elif choice2==2:
                asearch(cfile)

            elif choice2==3:
                ainsert(cfile)

            elif choice2==4:
                adel(cfile)

            elif choice2==5:
                aedit(cfile)

            elif choice2==6:
                print("Logged out!")
                break

    elif a==0:
        print("Incorrect password or E-mail")
        print("\n")

'''Client functions'''
#client varification
def cmain(file):
    x=0
    global cid
    cid = input("Enter E-mail id:").strip()
    pas = input("Enter password :")

    f = open(file, "r")
    rec = csv.reader(f)
    list1 = []

    for i in rec:
        if i != []:
            list1.append(i)

    f.close()

    for i in range(len(list1)):
        if str(list1[i][0])==cid and str(list1[i][1])==pas:
            x =  1

    return x



#sub functions
def cview(file):
    f = open(file, "r")
    rec1 = csv.reader(f)
    list1 = []

    for i in rec1:
        if i != []:
            list1.append(i)

    f.close()

    for j in range(len(list1)):
        if list1[j][0]==cid:
            rec = list1[j]
        
    
    data = {"E-MAIL":[rec[0]],"PASSWORD":[rec[1]],"NAME":[rec[2]],"PHONE NO.":[rec[3]],"STATE":[rec[4]],"BALANCE":[rec[6]],"Account Type":[rec[7]],"Interest":[rec[8]]}
    df=pd.DataFrame(data,index=[1])
    print("------------------------------------------------------------------------------------------------------")
    print(df)
    print("------------------------------------------------------------------------------------------------------\n")   

def ctrans(cfile): 
    while True:
        tmenu()
        choice = int(input("Enter your choice :"))

        if choice==1:
            deposit(cfile)

        elif choice==2:
            withdraw(cfile)

        elif choice==3:
            break

def passbook(cid):
    list3=[]
    print("YOUR FILE HAS BEEN GENRATED!!")

    f = open(cfile, "r")
    rec = csv.reader(f)
    list1 = []

    for i in rec:
        if i != []:
            list1.append(i)

    f.close()

    x=0
    for j in range(len(list1)):
        if list1[j][0] == cid:
            x = j 

    f1 = open(tfile, "r")
    rec1 = csv.reader(f1)
    list2 = []

    for k in rec1:
        if k != []:
            list2.append(k)

    f1.close()

    history = []
    for y in range(len(list2)):
        if list2[y][0] == cid:
            history.append(list2[y])

    for f in range(len(history)):
        list3.append((f+1))
            
    acctype = list1[x][7]
    name = list1[x][2]
    address = list1[x][4]
    phone = list1[x][3]
    sno = list3

    date = []
    particular = []
    withdraw = []
    deposit = []
    balance = []

    for f in range (len(history)):
        date.append(history[f][1])
        particular.append(history[f][2])
        withdraw.append(history[f][3])
        deposit.append(history[f][4])
        balance.append(history[f][5])   

    '''PDF'''
    c = canvas.Canvas(f"{name}.pdf",pagesize=letter, bottomup=0)

    #heading
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 48, "SBI")
    c.setFont("Helvetica", 11)
    c.drawString(100, 63, "SANYAM BANK OF INDIA")

    #logo
    c.drawImage("Logo.png", 20, 20, width=80, height=60)

    #last line
    c.line(0, 650, 612, 650)
    c.setFont("Helvetica", 10)
    c.drawString(5, 665, f"Print Date: {datetime.today()}")
    c.setFont("Helvetica", 12)
    c.drawString(10, 685, "SANYAM BANK OF INDIA")
    c.drawString(10, 705, "Paschim Vihar, New Delhi-11063")
    c.drawString(10, 725, "24-Hour Helpline: +91-11-3000-3050")
    c.drawString(10, 745, "E:sanyambank@gmail.com")
    c.drawString(10, 770, "www.sanyambank.com")

    #costumer details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(10, 150, f"Account Type:{acctype}")
    c.drawString(10, 170, f"Name:{name}")
    c.drawString(10, 190, f"Address:{address}")
    c.drawString(10, 210, f"phone : {phone}")
    c.drawString(10, 230, f"Email: {cid} ")

    # heading 2
    c.setFont("Helvetica-Bold", 12)
    c.drawString(200, 108, "TRANSACTION HISTORY")
    c.line(200, 111.6, 344, 111.6)
    # line 2
    c.line(0, 310, 612, 310)
    # line 3
    c.line(0, 340, 612, 340)
    # heading 3
    c.drawString(5, 330, "Sl. No. ")
    c.drawString(105, 330, "Date")
    c.drawString(205, 330, "Particular")
    c.drawString(305, 330, "Withdraw")
    c.drawString(405, 330, "Deposit")
    c.drawString(505, 330, "Balance")


    #sl no.
    b=355
    for i in range(len(sno)):
        c.setFont("Helvetica", 12)
        c.drawString(12,b, f"{sno[i]}")
        b = b+50

    #date
    n=355
    for i in range(len(date)):
        c.setFont("Helvetica", 12)
        c.drawString(80,n, f"{date[i]}")
        n = n+50

    #particular
    m=355
    for i in range(len(particular)):
        c.setFont("Helvetica", 12)
        c.drawString(205,m, f"{particular[i]}")
        m= m+50

    #withdraw
    w = 355
    for i in range(len(withdraw)):
        c.setFont("Helvetica", 12)
        c.drawString(305,w, f"{withdraw[i]}")
        w= w+50

    #deposit
    d = 355
    for i in range(len(deposit)):
        c.setFont("Helvetica",12)
        c.drawString(405,d,f"{deposit[i]}")
        d=d+50

    #balance
    s = 355
    for i in range(len(balance)):
        c.setFont("Helvetica",12)
        c.drawString(505,s,f"{balance[i]}")
        s=s+50
        
    c.showPage()
    c.save()

def deposit(cfile):
    x=0
    print("You can't deposit less than 2000\n")

    f=open(cfile,"r")
    rec = csv.reader(f)
    list1=[]

    for i in rec:
        if i!=[]:
            list1.append(i)

    f.close()

    for i in range(len(list1)):
        if list1[i][0]==cid:
            x = i

    pin = int(input("Enter transaction pin :"))
    
    if int(list1[x][5])==pin:
        print("Old Balance :",list1[x][6])

        amt = int(input("Enter Depositing amount :"))

        if amt>=2000:
            particular = input("Enter Particular :")
            list1[x][6] = int(list1[x][6]) +amt

            print("New Balance :",list1[x][6])

            f1 = open(cfile,"w")
            rec1 = csv.writer(f1,delimiter=",")

            
            for i in range(len(list1)):
                rec1.writerow(list1[i])

            #passbook
            f2  = open(tfile,"a")
            rec2 = csv.writer(f2,delimiter=",")
            currentdate=date()
            rec2.writerow([cid,currentdate,particular,"",amt,list1[x][6]])

        else:
            print("Please add more than 2000")

    else:
        print("Wrong pin")

def withdraw(cfile):
    x=0
    print("Min maintaining balance required to withdraw is 2000\n")

    f=open(cfile,"r")
    rec = csv.reader(f)
    list1=[]

    for i in rec:
        if i!=[]:
            list1.append(i)

    f.close()

    for i in range(len(list1)):
        if list1[i][0]==cid:
            x = i

    pin = int(input("Enter transaction pin :"))

    if pin == int(list1[x][5]):

        print("Old Balance :",list1[x][6])

        if int(list1[x][6])>2000:
            amt = int(input("Enter withdrawing amount :"))
            
            list1[x][6] = int(list1[x][6]) - amt 

            if int(list1[x][6])>2000:
                particular = input("Enter Particular :")
                print("\n")
                print("New Balance :",list1[x][6])
                f1 = open(cfile,"w")
                rec1 = csv.writer(f1,delimiter=",")
                for i in range(len(list1)):
                    rec1.writerow(list1[i])

            #passbook
                f2  = open(tfile,"a")
                rec2 = csv.writer(f2,delimiter=",")
                currentdate=date()
                rec2.writerow([cid,currentdate,particular,amt,"",list1[x][6]])

            else:
                print("Min balance required to withdraw is 2000")

        else:
            print("Min balance required to withdraw is 2000")

    else:
        print("Wrong pin")

def cedit(cfile):
    f = open(cfile, "r")
    rec = csv.reader(f)
    list1 = []
    for i in rec:
        if i != []:
            list1.append(i)

    f.close()
    irate=0
    c=0
    for i in range(len(list1)):
        if list1[i][0]==cid:
            x=i

    while True:
        print("\n")
        cemenu()

        choice = int(input("Enter your choice :"))
        if choice==1:
            email1=input("Enter new email :").strip()
            list1[x][0]=email1

        elif choice==2:
            name = input("Enter new name :")
            list1[x][1]=name

        elif choice==3:
            pas = input("Enter new passowrd :")
            list1[x][2]=pas

        elif choice==4:
            no= input("Enter new Phone NO. :")
            list1[x][3]=no

        elif choice==5:
            state = input("Enter new State :")
            list1[x][4] = state

        elif choice==6:
            pin=int(input("Enter New pin :"))
            list1[x][5] = pin

        elif choice==7:
            print("Changing your account type will effect interest rate!")
            acmenu()

            actype = input("Enter new acoount type(savings/rd/fd) :").lower().strip()
            list1[x][7]=actype
            if actype=="fd":
                irate=7

            elif actype=="rd":
                irate=5

            elif actype=="savings":
                irate=8   

            list1[x][8]=irate

        elif choice==8:
            f1 = open(cfile, "w")
            rec = csv.writer(f1, delimiter=",")
            for i in range(len(list1)):
                rec.writerow(list1[i])

            f1.close()
            break
            
cid=" "
def client():
    a = cmain(cfile) #client verification

    if a==1:
        while True:
            print("\n")
            cmenu()
            choice2=int(input("Enter your choice :"))

            if choice2==1:
                cview(cfile)

            elif choice2==2:
                ctrans(cfile)

            elif choice2==3:
                cedit(cfile)

            elif choice2==4:
                passbook(cid)

            elif choice2==5:
                print("Logged Out!")
                break

    elif a==0:
        print("Incorrect password or E-mail")
        print("\n")



while True:
    lmenu()
    choice1 = int(input("Enter your choice :"))
    #admin
    if choice1==1:
        admin()

    elif choice1==2:
        client()

    elif choice1==3:
        exit()

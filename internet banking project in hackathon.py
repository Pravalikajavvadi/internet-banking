user_name="pravalika"
password="Password789"
sav_acc="saving account"
curr_acc="current account"
pin="2582"
c_name=input("enter youtr name:")
c_pass=str(input("enter  your  password:"))
if c_name==user_name and c_pass==password:
    print("WELCOME TO INTERNET BANKING")
    print('''saving account or current account''')
    acc_type=input("select your account type from above:")
    if acc_type==sav_acc:
        ent_pin=input("enter your pin:")
        if ent_pin==pin:
            print('''
    1.deposits
    2.withdraw
    3.mini statement
    4.exit
    ''')
    elif acc_type==curr_acc:
        ent_pin=input("enter your pin:")
        if ent_pin==pin:
            print('''
    1.deposits
    2.withdraw
    3.mini statement
    4.exit
    ''')
    else:
        print("enter valid pin")
    amount=50000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("enter the amount:"))
        amount+=dep
        print("total amount:",amount)
    elif option==2:
        withd=int(input("enter the amount:"))
        amount-=withd
        print("total amount:",amount)
    elif option==3:
        print("=================ATM=================")
        print("user_name:",user_name)
        print("total amount:",amount)
        print("Thanks for visiting")
        print("==========================================")
    else:
        print("please enter correct login details")
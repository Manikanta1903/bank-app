# Project MAHALAKSHMI BANK
#(To open new bank account)
while True:
    print("Bank OWNER/FOUNDER is N.Manikanta")
    print("welcome to MAHALAKSHMI bank")
    ram="if you want a new account in our bank(MAHALAKSHMI)"
    print(ram)
    bhim=ram
    bhim=int(input('''please select option 1 or  2 or 3 
              1.new account
              2.verify account
              3.exit'''))
    if bhim==1:
        a=input("Enter the your Name")
        b=input("Enter the your Surname")
        c=input("Enter the your Gender")
        if c=="male":
            print("Mr.",b+a)
        elif c=="female":
             print("Ms.",b+a)
        elif c!="male" or "female":
            print(" ",b+a)
        e=input("Enter the Guradian Name")
        d=input(("Relation indication! please if your Father of daughter enter rela Father1 ")) 
        if d=="Father":
            print("F/o",e)
        elif d=="Father1":
            print("D/o",e)
        elif d=="Husband":
            print("W/o",e)
        AC_No=("410050811")
        AC_mo=("846596322")
        f=int(input('''choose account type for your comfort
              1.savings Bank Account
              2.Current Bank Account'''))
        if f==1:
            print("Account number is ",AC_No)
        elif f==2:
            print("Account number is ",AC_mo)
        g=int(input("Enter the cash deposit"))
        if type(g)==int:
            print("Deposited Succefully!",g)
        else:
            print("NOT Deposited")
    elif bhim==2:
        vi=b+a
        print("wlcome sir!",vi)
        if vi==b+a:
            print("avilable balance is",g)
            yp=int(input('''choose the option for your requriment Deposit
                       1.Cash
                       2.Check
                       3.ATM.Card'''))
            if yp==1:
                print("welcome to cash transction")
                money=int(input("Enter the Amount"))
                Balance=g+money
                print("Total current balance is ", Balance)
                print("Transction AMount is",Balance-g)
                print("Transction is succesfully!")
                print("Thank you , visit again")
            elif yp==2:
                print("welcome to Check transction")
                FROM_vj=b+a
                b_bal=g
                print("already you have balance",g)
                b_bal=int(input("Enter the Amount"))
                Balance=g+b_bal
                print("Total current balance is ", Balance)
                print("Transction  Amount is",Balance-g)
                print("Transction is succesfully!")
                print("Thank you , visit again")
            elif yp==3:
                print("welcome to ATM Card transction")
                card="MAHALAKSHMI ATM card"
                l=input("Insert your ATM card")
                if l==card:
                    print("insert your card",card)
                    money=int(input("Enter the Amount"))
                    Balance=g+money
                    print("your current balance is",Balance)
                    print("Transction Amount is",Balance-g)
                    print("Transction is succesfully!")
                    print("Thank you , visit again")
        else:
            print("NO Account for this Name",vi)
    else:
        print("Thank's for your visiting")
        print("for any kind help regarding bank and bank-account please contact my customer care No-8765012345 ")
              







































































        
        
    
            
           
           
    
 



















           
        
        
    
        
    

        


         
    
    

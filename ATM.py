user_id=input("Please enter the username")
pass_word=input("Please enter the Password")
username="santosh"
password="Janu12345$"
s='''
1.Debit
2.credit
3.Mini statement
4.Exit

'''
Amount=1000

if username==user_id and password==pass_word:
    while True:
            print(40*"=")
            print("Please select from the following options")
            print(40 * "-")
            print("For:",s)
            option=int(input())
            if option == 1:
                deb=int(input("Please enter the debit amount"))
                print("Available amount",Amount-deb)
            elif option==2:
                cre=int(input("Please enter the credit amount"))
                print("Available amount",Amount+cre)
            elif option==3:
                print("Available amount",Amount)
            elif option==4:
                break

else:
    print("User name or password incorrect")

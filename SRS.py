import time
import random
from selenium import webdriver

class B(object):
    def __init__(self,password=''):
        self.password=password

    def lower(self):
        lower=any(c.islower() for c in self.password)
        return lower
    def upper(self):
        upper= any(c.isupper() for c in self.password)
        return upper
    def digit(self):
        digit=any(c.isdigit() for c in self.password)
        return digit
    
    def validation(self):
        lower=self.lower()
        upper=self.upper()
        digit=self.digit()
        length=len(self.password)
        cond=lower and upper and digit and length >=6 and length<=10
        if cond==True:
            print("\nUser Created Successfully\n")
        elif not lower:
            print("Include a lowerCase ")
            exit()
        elif not upper:
            print("Include a upperCase")
            exit()
        elif not digit:
            print("Include a digit")
            exit()
        elif not length>=6 and length<=10:
            print("Password length must be 6-10 characters\n ")
            exit()


class C(object):
    def __init__(self):
        pass
    def otp(self):
        uname=input("Enter the Payer's Name: ")
        driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
        driver.get("https://web.whatsapp.com/")
        driver.maximize_window()
        input("Press 'ENter' to Send OTP")
        new=''
        for i in range(6):
            v=random.randint(0,9)
            new=new+str(v)

        
        msg="Your OTP is:"+new
        use=driver.find_element_by_xpath("//span[@title='{}']".format(uname))
        use.click()
        msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
        print("OTP has been sent!\n")
        one=input("Enter the OTP received: ")
        while one!=new:
            one=input("Incorrect OTP!\nEnter a valid OTP ")
        print("___PAYMENT SUCCESSFUL___  Transaction ID:TQG1125216\n")
        print("!!!!YOU HAVE SUCCESSFULLY REGISTERED!!!!\n\n\n")
        print("Your application ID is: 20201109")
        exit()

    
    
    def AForm(self):
        def payment():
            print("REGISTRATION FEES: RS.500/-\n")
            e=input("To CONFIRM and CONTINUE, type 'Y' else type'N'\n")
            if e=='Y':
                n=int(input("Select your payment method\n 1. Card\n 2. UPI\n"))
                if n==1:
                    d1=input("Enter your 16 digit card Number\n")
                    d2=input("Enter your CVV\n")
                    len1=len(d1)
                    len2=len(d2)
                    while len1!=16 and len2!=3:
                        print("Invalid input! Please enter a valid input")
                        d1=input("Enter your 16 digit card Number\n")
                        d2=input("Enter your CVV\n")
                        len1=len(d1)
                        len2=len(d2)
                    self.otp()
                elif n==2:
                    d1=input("Enter  your UPI id: ")
                    self.otp()

                    
                
            elif e=='N':
                print("You didn't pay the registration fees!")
                
        print("***REGISTRATION FORM***\n")
        name=input("Enter Your Full Name\n")
        age=int(input("Enter your Age\n"))
        gender=input("Enter your gender\n")
        print("----EDUCATION DETAILS----\n")
        college=input("Enter your UG college name\n")
        course=input("Enter your Course\n")
        stream=input("Enter your Stream\n")
        cgpa=int(input("Enter your CGPA\n"))
        print("PLEASE WAIT!!!\nYOUR APPLICATION IS BEING VERIFIED\n")
        times=int(10)
        for i in range(times):
            print("Wait for "+str(times - i)+" seconds" )
            time.sleep(1)
        if cgpa>=6:
            print("\n***APPLICATION VERIFIED***\n")
            print("******CONGRATULATIONS!!! YOU ARE ELIGIBLE!!!******\n")
        else:
            print("You are not Eligible!!!\n")
            exit()
        
        print("Choose your Course and Enter it's serial Number\n")
        num=int(input("1. B. Tech\n2. M.tech\n"))
        if num==1:
            val="B.Tech"
            print("Choose your Stream and Enter it's serial Number\n")
            stm=int(input("1. Computer Science and Engineering\n2.Chemical Engineering\n3.Electrical Engineering\n4.Mechanical Engineering\n5.Electronics and Communication Engineering\n"))
            if stm==1:
                val1="Computer Science and Engineering"
            elif stm==2:
                val1="Chemical Engineering"
            elif stm==3:
                val1="Electrical Engineering"
            elif stm==4:
                val1="Mechanical Engineering"
            elif stm==5:
                val1="Electronics and Communication Engineering"          
        elif num==2:
            val="M.Tech"
            print("Choose your Stream and Enter it's serial Number\n")
            stm=int(input("1. Computer Science and Engineering\n2.Chemical Engineering\n3.Electrical Engineering\n4.Mechanical Engineering\n5.Electronics and Communication Engineering\n"))
            if stm==1:
                val1="Computer Science and Engineering"
            elif stm==2:
                val1="Chemical Engineering"
            elif stm==3:
                val1="Electrical Engineering"
            elif stm==4:
                val1="Mechanical Engineering"
            elif stm==5:
                val1="Electronics and Communication Engineering"
        
        print("\n\nPLEASE REVIEW YOUR REGISTRATION FORM\n")
        print("---YOUR DETAILS---")
        print("Name:"+name+"\nAge:",age,"\nGender:"+gender+"\nCollege:"+college+"\nCourse: "+course+"\nStream:"+stream+"\nCGPA:",cgpa)
        print("\n---YOUR COURSE DETAILS---")
        print("Course: "+val+"\nStream: "+val1)
        d=input("To CONFIRM and CONTINUE, type 'Y' else type'N'\n")
        if d=='Y':
            print("\n\n\n\n\n     ******PAYMENT PORTAL******\n")
            payment()
        elif d=='N':
            print("     ***REGISTRATION FAILED***\n")
    



class A(object):
    def __init__(self):
        pass
    print("\n\n*****WELCOME TO SMIT*****\n")
    print("---Registration Portal---\n")
    print("If you are new please create an account or Sign In with your existing account\n")
    acc=input("If you have already created and account, type 'Y' else 'N' \n")
    def Database(data,data1):
        content=open('Database.txt','w')
        content.write(data)
        content.write(" ")
        content.write(data1)
        content.write(" ")
        content.close()
    def Login():
        user=input("Enter your User name\n")
        pwd=input("Enter your password\n")
        content=open('Database.txt','r')
        L=content.readlines()
        for i in L:
            L1=i.split()

        
            while user and pwd not in L1:
                print("User NOT FOUND!\n")
                print("TRY AGAIN!")
                user=input("\nEnter your User name\n")
                pwd=input("Enter your password\n")

            print(user+" LOGGED IN!\n")
            obj1=C()
            check1=obj1.AForm()
                
        
    if acc=='Y':
        Login()
        
    elif acc=='N':
        user=input("Create a user Id\n")
        pwd=input("Create a password\n")
        obj=B(pwd)
        obj.validation()
        Database(user,pwd)
        Login()
        

     

        
        






        
    

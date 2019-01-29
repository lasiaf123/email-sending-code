import smtplib,webbrowser,getpass
def get_mail():
    servicesAvailable=['hotmail','gmail','yahoo','outlook']
    while True :
        mail_id=input("E-mail :")
        if '@' in mail_id and('.com') in mail_id:
            _arate = mail_id.find("@")
            _com = mail_id.find(".com")
            sp = mail_id[_arate+1:_com]
            if sp in servicesAvailable:
                return mail_id,sp
                break
            else:
                print("We don't provide service for " + sp)
                print("We provide service only for : hotmail/outlook,yahoo,gmail  ")
                continue
        else:
            print("Invalid E-mail Type Again")
            continue
def set_smtp_domain(serviceProvider):
    if serviceProvider == 'gmail' :
        return 'smtp.gmail.com'
    elif serviceProvider == 'outlook' or serviceProvider == 'hotmail'  :
        return 'smtp.mail.outlook.com'
    
    elif serviceProvider == 'yahoo' :
        return 'smtp.mail.yahoo.com' 
            

print('Welcome you can send E-mail through this Program')
email=input("enter the email")
password=input("Password :")
while True:
    try:
        smtpDomain = smtplib.SMTP('smtp.gmail.com', 587) 
        smtpDomain.ehlo()
        smtpDomain.starttls()
       
        smtpDomain.login(email,Password)
    except:
        if servicesProvider == 'gmail' :
            print("Login successful, Allow less secure apps")
            print("Do you want Enable less secure apps")
            answer=input("yes or no ? :")
            if answer == "yes" :
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
                print("Your acces has been enabled")
                break
            else :
                print("Login unsuccessful , Please retype your E-mail and Password ")
                e_mail,servicesProvider = get_mail()
                password= getpass.getpass("Password :")
                continue
        else : 
            print("Login unsuccessful , Please type correct E-mail and Password ")
            e_mail,servicesProvider = get_mail()
            password= getpass.getpass("Password :")
            continue
    else :
          print("Login Successful")
          break
print("Please type recievers E-mail")
recieversAddress ,recieversSP =get_mail()
print("Add Subject and Message")
Subject= input("Subject: ")
Message= input("Message: ")
connection.sendmail(mail_id ,recieversAddress ,("Subject: " + str(Subject)) + "\n\n" + str(Message))
print("E-mail send successfully")

connection.quit()

        
        

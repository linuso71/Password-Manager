from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file= open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer=Fernet(key)

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #remove the \n from the line
            user, passw = data.split("|")
            print("user:" ,user ,"| Password: " , fer.decrypt(passw.encode()).decode())

def add():
    name=input("account name: ")
    pwd=input("Password ")

    with open("passwords.txt",'a') as f:
        #with willl open and close the file automatically
        #we name the file as f
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")

while True:
    mode = input("Would You like to a new password or view existing ones (view/add),press Q to quit").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invaid mode.")
        continue

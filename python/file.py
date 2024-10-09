def file_open(fname):
    while True:
        try:
           file=open(fname,"r")
           print("opened")
           return file
        except:
            print("filename not found")
            fname=input("Type filename again :")

file=file_open(input("Enter a file name:"))
x=file.readlines()
for i in x:
    print(i)
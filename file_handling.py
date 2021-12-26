
with open('test.txt','w') as file: #with statement automatically close file
    file.writelines(["Manish","Hari","Ram"])
    file.write("Hello everyone its me")

# file = open('test.txt','r+w')
# file.read(5) #read first five characters
# file.close()
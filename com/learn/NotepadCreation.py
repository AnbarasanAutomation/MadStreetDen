import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# filepath = desktop + "new.txt"
file1 = open("C:\\Users\\DELL\\Desktop\\new.txt", "w")
file2 =os.environ["HOMEPATH"] + "\Desktop\myfile.txt"
secondfile =open(file2,"w")
secondfile.close()
file1.close()




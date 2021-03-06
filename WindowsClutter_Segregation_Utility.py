
# A python utility to segregate the clutter on desktop window to your users directory in folders acc to their extension ( for ex : pdf files will move to PDF_Files folder ) 
# currently 4 extension's are supported in this code i.e docx , pdf , txt , xls
 
import shutil,os,re

print( "-------------Welcome To Clutter Segregation Utility----------------------");
usersDir=input('Enter the name of yours home dir or users dir in C Drive for ex: dipanshuasri =>'); 
dirName='C:\\Users\\'+usersDir+'\\DOC_Files'
dirName1='C:\\Users\\'+usersDir+'\\PDF_Files'
dirName2='C:\\Users\\'+usersDir+'\\TXT_Files'
dirName3='C:\\Users\\'+usersDir+'\\Excel_Files'

try:
    os.makedirs(dirName)    
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")  
       

try:
    os.makedirs(dirName1)    
    print("Directory " , dirName1 ,  " Created ")
except FileExistsError:
    print("Directory " , dirName1 ,  " already exists") 
    
try:
    os.makedirs(dirName2)    
    print("Directory " , dirName2 ,  " Created ")
except FileExistsError:
    print("Directory " , dirName2 ,  " already exists") 
    
try:
    os.makedirs(dirName3)    
    print("Directory " , dirName3 ,  " Created ")
except FileExistsError:
    print("Directory " , dirName3 ,  " already exists") 

         
source = 'C:\\Users\\'+usersDir+'\\Desktop\\'
destination_doc = 'C:\\Users\\'+usersDir+'\\DOC_Files'
destination_pdf = 'C:\\Users\\'+usersDir+'\\PDF_Files'
destination_txt = 'C:\\Users\\'+usersDir+'\\TXT_Files'
destination_xls = 'C:\\Users\\'+usersDir+'\\Excel_Files'

files= os.listdir(source)

print(type(files))
for f in files:
    x = re.search("\.doc*", f)
    if x:
       shutil.move(source+f,destination_doc)
    y = re.search("\.pdf", f)
    if y:
       shutil.move(source+f,destination_pdf)
    z = re.search("\.txt", f)
    if z:
       shutil.move(source+f,destination_txt)
    k = re.search("\.xls*", f)
    if k:
       shutil.move(source+f,destination_xls)
    


print("Doc Files copied under C:\\Users\\"+usersDir+"\\DOC_Files : Check it")
print("Pdf Files copied under C:\\Users\\"+usersDir+"\\PDF_Files : Check it")
print("Text files copied under C:\\Users\\"+usersDir+"\\DOC_Files : Check it")
print("Excel files copied under C:\\Users\\"+usersDir+"\\Excel_Files : Check it")

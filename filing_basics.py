
# r = open files in read mode-by default
# w = open files in write mode
# a = open files and append data in it
# x = if file exits then it will not work , if does`nt exist then it will create the file
# b = used to convert media into binary to write on files
# + = read and write
# t  = open files in txt mode such as notepad--default


f= open("first.txt" , "rt")
       # by dfault r but rb means it will read it in  binary form....
f.seek(10) #start from 10th position
print(f.read())
print(f.tell())
content = f.read()
print(content)
content = f.read(3)
print(content)

# TO PRINT CHARACTER BY CHARACTER
for line in content:
    print(line)

#**********TO PRINT LINE BY LINE we`hv to comment content variable
for line in f:
    print(line , end="")
#**************THE SHORT WAY TO PRINT THIS
print(f.readline())
print(f.readline())
print(f.readline())
#*********TO PRINT ALL LINES IN LIST
print(f.readlines())
f.close()
var =open("first.txt", "a")
jkl = var.write("she studied in UOS..\n")
# var.write function returns no.of chars
print(jkl)
var.close()

# TO OPEN FILE IN RAED AND WRITE MODE
var =open("first.txt", "r+")
print(var.read())
var.write("Thanks\n")

var.close()

# **********WriteLines method********* *
pq = open("first.txt", "a")
lines = ['Harry \n', 'jerry \n', 'peryy \n']
pq.writelines(lines) # for a bigger str use write
pq.close()

# ******** a way to avoid close
with open("first.txt", "a") as abc:
    abc.write("Hey Im inside with")
    abc.truncate(20) #file ka sizw 20 ho




import re
#Global Variables
fhand = "" 
#file handle
err = 0 
#error for catching and validating
lang = "" 
#string of the language name which are html, css, php
langi = -1 
#integer of the language which are 0,1,2
stag = 0
#the starting tags count
etag = 0
#the end tags count
data = {}
#A great dictionary to hold a huge 
# amount of data for the tags and thier content
lineorder = 0
# this will be added in the dictionary values
nested = ""
#This is for the nested tags
status = -1
#This is for knowing the status /mainly made for nested 
#status 10 means opened tag / status 12 means ???
line = ""
#this is the line that any function is reading now 
ldata = []
#listed data variable for the regex
dmap = []
# data map to replace them later
def fileHand():
    #Validating the file
    global err
    while True:
        try: 
            fhandle = open(input("please enter the folder's path or name : " ),"r")
            break
        except:
            print("Error!! 102: please enter a valid file name or path.\n")
            err = 102
            continue
    return fhandle 
#the front-slashes are used to mark the end of the function
#//////////////////////////////////////////////////////////
fhand = fileHand()  
#Globally using fhand as the file handle

def lingo(): 
    #This will be the programming language
    global err 
    global fhand
    global lang
    while True:
        if err == 103:
            err = 1001
            clear()
            break
        if err != 103 and err != 1001:
            line = fhand.readline()
            selector = line.find("///")
            #this is used to find the /// that gives the rule for the language
            if selector != -1:
                lang = line[3:].strip()
                #strip is added for beauty
                break
            else:
                continue
        else:
            lang = input("please enter the language manualy or I will blow up badly : ")
            err = 1001
            #err here changes value so it will not 
            # keep calling the other function infinitely
            break
#the front-slashes are used to mark the end of the function
#//////////////////////////////////////////////////////////

def clear(): 
    #this gives a clear integer representation of the language
    global lang
    global langi
    global err
    if err != 103:
        lingo()
    if lang.lower() == "html":
        langi = 0
        return langi
    elif lang.lower() == "css":
        langi =  1
        return langi
    elif lang.lower() == "php":
        langi =  2
        return langi
    else:
        print(f"Error!! 103 : {lang} is not a valid or available language.")
        print("Avaliable languages are html, css, php")
        err = 103
        lingo()
# I used the return so it breaks out of the function but i have global variable 
# to take care of my outputs.
#the front-slashes are used to mark the end of the function
#//////////////////////////////////////////////////////////
clear()
count = -1 #change this to 0 it used 1 for debug
#calling clear() so the global variables can update
def nest():
    #this is the function in case of nested tags 
    global status
    global nested
    global count
    global etag
    global stag
    global line
    tada = []
    if stag > etag and status != 12:
        # This means that the tag is open now
        status = 10
        nested += " " + line.rstrip()
    elif stag == etag and status != 12:
        #this means that the tags ended now 
        # TAKE IT UP TO THE NESTED ON THE SAME LINE RULE!!!
        status = 12
    elif status ==12:
        count+=1
        # nested on the line rule
        nested += " " + line.rstrip()
        status = -1
        #remeber to add the loop for maping the nested
        nested = nested.replace("[", "<")
        nested = nested.replace(",",">")
        nested = nested[:-1]
        nested += "$"
        tada = re.findall("<\S+",nested)
        clount = -1
        tadac = tada[:]
        for tag in tada:
            clount+=1
            tag = tag.split(">")[0] + ">"
            #becuase regex raised an error by getting 
            # the tag with the following text if they have no space
            if ">" not in tag:
                tag+=">"
            tadac[clount]= tag
        clount = -1
        index = 0
        for brac in nested:
            if index == 0:
                tadac[0]= tadac[0][1:]
                nested = nested.replace("$","</"+tadac[0])
            clount = nested.find("]")
            if brac == "]":
                index+=1
                nested = nested[:clount] +"</"+tadac[index][1:] +nested[clount+1:]
        data[f"line{str(count)}"] = nested 
        nested = ""
#the front-slashes are used to mark the end of the function
#//////////////////////////////////////////////////////////
def escape():
    #this will be the escape sequence in the future update
    pass             
def Rhtml(): 
    #html rules
    global count
    global stag
    global etag
    global data
    global lineorder
    global nested
    global line
    for line in fhand:
        spline = line.split(",")
        # if "/" in line:
        #     escape() 
        # this is for the escape sequence in the futer update
        if "," not in line:
            #this means that it is a self closing tag
            count+=1
            strCount = str(count)
            line = line.replace("[","<")
            line = line.replace("]",">")
            data[f"line{strCount}"] = line.strip()
            continue
        for i in line:
            if i == "[" and status != 12:
                stag +=1
            elif i == "]" and status != 12:
                etag +=1
        if status == 10 and etag == stag:
            nest()
            nest()
        if len(spline) ==2 and status != 12 and stag == etag:
            count+=1
            strCount = str(count)
            tag = spline[0][1:]
            content = spline[1][:-2]
            endTag = tag.split()[0]
            data[f"line{strCount}"] = f"<{tag}>{content}</{endTag}>"
        elif stag != etag:
            nest()
            continue
        #continue so it doesn't update the stag and the etag to 0
        else:
            #this means that thier are nested tags on 
            # that finish on the same line 
            # most interesting part now we need to find 
            # the last "[" so we can start of the middle
            if nested.count("[") != nested.count("]"):
                # make sure that it is in the wanted format
                print(f"Error, your openening tags {stag} doesnt equal your closing tags {etag}")
            else:
                # This should now look like this :
                # [tag,something [tag,something]]
                nest()
                nest()
        stag = 0
        etag = 0
#the front-slashes are used to mark the end of the function
#//////////////////////////////////////////////////////////
Rhtml()
sorted(data)
def multi(value):
    print("multiple values is not yet implemented : ",value)
    x = input("if you want to add main class you can input it here or c to cancel")
    if x.lower() != "c":
        return x
    else:
        quit()

def atr(value):
    #this fuction manages atributes
    if "." in value and ".." not in value:
        #we will replace the . with class=""
        value = value.split(".")
        value[1]=value[1].split()
        if len(value[1]) > 1:
            return multi(value[1])
        value[1] = value[1][0][:-1]
        value[1] = f"{value[0]}class='{value[1]}'>"
        return value[1]
    elif "'" in value:
        #we will replace atr'value with style="atr:value;"
        value = value.split()
        value[1] = value[1].split("'")
        if len(value[1]) > 2:
            return multi(value[1])
        value[1][1] = value[1][1][:-1]
        value[1] = f"{value[0]} style='{value[1][0]}:{value[1][1]};'>"
        return value[1]
    elif ".." in value:
        value = value.split("..")
        value[1]=value[1].split()
        if len(value[1]) > 1:
            return multi(value[1])
        value[1] = value[1][0][:-1]
        value[1] = f"{value[0]} id='{value[1]}'>"
        return value[1]
    elif "=" in value :
        value = value[:-1].strip()
        value = value.split("=")
        if len(value) > 2:
            multi(value)
        value[0] = value[0].strip()
        value[1] = value[1].strip()
        value = f"{value[0]}='{value[1]}'>"
        return value
#the front-slashes are used to mark the end of the function
#//////////////////////////////////////////////////////////


def FRhtml():
    global data
    global ldata
    global dmap
    counte = -1
    counter = -1    
    for key in data:
        ldata.append(re.findall("(<.+?>)",data[key]))
        #getting all of the tags with regex
    for i in ldata:
        counte+=1
        for o in i:
            counter+=1
            if "/" in o:
                ldata[counte].pop(counter)
        counter = -1
    counte = -1
    for i in ldata:
        #this is to make sure that thier is no end tags 
        #becuase thier is a flaw in the previous loop
        counte+=1
        i.reverse()
        for o in i:
            counter+=1
            if "/" in o:
                ldata[counte].pop(counter)
        counter = -1
    counte = -1
    for i in ldata:
        counte+=1
        for o in i:
            o.strip()
            counter+=1
            if len(o.split())>1:
                dmap.append((counte,counter,ldata[counte][counter]))
        counter = -1
    for i, o, p in dmap:
        ldata[i][o] = atr(p)
    for i in dmap:
        rep = ldata[i[0]][i[1]]
        data["line"+str(i[0])] = data["line"+str(i[0])].replace(i[2],rep)
    name = input("what is the name of the file you want without extention : ")
    title = input("please write the title of you page: ")
    fhandler = open(name+".html","w")
    fhandler.write(f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<title>{title}</title>\n</head>\n<body>")
    for key in data:
        fhandler.write(data[key]+"\n")
    fhandler.write("\n</body>\n</html>")
    fhandler.close()

#the front-slashes are used to mark the end of the function
#//////////////////////////////////////////////////////////
    # print(ldata, "\n\n", data , "\n\n", dmap)
FRhtml()
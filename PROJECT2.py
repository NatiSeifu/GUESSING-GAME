#Nati Seifu
#10/14/2022
#A helpful program that performs various functions on a piece of text


#importing essentials

import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import sys

print("Welcome!") # Let's begin!

# Reading file input by user and checking if it exists or not

while True:
    userinput = input('Insert Text File Name please (ex: textfile or myfile):')
    to_try = userinput + ".txt"
    
    try:
        with open(to_try, "r+") as f:
            readme = f.read()
            readme = readme.lower()
            break
    except:
        print("This file does not exist in the same directory as the saved python file. Put in a file name that exists in the directory")
        
print ("MAINMENU\nWhat would you like done to your text? (Press 'Z' to exit out of a given menu item)")



#defining various functions that will be called

#caesar shift function
def caesar(text, shift):
    newtext =''
    abcs = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in text:
        i = i.lower()
        if i in abcs: 
                csr =(ord(i) + int(shift))
                if csr <= 122:
                    newtext += chr(csr)
                if csr > 122:
                    newtext += chr(csr - 26) #takes care of z and y for the first 26 shifts
        else:
            csr = i
            newtext+= csr
    return newtext

#defining the counting function
def countword(text):
    print( "This appears", readme.count(text), "times\n\n")
    
#Starter 'email' code from https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f

def sendEmail(sender, sendee, header, body, password):
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login(sender, password)
    msg = MIMEMultipart()
    msg['From']= sender
    msg['To']= sendee
    msg['Subject']= header
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()

def print_chunk(x, text):
    if x>=100:
        print('"...'+text[x-100:x+100]+'..."')
    elif 0<x<100:
        print('"...'+text[0:x+100]+'..."')
def print_chunk2(x, text): #creating a return version of print_chunk in order to use it for the email section
    if x>=100:
        return ('"...'+text[x-100:x+100]+'..."')
    elif 0<x<100:
        return ('"...'+text[0:x+100]+'..."')
def chunk(text):
    n = 0
    while True:
            #print('n', n)
            x = readme.find(text, n)
            print_chunk(x, readme)
            #print('x', x)
            stop = input('\nPress ENTER to pull up another instance\n')
            if stop == 'Z' or x<0 :
                break
            n = x + 1
def replace(to_replace, replace_with):
        replace_with = replace_with.upper()
        readmeAltered = readme.replace(to_replace, replace_with)
        y = readmeAltered.find(replace_with)
        print_chunk(y, readmeAltered)
        saveornot = input ("\nWould you like a version of this text with the words replaced? 'Y' or 'N'\n")
        saveornot = saveornot.upper()
        if saveornot == 'Y':
            with open (replace_with + '_'+ "ReplacedVersion_" + to_try, "w+") as f:
                f.write(readmeAltered)
            print ("Okay! Your new file is saved as:" + "\u0332".join(replace_with + '_'+ "ReplacedVersion_" + to_try) +'\n')
            
#Looping the mainmenu
while True:
    print ("1. Count Occurence", "2. Context", "3. Search n' Replace", "4. Encode", "5. Try for a Surprise ;)", "6. Email me something!", "7. Quit", sep ="\n")  
    selection = input()

    if selection == '1': #Using the count function
        
        to_search = input ('What word/phrase would you like to search for?\n')
        to_search = to_search.lower()
        countword(to_search)


    if selection =='2': #Displaying a word in context
        
        print('What word/phrase would you like to see in context?\n')
        to_context = input()
        chunk(to_context)    



    if selection =='3': #Search, Replace and then Print a chunk of the new version of the text. Offer to save a file.
        
        to_replace = input('What word/phrase would you like to replace?\n')
        replace_with = input('What word/phrase would you like to replace it with?\n')
        to_replace =  to_replace.lower()
        replace(to_replace, replace_with)
        replace_with =  replace_with.lower()

    if selection == '4': #Encrypting text using letter shift
        
        print('Select encoding level. Pick a number ranging from 1-25:\n')
        while True:
            try:
                shift = int(input())
                if shift > 25:
                    raise ValueError #raising some form of error when the number selected is above 25 to keep the caesar function functional.
                break
            except:
                print ("Not a number or number out of range. Please try again.") 
        encoded_text = (caesar(readme, shift))
        with open(str(shift) + "codedversion.txt", "w+") as f: #saving encoded file
            f.write(encoded_text)
        print ("Here you go! Your new file is saved as:" + "\u0332".join(str(shift) + "codedversion.txt") +'\n', "\nYou can go communicate this text file in secret now ;)\n")



    if selection == '5': #replace all the words in the text with their Pig Latin versions and do the augh
        
        surprise = "Are you ready for the surprise I have for you? It is going to be a fun and educational experience for you hehe.......        :)\n"
        
        for i in surprise:
            print (i, end = '')
            time.sleep(0.06) 
        url_1 = "https://www.youtube.com/shorts/rpTHGtjWyOM"
        lesgo = ("Let's go!!!!!")
        time.sleep(3.0)
        for i in lesgo:
            print(i,end='')
            time.sleep(0.03)
        time.sleep(0.9)
        import webbrowser
        webbrowser.open(url_1)



    if selection == '6': #Sending the email
        
        sendee = input('What is your email address: ')
        sender = "pythonatemu@outlook.com"
        password = "1qazse4r"
        header = "Here is the promised text :)"
        opshun = input("Would you like a random section of the text sent to you or would you rather receive a piece of text that specifics a certain word? Press '1' for random or '2' to pick a word.")
        if opshun == '1':
    
            from random import randint
            z = randint(100, int(len(readme)*3/4))
            body = print_chunk2(z, readme)
            

        if opshun == '2':

            wrd = input("\nWhat word do you want sent to you in context?")
            x = readme.find(wrd)
            if x>=100:
                t = "..."+readme[x-100:x+100]+"..."
            elif 0<x<100:
                t = "..."+readme[0:x+100]+"..."
            body = t             
        sendEmail(sender, sendee, header, body, password)    



    if selection == '7': #Salud
        
        gbye = "Okay, I hope I was able to help you out today! Goodbye! <3"
        for i in gbye:
            print (i, end = '')
            time.sleep(0.04)
        break
        sys.exit()

        
        

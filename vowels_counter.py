#Using Collections module for counting and frequencies 
from collections import *
import collections

# Making list to be used in comparison witn input user 
vowels = ["a" , "e" , "i" , "o" , "u"]
result = []             # ----> for using later in frequency 

while True :
    user_input = input ("Enter the word : ")
    user_input_Lower = user_input.lower()



    
    for i in user_input_Lower :
        if i in vowels: 
            result.append(i)
            continue
      
    frequencies = collections.Counter(result) 

    if len (result) > 0 :
        print (f"No of Vowel letters in --> {user_input_Lower} --> {len(frequencies)} as following --> {frequencies}")  

    else: 
        print ( f"Your word --> {user_input_Lower} --> doesn't have Vowel Letters !")
    
    user_decision= input (" Would you like to do another operation ? ( y/n )")

    if user_decision == "y":
        continue
    else:
        break



    
   
        






# if you'd like to print only repeated letters 
# repeated = {}
# for key, value in frequencies.items():
#     if value > 1: 
#         repeated[key] = value

           

# alien= {} 
# alien["color"]="green"
# alien["points"] = 5 
# print(alien)


        

# word = input("Enter a word")

# Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# for i in range(0,26):
#     print(word.count(Alphabet[i]))

    


######################################################################################################      Imports

import arabic_reshaper      # to glue Farsi letters together
from bidi.algorithm import get_display      # to support R to L writing

######################################################################################################      farsi_shaper() Func

def farsi_shaper (string):      # implement to make a correct output for user
    reshaped_text = arabic_reshaper.reshape(string)
    new_string = get_display(reshaped_text)
    return new_string

######################################################################################################
letters_count = int(input("how many words do you have  =>  " ))
letters_need = int(input("len of letter you need  =>  "))
letters = []

print('Enter your letters  \n')
for i in range(letters_count):
    letters.append(input("here =====> "))

######################################################################################################   program main body  

with open("src\main_wordlist.csv", 'r',encoding='UTF-8-sig') as f:
    while True:        
        line = f.readline()
        if line == '':
            break
        word = line.split(':')
        if len(word[0]) == letters_need:
                    p = False
                    for i in word[0]:
                        if i in letters :
                            p = True
                        else:
                            p = False
                            break
                    if p == True :
                        word[0] = farsi_shaper(word[0])
                        print(word[0])     
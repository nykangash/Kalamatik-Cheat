######################################################################################################      Imports

import arabic_reshaper      # to glue Farsi letters together
from bidi.algorithm import get_display      # to support R to L writing

######################################################################################################      farsi_shaper() Func

def farsi_shaper (string):      # implement to make a correct output for user
    reshaped_text = arabic_reshaper.reshape(string)
    new_string = get_display(reshaped_text)
    return new_string

######################################################################################################  two_words_maker() Fucn

def two_words_maker(letters):       # making words with len(2)
    
    for i in letters:
        for j in letters:
            tmp = ''
            tmp += i
            tmp += j
            situ_words.append(tmp)
    
    return situ_words        

######################################################################################################

def three_words_maker(letters):
    for i in letters:
        for j in letters:
            for k in letters:
                tmp = ''
                tmp += i
                tmp += j
                tmp += k
                situ_words.append(tmp)
    
    return situ_words        


######################################################################################################  program intro for user to give desired input      

def four_words_maker(letters):
    for i in letters:
        for j in letters:
            for k in letters:
                for l in letters:
                    tmp = ''
                    tmp += i
                    tmp += j
                    tmp += k
                    tmp += l
                    situ_words.append(tmp)
    
    return situ_words        


######################################################################################################

def five_words_maker(letters):
    for i in letters:
        for j in letters:
            for k in letters:
                for l in letters:
                    for q in letters:
                        tmp = ''
                        tmp += i
                        tmp += j
                        tmp += k
                        tmp += l
                        tmp += q
                        situ_words.append(tmp)
    
    return situ_words        


######################################################################################################

letters_count = int(input("how many words do you have  =>  " ))
letter_len_needed = int(input("len of letter you need  =>  "))
situ_words = []
letters = []
print('Enter your letters  \n')
for i in range(letters_count):
    letters.append(input("here =====> "))

######################################################################################################   program main body  

with open("src\persian_dict_19k.csv", 'r',encoding='UTF-8-sig') as f:
    while True:        
        line = f.readline()
        if line == '':
            break
        word = line.split(':')
        match letter_len_needed:
            case 2:
                if len(word[0]) == letter_len_needed:
                    main_shit = list(set(two_words_maker(letters)))
                    for i in main_shit:
                        if word[0] == i :
                            i = farsi_shaper(i)
                            print(i)
                            break
            case 3:
                if len(word[0]) == letter_len_needed:
                    main_shit = list(set(three_words_maker(letters)))
                    for i in main_shit:
                        # print(word[0],'====================================================>  ', i)        
                        if word[0] == i :
                            p = farsi_shaper(i)
                            print(p)
                            main_shit.remove(i)
                            break
            case 4:
                if len(word[0]) == letter_len_needed:
                    main_shit = list(set(four_words_maker(letters)))
                    for i in main_shit:
                        # print(word[0],'====================================================>  ', i)        
                        if word[0] == i :
                            p = farsi_shaper(i)
                            print(p)
                            main_shit.remove(i)
                            break
            case 5:
                if len(word[0]) == letter_len_needed:
                    main_shit = list(set(five_words_maker(letters)))
                    for i in main_shit: 
                        print(word[0],'====================================================>  ', i)       
                        if word[0] == i :
                            i = farsi_shaper(i)
                            print(i)

                            break
            case _:
                print('Bad len, try again !!!')
                break


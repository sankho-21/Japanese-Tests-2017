# Japanese Short Tests
# By: Sankhojyoti Halder

import random

# Setting up the Dictionary
dict_hiragana = [["あ", "a"], ["い", "i"], ["う", "u"], ["え", "e"], ["お", "o"],
                 ["か", "ka"], ["き", "ki"], ["く", "ku"], ["け", "ke"], ["こ", "ko"],
                 ["さ", "sa"], ["し", "shi"], ["す", "tsu"], ["せ", "se"], ["そ", "so"],
                 ["た", "ta"], ["ち", "chi"], ["つ", "tsu"], ["て", "te"], ["と", "to"],
                 ["な", "na"], ["に", "ni"], ["ぬ", "nu"], ["ね", "ne"], ["の", "no"],
                 ["は", "ha;wa"], ["ひ", "hi"], ["ふ", "fu"], ["へ", "he"], ["ほ", "ho"],
                 ["ま", "ma"], ["み", "mi"], ["む", "mu"], ["め", "me"], ["も", "mo"],
                 ["や", "ya"], ["ゆ", "yu"], ["よ", "yo"],
                 ["ら", "ra"], ["り", "ri"], ["る", "ru"], ["れ", "re"], ["ろ", "ro"],
                 ["わ", "wa"], ["ゐ", "wi"], ["ゑ", "we"], ["を", "wo"],
                 ["が", "ga"], ["ぎ", "gi"], ["ぐ", "gu"], ["げ", "ge"], ["ご", "go"],
                 ["ざ", "za"], ["じ", "ji"], ["ず", "zu"], ["ぜ", "ze"], ["ぞ", "zo"],
                 ["だ", "da"], ["ぢ", "ji"], ["づ", "zu"], ["で", "de"], ["ど", "zo"],
                 ["ば", "ba"], ["び", "bi"], ["ぶ", "bu"], ["べ", "be"], ["ぼ", "bo"],
                 ["ぱ", "pa"], ["ぴ", "pi"], ["ぷ", "pu"], ["ぺ", "pe"], ["ぽ", "po"],
                 ["ん", "n"]]

dict_katakana = [["ア", "a"], ["イ", "i"], ["ウ", "u"], ["エ", "e"], ["オ", "o"],
                 ["カ", "ka"], ["キ", "ki"], ["ク", "ku"], ["ケ", "ke"], ["コ", "ko"],
                 ["サ", "sa"], ["シ", "shi"], ["ス", "tsu"], ["セ", "se"], ["ソ", "so"],
                 ["タ", "ta"], ["チ", "chi"], ["ツ", "tsu"], ["テ", "te"], ["ト", "to"],
                 ["ナ", "na"], ["ニ", "ni"], ["ヌ", "nu"], ["ネ", "ne"], ["ノ", "no"],
                 ["ハ", "ha;wa"], ["ヒ", "hi"], ["フ", "fu"], ["ヘ", "he"], ["ホ", "ho"],
                 ["マ", "ma"], ["ミ", "mi"], ["ム", "mu"], ["メ", "me"], ["モ", "mo"],
                 ["ヤ", "ya"], ["ユ", "yu"], ["ヨ", "yo"],
                 ["ラ", "ra"], ["リ", "ri"], ["ル", "ru"], ["レ", "re"], ["ロ", "ro"],
                 ["ワ", "wa"], ["ヰ", "wi"], ["ヱ", "we"], ["ヲ", "wo"],
                 ["ガ", "ga"], ["ギ", "gi"], ["グ", "gu"], ["ゲ", "ge"], ["ゴ", "go"],
                 ["ザ", "za"], ["ジ", "ji"], ["ズ", "zu"], ["ゼ", "ze"], ["ゾ", "zo"],
                 ["ダ", "da"], ["ヂ", "ji"], ["ヅ", "zu"], ["デ", "de"], ["ド", "do"],
                 ["バ", "ba"], ["ビ", "bi"], ["ブ", "bu"], ["ベ", "be"], ["ボ", "bo"],
                 ["パ", "pa"], ["ピ", "pi"], ["プ", "pu"], ["ペ", "pe"], ["ポ", "po"],
                 ["ン", "n"]]

dict_words = [["hai", "yes"], ["iie", "no"], ["konnichiwa", "hello"], ["sayonara", "goodbye"], ["oyasumi", "good night"],
              ["wakarimashita", "understood"], ["baka", "idiot"], ["arigatou", "thank you"], ["ohayo", "good morning"],
              ["khombawa", "good afternoon"], ["chotto", "wait"], ["matane", "see you later"], ["pati", "party"]]

# DONE


def hiragana_pronounce(limit):
    i = 0
    while i <= (limit - 1):
        ch = random.randint(0, (len(dict_words) - 1))
        print("What's the pronounciation of ", dict_words[ch][0], " ? ")
        ans = (input("Give answer here(lower case please): "))
        if ans == dict_words[ch][1]:
            print("Correct!!...let's try another one. \n \n ")
        else:
            print("That's wrong!.. the correct pronounciation is ", dict_words[ch][1])
        i += 1

# DONE


def katakana_pronounce(limit):
    i = 0
    while i <= (limit - 1):
        ch = random.randint(0, (len(dict_katakana) - 1))
        print("What's the pronounciation of ", dict_katakana[ch][0], " ? ")
        ans = (input("Give answer here(lower case please): "))
        if ans == dict_katakana[ch][1]:
            print("Correct!!...let's try another one. \n \n ")
        else:
            print("That's wrong!.. the correct pronounciation is ", dict_katakana[ch][1])
        i += 1

# DONE


def words_pronounce(limit):
    i = 0
    while i <= (limit - 1):
        ch = random.randint(0, (len(dict_hiragana) - 1))
        print("What's the meaning of ", dict_hiragana[ch][0], " ? ")
        ans = (input("Give answer here(lower case please): "))
        if ans == dict_hiragana[ch][1]:
            print("Correct!!...let's try another one. \n \n ")
        else:
            print("That's wrong!.. the correct meaning is ", dict_hiragana[ch][1])
        i += 1

# DONE


def hiragana_mcq(limit):
    i = 0
    while i <= (limit - 1):
        ch1 = random.randint(0, (len(dict_hiragana) - 1))
        while True:
            # Choosing other 3 options
            ch2 = random.randint(0, len(dict_hiragana))
            ch3 = random.randint(0, len(dict_hiragana))
            ch4 = random.randint(0, len(dict_hiragana))
            # Making sure no 2 options are same
            if ch1 != ch2 and ch1 != ch3 and ch1 != ch4 and ch2 != ch3 and ch2 != ch4 and ch3 != ch4:
                break
        opt = random.randint(1, 4)
        print("What is the pronounciation of ", dict_hiragana[ch1][0], " ? ")
        # To have the right answer at a,b,c or d randomly
        if opt == 1:
            print("(a) ", dict_hiragana[ch1][1], "(b) ", dict_hiragana[ch2][1], "(c) ", dict_hiragana[ch3][1], "(d) ", dict_hiragana[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "a":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct pronounciation is ", dict_words[ch1][1])
            i += 1
        if opt == 2:
            print("(a) ", dict_hiragana[ch2][1], "(b) ", dict_hiragana[ch1][1], "(c) ", dict_hiragana[ch3][1], "(d) ", dict_hiragana[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "b":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct pronounciation is ", dict_words[ch1][1])
            i += 1
        if opt == 3:
            print("(a) ", dict_hiragana[ch3][1], "(b) ", dict_hiragana[ch2][1], "(c) ", dict_hiragana[ch1][1], "(d) ", dict_hiragana[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "c":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct pronounciation is ", dict_words[ch1][1])
            i += 1
        if opt == 4:
            print("(a) ", dict_hiragana[ch4][1], "(b) ", dict_hiragana[ch2][1], "(c) ", dict_hiragana[ch3][1], "(d) ", dict_hiragana[ch1][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "d":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct pronounciation is ", dict_words[ch1][1])
            i += 1

# DONE


def katakana_mcq(limit):
    i = 0
    while i <= (limit - 1):
        ch1 = random.randint(0, (len(dict_katakana) - 1))
        while True:
            # Choosing other 3 options
            ch2 = random.randint(0, len(dict_katakana))
            ch3 = random.randint(0, len(dict_katakana))
            ch4 = random.randint(0, len(dict_katakana))
            # Making sure no 2 options are same
            if ch1 != ch2 and ch1 != ch3 and ch1 != ch4 and ch2 != ch3 and ch2 != ch4 and ch3 != ch4:
                break
        opt = random.randint(1, 4)
        print("What is the pronounciation of ", dict_katakana[ch1][0], " ? ")
        # To have the right answer at a,b,c or d randomly
        if opt == 1:
            print("(a) ", dict_katakana[ch1][1], "(b) ", dict_katakana[ch2][1], "(c) ", dict_katakana[ch3][1], "(d) ", dict_katakana[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "a":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct pronounciation is ", dict_katakana[ch1][1])
            i += 1
        if opt == 2:
            print("(a) ", dict_katakana[ch2][1], "(b) ", dict_katakana[ch1][1], "(c) ", dict_katakana[ch3][1], "(d) ", dict_katakana[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "b":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct pronounciation is ", dict_katakana[ch1][1])
            i += 1
        if opt == 3:
            print("(a) ", dict_katakana[ch3][1], "(b) ", dict_katakana[ch2][1], "(c) ", dict_katakana[ch1][1], "(d) ", dict_katakana[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "c":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct pronounciation is ", dict_katakana[ch1][1])
            i += 1
        if opt == 4:
            print("(a) ", dict_katakana[ch4][1], "(b) ", dict_katakana[ch2][1], "(c) ", dict_katakana[ch3][1], "(d) ", dict_katakana[ch1][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "d":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct pronounciation is ", dict_katakana[ch1][1])
            i += 1

# DONE


def words_mcq(limit):
    i = 0
    while i <= (limit - 1):
        ch1 = random.randint(0, (len(dict_words) - 1))
        while True:
            # Choosing other 3 options
            ch2 = random.randint(0, len(dict_words))
            ch3 = random.randint(0, len(dict_words))
            ch4 = random.randint(0, len(dict_words))
            # Making sure no 2 options are same
            if ch1 != ch2 and ch1 != ch3 and ch1 != ch4 and ch2 != ch3 and ch2 != ch4 and ch3 != ch4:
                break
        opt = random.randint(1, 4)
        print("What is the meaning of ", dict_words[ch1][0], " ? ")
        # To have the right answer at a,b,c or d randomly
        if opt == 1:
            print("(a) ", dict_words[ch1][1], "(b) ", dict_words[ch2][1], "(c) ", dict_words[ch3][1], "(d) ", dict_words[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "a":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct meaning is ", dict_words[ch1][1])
            i += 1
        if opt == 2:
            print("(a) ", dict_words[ch2][1], "(b) ", dict_words[ch1][1], "(c) ", dict_words[ch3][1], "(d) ", dict_words[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "b":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct meaning is ", dict_words[ch1][1])
            i += 1
        if opt == 3:
            print("(a) ", dict_words[ch3][1], "(b) ", dict_words[ch2][1], "(c) ", dict_words[ch1][1], "(d) ", dict_words[ch4][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "c":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct meaning is ", dict_words[ch1][1])
            i += 1
        if opt == 4:
            print("(a) ", dict_words[ch4][1], "(b) ", dict_words[ch2][1], "(c) ", dict_words[ch3][1], "(d) ", dict_words[ch1][1])
            ans = input("Choose an option(just the letter in lower case..no brackets needed): ")
            if ans == "d":
                print("Correct!!...")
                if i != (limit - 1):
                    print("let's try another one. \n \n ")
            else:
                print("That's wrong!.. the correct meaning is ", dict_words[ch1][1])
            i += 1


# DONE
def learn_words(limit):
    i = 0
    while i <= limit:
        ch = random.randint(0, (len(dict_words) - 1))
        print("New Word: ", dict_words[ch][0], " Meaning: ", dict_words[ch][1])
        i += 1


# DONE
def learn_hiragana(limit):
    i = 0
    while i <= limit:
        ch = random.randint(0, (len(dict_hiragana) - 1))
        print("New Character: ", dict_hiragana[ch][0], " pronounciation: ", dict_hiragana[ch][1])
        i += 1


# DONE
def learn_katakana(limit):
    i = 0
    while i <= limit:
        ch = random.randint(0, (len(dict_katakana) - 1))
        print("New Character: ", dict_katakana[ch][0], " pronounciation: ", dict_katakana[ch][1])
        i += 1


print("WELCOME TO JAPANESE LEARING \n ****** \n What would you like to do today?")
spam = 0
while spam == 0:
    user = input("(a)Katakana   (b)Hiragana  (c)Learn New Words).... \n type a, b or c and hit Enter")
    if user == "c":
        choicec = input("What you wanna attemp? test or mcq or learn(type in whichever is preffered)")
        if choicec == "test":
            limitc1 = input("How many meanings do you wanna test?")
            words_pronounce(limitc1)
        if choicec == "mcq":
            limitc2 = input("How many mcq do you want?")
            words_mcq(limitc2)
        if choicec == "learn":
            limitc3 = input("How many words do you wanna learn?")
            learn_words(limitc3)
    elif user == "b":
        choiceb = input("What you wanna attemp? test or mcq or learn(type in whichever is preffered)")
        if choiceb == "test":
            limitb1 = input("How many meanings do you wanna test?")
            hiragana_pronounce(limitb1)
        if choiceb == "mcq":
            limitb2 = input("How many mcq do you want?")
            hiragana_mcq(limitb2)
        if choiceb == "learn":
            limitb3 = input("How many Characters do you wanna learn?")
            learn_hiragana(limitb3)
    elif user == "a":
        choicea = input("What you wanna attemp? test or mcq(type in whichever is preffered)")
        if choicea == "test":
            limita1 = input("How many meanings do you wanna test?")
            words_pronounce(limita1)
        if choicea == "mcq":
            limita2 = input("How many mcq do you want?")
            words_mcq(limita2)
        if choiceb == "learn":
            limitb3 = input("How many Characters do you wanna learn?")
            learn_words(limitb3)
    print("Do you wanna quit? or wanna try more?")
    choice = input("Type in 'quit' or 'more': ")
    if choice == "quit":
        spam = 1
    else:
        spam = 0

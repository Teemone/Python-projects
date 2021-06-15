import random

class Password:

    alpha="a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alphabets = alpha.split(" ")
    numbers = ["0","1","2", "3", "4", "5", "6", "7", "8", "9"]
    symbols_list = ["&","~","%","$","^","@","!","*","#"]
    symbols_dict = {"ampersand":"&", "tilde":"~","percentage":"%", "dollar-sign":"$", "caret":"^", "at-sign":"@","exclamation":"!", "asterisk":"*", "hash":"#"}

    # Returns an alpha-numeric password to the user
    def alpha_numeric(self, letters_len, numbers_len):
        random.shuffle(self.alphabets)
        random.shuffle(self.numbers)
        choice_alph=random.choice(self.alphabets)
        choice_num = random.choice(self.numbers)
        alpha_list=[]
        num_list=[]
        for i in range(letters_len):
            alpha_list.append(random.choice(self.alphabets))
        
        for j in range (numbers_len):
            num_list.append(random.choice(self.numbers))

        toUpper = random.choice(alpha_list) + random.choice(self.symbols_list)# Concatinating and Storing a random letter from alpha_list and a random symbol form symbols_list

        password = []
        password.append(toUpper.upper())
        password.append(alpha_list)
        password.append(num_list)
        random.shuffle(password)
       

        return self.shuffle_password(password)


    # Removes any duplicate character in the list and returns a list without any duplicate characters
    def get_non_duplicate(self, list):
        dummy_list=[]
        for items in list:
            if items not in dummy_list:
                dummy_list.append(items)
        if len(dummy_list) < len(list):
            rand = random.choice(self.alphabets)
            while rand not in dummy_list:
                dummy_list.append(rand)
                if rand in dummy_list:
                    break       
        return dummy_list


    # Shuffles the password
    def shuffle_password(self, password):
        password_final=""
        password_final_final=""
        for char in password:
            for k in char:
                password_final+=k+" "
        split_psswd = password_final.split(" ")
        random.shuffle(split_psswd)
        for i in split_psswd:
            for j in i:
                password_final_final+=j
        
        return password_final_final.strip()


    # Returns a random symbol
    def returnSymbol(self, value):
        signs=''
        keys=self.symbols.keys()
        for key in keys:
            signs += self.symbols.get(key)+" "

        a = signs.split(" ")


p = Password()
print(p.alpha_numeric(2,5))


def first_uniq_char(string):
    letters = ""
    for character in string:
        if character not in letters:
            letters += character.lower()
    #print(string)
    #print(letters)
    
    for i in letters:
        count = 0
        for j in string:
            if j ==i:
                count = count + 1
        if count ==1:
            chr = i
            break
     
    if count != 1:
        print("No unique character")
        return 100
    else:
        pos= string.index(chr)
        return pos
        

if __name__ == '__main__':
    string = input("Enter the string: ")
    print(string)
    position = first_uniq_char(string)
    if position == 100:
        print("Try again")
    else:
        print("The position of the first unique character is :", position)
    
def sum_alphabet(words):
    str_dict = {"a":1,
                "b":2,
                "c":3,
                "d":4,
                "e":5,
                "f":6,
                "g":7,
                "h":8,
                "i":9,
                "j":10,
                "k":11,
                "l":12,
                "m":13,
                "n":14,
                "o":15,
                "p":16,
                "q":17,
                "r":18,
                "s":19,
                "t":20,
                "u":21,
                "v":22,
                "w":23,
                "x":24,
                "y":25,
                "z":26 }

    array_totals = []
    for word in words:
        word_total = 0
        for letter in word:
            str_var = letter
            str_value = str_dict.get(str_var)
            if str_value is not None:
                word_total = word_total + str_value
                print("total for word", letter, "is", word_total)
        
        array_totals.append(word_total)

    return array_totals


if __name__ == "__main__":
    words = ["sport" , "good" , "bad"]
    array_final = sum_alphabet(words)
    print(array_final)
    
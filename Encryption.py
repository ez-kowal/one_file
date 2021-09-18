from string import ascii_letters
from typing import Optional

def bubble_sort(list: list):
    """
    This funstion takes in a list and sorts it using the bubble alhorithm.
    This usally takes 0(n^2) time

    =============================
    Learn more about Bubble sort on wikipedia: https://en.wikipedia.org/wiki/Bubble_sort
    """
    try:
        for i in range(len(list)-1):
            for j in range(0, len(list) - 1 - i):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
            print(list)
        return list
    except Exception:
        print(Exception)



def encrypt_with_caesar(input_string:str,key: Optional[int] = 3) -> str:
    """
    This function "Encrypts" a string using Ceaser's Cypher
    This function takes in 1 requied and 2 optional parameters.
    
    Requied:
    
    input_string: String
    *this is the string thats going to be "Encrypted".

    Optional:
    
    key: Integer
    *this is a Optional parameters that lets you specify how many characters the string will be moved.

    =============================
    learn more about Caeser's cipher on wikipedia: https://en.m.wikipedia.org/wiki/Caesar_cipher
    """
    result = ""

    alpha = ascii_letters
    for char in input_string:
        if char not in alpha:
            result += char
        else:
            new_key = (alpha.index(char) + key) % len(alpha)
            result += alpha[new_key]

    return result

def decrypt_a_caesar(input_string: str, key: Optional[int] = 3) -> str:
    """
    This Function Decrypts Caesers Cipher.
    it uses 2 parameters one requied and on optional

    Requied:
    
    input_string: String
    *this is the "encrypted" string.

    Optional:
    
    key: Integer
    *this is a Optional parameters that lets you specify how many characters the string was moved. 3 by deafult

    =============================
    learn more about Caeser's cipher on wikipedia: https://en.m.wikipedia.org/wiki/Caesar_cipher
    """
    key *= -1

    return encrypt_with_caesar(input_string, key)

ran_list = [624,324,65452,3,634,7,4,353,34,43,563,456,3,43,456,534,563,213,4,562]
ran_string = "A quick brown fox jumps over the lazy dog."

if __name__ == "__main__":
    print(ran_string)
    temp = encrypt_with_caesar(ran_string,5)
    print(temp)
    print(decrypt_a_caesar(temp,5))
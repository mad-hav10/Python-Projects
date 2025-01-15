#Ceaser Cypher
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

repeat_of_game = True
print("Welcome to Ceaser Cypher\n")

def EncodeOrDecode(text, shift) :
    shifted_text = ""
    if encode_or_decode == "decrypt" :
        shift *= -1

    for letter in text :
        if letter not in alphabets :
            shifted_text += letter

        else :
            shifted_index = alphabets.index(letter) + shift
            shifted_index %= len(alphabets)
            shifted_text += alphabets[shifted_index]

    print(shifted_text)

while repeat_of_game :
    encode_or_decode = input("Do you want to Encrypt the text or Decrypt the Text\n").lower()

    if encode_or_decode == "encrypt" :
        text = input("Enter the text you wnat to encrypt\n")
        shift = int(input("Enter the ammount of shift you want\n"))

    else :
        text = input("Enter the text you want to decrypt\n")
        shift = int(input("Enter the ammount of shift you want\n"))

    EncodeOrDecode(text, shift)

    continue_or_not = input("Press 1 to continue or 0 to end\n")
    if continue_or_not == "0" :
        repeat_of_game = False
        print("Thanks\n")
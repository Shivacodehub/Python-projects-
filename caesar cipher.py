alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encryption(enc, shift):
    afterenc = ""
    for char in enc:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            indexval = alpha.index(char)
            new_char = alpha[(indexval + shift) % 26]
            afterenc += new_char.upper() if is_upper else new_char
        else:
            afterenc += char  # keep spaces/punctuation as is
    print("Encrypted message:", afterenc)

def decryption(dec, shift):
    afterdec = ""
    for char in dec:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            indexval = alpha.index(char)
            num = (indexval - shift + 26) % 26
            afterdec += alpha[num].upper() if is_upper else alpha[num]
        else:
            afterdec += char
    print("Decrypted message:", afterdec)

while True:
    inpt = input("Type 'encrypt' for encryption or 'decrypt' for decryption: ").strip().lower()
    if inpt in ["encrypt", "decrypt"]:
        message = input("Enter the message: ")
        shif = int(input("Enter the shift number: "))
        if inpt == "encrypt":
            encryption(enc=message, shift=shif)
        else:
            decryption(dec=message, shift=shif)
    else:
        print("Invalid input. Try again.")

    again = input("Do you want to try again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Good bye 👋🏻")
        break
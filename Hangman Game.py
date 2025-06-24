import random
import time

fruits = ["apple", "banana", "orange", "pineapple", "jackfruit", "mango", "papaya", "watermelon", "guva", "muskmelon"]
vegetables = ["brinjal", "pumpkin", "coriander", "drumstick", "ridgeguard", "lemon"]
body_parts = ["head", "neck", "foot", "arms", "stomach", "tigh"]
brands = ["oracle", "Toyota", "instagram", "verizon", "hyundai", "disney"]
jewellery = ["necklace", "bangles", "anklets", "earrings"]
words = [fruits, vegetables, body_parts, brands, jewellery]

while True:
    word1 = random.choice(words)
    word2 = random.choice(word1)
    word3 = list(word2)
    word4 = word3.copy()  # Used for tracking which letters have been revealed
    lenth = len(word3)
    blank = list('_' * lenth)
    miss = 0
    taken = False

    print("\n🔠 New Game Started!")
    print(" ".join(blank))

    start_time = time.time()

    while True:
        answ = input("Enter the alphabet: ").lower()

        if answ in word4:
            found = False
            for i in range(lenth):
                if word3[i] == answ and word4[i] == answ:
                    blank[i] = answ
                    word4[i] = " "  # Mark this letter as used
                    found = True
                    break  # Reveal only ONE letter per correct guess

            print("✅", " ".join(blank))

            if ''.join(blank) == word2:
                end_time = time.time()
                total_time = end_time - start_time
                print("🎉 You win! The word was:", word2)
                print(f"⏱️ Time taken: {int(total_time)} seconds")
                break
        else:
            miss += 1
            print("❌ Wrong guess!")

            if miss == 1:
                print("___________|\n"
                      "    |      |\n"
                      "    |      |\n"
                      "    O      |\n"
                      "           |\n"
                      "           |\n"
                      "=============")
            elif miss == 2:
                print("___________|\n"
                      "    |      |\n"
                      "    |      |\n"
                      "    O      |\n"
                      "    |      |\n"
                      "           |\n"
                      "=============")
            elif miss == 3:
                print("___________|\n"
                      "    |      |\n"
                      "    |      |\n"
                      "    O      |\n"
                      "   /|      |\n"
                      "           |\n"
                      "=============")
            elif miss == 4:
                print("___________|\n"
                      "    |      |\n"
                      "    |      |\n"
                      "    O      |\n"
                      "   /|\     |\n"
                      "           |\n"
                      "=============")
            elif miss == 5:
                print("___________|\n"
                      "    |      |\n"
                      "    |      |\n"
                      "    O      |\n"
                      "   /|\     |\n"
                      "   /       |\n"
                      "=============")
            elif miss == 6:
                print("___________|\n"
                      "    |      |\n"
                      "    |      |\n"
                      "    O      |\n"
                      "   /|\     |\n"
                      "   / \     |\n"
                      "=============")
                end_time = time.time()
                total_time = end_time - start_time
                print("😞 You lose! The word was:", word2)
                print(f"⏱️ Time taken: {int(total_time)} seconds")
                break

            if not taken:
                hint = int(input("Do you want to take a Hint? If yes enter 1 else enter 0: "))
                if hint == 1:
                    if word2 in fruits:
                        print("🧠 Hint: The word is related to **fruits**")
                    elif word2 in vegetables:
                        print("🧠 Hint: The word is related to **vegetables**")
                    elif word2 in body_parts:
                        print("🧠 Hint: The word is related to **body parts**")
                    elif word2 in brands:
                        print("🧠 Hint: The word is related to **brands**")
                    elif word2 in jewellery:
                        print("🧠 Hint: The word is related to **jewellery**")
                    taken = True

    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("👋 Thanks for playing! Goodbye.")
        break
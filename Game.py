import random

words = ["apple", "tiger", "house", "plane", "chair"]

secret_word = random.choice(words)
guessed_letters = []  
incorrect_guesses = 0
max_incorrect = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(secret_word))  

while incorrect_guesses < max_incorrect:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabetic letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess. You have {max_incorrect - incorrect_guesses} tries left.")

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word correctly:", secret_word)
        break
else:
    print("💀 Game over! The word was:", secret_word)

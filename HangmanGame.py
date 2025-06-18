import random

# List of predefined words
word_list = ["apple", "grape", "mango", "peach", "berry"]
word = random.choice(word_list)  # Randomly choose a word from the list
word_letters = list(word)

guessed_letters = []
attempts = 6
display_word = ["_" for _ in word_letters]

print("🎮 Welcome to the Hangman Game!")
print("Guess the word, one letter at a time.")
print("You have", attempts, "lives.")

# Game loop
while attempts > 0 and "_" in display_word:
    print("\nWord: " + " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter a single valid letter!")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        print("✅ Correct guess!")
        for i in range(len(word_letters)):
            if word_letters[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong guess! Remaining lives:", attempts)

# Game result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The correct word was:", word)

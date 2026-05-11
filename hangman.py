import random

# Predefined list of 5 words with hints
WORDS = [
    {"word": "python",  "hint": "A popular programming language"},
    {"word": "guitar",  "hint": "A stringed musical instrument"},
    {"word": "planet",  "hint": "Orbits around a star"},
    {"word": "bridge",  "hint": "Connects two sides across a gap"},
    {"word": "jungle",  "hint": "A dense tropical forest"},
]

MAX_WRONG = 6

# Hangman stages (0 wrong = empty gallows, 6 wrong = full figure)
HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
    """,
]


def display_state(secret, guessed, wrong_letters, wrong_count):
    print(HANGMAN_STAGES[wrong_count])
    # Display the word with guessed letters revealed
    display_word = " ".join(
        ch.upper() if ch in guessed else "_" for ch in secret
    )
    print(f"  Word: {display_word}\n")
    if wrong_letters:
        print(f"  Wrong guesses ({wrong_count}/{MAX_WRONG}): {', '.join(sorted(wrong_letters)).upper()}")
    else:
        print(f"  Wrong guesses: none yet")
    print()


def play_game():
    # Pick a random word
    pick = random.choice(WORDS)
    secret = pick["word"]
    hint   = pick["hint"]

    guessed       = set()   # all guessed letters
    wrong_letters = set()   # only the incorrect ones
    wrong_count   = 0

    print("\n" + "=" * 40)
    print("        W E L C O M E  T O  H A N G M A N")
    print("=" * 40)
    print(f"  Hint: {hint}")
    print(f"  The word has {len(secret)} letters.\n")

    # Main game loop
    while wrong_count < MAX_WRONG:
        display_state(secret, guessed, wrong_letters, wrong_count)

        # Check win condition
        if all(ch in guessed for ch in secret):
            print(f"  *** You won! The word was: {secret.upper()} ***\n")
            break

        # Get a valid single letter from the player
        while True:
            guess = input("  Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("  Please enter a single letter (a-z).")
            elif guess in guessed:
                print(f"  You already guessed '{guess.upper()}'. Try another.")
            else:
                break

        guessed.add(guess)

        if guess in secret:
            print(f"  Good guess! '{guess.upper()}' is in the word.")
        else:
            wrong_count += 1
            wrong_letters.add(guess)
            remaining = MAX_WRONG - wrong_count
            print(f"  Wrong! '{guess.upper()}' is not in the word. "
                  f"{remaining} guess{'es' if remaining != 1 else ''} left.")
        print()

    else:
        # Loop exhausted — player lost
        display_state(secret, guessed, wrong_letters, wrong_count)
        print(f"  *** Game over! The word was: {secret.upper()} ***\n")


def main():
    while True:
        play_game()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing Hangman! Goodbye.\n")
            break


if __name__ == "__main__":
    main()
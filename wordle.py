"""Structured Wordle!"""

# declares named constraint variables for the emoji boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(guess: str, letter: str) -> bool:
    """Given a guess string, and a desired letter, contains_char searches through guess and returns True if letter is in guess, and False if it is not."""
    # asserts that the length of the letter is 1, or else it throws an error
    assert len(letter) == 1
    idx: int = 0
    exists: bool = False
    # loops through the guess string, checking to see if letter is found in guess
    while idx < len(guess):
        if (guess[idx] == letter):
            exists = True
        idx = idx + 1
    # if letter is found in string, returns True, else, returns False
    return exists


def emojified(guess: str, secret: str) -> str:
    """Given a guess string and a secret string, will output the emoji codified string based off of the comparision of the two strings (white box if there is never an instance of the guess letter at index in secret, yellow box if there is an instance of the guess letter in the secret string, and a green box if the letter of guess and secret match at the same index)."""
    # asserts that the length of guess matches the length of secret, else, throws an error
    assert len(guess) == len(secret)
    emoji: str = ""
    idx = 0
    # loops through guess
    while idx < len(guess):
        # checks to see if current index of guess is ever found in secret
        exists: bool = contains_char(secret, guess[idx])
        # if current letter of guess is found in secret...
        if exists is True:
            # if current index of guess is the same as the current index of secret (letters are in the same place), adds a green box to emoji
            if (guess[idx] == secret[idx]):
                emoji = emoji + GREEN_BOX
            # because we know that current index of guess is found in secret somewhere, can add a yellow box to emoji
            else:
                emoji = emoji + YELLOW_BOX
        # current letter of guess is never found in secret, so will add a white box to emoji
        else:
            emoji = emoji + WHITE_BOX
        idx = idx + 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Asks user for a guess word based off of a desired length."""
    # asks the user for a guess and stores it in guess variable
    guess = input(f"Enter a {expected_length} character word: ")
    # continues asking user for a guess until the length of their guess matches expected_length
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    secret_len: int = len(secret)
    turn: int = 1
    won_game: bool = False
    # loops through 6 turns, or until user has won the game
    while turn < 7 and won_game is False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(secret_len)
        # prints emoji string of the comparison between guess and secret
        print(emojified(guess, secret))
        # if user guess is secret word, sets won_game = True so that the game stops on the next round
        if (guess == secret):
            won_game = True
        # else, if user did not provide the secret word, keeps the game going
        else:
            turn += 1
    # after there have been 6 turns or the user won the game...
    # if the user wins the game, prints statement
    if (won_game is True):
        print(f"You won in {turn}/6 turns!")
    # else, because the user did not win the game, prints statement
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
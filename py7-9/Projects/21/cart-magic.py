import random
import math

# დასაშვები ბარათების რაოდენობები (კენტი და სამის ჯერადი)
SIZES = [9, 15, 21, 27, 33, 39, 45, 51]


def print_columns(cards):
    """ბეჭდავს 3 სვეტად."""
    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    print("\n  I ᲮᲐᲖᲘ:", col1)
    print("\n II ᲮᲐᲖᲘ:", col2)
    print("\nIII ᲮᲐᲖᲘ:", col3)
    print("\n")
    return col1, col2, col3


def get_column():
    """იღებს სვეტის ნომერს (1–3)."""
    while True:
        c = input("WHICH COLUMN IS YOUR NUMBER IN? (1/2/3): ").strip()
        if c in ("1", "2", "3"):
            return int(c)
        print("PLEASE TYPE 1, 2 OR 3.")


def rebuild(cards, chosen):
    """
    აწყობს ახალ სიას ისე, რომ არჩეული სვეტი ALWAYS მოხვდეს შუაში.
    წესის დაცვით: LEFT – CHOSEN – RIGHT
    """
    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    columns = [col1, col2, col3]

    chosen_col = columns[chosen - 1]
    other_cols = [c for i, c in enumerate(columns) if i != chosen - 1]

    # ALWAYS: other – chosen – other
    return other_cols[0] + chosen_col + other_cols[1]


def rounds_needed(n):
    """საჭირო რაუნდები: ceil(log3(n))."""
    return math.ceil(math.log(n, 3))


def main():
    print("\n--- MULTI-SIZE CARD TRICK WITH TWO-DIGIT NUMBERS ---")

    # 1) რენდომული ზომა
    N = random.choice(SIZES)
    m = N // 3
    print(f"\nCARDS SELECTED: {N} (3 columns × {m} rows)")

    # 2) ვქმნით რენდომულ ორნიშნა ბარათებს
    cards = random.sample(range(10, 100), N)
    print("\nTHESE ARE YOUR CARDS (10–99).")
    print("CHOOSE ONE NUMBER AND REMEMBER IT.\n")

    # 3) ვანგარიშობთ საჭირო რაუნდებს
    k = rounds_needed(N)
    print(f"WE WILL DO {k} ROUNDS.\n")

    # 4) ვამუშავებთ ფოკუსის 3-სვეტიან ალგორითმს
    for i in range(1, k + 1):
        print(f"--- ROUND {i} ---")
        print_columns(cards)
        chosen = get_column()
        cards = rebuild(cards, chosen)

    # 5) საბოლოო პოზიცია — ცენტრალური (fixed point)
    final_position = (N + 1) // 2
    guessed = cards[final_position - 1]

    print("\nI KNOW YOUR NUMBER NOW!")
    print("YOUR NUMBER IS:", guessed)


if __name__ == "__main__":
    main()

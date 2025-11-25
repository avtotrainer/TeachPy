import random
import math

SIZES = [9, 15, 21, 27, 33, 39, 45, 51]


def make_card(num):
    """ერთსტრიქონიანი ASCII კარტი."""
    return f"[{num:02d}]"


def print_horizontal_rows(cards):
    """ბეჭდავს ბარათებს სტრიქონებად 3-კოლონად (ჰორიზონტალურად)."""

    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    rows = max(len(col1), len(col2), len(col3))

    print("\nCOLUMN 1      COLUMN 2      COLUMN 3")
    print("-----------   -----------   -----------")

    for i in range(rows):
        c1 = make_card(col1[i]) if i < len(col1) else "      "
        c2 = make_card(col2[i]) if i < len(col2) else "      "
        c3 = make_card(col3[i]) if i < len(col3) else "      "
        print(f"{c1:<12}{c2:<12}{c3:<12}")


def get_column():
    while True:
        c = input("\nWHICH COLUMN IS YOUR NUMBER IN? (1/2/3): ").strip()
        if c in ("1", "2", "3"):
            return int(c)
        print("PLEASE TYPE 1, 2 OR 3.")


def rebuild(cards, chosen):
    """არჩეული სვეტი ALWAYS შუაში გადადის."""
    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    columns = [col1, col2, col3]

    chosen_col = columns[chosen - 1]
    other_cols = [c for i, c in enumerate(columns) if i != chosen - 1]

    # left – chosen – right
    return other_cols[0] + chosen_col + other_cols[1]


def rounds_needed(n):
    return math.ceil(math.log(n, 3))


def main():
    print("\n--- 100% HORIZONTAL CARD TRICK ---")

    N = random.choice(SIZES)
    m = N // 3
    print(f"\nCARDS SELECTED: {N}  (3 columns × {m} rows)")

    cards = random.sample(range(10, 100), N)
    print("\nCHOOSE ANY NUMBER AND REMEMBER IT.\n")

    k = rounds_needed(N)
    print(f"WE WILL DO {k} ROUNDS.\n")

    for i in range(1, k + 1):
        print(f"\n--- ROUND {i} ---")
        print_horizontal_rows(cards)
        chosen = get_column()
        cards = rebuild(cards, chosen)

    center = (N + 1) // 2
    guessed = cards[center - 1]

    print("\nI KNOW YOUR NUMBER!")
    print("YOUR NUMBER IS:", guessed)
    print()


if __name__ == "__main__":
    main()

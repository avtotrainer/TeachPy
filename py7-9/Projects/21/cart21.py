"""
21-კარტიანი ფოკუსის თამაში.
ბავშვი ირჩევს ჩაფიქრებულ რიცხვს 1-21 სიისგან.
კომპიუტერი 3-ჯერ კითხულობს: რომელ სვეტშია?
და მესამე 반복ის შემდეგ გამოიცნობს.
"""


def print_columns(cards):
    """ბეჭდავს 3 სვეტად – 7-7-7."""
    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    print("\nCOLUMN 1:", col1)
    print("COLUMN 2:", col2)
    print("COLUMN 3:", col3)

    return col1, col2, col3


def get_column():
    """იღებს რომელი სვეტია (1,2,3)"""
    while True:
        c = input("WHICH COLUMN IS YOUR NUMBER IN? (1/2/3): ").strip()
        if c in ["1", "2", "3"]:
            return int(c)
        print("PLEASE TYPE ONLY 1, 2 OR 3.")


def rebuild(cards, chosen):
    """
    ალაგებს ბარათებს ისე, რომ არჩეული სვეტი ALWAYS იყოს შუაში.
    თანმიმდევრობა: LEFT – CHOSEN – RIGHT
    """
    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    columns = [col1, col2, col3]

    # არჩეული სვეტი ALWAYS შუაში უნდა დადგეს
    chosen_col = columns[chosen - 1]
    other_cols = [c for i, c in enumerate(columns) if i != chosen - 1]

    # ააწყე ახალი სია: სხვა, არჩეული, სხვა
    new_order = other_cols[0] + chosen_col + other_cols[1]

    return new_order


def main():
    print("THINK OF A NUMBER FROM 1 TO 21.\n")
    cards = list(range(1, 21 + 1))

    for i in range(1, 4):
        print(f"\n--- ROUND {i} ---")
        print("REMEMBER YOUR NUMBER AND LOOK AT THE COLUMNS BELOW:")
        col1, col2, col3 = print_columns(cards)

        chosen = get_column()
        cards = rebuild(cards, chosen)

    print("\nI KNOW YOUR NUMBER...")
    print("YOUR NUMBER IS:", cards[10])  # index 10 == 11th position


if __name__ == "__main__":
    main()

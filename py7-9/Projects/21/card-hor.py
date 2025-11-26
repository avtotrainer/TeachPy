import random
import math
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import box
from rich.align import Align

console = Console()

SIZES = [33]

# SIZES = [9, 15, 21, 27, 33]


def make_card(num):
    """მინიმალური სიმაღლის ჰორიზონტალური კარტი."""
    return Panel(
        f"[bold white]{num}[/bold white]",
        width=7,
        height=3,
        box=box.ROUNDED,
        border_style="cyan",
    )


def print_horizontal_rows(cards):
    """
    ბეჭდავს ბარათებს ჰორიზონტალური ხაზებით:
    1) col1 მთელი სტრიქონი
    2) col2 მთელი სტრიქონი
    3) col3 მთელი სტრიქონი
    """

    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    # ფუნქცია: ტექსტის ბარათი, იმავე ზომით, როგორც რიცხვის ბარათი
    def make_label(text):
        return Panel(
            f"[bold yellow]{text}[/bold yellow]",
            width=7,
            height=3,
            border_style="yellow",
            box=box.ROUNDED,
        )

    # პირველი სტრიქონი – col1
    row1 = [make_label("  I →")] + [make_card(x) for x in col1]
    # row1 = [make_card(x) for x in col1]
    console.print(Columns(row1, expand=False, equal=True))
    console.print()

    # მეორე სტრიქონი – col2
    row2 = [make_label(" II →")] + [make_card(x) for x in col2]
    console.print(Columns(row2, expand=False, equal=True))
    console.print()

    # მესამე სტრიქონი – col3
    row3 = [make_label("III →")] + [make_card(x) for x in col3]
    console.print(Columns(row3, expand=False, equal=True))
    console.print()


def get_column():
    while True:
        c = console.input(
            "[yellow]ᲠᲝᲛᲔᲚ ᲡᲕᲔᲢᲨᲘᲐ ᲨᲔᲜᲘ ᲠᲘᲪᲮᲕᲘ? (1/2/3): [/yellow]"
        ).strip()
        if c in ("1", "2", "3"):
            return int(c)
        console.print("[red]მხოლოდ 1, 2 ან 3.[/red]")


def rebuild(cards, chosen):
    """არჩეული სვეტი ALWAYS გადადის შუაში."""
    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    cols = [col1, col2, col3]
    chosen_col = cols[chosen - 1]
    others = [c for i, c in enumerate(cols) if i != chosen - 1]

    return others[0] + chosen_col + others[1]


def rounds_needed(n):
    return math.ceil(math.log(n, 3))


def main():
    N = random.choice(SIZES)
    m = N // 3
    console.print(f"[bold]სულ გვაქვს {N} რიცხვი[/bold]")

    cards = random.sample(range(10, 100), N)

    console.print("\n[green]ამოირჩიე ერთი და დაიმახსოვრე.[/green]\n")

    k = rounds_needed(N)
    console.print(f"[bold cyan]ჩვენ ჩავატარებთ {k} რაუნდს.[/bold cyan]\n")

    for i in range(1, k + 1):
        console.print(f"[bold magenta]--- რაუნდი {i} ---[/bold magenta]")
        print_horizontal_rows(cards)
        chosen = get_column()
        cards = rebuild(cards, chosen)

    # შუა ელემენტი იქნება გამოცნობილი რიცხვი
    center = (N + 1) // 2
    guessed = cards[center - 1]

    console.print(Align.center("\n[bold green]მე ვიცი შენი რიცხვი![/bold green]"))
    final_card = make_card(guessed)
    console.print(Align.center(final_card))


if __name__ == "__main__":
    main()

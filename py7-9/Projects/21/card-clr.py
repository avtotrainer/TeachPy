import random
import math
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import box
from rich.align import Align

console = Console()

SIZES = [9, 15, 21, 27, 33]


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
    ბეჭდავს ბარათებს სტრიქონებად:
    თითო სტრიქონი = სამი კარტი (სვეტ1, სვეტ2, სვეტ3)
    """
    col1 = cards[0::3]
    col2 = cards[1::3]
    col3 = cards[2::3]

    rows = max(len(col1), len(col2), len(col3))

    console.print("\n[bold magenta]   I      II      III  [/bold magenta]\n")

    for i in range(rows):
        row_cards = []
        row_cards.append(
            make_card(col1[i]) if i < len(col1) else Panel("", width=7, height=3)
        )
        row_cards.append(
            make_card(col2[i]) if i < len(col2) else Panel("", width=7, height=3)
        )
        row_cards.append(
            make_card(col3[i]) if i < len(col3) else Panel("", width=7, height=3)
        )

        # Columns დაბეჭდავს 3 პანელს ჰორიზონტალურად ერთ სტრიქონად
        console.print(Columns(row_cards, expand=False, equal=True))


def get_column():
    while True:
        c = console.input(
            "[yellow]ᲠᲝᲛᲔᲚ  ᲡᲕᲔᲢᲨᲘᲐ ᲨᲔᲜᲡ ᲛᲘᲔᲠ ᲐᲠᲩᲔᲣᲚᲘ ᲠᲘᲪᲮᲕᲘ? (1/2/3): [/yellow]"
        ).strip()
        if c in ("1", "2", "3"):
            return int(c)
        console.print("[red]ᲛᲮᲝᲚᲝᲓ 1, 2 ᲐᲜ 3.[/red]")


def rebuild(cards, chosen):
    """არჩეული სვეტი ALWAYS შუაში გადადის."""
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
    console.print(f"[bold]ᲡᲣᲚ  ᲒᲕᲐᲥᲕᲡ {N} ᲠᲘᲪᲮᲕᲘ[/bold]")

    cards = random.sample(range(10, 100), N)

    console.print("\n[green]ᲐᲛᲝᲘᲠᲩᲘᲔ ᲔᲠᲗᲘ ᲓᲐ ᲓᲐᲘᲛᲐᲮᲡᲝᲕᲠᲔ.[/green]\n")

    k = rounds_needed(N)
    console.print(f"[bold cyan]ᲩᲕᲔᲜ ᲩᲐᲕᲐᲢᲐᲠᲔᲑᲗ  {k} ᲠᲐᲣᲜᲓᲡ.[/bold cyan]\n")

    for i in range(1, k + 1):
        console.print(f"[bold magenta]--- ᲠᲐᲣᲜᲓᲘ {i} ---[/bold magenta]")
        print_horizontal_rows(cards)
        chosen = get_column()
        cards = rebuild(cards, chosen)

    center = (N + 1) // 2
    guessed = cards[center - 1]

    console.print(Align.center("\n[bold green]ᲛᲔ ᲕᲘᲪᲘ ᲨᲔᲜᲘ ᲠᲘᲪᲮᲕᲘ![/bold green]"))
    # console.print(f"[white]ᲨᲔᲜᲘ ᲠᲘᲪᲮᲕᲘᲐ:[/white] [bold cyan]{guessed}[/bold cyan]\n")
    final_card = make_card(guessed)
    # console.print(Panel(final_card, title="ᲨᲔᲜᲘ ᲠᲘᲪᲮᲕᲘᲐ", border_style="green"))
    console.print(Align.center(final_card))


if __name__ == "__main__":
    main()

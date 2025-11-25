from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align
from rich.text import Text
from rich import box
import random

console = Console()

# ================================
# STEP 1 — 20 უნიკაური რიცხვი → 10 წყვილი
# ================================
# numbers-ში მივიღებთ 20 უნიკალურ ელემენტიან რიცხვების სიას დიაპაზონიდან 10–99.
numbers = random.sample(range(10, 100), 20)
# მიღებთ 10 წყვილს
pairs = [(numbers[i], numbers[i + 1]) for i in range(0, 20, 2)]


def make_pair_card(a, b):
    return Panel(
        f"[bold]{a}   {b}[/bold]",
        width=11,
        height=3,
        border_style="yellow",
        box=box.ROUNDED,
    )


def show_pairs():
    console.print(
        "\n[bold yellow]ᲓᲐᲘᲛᲐᲮᲡᲝᲕᲠᲔ, ᲩᲐᲘᲬᲔᲠᲔ ᲠᲝᲛᲔᲚᲘᲛᲔ ᲬᲧᲕᲘᲚᲘ:[/bold yellow]\n"
    )
    for a, b, c, d in pairs:
        console.print(Align.center(make_pair_card(a, b), make_pair_card(c, d)))
    console.print()


# ================================
# STEP 2 — ზუსტი 20 კოორდინატი შენს შიფრზე
# ================================
LETTER_TO_COORDS = {
    "N": [(0, 0), (2, 1)],
    "A": [(0, 1), (0, 4)],
    "U": [(0, 2), (1, 0)],
    "K": [(0, 3), (3, 4)],
    "M": [(1, 1), (2, 0)],
    "E": [(1, 2), (1, 3)],
    "T": [(1, 4), (3, 2)],
    "O": [(2, 2), (2, 4)],
    "G": [(2, 3), (3, 0)],
    "I": [(3, 1), (3, 3)],
}

LETTER_ROWS = {
    "N": [1, 3],
    "A": [1],
    "U": [1, 2],
    "K": [1, 4],
    "M": [2, 3],
    "E": [2],
    "T": [2, 4],
    "O": [3],
    "G": [3, 4],
    "I": [4],
}

# coords 20 თანმიმდევრობით
coords = [pos for positions in LETTER_TO_COORDS.values() for pos in positions]

# GRID 5×4
grid = [[None for _ in range(5)] for __ in range(4)]

# placing numbers
flat_numbers = [x for pair in pairs for x in pair]
for num, (r, c) in zip(flat_numbers, coords):
    grid[r][c] = num


# ================================
# GRID print
# ================================
def make_single_card(num):
    return Panel(
        f"[bold]{num}[/bold]", width=6, height=3, border_style="cyan", box=box.ROUNDED
    )


def show_grid():
    console.print("\n[bold cyan]MAGIC 5×4 GRID[/bold cyan]\n")
    for r in range(4):
        row_cards = [make_single_card(grid[r][c]) for c in range(5)]
        console.print(Align.center(Columns(row_cards, equal=True, expand=False)))
        console.print()


# ================================
# TWO CARD PANEL (side-by-side)
# ================================
def make_two_number_panel(a, b):
    left = Panel(
        f"[bold]{a}[/bold]", width=6, height=3, border_style="green", box=box.ROUNDED
    )
    right = Panel(
        f"[bold]{b}[/bold]", width=6, height=3, border_style="green", box=box.ROUNDED
    )

    title = Text("ᲨᲔᲜᲘ ᲬᲧᲕᲘᲚᲘ", style="bold yellow")

    return Panel(
        Columns([left, right], equal=True, expand=False),
        border_style="bright_green",
        box=box.DOUBLE,
        width=17,
        title=title,
    )


# ================================
# GUESSING LOOP
# ================================
def guess_loop():
    console.print(
        "\n[bold magenta]ᲐᲮᲚᲐ ᲛᲔ ᲒᲐᲛᲝᲕᲘᲪᲜᲝᲑ ᲨᲔᲜᲘ ᲠᲘᲪᲮᲕᲔᲑᲘᲡ ᲬᲧᲕᲘᲚᲡ[/bold magenta]"
    )

    while True:
        rows_input = console.input(
            "[cyan]ᲠᲝᲛᲔᲚ ᲠᲘᲒ(ᲔᲑ)ᲨᲘᲐ ᲨᲔᲜᲘ ᲠᲘᲪᲕᲔᲑᲘ? (ᲛᲐᲒᲐᲚᲘᲗᲘ: 1 / 1 3 / 2 4): [/cyan]"
        ).strip()

        try:
            chosen = sorted(map(int, rows_input.split()))
        except:
            console.print("[red]ᲛᲘᲣᲦᲔᲑᲔᲚᲘ ᲤᲝᲠᲛᲐᲢᲘᲐ, ᲡᲪᲐᲓᲔ ᲗᲐᲕᲘᲓᲐᲜ.[/red]")
            continue

        found_letter = None
        for letter, pattern in LETTER_ROWS.items():
            if sorted(pattern) == chosen:
                found_letter = letter
                break

        if found_letter is None:
            console.print("[red]ᲡᲮᲕᲐ ᲠᲐᲦᲐᲪᲐᲡ ᲐᲭᲔᲠ, ᲡᲪᲐᲓᲔ ᲗᲐᲕᲘᲓᲐᲜ.[/red]")
            continue

        # ორი კოორდინატი
        (r1, c1), (r2, c2) = LETTER_TO_COORDS[found_letter]
        n1, n2 = grid[r1][c1], grid[r2][c2]

        console.print()
        console.print(Align.center(make_two_number_panel(n1, n2)))
        console.print()

        again = (
            console.input(
                "[yellow]ᲒᲐᲛᲝᲕᲘᲪᲜᲝ ᲡᲮᲕᲐ ᲬᲧᲕᲘᲚᲘ? (Enter = yes, n = no): [/yellow]"
            )
            .strip()
            .lower()
        )
        if again in ("n", "no"):
            console.print("[red]ᲡᲔᲐᲜᲡᲘ ᲓᲐᲛᲗᲐᲕᲓᲐ, ᲜᲐᲮᲕᲐᲓᲘᲡ...[/red]")
            break

        show_grid()


# ================================
# RUN
# ================================
show_pairs()
console.input("[green]ᲓᲐᲐᲭᲘᲠᲔ Enter-Ს ᲓᲐ ᲒᲐᲩᲕᲔᲜᲔᲑ ᲛᲐᲒᲘᲣᲠ ᲪᲮᲠᲘᲚᲡ...[/green]")
show_grid()
guess_loop()

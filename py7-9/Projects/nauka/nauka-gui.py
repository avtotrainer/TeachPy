import random
import tkinter as tk
from tkinter import messagebox


# ============================================================
#  NAUKA SHIFR — EXACT COORDINATES
# ============================================================
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

COORDS_ORDERED = [p for v in LETTER_TO_COORDS.values() for p in v]


# ============================================================
#  SIMPLE NON-CANVAS CARD  (safe for tkinter layering)
# ============================================================
def make_card(parent, text, bg="#fff6bf", fg="#111", bd_color="#f2c94c"):
    frame = tk.Frame(parent, bg=bd_color, highlightthickness=0)
    inner = tk.Frame(frame, bg=bg)
    label = tk.Label(
        inner, text=text, bg=bg, fg=fg, font=("DejaVu Sans Mono", 22, "bold")
    )
    label.pack(expand=True, fill="both", padx=6, pady=6)
    inner.pack(expand=True, fill="both", padx=3, pady=3)
    return frame


# ============================================================
#  MAIN APP
# ============================================================
class NaukaGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NAUKA — Kids Magic Guess")
        self.geometry("980x720")
        self.configure(bg="#f7fbff")

        # Kids colors
        self.BG = "#f7fbff"
        self.CARD = "#fff6bf"
        self.BORDER = "#f2c94c"
        self.HI = "#d6ecff"
        self.HI_BORDER = "#4ea8de"

        # Screens
        self.frame_pairs = tk.Frame(self, bg=self.BG)
        self.frame_grid = tk.Frame(self, bg=self.BG)

        for f in (self.frame_pairs, self.frame_grid):
            f.place(relwidth=1, relheight=1)

        # Build both pages
        self.build_pairs_screen()
        self.build_grid_screen()

        # Data
        self.pairs = []
        self.grid_nums = [[None for _ in range(5)] for _ in range(4)]

        # Start game
        self.new_game()
        self.show(self.frame_pairs)

    # ========================================================
    def show(self, frame):
        frame.tkraise()

    # ========================================================
    #  PAGE 1 — PAIRS
    # ========================================================
    def build_pairs_screen(self):
        title = tk.Label(
            self.frame_pairs,
            text="აირჩიე და დაიმახსოვრე ერთი წყვილი",
            font=("DejaVu Sans", 30, "bold"),
            bg=self.BG,
        )
        title.pack(pady=20)

        self.pairs_box = tk.Frame(self.frame_pairs, bg=self.BG)
        self.pairs_box.pack(expand=True, fill="both", padx=20, pady=10)

        btns = tk.Frame(self.frame_pairs, bg=self.BG)
        btns.pack(pady=15)

        tk.Button(
            btns,
            text="გაგრძელება →",
            font=("DejaVu Sans", 20, "bold"),
            bg="#ffd166",
            command=lambda: self.show(self.frame_grid),
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btns,
            text="ახალი თამაში",
            font=("DejaVu Sans", 18, "bold"),
            bg="#9ad0ff",
            command=self.new_game,
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            btns,
            text="დასრულება",
            font=("DejaVu Sans", 18, "bold"),
            bg="#ff9aa2",
            command=self.destroy,
        ).grid(row=0, column=2, padx=10)

    # ========================================================
    #  PAGE 2 — GRID
    # ========================================================
    def build_grid_screen(self):
        title = tk.Label(
            self.frame_grid,
            text="რომელ ხაზ(ებ)შია შენი რიცხვები?",
            font=("DejaVu Sans", 28, "bold"),
            bg=self.BG,
        )
        title.pack(pady=15)

        self.grid_box = tk.Frame(self.frame_grid, bg=self.BG)
        self.grid_box.pack(expand=True, fill="both", padx=20)

        # checkboxes
        select = tk.Frame(self.frame_grid, bg=self.BG)
        select.pack(pady=15)

        self.row_vars = [tk.IntVar() for _ in range(4)]
        romans = ["I", "II", "III", "IV"]

        for i in range(4):
            tk.Checkbutton(
                select,
                text=f"{romans[i]} ხაზი",
                variable=self.row_vars[i],
                font=("DejaVu Sans", 22, "bold"),
                bg=self.BG,
                command=self.update_highlight,
            ).grid(row=0, column=i, padx=15)

        # buttons
        btns = tk.Frame(self.frame_grid, bg=self.BG)
        btns.pack(pady=10)

        tk.Button(
            btns,
            text="გამოცნობა",
            font=("DejaVu Sans", 20, "bold"),
            bg="#7ee787",
            command=self.on_guess,
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btns,
            text="შემდეგი მოსწავლე",
            font=("DejaVu Sans", 18, "bold"),
            bg="#ffd166",
            command=self.next_student,
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            btns,
            text="← უკან",
            font=("DejaVu Sans", 18, "bold"),
            bg="#9ad0ff",
            command=lambda: self.show(self.frame_pairs),
        ).grid(row=0, column=2, padx=10)

        tk.Button(
            btns,
            text="დასრულება",
            font=("DejaVu Sans", 18, "bold"),
            bg="#ff9aa2",
            command=self.destroy,
        ).grid(row=0, column=3, padx=10)

        # Results
        self.result_box = tk.Frame(self.frame_grid, bg=self.BG)
        self.result_box.pack(pady=10)

    # ========================================================
    #  NEW GAME
    # ========================================================
    def new_game(self):
        nums = random.sample(range(10, 100), 20)
        self.pairs = [(nums[i], nums[i + 1]) for i in range(0, 20, 2)]

        # place in grid
        flat = [x for p in self.pairs for x in p]
        self.grid_nums = [[None for _ in range(5)] for _ in range(4)]
        for num, (r, c) in zip(flat, COORDS_ORDERED):
            self.grid_nums[r][c] = num

        self.render_pairs()
        self.render_grid()
        self.clear_result()
        self.clear_rows()

    # ========================================================
    #  RENDER PAIRS
    # ========================================================
    def render_pairs(self):
        for w in self.pairs_box.winfo_children():
            w.destroy()

        for i, (a, b) in enumerate(self.pairs):
            row = i // 2
            col = i % 2

            holder = tk.Frame(self.pairs_box, bg=self.BG)
            holder.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)

            for r in range(5):
                self.pairs_box.grid_rowconfigure(r, weight=1)
            for c in range(2):
                self.pairs_box.grid_columnconfigure(c, weight=1)

            card = make_card(holder, f"{a}   {b}", bg=self.CARD, bd_color=self.BORDER)
            card.pack(expand=True, fill="both")

    # ========================================================
    #  RENDER GRID 5×4
    # ========================================================
    def render_grid(self):
        for w in self.grid_box.winfo_children():
            w.destroy()

        self.cards = [[None for _ in range(5)] for _ in range(4)]

        for r in range(4):
            self.grid_box.grid_rowconfigure(r, weight=1)
        for c in range(5):
            self.grid_box.grid_columnconfigure(c, weight=1)

        for r in range(4):
            for c in range(5):
                holder = tk.Frame(self.grid_box, bg=self.BG)
                holder.grid(row=r, column=c, sticky="nsew", padx=7, pady=7)

                card = make_card(
                    holder,
                    str(self.grid_nums[r][c]),
                    bg=self.CARD,
                    fg="#2e7d32",
                    bd_color=self.BORDER,
                )
                card.pack(expand=True, fill="both")

                self.cards[r][c] = card

        self.update_highlight()

    # ========================================================
    def update_highlight(self):
        for r in range(4):
            marked = self.row_vars[r].get() == 1
            for c in range(5):
                card = self.cards[r][c]
                if marked:
                    card.configure(bg=self.HI)
                    for child in card.winfo_children():
                        child.configure(bg=self.HI)
                else:
                    card.configure(bg=self.CARD)
                    for child in card.winfo_children():
                        child.configure(bg=self.CARD)

    def clear_rows(self):
        for v in self.row_vars:
            v.set(0)
        self.update_highlight()

    # ========================================================
    #  GUESS
    # ========================================================
    def on_guess(self):
        rows = [i + 1 for i, v in enumerate(self.row_vars) if v.get() == 1]
        if not rows:
            messagebox.showwarning("ყურადღება", "მონიშნე ერთი მაინც ხაზი!")
            return

        rows = sorted(rows)

        found = None
        for letter, pattern in LETTER_ROWS.items():
            if sorted(pattern) == rows:
                found = letter
                break

        if not found:
            messagebox.showerror("შეცდომა", "ასეთი ხაზების კომბინაცია არ არსებობს.")
            return

        (r1, c1), (r2, c2) = LETTER_TO_COORDS[found]
        n1 = self.grid_nums[r1][c1]
        n2 = self.grid_nums[r2][c2]

        self.show_result(n1, n2)

    # ========================================================
    def clear_result(self):
        for w in self.result_box.winfo_children():
            w.destroy()

    def show_result(self, n1, n2):
        self.clear_result()

        tk.Label(
            self.result_box,
            text="შენი წყვილი:",
            bg=self.BG,
            font=("DejaVu Sans", 22, "bold"),
        ).pack()

        row = tk.Frame(self.result_box, bg=self.BG)
        row.pack()

        left = make_card(row, n1, bg=self.CARD)
        left.grid(row=0, column=0, padx=15, pady=10)

        right = make_card(row, n2, bg=self.CARD)
        right.grid(row=0, column=1, padx=15, pady=10)

    # ========================================================
    def next_student(self):
        self.clear_rows()
        self.clear_result()


# ============================================================
#   RUN
# ============================================================
if __name__ == "__main__":
    NaukaGui().mainloop()

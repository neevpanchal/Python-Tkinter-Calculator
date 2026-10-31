"""
Modern Tkinter Calculator
=========================
Author: Neev Panchal
GitHub: https://github.com/neevpanchal/Python-Tkinter-Calculator
License: MIT

An enhanced, modern desktop calculator application featuring a clean dark UI,
full keyboard navigation, safe arithmetic evaluation, and responsive design.
"""

import math
import tkinter as tk
from tkinter import font as tkfont


class Calculator:
    """Modern Desktop Calculator Application built with Tkinter."""

    # Color Palette (Modern Apple/Obsidian Dark Theme)
    COLOR_BG = "#18181b"          # Main window background (Zinc 900)
    COLOR_DISPLAY_BG = "#27272a"  # Display card background (Zinc 800)
    COLOR_EXPR = "#a1a1aa"        # Small expression history text (Zinc 400)
    COLOR_TEXT = "#ffffff"        # Main text color
    COLOR_NUM_BTN = "#3f3f46"     # Numeric buttons (Zinc 700)
    COLOR_NUM_HOVER = "#52525b"   # Numeric button hover
    COLOR_OP_BTN = "#f97316"      # Operator buttons (Orange 500)
    COLOR_OP_HOVER = "#fb923c"    # Operator hover (Orange 400)
    COLOR_SPEC_BTN = "#52525b"    # Special buttons (C, ⌫, %) (Zinc 600)
    COLOR_SPEC_HOVER = "#71717a"  # Special button hover
    COLOR_EQUAL_BTN = "#10b981"   # Equal button (Emerald 500)
    COLOR_EQUAL_HOVER = "#34d399" # Equal hover

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("340x510")
        self.root.resizable(False, False)
        self.root.configure(bg=self.COLOR_BG)

        # Center the window on screen
        self._center_window()

        # Calculator State
        self.expression = ""
        self.last_result = None
        self.just_calculated = False

        # Build UI and setup Keyboard bindings
        self._create_display()
        self._create_buttons()
        self._bind_keys()

    def _center_window(self):
        """Centers the Tkinter window on the primary display."""
        self.root.update_idletasks()
        width = 340
        height = 510
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = max(0, (screen_width - width) // 2)
        y = max(0, (screen_height - height) // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def _create_display(self):
        """Creates a modern two-line display showing expression history and current input."""
        display_frame = tk.Frame(self.root, bg=self.COLOR_DISPLAY_BG, padx=16, pady=16)
        display_frame.pack(fill="x", padx=16, pady=(16, 12))

        # Top line: shows full expression (e.g., 25 + 15 =)
        self.history_label = tk.Label(
            display_frame,
            text="",
            font=("Segoe UI", 11),
            fg=self.COLOR_EXPR,
            bg=self.COLOR_DISPLAY_BG,
            anchor="e"
        )
        self.history_label.pack(fill="x")

        # Bottom line: main active entry / result
        self.entry_var = tk.StringVar(value="0")
        self.entry = tk.Label(
            display_frame,
            textvariable=self.entry_var,
            font=("Segoe UI", 26, "bold"),
            fg=self.COLOR_TEXT,
            bg=self.COLOR_DISPLAY_BG,
            anchor="e"
        )
        self.entry.pack(fill="x", pady=(4, 0))

    def _create_buttons(self):
        """Creates the calculator grid with hover animations and curated colors."""
        button_frame = tk.Frame(self.root, bg=self.COLOR_BG)
        button_frame.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        # Button Layout: (label, row, col, type, command_param)
        layout = [
            ("C", 0, 0, "spec", self.clear),
            ("⌫", 0, 1, "spec", self.backspace),
            ("%", 0, 2, "spec", lambda: self.operator_click("%")),
            ("÷", 0, 3, "op", lambda: self.operator_click("/")),

            ("7", 1, 0, "num", lambda: self.number_click("7")),
            ("8", 1, 1, "num", lambda: self.number_click("8")),
            ("9", 1, 2, "num", lambda: self.number_click("9")),
            ("×", 1, 3, "op", lambda: self.operator_click("*")),

            ("4", 2, 0, "num", lambda: self.number_click("4")),
            ("5", 2, 1, "num", lambda: self.number_click("5")),
            ("6", 2, 2, "num", lambda: self.number_click("6")),
            ("-", 2, 3, "op", lambda: self.operator_click("-")),

            ("1", 3, 0, "num", lambda: self.number_click("1")),
            ("2", 3, 1, "num", lambda: self.number_click("2")),
            ("3", 3, 2, "num", lambda: self.number_click("3")),
            ("+", 3, 3, "op", lambda: self.operator_click("+")),

            ("±", 4, 0, "num", self.toggle_sign),
            ("0", 4, 1, "num", lambda: self.number_click("0")),
            (".", 4, 2, "num", self.dot_click),
            ("=", 4, 3, "equal", self.calculate),
        ]

        # Configure 5 rows and 4 columns grid weights
        for r in range(5):
            button_frame.rowconfigure(r, weight=1, uniform="row")
        for c in range(4):
            button_frame.columnconfigure(c, weight=1, uniform="col")

        self.buttons = {}
        for text, row, col, btype, cmd in layout:
            bg_color, hover_color, text_color = self._get_button_colors(btype)

            btn = tk.Button(
                button_frame,
                text=text,
                font=("Segoe UI", 15, "bold" if btype in ("op", "equal") else "normal"),
                fg=text_color,
                bg=bg_color,
                activebackground=hover_color,
                activeforeground=text_color,
                bd=0,
                relief="flat",
                cursor="hand2",
                command=cmd
            )
            btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

            # Mouse hover effect
            btn.bind("<Enter>", lambda e, b=btn, h=hover_color: b.configure(bg=h))
            btn.bind("<Leave>", lambda e, b=btn, bg=bg_color: b.configure(bg=bg))
            self.buttons[text] = btn

    def _get_button_colors(self, btype: str):
        """Returns (background, hover, text) colors for a button type."""
        if btype == "op":
            return self.COLOR_OP_BTN, self.COLOR_OP_HOVER, self.COLOR_TEXT
        if btype == "equal":
            return self.COLOR_EQUAL_BTN, self.COLOR_EQUAL_HOVER, self.COLOR_TEXT
        if btype == "spec":
            return self.COLOR_SPEC_BTN, self.COLOR_SPEC_HOVER, self.COLOR_TEXT
        return self.COLOR_NUM_BTN, self.COLOR_NUM_HOVER, self.COLOR_TEXT

    def _bind_keys(self):
        """Binds physical keyboard keys to calculator actions."""
        # Digits
        for digit in "0123456789":
            self.root.bind(digit, lambda e, d=digit: self.number_click(d))
            self.root.bind(f"<KP_{digit}>", lambda e, d=digit: self.number_click(d))

        # Operators
        self.root.bind("+", lambda e: self.operator_click("+"))
        self.root.bind("-", lambda e: self.operator_click("-"))
        self.root.bind("*", lambda e: self.operator_click("*"))
        self.root.bind("/", lambda e: self.operator_click("/"))
        self.root.bind("%", lambda e: self.operator_click("%"))

        # Decimals
        self.root.bind(".", lambda e: self.dot_click())
        self.root.bind("<KP_Decimal>", lambda e: self.dot_click())

        # Calculate
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<KP_Enter>", lambda e: self.calculate())
        self.root.bind("=", lambda e: self.calculate())

        # Clear & Backspace
        self.root.bind("<BackSpace>", lambda e: self.backspace())
        self.root.bind("<Escape>", lambda e: self.clear())
        self.root.bind("c", lambda e: self.clear())
        self.root.bind("C", lambda e: self.clear())

    # ---------------- Calculator Logic ----------------

    def number_click(self, digit: str):
        """Appends a number to the current expression."""
        if self.just_calculated:
            self.expression = ""
            self.just_calculated = False

        if self.expression == "0":
            self.expression = digit
        else:
            self.expression += digit

        self._update_display(self.expression)

    def dot_click(self):
        """Handles decimal point insertion safely."""
        if self.just_calculated:
            self.expression = "0"
            self.just_calculated = False

        if not self.expression or self.expression[-1] in "+-*/%":
            self.expression += "0."
        else:
            # Check current number segment for existing decimal point
            parts = [p for p in "+-*/%" if p in self.expression]
            last_op_index = -1
            for op in "+-*/%":
                idx = self.expression.rfind(op)
                if idx > last_op_index:
                    last_op_index = idx
            current_segment = self.expression[last_op_index + 1:]
            if "." not in current_segment:
                self.expression += "."

        self._update_display(self.expression)

    def operator_click(self, op: str):
        """Appends an operator, replacing the previous one if clicked sequentially."""
        self.just_calculated = False

        if not self.expression:
            if self.last_result is not None:
                self.expression = str(self.last_result) + op
            elif op == "-":
                self.expression = "-"
            return

        # If previous character is an operator, replace it
        if self.expression[-1] in "+-*/%":
            self.expression = self.expression[:-1] + op
        else:
            self.expression += op

        self._update_display(self.expression)

    def toggle_sign(self):
        """Toggles the positive/negative sign of the current number."""
        if not self.expression or self.expression == "0":
            return

        # Find the last number token
        last_op_index = -1
        for op in "+-*/%":
            idx = self.expression.rfind(op)
            if idx > last_op_index:
                last_op_index = idx

        if last_op_index == -1:
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression
        else:
            prefix = self.expression[:last_op_index + 1]
            token = self.expression[last_op_index + 1:]
            if token.startswith("-"):
                self.expression = prefix + token[1:]
            else:
                self.expression = prefix + f"(-{token})"

        self._update_display(self.expression)

    def backspace(self):
        """Removes the last character from the active expression."""
        if self.just_calculated:
            self.clear()
            return

        if self.expression:
            self.expression = self.expression[:-1]
            self._update_display(self.expression if self.expression else "0")

    def clear(self):
        """Resets the calculator state and display."""
        self.expression = ""
        self.last_result = None
        self.just_calculated = False
        self.history_label.config(text="")
        self.entry_var.set("0")

    def calculate(self):
        """Evaluates the mathematical expression safely with precise formatting."""
        if not self.expression:
            return

        expr_to_eval = self.expression.strip()

        # Handle ending operators gracefully
        while expr_to_eval and expr_to_eval[-1] in "+-*/%":
            expr_to_eval = expr_to_eval[:-1]

        if not expr_to_eval:
            return

        # Replace visual symbols with python operators
        formatted_expr = expr_to_eval.replace("×", "*").replace("÷", "/")

        try:
            # Safe evaluation with restricted environment
            result = eval(formatted_expr, {"__builtins__": {}, "math": math}, {})

            # Format the output cleanly
            if isinstance(result, float):
                # Clean IEEE-754 precision issues (e.g., 0.1 + 0.2 -> 0.3)
                result = round(result, 10)
                if result.is_integer():
                    result = int(result)

            display_result = f"{result:,}" if isinstance(result, int) else f"{result}"
            self.history_label.config(text=f"{expr_to_eval} =")
            self.entry_var.set(display_result)

            self.last_result = result
            self.expression = str(result)
            self.just_calculated = True

        except ZeroDivisionError:
            self.history_label.config(text=f"{expr_to_eval} =")
            self.entry_var.set("Cannot divide by 0")
            self.expression = ""
            self.just_calculated = True
        except Exception:
            self.history_label.config(text="Error")
            self.entry_var.set("Invalid Expression")
            self.expression = ""
            self.just_calculated = True

    def _update_display(self, text: str):
        """Updates the main display with clean visual symbols for operators."""
        display_text = (
            text.replace("*", " × ")
            .replace("/", " ÷ ")
            .replace("+", " + ")
            .replace("-", " - ")
            .replace("%", " % ")
        )
        self.entry_var.set(display_text)


def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()

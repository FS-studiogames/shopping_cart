import tkinter as tk
from tkinter import messagebox
import cart as student

PRODUCTS = [
    ("Apple", 0.50),
    ("Banana", 0.25),
    ("Bread", 2.00),
    ("Milk", 1.20),
    ("Cheese", 3.50),
    ("Chocolate", 1.75),
]


class ShopApp:
    def __init__(self, root):
        self.root = root
        self.cart = {}
        self.quantity = tk.IntVar(value=1)
        root.title("Python Shop")
        self.build_products()
        self.build_cart()
        self.refresh()

    def build_products(self):
        frame = tk.LabelFrame(self.root, text="Products", padx=10, pady=10)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        tk.Label(frame, text="Quantity:").grid(row=0, column=0, sticky="w")
        tk.Spinbox(frame, from_=1, to=20, width=5, textvariable=self.quantity).grid(row=0, column=1, sticky="w")
        for row, (name, price) in enumerate(PRODUCTS, start=1):
            tk.Label(frame, text=f"{name}  ${price:.2f}", width=16, anchor="w").grid(row=row, column=0, pady=2)
            tk.Button(frame, text="Add", width=6, command=lambda n=name, p=price: self.add(n, p)).grid(row=row, column=1)
            tk.Button(frame, text="Remove", width=6, command=lambda n=name: self.remove(n)).grid(row=row, column=2)

    def build_cart(self):
        frame = tk.LabelFrame(self.root, text="Your cart", padx=10, pady=10)
        frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")
        self.listbox = tk.Listbox(frame, width=35, height=10)
        self.listbox.pack()
        self.total_label = tk.Label(frame, font=("Arial", 14, "bold"))
        self.total_label.pack(pady=5)
        self.debug_label = tk.Label(frame, fg="gray", wraplength=260, justify="left")
        self.debug_label.pack()

    def call(self, function, *args):
        try:
            return function(*args)
        except Exception as error:
            messagebox.showerror("Bug in cart.py", f"{function.__name__}() crashed:\n{type(error).__name__}: {error}")
            return None

    def add(self, name, price):
        self.call(student.add_item, self.cart, name, price, self.quantity.get())
        self.refresh()

    def remove(self, name):
        self.call(student.remove_item, self.cart, name)
        self.refresh()

    def refresh(self):
        self.show_lines()
        self.show_total()
        self.debug_label.config(text=f"cart = {self.cart}")

    def show_lines(self):
        self.listbox.delete(0, tk.END)
        lines = self.call(student.show_cart, self.cart)
        if lines is None:
            self.listbox.insert(tk.END, "show_cart() returned nothing")
            return
        for line in lines:
            self.listbox.insert(tk.END, line)

    def show_total(self):
        total = self.call(student.total_price, self.cart)
        if isinstance(total, (int, float)):
            self.total_label.config(text=f"Total: ${total:.2f}")
        else:
            self.total_label.config(text=f"Total: {total}")


if __name__ == "__main__":
    window = tk.Tk()
    ShopApp(window)
    window.mainloop()
import tkinter as tk
from tkinter import ttk

def convert_currency():
    print(f"Converting {amount_entry.get()} from {from_dropdown.get()} to {to_dropdown.get()}...")

def on_enter(e): convert_button.config(bg="#0071e3")
def on_leave(e): convert_button.config(bg="#0088ff")

# Main Application Window setup
root = tk.Tk()
root.title("Currency Converter") 
root.configure(bg="#0f0f11")
root.geometry("800x600")
root.resizable(False, False)

style = ttk.Style()
style.theme_use('default')
style.configure("TCombobox", fieldbackground="#1e1e1e", background="#2c2c2e", foreground="white", arrowcolor="white")
root.option_add("*TCombobox*Listbox.background", "#1e1e1e")
root.option_add("*TCombobox*Listbox.foreground", "white")
root.option_add("*TCombobox*Listbox.selectBackground", "#0a84ff")

# UI Elements
title_label = tk.Label(root, text="Currency Converter", font=("Arial", 26, "bold"), bg="#0f0f11", fg="white")
title_label.pack(pady=(40, 20))

info_label = tk.Label(root, text="Enter Amount:", font=("Arial", 11), bg="#0f0f11", fg="#888888")
info_label.pack(pady=(5, 0))

amount_entry = tk.Entry(root, font=("Arial", 16), bg="#1e1e1e", fg="white", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#2c2c2e", highlightcolor="#0a84ff", justify="center")
amount_entry.pack(pady=(5, 20), ipady=10, ipadx=15)

currency_options = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "INR", "BRL"]

# Convert from dropdown
from_label = tk.Label(root, text="Convert from:", font=("Arial", 11), bg="#0f0f11", fg="#888888")
from_label.pack(pady=(5, 0))
from_dropdown = ttk.Combobox(root, values=currency_options, state="readonly", font=("Arial", 14), justify="center", width=6)
from_dropdown.set("GBP")
from_dropdown.pack(pady=5)

# Directional text
to_label = tk.Label(root, text="to", font=("Arial", 12, "italic"), bg="#0f0f11", fg="#888888")
to_label.pack(pady=2)

# Convert to dropdown
to_dropdown_label = tk.Label(root, text="Convert to:", font=("Arial", 11), bg="#0f0f11", fg="#888888")
to_dropdown_label.pack(pady=(5, 0))
to_dropdown = ttk.Combobox(root, values=currency_options, state="readonly", font=("Arial", 14), justify="center", width=6)
to_dropdown.set("USD")
to_dropdown.pack(pady=5)

# Convert Button
convert_button = tk.Label(root, text="Convert", font=("Arial", 14, "bold"), bg="#0088ff", fg="white", cursor="hand2", padx=40, pady=10)
convert_button.pack(pady=(25, 30))

convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)
convert_button.bind("<Button-1>", lambda event: convert_currency())

root.mainloop()
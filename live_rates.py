import tkinter as tk
from tkinter import ttk

def open_live_rates_page(parent_window):
    
    rates_win = tk.Toplevel(parent_window)
    rates_win.title("Live Rates Board")
    rates_win.geometry("380x480")
    rates_win.configure(bg="#1a1a1a")
    rates_win.resizable(False, False)

    style = ttk.Style(rates_win)
    style.theme_use('default')
    style.configure("TCombobox", fieldbackground="#1e1e1e", background="#2c2c2c", foreground="white", arrowcolor="white")

    header = tk.Label(rates_win, text="Exchange Rates Dashboard (Base: GBP)", font=("Arial", 12, "bold"), bg="#1a1a1a", fg="white")
    header.pack(pady=(15, 5))

    display_box = tk.Text(rates_win, width=36, height=16, font=("Courier", 11), bg="#111111", fg="white", wrap="none", bd=0, padx=12, pady=12)
    display_box.pack(pady=10)

    
    def render_layout_design():
        display_box.config(state="normal")
        display_box.delete("1.0", tk.END)
        
    
        display_box.insert(tk.END, "Market Date : YYYY-MM-DD\n")
        display_box.insert(tk.END, "Last Synced : HH:MM:SS\n")
        display_box.insert(tk.END, "=" * 32 + "\n\n")
        display_box.insert(tk.END, f"{'Currency':<12} | {'Live Rate':<12}\n")
        display_box.insert(tk.END, "-" * 32 + "\n")
        
        display_box.config(state="disabled")

    reload_btn = tk.Label(rates_win, text=" Refresh Board Data", font=("Arial", 10, "bold"), bg="#0288ff", fg="white", cursor="hand2", padx=12, pady=6)
    reload_btn.pack(pady=(5, 15))
    
    reload_btn.bind("<Button-1>", lambda event: render_layout_design())

    render_layout_design()
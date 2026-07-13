import tkinter as tk
from tkinter import ttk
from datetime import datetime
import currency_api

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

    history_subtitle = tk.Label(rates_win, text="Exchange Rates Pulled From the API", font=("Arial", 10, "italic"), bg="#141416", fg="#666666")
    history_subtitle.pack(pady=(0, 15))

    display_box = tk.Text(rates_win, width=36, height=16, font=("Courier", 11), bg="#111111", fg="white", wrap="none", bd=0, padx=12, pady=12)
    display_box.pack(pady=10)

    def render_layout_design():
        display_box.config(state="normal")
        display_box.delete("1.0", tk.END)
        
        all_rates = currency_api.fetch_live_rates("GBP")
        current_time = datetime.now().strftime("%H:%M:%S")
        
        display_box.insert(tk.END, "Market Date : Live Data\n")
        display_box.insert(tk.END, f"Last Synced : {current_time}\n")
        display_box.insert(tk.END, "=" * 32 + "\n\n")
        display_box.insert(tk.END, f"{'Currency':<12} | {'Live Rate':<12}\n")
        display_box.insert(tk.END, "-" * 32 + "\n")
        
        if all_rates:
            target_symbols = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "INR", "BRL"]
            for symbol in target_symbols:
                if symbol in all_rates:
                    rate_value = all_rates[symbol]
                    display_box.insert(tk.END, f"{symbol:<12} | {rate_value:<12.4f}\n")
        else:
            display_box.insert(tk.END, "\n      Error fetching rates.\n")
            
        display_box.config(state="disabled")

    reload_btn = tk.Label(rates_win, text=" Refresh Board Data", font=("Arial", 10, "bold"), bg="#0288ff", fg="white", cursor="hand2", padx=12, pady=6)
    reload_btn.pack(pady=(5, 15))
    
    reload_btn.bind("<Button-1>", lambda event: render_layout_design())

    render_layout_design()
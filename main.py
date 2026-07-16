import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import currency_api
import conversion_log
import live_rates 
import upload_cvs_toDB

def convert_currency():
    from_curr = from_dropdown.get()
    to_curr = to_dropdown.get()
    user_input = amount_entry.get()
    
    if from_curr == to_curr:
        messagebox.showerror("Error", f"Cannot convert {from_curr} to the same currency.")
        return
        
    if not user_input:
        messagebox.showerror("Error", "Please enter an amount to convert.")
        return
        
    try:
        amount = float(user_input)
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than zero.")
            return
        rates = currency_api.fetch_live_rates(from_curr)
        
        if rates is None:
            messagebox.showerror("Network Error", "Failed to get live rates. Check internet connection.")
            return
            
        target_rate = rates.get(to_curr)
        if not target_rate:
            messagebox.showerror("Error", f"Could not find exchange rate for {to_curr}.")
            return
            
        final_result = round(amount * target_rate, 2)
        
        print(f"SUCCESS: {amount} {from_curr} = {final_result} {to_curr}")
        conversion_log.log_conversion(from_curr, to_curr, amount, final_result)
        messagebox.showinfo("SUCCESS", f"{amount} {from_curr} = {final_result} {to_curr}")
        refresh_history_display()
    
    except ValueError:
        messagebox.showerror("Error", f"'{user_input}' is not a valid number.")

def refresh_history_display():

    updated_text = conversion_log.read_last_entries()
    
    history_box.config(state="normal")
    history_box.delete("1.0", tk.END)
    history_box.insert(tk.END, updated_text)
    history_box.config(state="disabled")


#----App Design and Layout----# 
# Button effects
def on_enter(e): convert_button.config(bg="#0071e3")
def on_leave(e): convert_button.config(bg="#0088ff")

# Main App Window Setup 
root = tk.Tk()
root.title("Currency Converter") 
root.geometry("850x600") # made the window pannel bigger to accommodate the new right panel for the log. 
root.resizable(False, False) # cannot resize the window to avoid layout issues. 


style = ttk.Style()
style.theme_use('default')
style.configure("TCombobox", fieldbackground="#1e1e1e", background="#2c2c2e", foreground="white", arrowcolor="white")
root.option_add("*TCombobox*Listbox.background", "#1e1e1e")
root.option_add("*TCombobox*Listbox.foreground", "white")
root.option_add("*TCombobox*Listbox.selectBackground", "#0a84ff")

# 1. LEFT PANEL: CONVERTER
left_panel = tk.Frame(root, bg="#0f0f11", width=425, height=600)
left_panel.pack(side="left", fill="both", expand=True)

#Left side window UI Elements
title_label = tk.Label(left_panel, text="Currency Converter", font=("Arial", 24, "bold"), bg="#0f0f11", fg="white")
title_label.pack(pady=(50, 30))

info_label = tk.Label(left_panel, text="Enter Amount:", font=("Arial", 11), bg="#0f0f11", fg="#888888")
info_label.pack(pady=(5, 0))

amount_entry = tk.Entry(left_panel, font=("Arial", 16), bg="#1e1e1e", fg="white", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#2c2c2e", highlightcolor="#0a84ff", justify="center")
amount_entry.pack(pady=(5, 20), ipady=10, ipadx=15)

# Placeholder currency options for the dropdowns (will be replaced with API options later)
currency_options = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "INR", "BRL"]

from_label = tk.Label(left_panel, text="Convert from:", font=("Arial", 11), bg="#0f0f11", fg="#888888")
from_label.pack(pady=(5, 0))
from_dropdown = ttk.Combobox(left_panel, values=currency_options, state="readonly", font=("Arial", 14), justify="center", width=6)
from_dropdown.set("GBP")
from_dropdown.pack(pady=5)

to_label = tk.Label(left_panel, text="to", font=("Arial", 12, "italic"), bg="#0f0f11", fg="#888888")
to_label.pack(pady=2)

to_dropdown_label = tk.Label(left_panel, text="Convert to:", font=("Arial", 11), bg="#0f0f11", fg="#888888")
to_dropdown_label.pack(pady=(5, 0))
to_dropdown = ttk.Combobox(left_panel, values=currency_options, state="readonly", font=("Arial", 14), justify="center", width=6)
to_dropdown.set("USD")
to_dropdown.pack(pady=5)

convert_button = tk.Label(left_panel, text="Convert", font=("Arial", 14, "bold"), bg="#0088ff", fg="white", cursor="hand2", padx=40, pady=10)
convert_button.pack(pady=(35, 30))

convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)
convert_button.bind("<Button-1>", lambda event: convert_currency())


# RIGHT PANEL: TRANSACTION AUDIT LOG
right_panel = tk.Frame(root, bg="#141416", width=425, height=600, highlightthickness=1, highlightbackground="#2c2c2e")
right_panel.pack(side="right", fill="both", expand=True)

#Right Side Window Elements

##------Live Currenecy Rates Page------##
right_live_rate_button = tk.Label(right_panel,text="View Live Rates Board", font=["Arial", 9, "bold"],bg="#444343",fg="white",cursor="hand2",padx=8,pady=4)
right_live_rate_button.pack(anchor="ne", padx=20, pady=(25, 0))
right_live_rate_button.bind("<Button-1>", lambda event: live_rates.open_live_rates_page(root))

#--------History Log Section--------#
history_title = tk.Label(right_panel, text="Historical Log", font=("Arial", 18, "bold"), bg="#141416", fg="white")
history_title.pack(pady=(50, 5))

history_subtitle = tk.Label(right_panel, text="Local Saved Conversions (no need to worry these are auto-saved! )", font=("Arial", 10, "italic"), bg="#141416", fg="#666666")
history_subtitle.pack(pady=(0, 15))

history_box = tk.Text(right_panel, height=15, width=64, bg="#1e1e1e", fg="#a1a1aa", font=("Courier", 11), bd=0, highlightthickness=1, highlightbackground="#2c2c2e", padx=10, pady=10)
history_box.pack(pady=10)

history_box.insert(tk.END, "No local history found.\nRun a conversion to append data.")
history_box.config(state="disabled")

clear_csv_button = tk.Label(right_panel, text="Clear Log", font=("Arial", 10, "bold"), bg="#ff3b30", fg="white", cursor="hand2", padx=12, pady=6)
clear_csv_button.pack(pady=(5, 15))
clear_csv_button.bind("<Button-1>", lambda event: [messagebox.showinfo("Clear Log", conversion_log.clear_cvs()), refresh_history_display()])

download_csv_button = tk.Label(right_panel, text="Download Log", font=("Arial", 10, "bold"), bg="#34c759", fg="white", cursor="hand2", padx=12, pady=6)
download_csv_button.pack(pady=(5, 15))
download_csv_button.bind("<Button-1>", lambda event: [messagebox.showinfo("Download Log", conversion_log.download_csv()), refresh_history_display()])

#In Development (getting prepared for future updates *uploading the CVS to a local DB for research and analysis purposes*)
upload_csv_button = tk.Label(right_panel, text="Upload Log (In Development)", font=("Arial", 10, "bold"), bg="#ff9f0a", fg="white", cursor="hand2", padx=12, pady=6)
upload_csv_button.pack(pady=(5, 15))
upload_csv_button.bind("<Button-1>", lambda event: upload_cvs_toDB.upload_csv_to_db(root))

refresh_history_display()
root.mainloop()
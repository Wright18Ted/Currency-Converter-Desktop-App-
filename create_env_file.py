import os
import tkinter as tk
from tkinter import messagebox


def delete_env_file():
    if os.path.exists(".env"):
        try:
            os.remove(".env")
            messagebox.showinfo("Success", ".env file deleted successfully!")
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to delete .env file:\n{e}")
    else:
        messagebox.showinfo("Info", ".env file does not exist.")

def create_env_file(parent_window):
    current_settings = {
        "POSTGRES_HOST": "localhost", 
        "POSTGRES_DB": "currency_db", 
        "POSTGRES_USER": "postgres", 
        "POSTGRES_PASSWORD": ""
    }
    
    if os.path.exists(".env"):
        try:
            with open(".env", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and "=" in line:
                        key, val = line.split("=", 1)
                        if key in current_settings:
                            current_settings[key] = val
        except Exception:
            pass

   #Window setup for the .env file creation UI.  
    env_window = tk.Toplevel(parent_window)
    env_window.title("Create .env File")
    env_window.geometry("500x360")  
    env_window.configure(bg="#1a1a1a")
    env_window.resizable(False, False)
    env_window.grab_set()

    
    title_label = tk.Label(env_window, text="Create .env File", font=("Arial", 24, "bold"), bg="#1a1a1a", fg="white")
    title_label.pack(pady=(15, 5))

    sub_label = tk.Label(env_window, text="Configure your PostgreSQL database connection details", font=("Arial", 9), bg="#1a1a1a", fg="#a1a1aa")
    sub_label.pack(pady=(0, 15))

    
    label_style = {"bg": "#1a1a1a", "fg": "#a1a1aa", "font": ("Arial", 10, "bold")}
    entry_style = {"bg": "#2c2c2e", "fg": "white", "bd": 0, "insertbackground": "white", "font": ("Arial", 10), "highlightthickness": 1, "highlightbackground": "#3a3a3c", "highlightcolor": "#007acc"}

    
    fields_frame = tk.Frame(env_window, bg="#1a1a1a")
    fields_frame.pack(padx=40, fill="x")

    
    tk.Label(fields_frame, text="DB Host:", **label_style).grid(row=0, column=0, sticky="w", pady=6)
    host_entry = tk.Entry(fields_frame, **entry_style)
    host_entry.insert(0, current_settings["POSTGRES_HOST"])
    host_entry.grid(row=0, column=1, sticky="ew", pady=6, padx=(15, 0))

    
    tk.Label(fields_frame, text="DB Name:", **label_style).grid(row=1, column=0, sticky="w", pady=6)
    db_entry = tk.Entry(fields_frame, **entry_style)
    db_entry.insert(0, current_settings["POSTGRES_DB"])
    db_entry.grid(row=1, column=1, sticky="ew", pady=6, padx=(15, 0))

    
    tk.Label(fields_frame, text="DB User:", **label_style).grid(row=2, column=0, sticky="w", pady=6)
    user_entry = tk.Entry(fields_frame, **entry_style)
    user_entry.insert(0, current_settings["POSTGRES_USER"])
    user_entry.grid(row=2, column=1, sticky="ew", pady=6, padx=(15, 0))

   
    tk.Label(fields_frame, text="DB Password:", **label_style).grid(row=3, column=0, sticky="w", pady=6)
    pass_entry = tk.Entry(fields_frame, show="*", **entry_style)
    pass_entry.insert(0, current_settings["POSTGRES_PASSWORD"])
    pass_entry.grid(row=3, column=1, sticky="ew", pady=6, padx=(15, 0))

    fields_frame.columnconfigure(1, weight=1)

    #Save button functionality to save the .env file with the provided database connection details. 
    def save_env():
        host = host_entry.get().strip()
        db_name = db_entry.get().strip()
        user = user_entry.get().strip()
        password = pass_entry.get().strip()

        if not all([host, db_name, user, password]):
            messagebox.showerror("Validation Error", "All fields must be filled out!", parent=env_window)
            return

        try:
            with open(".env", "w", encoding="utf-8") as f:
                f.write(f"POSTGRES_HOST={host}\n")
                f.write(f"POSTGRES_DB={db_name}\n")
                f.write(f"POSTGRES_USER={user}\n")
                f.write(f"POSTGRES_PASSWORD={password}\n")
                
            messagebox.showinfo("Success", ".env file saved successfully!", parent=env_window)
            env_window.destroy()
            
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to save .env file:\n{e}", parent=env_window)

    save_btn = tk.Button(
        env_window, text="Save Configuration", command=save_env, bg="#007acc", fg="white", font=("Arial", 10, "bold"), activebackground="#005999", activeforeground="white", bd=0, cursor="hand2", pady=8
    )
    save_btn.pack(pady=(20, 0), fill="x", padx=40)


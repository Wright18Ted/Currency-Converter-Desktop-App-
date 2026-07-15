import tkinter as tk

def upload_csv_to_db(parent_window):
    uploadCVS= tk.Toplevel(parent_window)
    uploadCVS.title("Upload CSV to Database")
    uploadCVS.geometry("850x600")
    uploadCVS.configure(bg="#1a1a1a")
    uploadCVS.resizable(False, False)

    title_label = tk.Label(uploadCVS, text="Upload CSV to Database", font=("Arial", 24, "bold"), bg="#1a1a1a", fg="white")
    title_label.pack(pady=(15, 5))

    developement_label = tk.Label(uploadCVS, text="This feature is currently in development.", font=("Arial", 10, "italic"), bg="#1a1a1a", fg="#FF0000")
    developement_label.pack(pady=(0, 15))
    
    log_subtitle = tk.Label(uploadCVS, text="Upload your conversion log CSV to the database for analysis.", font=("Arial", 10, "italic"), bg="#1a1a1a", fg="#666666")
    log_subtitle.pack(pady=(0, 15))

    upload_terminal_label = tk.Label(uploadCVS, text="Upload Terminal:", font=("Arial", 12, "bold"), bg="#1a1a1a", fg="white")
    upload_terminal_label.pack(pady=(0, 5))
    terminal_box = tk.Text(uploadCVS, height=25, width=75, bg="#1e1e1e", fg="white", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#2c2c2e", highlightcolor="#0a84ff")
    terminal_box.pack(pady=(0, 15), padx=15)
    terminal_box.config(state="disabled") #Stops the user from typing in the terminal box. It is only for displaying messages.

    create_env_file_button = tk.Button(uploadCVS, text="Create .env File", font=("Arial", 12, "bold"), bg="#d99910", fg="white", cursor="hand2", padx=20, pady=10)
    create_env_file_button.pack(pady=(0, 15))

    upload_button = tk.Button(uploadCVS, text="Upload CSV To Local Database", font=("Arial", 12, "bold"), bg="#13dd17", fg="white", cursor="hand2", padx=20, pady=10)
    upload_button.pack(pady=(0, 15))





    




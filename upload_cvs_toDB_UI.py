import tkinter as tk

import create_env_file
from upload_cvs_toDB_Connection import load_CSV_To_Local_DB
from upload_csv_toDB_InfoPage import info_page_for_CSV_Upload

def upload_csv_to_db(parent_window):
    uploadCVS= tk.Toplevel(parent_window)
    uploadCVS.title("Upload CSV to Database")
    uploadCVS.geometry("850x700")
    uploadCVS.configure(bg="#1a1a1a")
    uploadCVS.resizable(True, True)

    title_label = tk.Label(uploadCVS, text="Upload CSV to Database", font=("Arial", 24, "bold"), bg="#1a1a1a", fg="white")
    title_label.pack(pady=(15, 5))

    developement_label = tk.Label(uploadCVS, text="This feature is currently in development.", font=("Arial", 10, "italic"), bg="#1a1a1a", fg="#FF0000")
    developement_label.pack(pady=(0, 15))
    
    log_subtitle = tk.Label(uploadCVS, text="Upload your conversion log CSV to the database for analysis.", font=("Arial", 10, "italic"), bg="#1a1a1a", fg="#666666")
    log_subtitle.pack(pady=(0, 15))

    information_button = tk.Button(uploadCVS, text="Information", font=("Arial", 12, "bold"), bg="#0288ff", fg="white", cursor="hand2", padx=20, pady=10)
    information_button.pack(anchor="e", padx=(0, 20))
    information_button.bind("<Button-1>", lambda event: info_page_for_CSV_Upload(parent_window))

    upload_terminal_label = tk.Label(uploadCVS, text="Upload Terminal:", font=("Arial", 12, "bold"), bg="#1a1a1a", fg="white")
    upload_terminal_label.pack(pady=(0, 5))
    terminal_box = tk.Text(uploadCVS, height=25, width=75, bg="#1e1e1e", fg="white", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#2c2c2e", highlightcolor="#0a84ff")
    terminal_box.pack(pady=(0, 15), padx=15)
    terminal_box.config(state="disabled") #Stops the user from typing in the terminal box. It is only for displaying messages.

    create_env_file_button = tk.Button(uploadCVS, text="Create .env File", font=("Arial", 12, "bold"), bg="#d99910", fg="white", cursor="hand2", padx=20, pady=10)
    create_env_file_button.pack(pady=(0, 15))
    create_env_file_button.bind("<Button-1>", lambda event: create_env_file.create_env_file(uploadCVS))  # Calls the create_env_file function when clicked.

    #delete .env file button
    delete_env_file_button = tk.Button(uploadCVS, text="Delete .env File", font=("Arial", 12, "bold"), bg="#FF0000", fg="white", cursor="hand2", padx=20, pady=10)
    delete_env_file_button.pack(pady=(0, 15))
    delete_env_file_button.bind("<Button-1>", lambda event: create_env_file.delete_env_file()) # Calls the delete_env_file function when clicked.
   

    upload_button = tk.Button(uploadCVS, text="Upload CSV To Local Database", font=("Arial", 12, "bold"), bg="#13dd17", fg="white", cursor="hand2", padx=20, pady=10)
    upload_button.pack(pady=(0, 15))
    upload_button.bind("<Button-1>", lambda event: load_CSV_To_Local_DB())  # Calls the upload_csv_to_db function when clicked.
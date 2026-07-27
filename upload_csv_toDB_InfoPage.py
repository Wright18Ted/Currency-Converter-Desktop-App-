import tkinter as tk

def info_page_for_CSV_Upload(parent_window):
    info_upload = tk.Toplevel(parent_window)
    info_upload.title("Upload CSV To Database Info")
    info_upload.geometry("850x700")
    info_upload.configure(bg="#1a1a1a")
    info_upload.resizable(True, True)

    
    title_label = tk.Label(info_upload, text="Upload CSV to Database Information Page", font=("Helvetica", 18, "bold"), fg="#ffffff", bg="#1a1a1a")
    title_label.pack(pady=30)

    subtitle_info_page = tk.Label(info_upload, text="Information & Upload Guidelines for uploading the cvs to Local DB", font=("Helvetica", 12), fg="#a0a0a0", bg="#1a1a1a")
    subtitle_info_page.pack(pady=(5, 0))

    #What you need? - question1 
    q1_label = tk.Label(info_upload, text="Question 1: How the upload Works?", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q1_label.pack(fill="x", padx=40, pady=(10, 5))

    q1_answer_label = tk.Label(info_upload, text="The script reads your selected CSV file, validates row entries, and parses the columns to push transaction records directly into your local database table.", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q1_answer_label.pack(fill="x", padx = 40, pady =(10,5 ))

    #What You Need Question 2 

    q2_label = tk.Label(info_upload, text="Question 2: What You need?", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q2_label.pack(fill="x", padx=40, pady=(10, 5))
    
    q2_answer_label = tk.Label(info_upload, text="A properly structured .csv file, a configured .env file with your database credentials, and a local PostgreSQL database running in Docker.", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q2_answer_label.pack(fill="x", padx = 40, pady =(10,5 ))

    #Question3 - Is there a maximum file size or row limit? 
    q3_label = tk.Label(info_upload, text="Question 3: Is there a maximum file size or row limit?", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q3_label.pack(fill="x", padx=40, pady=(10, 5))
        
    q3_answer_label = tk.Label(info_upload, text="There is no strict row limit, but keeping files under 10MB or 5,000 rows per batch ensures fast database batch inserts without UI lag", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q3_answer_label.pack(fill="x", padx = 40, pady =(10,5 ))

    #Question 4 - Where can I see if my upload succeeded or failed?
    q4_label = tk.Label(info_upload, text="Question 4: Where can I see if my upload succeeded or failed?", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q4_label.pack(fill="x", padx=40, pady=(10, 5))
            
    q4_answer_label = tk.Label(info_upload, text="Check the Upload Terminal box on the main upload window for real-time connection status, success notifications, or error logs.", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q4_answer_label.pack(fill="x", padx = 40, pady =(10,5 ))

    #Question 5 - What is a .env file and How do i ensure it stays Private?
    q5_label = tk.Label(info_upload, text="Question 5: What is a .env file and How do i ensure it stays Private?", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q5_label.pack(fill="x", padx=40, pady=(10, 5))
                
    q5_answer_label = tk.Label(info_upload, text="Use the built-in app function to generate the .env file when configuring your setup, then delete it immediately after use so it never stays unattended in local storage.", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#1a1a1a",anchor="w")
    q5_answer_label.pack(fill="x", padx = 40, pady =(10,5 ))







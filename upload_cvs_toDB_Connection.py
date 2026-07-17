import psycopg2
import os
import csv
from dotenv import load_dotenv
from tkinter import messagebox

def load_CSV_To_Local_DB():
    load_dotenv(override=True)
    host_name = os.environ.get("POSTGRES_HOST")
    database_name = os.environ.get("POSTGRES_DB")
    user_name = os.environ.get("POSTGRES_USER")
    user_password = os.environ.get("POSTGRES_PASSWORD")

    csv_filename = "conversion_log.csv" 

    if not os.path.exists(csv_filename):
        print(f"Error: Local file '{csv_filename}' not found.")
        messagebox.showerror("File Error", f"Could not find '{csv_filename}' in your project folder.")
        return

    try:
        print('Opening connection...')
        conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password} connect_timeout=3'
        
        with psycopg2.connect(conn_string) as connection:
            print('Opening cursor...')
            with connection.cursor() as cursor:

                print('Creating tables...')
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS conversion_log (
                    id SERIAL PRIMARY KEY,
                    from_currency VARCHAR(10) NOT NULL,
                    to_currency VARCHAR(10) NOT NULL,
                    amount NUMERIC NOT NULL,
                    result NUMERIC NOT NULL,
                    conversion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                '''
                cursor.execute(create_table_query)
                print('Table "conversion_log" verified/created successfully.')

                print(f'Reading data from {csv_filename}...')
                with open(csv_filename, mode='r', encoding='utf-8-sig') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    
                    insert_query = '''
                    INSERT INTO conversion_log (from_currency, to_currency, amount, result, conversion_time)
                    VALUES (%s, %s, %s, %s, %s);
                    '''
                    
                    inserted_count = 0
                    for row in csv_reader:
                        cursor.execute(insert_query, (
                            row['from Currency'],
                            row['to Currency'],
                            float(row['Amount']),
                            float(row['Result']),
                            row.get('Timestamp') if row.get('Timestamp') else None
                        ))
                        inserted_count += 1
                
                connection.commit()
                print(f'Successfully loaded {inserted_count} records!')
                messagebox.showinfo("Success", f"Successfully uploaded {inserted_count} records to the database!")

    except Exception as ex:
        print('Failed to upload:', ex)
        messagebox.showerror("Database Error", f"An error occurred:\n{ex}")
    
    finally:
        print('Connection closed.')
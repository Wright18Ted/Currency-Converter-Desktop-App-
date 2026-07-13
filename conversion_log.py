import csv
import os
import time 

csv_file_path = 'conversion_log.csv'

def log_conversion(from_curr, to_curr, amount, result):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, from_curr, to_curr, amount, result])

def read_last_entries(limit=15):
    import os
    if not os.path.exists(csv_file_path):
        return "No local history found.\nRun a conversion to append data."
        
    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            lines = list(reader)
            if len(lines) <= 1:  
                return "No local history found.\nRun a conversion to append data."
                
            data_rows = lines[-limit:]
            output = ""   
            for row in data_rows:
                time_str = row[0].split(" ")[1] if " " in row[0] else row[0]
                output += f"{time_str:<12} | {row[1]:<4} -> {row[2]:<4} | {row[3]:<8} | {row[4]:<8}\n"

            return output
    except Exception as e:
        return f"Error reading log pipeline: {e}"
    
def clear_cvs():
    if os.path.exists(csv_file_path):
        try:
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "From Currency", "To Currency", "Amount", "Result"])
            return "Conversion log cleared successfully."
        except Exception as e:
            return f"Error clearing log pipeline: {e}"
    else:
        return "No log file found to clear."
 
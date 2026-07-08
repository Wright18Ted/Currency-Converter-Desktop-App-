import csv
import time 

def log_conversion(from_curr, to_curr, amount, result):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open('conversion_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, from_curr, to_curr, amount, result])

   

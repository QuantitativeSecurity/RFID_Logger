import datetime

def log_rfid_info(rfid_data):
    # format the current date and time
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # log the information
    with open("rfid_logs.txt", "a") as f:
        f.write(f"{current_time}: {rfid_data}\n")
        print(f"RFID information logged at {current_time}: {rfid_data}")

while True:
    # wait for an RFID chip to be used
    rfid_data = input("Please scan an RFID chip: ")
    log_rfid_info(rfid_data)

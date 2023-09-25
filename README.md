RFID Logger

This script logs RFID data along with the current date and time to a file named rfid_logs.txt.
Description

Whenever an RFID chip is scanned, the user is prompted to input the RFID data. This data, along with the current date and time, is then appended to the rfid_logs.txt file. The script will continue to prompt the user for RFID data until it is manually stopped.
Requirements

    Python 3.x

Usage

    Run the script:

    bash

    python3 rfid_logger.py

    Scan an RFID chip:
    When prompted with "Please scan an RFID chip:", input the RFID data and press Enter.

    View the log:
    The RFID data, along with the current date and time, will be appended to the rfid_logs.txt file. A confirmation message will also be printed to the console.

    Stop the script:
    To stop the script, press Ctrl + C.

Note

This script simulates the logging of RFID data by prompting the user for input. In a real-world scenario, you might integrate this with an RFID reader to automatically read and log the RFID data.

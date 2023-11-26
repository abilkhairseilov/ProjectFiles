import os
import sys
import datetime
import threading

class LoggerThread(threading.Thread):
    def __init__(self, filename="logs.txt"):
        super(LoggerThread, self).__init__()
        self.filename = filename
        self.setup_logger()

    def setup_logger(self):
        if os.path.exists(self.filename):
            filemode = "a"
        else:
            filemode = "w"

        self.log_file = open(self.filename, filemode)
        sys.stdout = self.log_file

    def log_message(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_file.write(log_entry)
        print(log_entry, end='')  # Print to console as well if needed

    def run(self):
        while True:
            try:
                message = input()  # Read input from the console
                if message.lower() == 'exit':
                    break
                self.log_message(message)
            except EOFError:
                break

        self.log_file.close()
        sys.stdout = sys.__stdout__  # Restore original stdout

# Start the logger thread when this module is run
if __name__ == "__main__":
    logger_thread = LoggerThread()
    logger_thread.start()
    logger_thread.join()

class LogFile:
    def __init__(self, filename="log.txt"):
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as file:
            file.write(message + "\n")
    
    
    #optional part  - log clear function
    # def clear_log(self): 
    #     with open(self.filename, "w") as file:
    #         file.write("Log started:\n")

if __name__ == "__main__":
    log = LogFile()
    log_filename = "log.txt"

    # Reading the log file 
    with open(log_filename, "r") as log_file:
        log_content = log_file.read()

    print("Log File Content:")
    print(log_content)

    # Log process
    log.clear_log()  #Clear log file ( optional )
    log.log("Starting the scenario...")
    log.log("Login step completed.")
    log.log("Navigating to some page...")
    log.log("Scenario completed.")


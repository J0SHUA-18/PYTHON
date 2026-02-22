import os

log_path = input("Enter path of the server log file (.txt): ")

if os.path.exists(log_path) == False:
    print("Error: The log file path does not exist.")

elif log_path.endswith(".txt") == False:
    print("Error: The file is not a .txt file.")

else:
    if os.path.getsize(log_path) == 0:
        print("Error: The file is empty.")

    else:
        destination_folder = input("Enter destination folder path for summary report: ")

        if os.path.exists(destination_folder) == False:
            print("Error: Destination folder does not exist.")

        else:
            total_logs = 0
            info_count = 0
            warning_count = 0
            error_count = 0
            critical_count = 0

            file = open(log_path, "r")

            for line in file:
                total_logs += 1

                if "INFO" in line:
                    info_count += 1

                elif "WARNING" in line:
                    warning_count += 1

                elif "ERROR" in line:
                    error_count += 1

                elif "CRITICAL" in line:
                    critical_count += 1

            file.close()

            summary_text = ""
            summary_text += "LOG SUMMARY REPORT\n"
            summary_text += "---------------------\n"
            summary_text += "Total log entries: " + str(total_logs) + "\n"
            summary_text += "Total INFO messages: " + str(info_count) + "\n"
            summary_text += "Total WARNING messages: " + str(warning_count) + "\n"
            summary_text += "Total ERROR messages: " + str(error_count) + "\n"
            summary_text += "Total CRITICAL messages: " + str(critical_count) + "\n"

            summary_path = os.path.join(destination_folder, "log_summary.txt")
            summary_file = open(summary_path, "w")
            summary_file.write(summary_text)
            summary_file.close()

            print("\nProcessing Complete!\n")
            print(summary_text)
            print("Summary file saved at:", summary_path)
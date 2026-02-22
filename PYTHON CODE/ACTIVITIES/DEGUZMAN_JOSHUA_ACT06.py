import os

# Ask for folder path
folder_path = input("Enter folder path to analyze: ")

# Check if exist
if os.path.exists(folder_path) == False:
    print("Error: The folder path does not exist.")

# Location
elif os.path.isdir(folder_path) == False:
    print("Error: The path provided is not a directory.")

else:
    files = os.listdir(folder_path)

    # display if empty
    if len(files) == 0:
        print("Error: The folder is empty.")

    else:
        file_types = {}   # dictionary to store file types

        for file in files:

            full_path = os.path.join(folder_path, file)

            if os.path.isfile(full_path):

                parts = file.split(".")
                
                if len(parts) > 1:
                    extension = "." + parts[-1]
                else:
                    extension = "No Extension"

                if extension in file_types:
                    file_types[extension].append(file)
                else:
                    file_types[extension] = [file]

        print("\nFile Analysis Result:\n")

        for extension in file_types:
            print("File Type:", extension)

            for file in file_types[extension]:
                print("  -", file)

            print("Total files:", len(file_types[extension]))
            print()
import os
import shutil

downloads_path = input("Enter Downloads folder path: ")


if os.path.exists(downloads_path) == False:
    print("Error: The Downloads path does not exist.")

elif os.path.isdir(downloads_path) == False:
    print("Error: The path is not a directory.")

else:
    destination_path = input("Enter destination folder path (Press Enter to use Downloads folder): ")

    if destination_path == "":
        destination_path = downloads_path

    if os.path.exists(destination_path) == False:
        print("Error: Destination path does not exist.")

    else:
        files = os.listdir(downloads_path)

        if len(files) == 0:
            print("Error: There are no files to process.")

        else:
            images_folder = os.path.join(destination_path, "Images")
            documents_folder = os.path.join(destination_path, "Documents")

            if os.path.exists(images_folder) == False:
                os.mkdir(images_folder)

            if os.path.exists(documents_folder) == False:
                os.mkdir(documents_folder)

            image_types = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]
            document_types = [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"]

            total_files = 0
            image_count = 0
            document_count = 0
            skipped_count = 0

            for file in files:

                full_path = os.path.join(downloads_path, file)

                if os.path.isfile(full_path):

                    total_files += 1

                    parts = file.split(".")

                    if len(parts) > 1:
                        extension = "." + parts[-1].lower()
                    else:
                        extension = ""

                    if extension in image_types:
                        shutil.move(full_path, os.path.join(images_folder, file))
                        image_count += 1

                    elif extension in document_types:
                        shutil.move(full_path, os.path.join(documents_folder, file))
                        document_count += 1

                    else:
                        skipped_count += 1

            print("\nSummary:")
            print("Total files processed:", total_files)
            print("Image files moved:", image_count)
            print("Document files moved:", document_count)
            print("Files skipped:", skipped_count)
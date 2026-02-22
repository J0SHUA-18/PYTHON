
files = []
file_sizes = []

total_capacity = float(input("Enter The Disk Capacity (in MB or GB): "))
total_used = 0

while True:

    if total_used >= total_capacity:
        print("\nDisk is already FULL!.")
        break

    print("\n1. Add File")
    print("2. Stop")
    choice = input("Choose option: ")

    if choice == "1":
        file_name = input("Enter File Name: ")
        file_size = float(input("Enter File Size: "))

        if file_size > (total_capacity - total_used):
            print("WARNING: File size is larger than remaining space!")
        else:
            files.append(file_name)
            file_sizes.append(file_size)
            total_used += file_size
            print("File added successfully.")

    elif choice == "2":
        print("Stopping file input...")
        break

    else:
        print("Invalid choice. Try again.")

remaining_space = total_capacity - total_used
usage_percent = (total_used / total_capacity) * 100

print("\n ------DISK SUMMARY------")
print("Total Disk Capacity:", total_capacity)
print("Total Used Space:", total_used)
print("Remaining Space:", remaining_space)
print("Disk Usage Percentage: {:.2f}%".format(usage_percent))

print("\nFiles Stored:")
for i in range(len(files)):
    print("-", files[i], "(", file_sizes[i], ")")

# Disk Status
if usage_percent < 80:
    print("\nDisk Status: HEALTHY")
elif 80 <= usage_percent <= 94:
    print("\nDisk Status: WARNING LEVEL")
else:
    print("\nDisk Status: CRITICAL")
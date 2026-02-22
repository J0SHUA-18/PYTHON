import platform
import psutil
import os
import csv

def get_system_info():
    print("\n-------SYSTEM INFORMATION------")
    print("OS:", platform.system(), "\nOS Version:", platform.version(), "\nArchitecture:", platform.machine())
    cpu_freq = psutil.cpu_freq()
    print("\nCPU Cores:", psutil.cpu_count(logical=True), "\nCPU Frequency:", cpu_freq.current if cpu_freq else "Unavailable", "MHz")
    memory = psutil.virtual_memory()
    print("\nTotal Memory:", round(memory.total / (1024**3), 2), "GB", "\nAvailable Memory:", round(memory.available / (1024**3), 2), "GB")

def get_performance_metrics():
    print("\n-----PERFORMANCE METRICS-----")
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU Usage:", cpu_usage, "%")
    memory = psutil.virtual_memory()
    print("RAM Usage:", memory.percent, "%")
    return cpu_usage, memory.percent

def get_disk_usage():
    print("\n-----DISK USAGE-----")
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"\nPartition: {partition.device}\n  Total: {round(usage.total / (1024**3),2)} GB\n  Used: {round(usage.used / (1024**3),2)} GB\n  Usage: {usage.percent}%")
        except PermissionError:
            print(f"Permission denied for {partition.device}")

def health_summary(cpu, ram):
    print("\n-----HEALTH SUMMARY-----")
    status = "Good"
    if cpu > 80 or ram > 80: status = "Critical"
    elif cpu > 60 or ram > 60: status = "Moderate"
    print("System Health Status:", status)
    if cpu > 80: print("⚠ Warning: High CPU usage!")
    if ram > 80: print("⚠ Warning: High Memory usage!")

def generate_report(cpu, ram):
    try:
        with open("system_report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Metric", "Value"])
            writer.writerow(["CPU Usage (%)", cpu])
            writer.writerow(["RAM Usage (%)", ram])
        print("\nReport saved as system_report.csv")
    except Exception as e: print("Error creating report:", e)

def menu():
    while True:
        print("\n===== SYSTEM HEALTH CHECK MENU =====\n1. View System Information\n2. View Performance Metrics\n3. View Disk Usage\n4. Full System Check\n5. Exit")
        choice = input("Select an option (1-5): ")
        if choice == "1": get_system_info()
        elif choice == "2": cpu, ram = get_performance_metrics(); health_summary(cpu, ram)
        elif choice == "3": get_disk_usage()
        elif choice == "4": get_system_info(); cpu, ram = get_performance_metrics(); get_disk_usage(); health_summary(cpu, ram); generate_report(cpu, ram)
        elif choice == "5": print("Exiting program..."); break
        else: print("Invalid selection. Please choose 1-5.")

if __name__ == "__main__":
    try: menu()
    except Exception as e: print("Unexpected error occurred:", e)
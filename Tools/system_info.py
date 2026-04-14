import psutil
import sys

def main():
    menu = """
    CPU - [1]
    RAM - [2]
    All Information - [3]
    """
    print(menu)
    try:
        user_choice = int(input("Enter a number associated with following options: "))
    except ValueError:
        sys.exit("Invalid Option")
    if user_choice == 1:
        print(f"{cpu_info()}%")
    elif user_choice == 2:
        usage_percent,used_memory = ram_info()
        print(f"RAM: {usage_percent}")
        print(f"Used RAM: {used_memory}")
    elif user_choice == 3:
        usage_percent,used_memory = ram_info()
        print(f"CPU: {cpu_info()}")
        print(f"RAM: {usage_percent}")
        print(f"Used RAM: {used_memory}")
    else:
        print("Invalid Choice.")

def cpu_info():
    return psutil.cpu_percent(interval=1)

def ram_info():
    mem = psutil.virtual_memory()
    stats = []
    memory_usage_percent = mem.percent
    total_memory = f"{mem.total / (1024**3):.2f}"
    used_memory = f"{mem.used / (1024**3):.2f}"
    stats.append(f"{memory_usage_percent}%")
    stats.append(f"{used_memory} GB / {total_memory} GB")
    return stats

if __name__=="__main__":
    main()
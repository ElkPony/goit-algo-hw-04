import sys
import os
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def print_directory_tree(directory, prefix="    "):
    try:
        path = Path(directory).resolve()
        if not path.exists() or not path.is_dir():
            print(Fore.RED + "Помилка: Вказаний шлях не є директорією або не існує.")
            return
        
        for item in path.iterdir():
            if item.is_dir():
                print(Fore.BLUE + f"{prefix} {item.name}/")
                print_directory_tree(item, prefix + "  ")
            else:
                print(Fore.GREEN + f"{prefix} {item.name}")

    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Використання: python script.py <шлях_до_директорії>")
    else:
        print_directory_tree(sys.argv[1])

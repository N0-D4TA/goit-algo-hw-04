import sys
from pathlib import Path
from colorama import Fore, init


init(autoreset=True)

def print_directory_structure(root_dir: Path, prefix=""):
    try:
        # Getting list of contents
        structure = list(root_dir.iterdir())
    except PermissionError:
        print(Fore.RED + "Permission denied: " + str(root_dir))
        return
    except FileNotFoundError:
        print(Fore.RED + "Directory not found: " + str(root_dir))
        return

    for i, subdir in enumerate(structure):
        is_last = i == len(structure) - 1

        # Forming lines output
        connector = "└── " if is_last else "├── "
        next_prefix = "    " if is_last else "│   "

        # Marking directories and files different
        if subdir.is_dir():
            print(prefix + connector + Fore.YELLOW + subdir.name)
            # Calling recursive for contents
            print_directory_structure(subdir, prefix + next_prefix)
        else:
            print(prefix + connector + Fore.MAGENTA + subdir.name)

if __name__ == "__main__":
    # Check for right args, excluding IndexError
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python dir_structure.py <directory_path>")
        sys.exit(1)

    # Getting path from 
    dir_path = Path(sys.argv[1])

    # Check if not file or smth
    if not dir_path.is_dir():
        print(Fore.RED + f"Error: {dir_path} is not a valid directory.")
        sys.exit(1)

    # Structure output
    print(Fore.YELLOW + f"Directory structure of '{dir_path}':")
    print_directory_structure(dir_path)

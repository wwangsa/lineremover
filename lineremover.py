import sys
import os


def delete_multiple_lines(path, file_name, line_numbers):
    """Removing specific lines from a text file and save it under new file name"""

    try:
        orig_file = os.path.join(path, file_name)
        mod_file = os.path.join(path + "mods", "mod_" + file_name)

        if os.path.exists(mod_file):
            try:
                os.remove(mod_file)
            except:
                print(f"{path}: {mod_file} does not exist")

        with open(orig_file, 'r', encoding='utf-8') as source_file, open(mod_file, 'w',
                                                                         encoding='utf-8') as target_file:
            for line_num, line in enumerate(source_file.readlines(), start=1):
                if line_num not in line_numbers:
                    target_file.write(line)

        print(f"{file_name} ==> Created")
    except:
        print(f"{file_name} ==> Failed")


def main():
    # allowing the flexibility of the program to run
    if len(sys.argv) != 3:
        print(f"This script only takes 2 arguments:")
        print(f"1. Directory path where the files are enclosed by double quotes")
        print(
            f"2. List of line number(s) to be removed separated by comma when more than one enclosed by double quotes")
        sys.exit(0)

    # Check the directory path
    try:
        dir_path = os.path.join(sys.argv[1], '')
    except:
        print("The directory path is not in the correct form: " + dir_path)
        raise

    if not os.path.isdir(dir_path):
        print("The directory path on the 1st parameter doesn't exist")
        sys.exit(0)
    # Convert second argument into tuple
    try:
        line_numbers = tuple(map(int, sys.argv[2].replace("\"", "").split(',')))
    except:
        print("Could not convert second argument as a tuple.")
        raise

    # Create subdirectory called mods to store the results
    if not os.path.isdir(os.path.join(dir_path, "mods")):
        os.makedirs(os.path.join(dir_path, "mods"))

    print("The following file(s) has been modified and saved under mods subfolder: ")
    for file in os.listdir(dir_path):
        # Excludes mods subfolder
        if file.lower() != 'mods':
            delete_multiple_lines(dir_path, file, line_numbers)

    print(
        f"Line {str(line_numbers)} have been removed from above files and the modified version is saved under mods subfolder")


if __name__ == "__main__":
    main()
    sys.exit(0)

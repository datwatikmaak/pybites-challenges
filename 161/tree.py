import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    total_dirs = 0
    total_files = 0

    for root, dirs, files in os.walk(directory):
        total_dirs += len(dirs)
        total_files += len(files)

    print(f"Aantal dirs: {total_dirs}")
    print(f"Aantal files: {total_files}")


count_dirs_and_files()

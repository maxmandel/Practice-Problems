import os

def print_dir_contents(directory_path):
    # Initialize counters and lists
    file_count = 0
    subdirectory_count = 0
    files = []
    subdirectories = []

    # Iterate through the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        # Check if it's a file
        if os.path.isfile(item_path):
            file_count += 1
            files.append(item)

        # Check if it's a subdirectory
        elif os.path.isdir(item_path):
            subdirectory_count += 1
            subdirectories.append(item)

    print(f"Contents of directory {directory_path}")
    
    if file_count > 0:
        print(f"{file_count} files:")
        for file in sorted(files):
            print(f"    {file}")

    if subdirectory_count > 0:
        print(f"{subdirectory_count} subdirectories:")
        for subdirectory in sorted(subdirectories):
            print(f"   {subdirectory}")

# Example usage
print_dir_contents('/Users/maxmandel/max_cs_practice')
import os
import re

def count_lines(directory):
    total_lines = 0
    readme_pattern = re.compile(r'readme.*', re.IGNORECASE)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if readme_pattern.search(file):
                # Skip README files
                continue
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    total_lines += len(lines)
            except (UnicodeDecodeError, IsADirectoryError):
                # Ignore files that cannot be decoded or are directories
                pass
    return total_lines

if __name__ == "__main__":
    current_dir = os.getcwd()
    total_lines = count_lines(current_dir+"/brain")
    print(f"Total lines of code in the repository: {total_lines}")
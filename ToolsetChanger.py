import os
import re
import sys

def replace_platform_toolset(foldername, filename, new_toolset):
    filepath = os.path.join(foldername, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    content = re.sub(r'(<PlatformToolset>)[^<]*(</PlatformToolset>)',
                     r'\1' + new_toolset + r'\2', content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Replaced PlatformToolset with {new_toolset} in {filename}")

def scan_folder(path, new_toolset):
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.vcxproj'):
                replace_platform_toolset(foldername, filename, new_toolset)

def main():
    if len(sys.argv) < 3:
        print('Usage: python ToolsetChanger.py <directory> <new_toolset>')
        return

    path = sys.argv[1]
    new_toolset = sys.argv[2]
    scan_folder(path, new_toolset)

if __name__ == '__main__':
    main()

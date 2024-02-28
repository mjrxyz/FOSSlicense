import re
import os

def detect_licenses(file_path):
    mit_pattern = re.compile(r'MIT License')
    gpl_pattern = re.compile(r'GNU General Public License')
    apache_pattern = re.compile(r'Apache License')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    licenses = []
    if mit_pattern.search(content):
        licenses.append('MIT License')
    if gpl_pattern.search(content):
        licenses.append('GNU General Public License')
    if apache_pattern.search(content):
        licenses.append('Apache License')

    return licenses

def analyze_directory(directory_path):
    licenses_count = {}

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            detected_licenses = detect_licenses(file_path)

            if detected_licenses:
                licenses_count[file_path] = detected_licenses

    return licenses_count

directory_path = '/path/to/your/source/code'
result = analyze_directory(directory_path)


for file_path, licenses in result.items():
    print(f'{file_path}: {", ".join(licenses)}')

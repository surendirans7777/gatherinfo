from urllib.parse import urlparse
import os
import sys

# Check if the filename was provided
if len(sys.argv) < 2:
    print("Usage: python script.py <filename-list>")
    sys.exit(1)

input_file = sys.argv[1]

# Set to store unique extensions
unique_extensions = set()

# Read URLs and extract extensions
with open(input_file, 'r') as file:
    urls = file.readlines()
    for url in urls:
        url = url.strip()  # Remove any surrounding whitespace
        if url:  # Skip empty lines
            parsed_url = urlparse(url)
            path = parsed_url.path
            ext = os.path.splitext(path)[1]  # Extract file extension
            if ext:
                unique_extensions.add(ext.lower())  # Store extension in lowercase for uniformity

# Print unique extensions to the terminal
print("Unique file extensions in URLs:")
for ext in sorted(unique_extensions):
    print(ext)

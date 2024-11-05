from urllib.parse import urlparse
import sys

# Check if the filename was provided
if len(sys.argv) < 2:
    print("Usage: python script.py <filename-list>")
    sys.exit(1)

input_file = sys.argv[1]

# Set to store unique paths
unique_paths = set()

# Read URLs and extract paths
with open(input_file, 'r') as file:
    urls = file.readlines()
    for url in urls:
        url = url.strip()  # Remove any surrounding whitespace
        if url:  # Skip empty lines
            parsed_url = urlparse(url)
            path = parsed_url.path
            if path:
                unique_paths.add(path)

# Print unique paths to the terminal
print("Unique paths from URLs:")
for path in sorted(unique_paths):
    print(path)

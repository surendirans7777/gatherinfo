import tldextract
import sys

# Check if the filename was provided
if len(sys.argv) < 2:
    print("Usage: python script.py <filename-list>")
    sys.exit(1)

input_file = sys.argv[1]

# Set to store unique domains and subdomains
unique_domains = set()

# Read URLs and extract domains
with open(input_file, 'r') as file:
    urls = file.readlines()
    for url in urls:
        url = url.strip()  # Remove any surrounding whitespace
        if url:  # Skip empty lines
            extracted = tldextract.extract(url)
            # Combine subdomain and domain for output
            if extracted.subdomain:
                full_domain = f"{extracted.subdomain}.{extracted.domain}.{extracted.suffix}"
            else:
                full_domain = f"{extracted.domain}.{extracted.suffix}"
            unique_domains.add(full_domain)

# Print unique domains and subdomains to the terminal
print("Unique domains and subdomains:")
for domain in sorted(unique_domains):
    print(domain)

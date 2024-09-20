import re
import os

def clean_wildcard_subdomains(directory):
    #match "*.example.com" wildcards
    pattern = r'\*\.([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
  
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
          
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Search for the pattern and replace it
            updated_content = re.sub(pattern, r'\1', content)
            
            # If changes, write the updated content back to the file
            if content != updated_content:
                with open(file_path, 'w') as f:
                    f.write(updated_content)
                print(f"Updated: {file_path}")


if __name__ == "__main__":
    directory_to_search = "path/to/your/directory"
    clean_wildcard_subdomains(directory_to_search)

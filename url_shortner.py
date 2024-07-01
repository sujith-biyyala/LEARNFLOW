import string
import random

# Dictionary to store the URL mappings
url_mapping = {}

# Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

# Function to shorten a URL
def shorten_url(long_url):
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return short_url

# Function to retrieve the original URL from the short URL
def get_long_url(short_url):
    return url_mapping.get(short_url)

# Main function to manage user interactions
def main():
    while True:
        action = input("Select an action ([1]shorten URL,[2]retrieve URL, [3]exit): ").strip().lower()
        if action == 's':
            long_url = input("Please enter the URL to shorten: ").strip()
            short_url = shorten_url(long_url)
            print(f"The shortened URL is: {short_url}")
        elif action == 'l':
            short_url = input("Please enter the shortened URL: ").strip()
            long_url = get_long_url(short_url)
            if long_url:
                print(f"The original URL is: {long_url}")
            else:
                print("The provided shortened URL was not found in our records.")
        elif action == 'e':
            print("Exiting the URL shortener program. Goodbye!")
            break
        else:
            print("Invalid action. Please choose 's' to shorten a URL, 'l' to retrieve an original URL, or 'e' to exit.")

if _name_ == '_main_':
    main()

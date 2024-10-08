import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Directory where you want to save resources
save_directory = "website_resources"
os.makedirs(save_directory, exist_ok=True)

# Set up Chrome options and enable performance logging
chrome_options = Options()

# Enable performance logging
chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

# Initialize the Chrome driver with options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# The website you want to scrape
url = 'http://example.com'
driver.get(url)

# Allow the page to fully load
time.sleep(5)  # Adjust the wait time based on the complexity of the page

# Fetch the performance logs, which contain network requests
logs = driver.get_log('performance')

# Function to parse the logs and extract URLs of resources (images, CSS, JS, etc.)
def get_resource_urls(logs):
    urls = set()
    for log in logs:
        log_message = log['message']
        if 'Network.responseReceived' in log_message:
            # Try to extract the URL from the message
            try:
                url_start = log_message.find('url') + 6
                url_end = log_message.find('"', url_start)
                resource_url = log_message[url_start:url_end]
                
                # if any(resource_url.endswith(ext) for ext in ['.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.woff', '.woff2', '.ttf']):
                #     urls.add(resource_url)
            
                urls.add(resource_url)
            except:
                pass
    return urls

# Get the resource URLs
resource_urls = get_resource_urls(logs)

# Function to download the resources
def download_resource(url, save_directory):
    try:
        response = requests.get(url)
        folders = url.split("/")[3:-1]
        print(folders)
        os.makedirs(os.path.join(save_directory, *folders), exist_ok=True)
        resource_name = url.split("/")[-1]
        resource_path = os.path.join(save_directory, *folders, resource_name)
        
        # Save the resource to the specified directory
        with open(resource_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {resource_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Download each resource
for resource_url in resource_urls:
    download_resource(resource_url, save_directory)

# Quit the Selenium browser instance
driver.quit()


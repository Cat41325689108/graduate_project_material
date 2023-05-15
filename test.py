# Import the libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of Bilibili
url = "https://www.bilibili.com/"

# Define a user-agent header
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

# Send a GET request to the URL and get the response with the header
response = requests.get(url, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response content as HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the elements with the class "info-box .title" in the HTML
    titles = soup.find_all(class_="info-box .title")

    # Loop through the titles and print their text
    for title in titles:
        print(title.text)
else:
    # Print an error message if the response is not successful
    print("Something went wrong!")
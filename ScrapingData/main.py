import requests
from bs4 import BeautifulSoup
file_path = "index.html"
res = requests.get('https://www.eggtrading.com/')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.body)
# with open(file_path, "w") as file:
#     file.write(res.text)


# ***************************

# import requests
# import os
# from bs4 import BeautifulSoup

# url = "https://www.eggtrading.com/"  # Replace with the URL of the website you want to scrape
# response = requests.get(url)
# html_content = response.text


# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(html_content, "html.parser")

# # Remove all <script> tags from the parsed soup
# for script in soup(["script"]):
#     script.extract()

# # Extract CSS links
# css_links = [link["href"] for link in soup.find_all("link", rel="stylesheet")]

# # Extract CSS content
# css_content = []
# for link in css_links:
#     css_url = link if link.startswith("http") else url + link
#     css_response = requests.get(css_url)
#     css_content.append(css_response.text)

# # Create directories if they don't exist
# os.makedirs("output", exist_ok=True)

# # Save HTML content to a file
# with open("output/extracted.html", "w", encoding="utf-8") as html_file:
#     html_file.write(str(soup))

# # Save each CSS content to separate files
# for idx, css in enumerate(css_content, start=1):
#     css_filename = f"output/extracted_css_{idx}.css"
#     with open(css_filename, "w", encoding="utf-8") as css_file:
#         css_file.write(css)

# print("HTML and CSS content saved to files.")
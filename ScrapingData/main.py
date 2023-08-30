import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import pprint
import csv

class HackerNewsSpider(scrapy.Spider):
    name = 'hacker_news'
    start_urls = ['https://news.ycombinator.com/news', 'https://news.ycombinator.com/news?p=2']

    def parse(self, response):
        links = response.css('.titleline > a')
        subtext = response.css('.subtext')

        hn = []
        for idx, item in enumerate(links):
            title = item.css('::text').get()
            href = item.css('::attr(href)').get()
            vote = subtext[idx].css('.score')
            if vote:
                points = int(vote.css('::text').get().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        pprint.pprint(hn)
        # Write the data to a CSV file
        with open('hacker_news.csv', 'w', newline='') as csvfile:
            fieldnames = ['Title', 'Link', 'Votes']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(hn)

        return self.sort_stories_by_votes(hn)

    def sort_stories_by_votes(self, hnlist):
        return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


process = CrawlerProcess()
process.crawl(HackerNewsSpider)
process.start()


# import requests
# from bs4 import BeautifulSoup
# import pprint

# res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
# soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')

# links = soup.select('.titleline > a') #heads up! .storylink changed to .titleline
# subtext = soup.select('.subtext')
# links2 = soup2.select('.titleline > a') #heads up! .storylink changed to .titleline
# subtext2 = soup2.select('.subtext')

# mega_links = links + links2
# mega_subtext = subtext + subtext2

# def sort_stories_by_votes(hnlist):
#   return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

# def create_custom_hn(links, subtext):
#   hn = []
#   for idx, item in enumerate(links):
#     title = item.getText()
#     href = item.get('href', None)
#     vote = subtext[idx].select('.score')
#     if len(vote):
#       points = int(vote[0].getText().replace(' points', ''))
#       if points > 99:
#         hn.append({'title': title, 'link': href, 'votes': points})
#   return sort_stories_by_votes(hn)
 
# pprint.pprint(create_custom_hn(mega_links, mega_subtext))




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
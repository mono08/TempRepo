from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article = soup.find_all(class_="titlelink", name="a")
article_texts = []
article_links = []
for article_tag in article:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_num = max(article_upvote)
largest_index = article_upvote.index(largest_num)

print(article_texts[largest_index])
print(article_links[largest_index])




# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.a)
# anchor = soup.find_all(name="a")
#
# for tag in anchor:
#     print(tag.get("href"))
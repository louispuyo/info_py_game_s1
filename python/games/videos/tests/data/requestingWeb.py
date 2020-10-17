import requests

pattern = "cat"
# response = requests.get(f"https://www.google.com/search?hl=fr&authuser=0&tbm=isch&sxsrf=ALeKk02uD4iC7g-cGABAV8kggqP9WXJ8Yw%3A1602422789919&source=hp&biw=1440&bih=646&ei=BQiDX5q_NczolwTlo52IAg&q=%C3%{pattern}&oq=&gs_lcp=CgNpbWcQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGCmpAFoAXAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img")

# file = open(f"python/games/videos/tests/img/{pattern}.png", "wb")
# file.write(response.content)
# file.close()



from bs4 import BeautifulSoup
import requests

url=f"https://www.google.com/search?hl=fr&authuser=0&tbm=isch&sxsrf=ALeKk02uD4iC7g-cGABAV8kggqP9WXJ8Yw%3A1602422789919&source=hp&biw=1440&bih=646&ei=BQiDX5q_NczolwTlo52IAg&q=%C3%{pattern}&oq=&gs_lcp=CgNpbWcQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGCmpAFoAXAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img"

# Make a GET request to fetch the raw HTML content
# html_content = requests.get(url).text

# # Parse the html content
# soup = BeautifulSoup(html_content, "lxml")
# print(soup.prettify()) # print the parsed data of html


# # response = requests.get(f"https://www.google.com/search?hl=fr&authuser=0&tbm=isch&sxsrf=ALeKk02uD4iC7g-cGABAV8kggqP9WXJ8Yw%3A1602422789919&source=hp&biw=1440&bih=646&ei=BQiDX5q_NczolwTlo52IAg&q=%C3%{pattern}&oq=&gs_lcp=CgNpbWcQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGCmpAFoAXAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img")
# html_doc = soup.prettify()

# soup = BeautifulSoup(html_doc)
    
# for p in soup.find_all('html'):
#      print(p.get("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img"))


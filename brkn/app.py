from flask import Flask ,render_template
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
 
@app.route("/")
def start():
    url = "https://www.geeksforgeeks.org"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Find all the links in the HTML
    links = soup.find_all('a')

    # Iterate through the links and display the status code and URL
    all_links = []
    broken_links = []

    
    for link in links:
        link_url= link.get('href') 
        all_links.append(link_url)
        try:
            response = requests.head(link_url)
            print(f"[ {response.status_code} ] -  {link_url}")
            if response.status_code != 200:
                broken_links.append(link_url)
        except:
            broken_links.append(link_url)
        
 ##   for link in all_links:
  #      response = requests.head(link_url)
   #     if response.status_code != 200:
    #        res = response.status_code
     #       broken_links.append(link + str(res))


  #  print(all_links)
    for link in broken_links:
        print(link)

    success = len(all_links)

    failure = len(broken_links)

 
    return render_template("index.html", all_links = all_links , broken_links = broken_links, success = success, failure = failure)
if __name__ == "__main__":
    app.run(debug = True)
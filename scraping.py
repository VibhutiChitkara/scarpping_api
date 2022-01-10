import requests
from bs4 import BeautifulSoup


def scrape_game(url):
    try:
        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')
    # Create top_items as empty list
        oldglory_toronto = []
    # Extract and store in top_items according to instructions on the left
        products = soup.findAll("div", {"class": "matchReportSubInt" })
        for product in products:
            name = product.findAll('p')[0].text.strip()
            events = product.findAll('small')[0].text.strip()
            oldglory_toronto.append({
                "player_name": name,
                "events": events,
                })
                
        keys = str(oldglory_toronto[0:23])
        if (len(list(keys)) > 0):
            return True, keys
        else:
            return False, None
    
    except:
        print("error")
        return False 
import requests
import deque
import threading
import concurrent.futures import ThreadPoolExecutor

url = "https://gogrok.io"
pages = []
que = deque([url])
lock = threading.Lock()
visited = set()

def fetch_data(url):
    response = requests.get(url)
    return response.text

def extract_links(url):
    pass
    return ["https://gogrok.io", "https://gogrok.io"]

def web_crawler():
    while que:
        curr = que.popleft()
        with lock:
            if curr in visited:
                continue

            visited.add(curr)
        
        try:
            html = fetch_data(url)
            links = extract_links(html)
            with lock:
                for link in links:
                    if link not in visited:
                        que.append(link)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(web_crawler) for _ in range(5)]

for future in futures:
    future.result()


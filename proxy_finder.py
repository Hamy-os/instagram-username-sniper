from urllib.request import urlopen
import urllib
import threading


def find_proxies():
    proxy_urls = [
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt", 
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
            ]
    urlopen = urllib.request.urlopen("https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list")
    proxies = urlopen.read().decode("utf-8").splitlines()
    with open("proxies/raw_proxies.txt", "w") as f:
        for proxy in proxies:
            if proxy.startswith("{"):
                proxy = proxy.split('"host": "')[1].split('"')[0] + ":" + proxy.split('"port": ')[1].split(",")[0]
                f.write(proxy + "\n")
        for url in proxy_urls:
            try:
                urlopen = urllib.request.urlopen(url)
                proxies = urlopen.read().decode("utf-8").splitlines()
                for proxy in proxies:
                    f.write(proxy + "\n")
            except:
                print(f"Error fetching proxies from {url}")
        total = list(set(proxies))
        print("Found", len(total), "proxies")
    f.close()
    return True

working = 0
broken = 0

def check_proxy(proxy):
    global working
    global broken
    try:
        proxy_handler = urllib.request.ProxyHandler({"http": proxy, "https": proxy})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [("User-agent", "Mozilla/5.0")]
        urllib.request.install_opener(opener)
        req = urllib.request.Request("https://www.google.com")
        urllib.request.urlopen(req, timeout=5)
        with open("proxies/working_proxies.txt", "a") as f:
            f.write(proxy + "\n")
        working += 1
    except:
        broken += 1
    print(f"Working: {working} | Broken: {broken} | Total: {working + broken}")

def check_proxies():
    with open("proxies/raw_proxies.txt", "r") as f:
        proxies = f.read().splitlines()
        for proxy in proxies:
            threading.Thread(target=check_proxy, args=(proxy,)).start()
    # wait till all threads are done
    if threading.active_count() < 1:
        print("Done")
        return True

if __name__ == "__main__":
    find_proxies()
    check_proxies()
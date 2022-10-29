# Social Media username Sniper

## Installation

```bash
git clone https://github.com/Hamy-os/instagram-username-sniper.git
cd instagram-username-sniper
npm install
python .\proxy_finder.py
node main.js
```

## How it works

1. Proxy Finder fetches proxies and parses them
2. Main.js makes an api request to checkmarks.com using a random proxy and depending on response it will either save the username or move on to the next one ( it also saves failed usernames )

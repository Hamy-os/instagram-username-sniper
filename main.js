import fetch from 'node-fetch';
import fs from 'fs';
import HttpsProxyAgent from 'https-proxy-agent';

const saveInfo = async (username, website, status) => {
    if (status == "1") {
        fs.appendFile(`working/working_${website}.txt`, `${username}\n`, function (err) {
            if (err) throw err;
            console.log('Saved for website: ' + website);
        });
    }
}

const getUsernameStatus = async (username) => {
    try {
        // use a random proxy from working_proxies.txt
        const proxy = fs.readFileSync('proxies/working_proxies.txt').toString().split("\n")
        const randomProxy = proxy[Math.floor(Math.random() * proxy.length)]
        const proxyUrl = `http://${randomProxy}`
        await fetch("https://checkmarks.com/", {
            "headers": {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.8",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "x-requested-with": "XMLHttpRequest",
                "cookie": "PHPSESSID=cd2hv4s3mp9drcbo03ungltva6",
                "Referer": "https://checkmarks.com/",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            },
            "body": `checkusername=true&username=${username}&token=vgyZWmBhj3`,
            "method": "POST",
            "agent": new HttpsProxyAgent(proxyUrl)
        })
        .then(res => res.json())
        .then(json => {
            json.usernames.forEach(website => {
                switch (website.website) {
                    case "instagram":
                    case "twitter":
                    case "facebook":
                    case "snapchat":
                        saveInfo(username, website.website, website.status);
                }})
        });
    } catch (err) {
        console.log(err);
        fs.appendFile('assets/failed.txt', `${username} \n`, (err) => {
            if (err) throw err;
        });
    }
}

const main = async () => {
    const usernames =   fs.readFileSync('assets/three.txt').toString().split("\r\n")
    for (let i = 0; i < usernames.length; i++) {
        await new Promise(r => setTimeout(r, 1000));
        console.log("Checking username: " + usernames[i]);
        getUsernameStatus(usernames[i]);
    }}

await main()
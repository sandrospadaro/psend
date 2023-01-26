import requests
import json
import argparse
import sys


def psend(keys, title, payload, url):
    service_url = "http://xdroid.net/api/message"

    for key in keys:
        response = requests.get(service_url, params={
                                "k": key, "t": title, "c": payload, "u": url})

        if response.status_code != 200:
            print("[-] Error sending notification with API Key " + key)
            print("[-] status code: " + response.status_code)
            return 1
        else:
            content = json.loads(response.content)
            if not content["success"] == "1":
                print("[-] Error sending notification with API Key " + key)
                print("[-] success: " + content["success"])
                print("[-] success: " + content["error"])
                return 2
            else:
                print("[+] Notification sent successfully with API Key " + key)
                print("[+] success: " + content["success"])
                print("[+] error: " + content["error"])
    return 0


def main():
    parser = argparse.ArgumentParser(
        prog='psend',
        description='Utility to send push notifications',
        epilog='Send push notifications to Simple Push Notification API (https://play.google.com/store/apps/details?id=net.xdroid.pn)')
    parser.add_argument('-k', '--keys', dest="keys",
                        metavar="KEY", required=True, nargs='+')
    parser.add_argument('-t', '--title', dest="title", required=True)
    parser.add_argument('-c', '--content', dest="content", required=True)
    parser.add_argument('-u', '--url', dest="url", required=False)

    args = parser.parse_args()
    keys = args.keys
    title = args.title
    payload = args.content
    url = args.url

    return_code = psend(keys, title, payload, url)
    sys.exit(return_code)

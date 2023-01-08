if __name__ == "__main__":
    import requests
    import json
    import argparse

    # http://xdroid.net/api/message?k=k-546329599a65&t=sample&c=from+asus+ASUS_X00TD&u=http%3A%2F%2Fgoogle.com


    parser = argparse.ArgumentParser(
                        prog = 'pnotify_send',
                        description = 'Utility to send push notification',
                        epilog = 'Send push notification to Simple Push Notification API (https://play.google.com/store/apps/details?id=net.xdroid.pn)')
    parser.add_argument('-k', '--key', dest="key", required=True, nargs='+')
    parser.add_argument('-t', '--title', dest="title", required=True)
    parser.add_argument('-c', '--content', dest="content", required=True)
    parser.add_argument('-u', '--url', dest="url", required=False)


    service_url = "http://xdroid.net/api/message"
    args = parser.parse_args()
    keys = args.key
    title = args.title
    payload = args.content
    url = args.url

    for key in keys:
        response = requests.get(service_url, params={"k": key, "t": title, "c": payload, "u": url })

        if response.status_code != 200:
            print("[-] Errore durante l'invio della notifica al dispositivo", key)
            print("[-] status code:", response.status_code) 
            exit(1)
        else:
            content = json.loads(response.content)
            if not content["success"] == "1":
                print("[-] Errore durante l'invio della notifica al dispositivo", key)
                print("[-] success:", content["success"])
                print("[-] success:", content["error"])
                exit(2)
            else:
                print("[+] Invio della notifica avvenuto con successo al dispositivo", key)
                print("[+] success:", content["success"])
                print("[+] error:", content["error"])
import json
import requests

def load_sites(file_path='sites.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

def check_username(username, sites):
    print(f"[*] '{username}' kullanıcı adı kontrol ediliyor...\n")
    for site, url_template in sites.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] {site}: Bulundu! --> {url}")
            elif response.status_code == 404:
                print(f"[-] {site}: Bulunamadı.")
            else:
                print(f"[?] {site}: Durum Kodu: {response.status_code}")
        except requests.RequestException:
            print(f"[!] {site}: Hata oluştu.")

if __name__ == "__main__":
    username = input("Kullanıcı adını girin: ")
    sites = load_sites()
    check_username(username, sites)

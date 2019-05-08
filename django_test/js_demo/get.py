import requests
import time

def main():
    url = "http://172.18.58.217:8052/shishibaozhang"
    r = requests.get(url)
    print(r.text)

if __name__ == "__main__":
    main()
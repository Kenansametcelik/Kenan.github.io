import requests

url = input("Lütfen site URL'sini girin: ")


try:
    response = requests.get(url)
    response.raise_for_status()  
    print("Site kaynak kodu:\n")
    print(response.text)  
except requests.exceptions.RequestException as e:
    print(f"Hata oluştu: {e}")

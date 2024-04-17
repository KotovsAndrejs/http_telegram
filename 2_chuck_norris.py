# 
# Uzdevums: Izmantojot bibliotēku "requests" uzģenerēt Chuck Norris jokus
# https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
# https://api.chucknorris.io/
# 
# 1. Izdrukā 3 nejaušus jokus no Chuck Norris
# 
# 2. Izdrukā 3 nejaušus jokus no Chuck Norris par programmēšanu
# 
import requests


while True:
    print("\nNejaušo datu ģenerators:")
    print("1. Izdrukā 3 nejaušus jokus no Chuck Norris")
    print("2. Izdrukā 3 nejaušus jokus no Chuck Norris par programmēšanu")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        for i in range(3):
            r = requests.get('https://api.chucknorris.io/jokes/random')
            joke = r.json()
            print(joke["value"])
        pass
    elif choice == "2":
        for i in range(3):
            r = requests.get('https://api.chucknorris.io/jokes/random?category=dev')
            joke = r.json()
            print(joke["value"])
        pass

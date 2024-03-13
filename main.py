import requests
import json

def fetch_players(ip):
    url = f"http://{ip}:30120/players.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            players = response.json()
            return players
        else:
            print("Error Found. Status code:", response.status_code)
            return None
    except Exception as e:
        print("IP Does not exist.:", e)
        return None

def sort_by_id(player):
    return player['id']

def main():
    ip = input("Enter IP: ")
    players = fetch_players(ip)
    if players is not None:
        sorted_players = sorted(players, key=sort_by_id)
        print("Spelare på servern:")
        for player in sorted_players:
            print("Namn:", player.get('name', ''))
            print("Steam:", player['identifiers'][0])
            print("Spelarens ID:", player['id'])
            print()

    input("Tryck på Enter för att avsluta...")

if __name__ == "__main__":
    main()

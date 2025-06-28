import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url=url)
    
    if response.status_code == 200:
        pokemon_content = response.json()
        return pokemon_content
            
    else:
        print(f"error code: {response.status_code}")

def main():
    pokemon_name = "lapras"
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info:
        print(f"name: {pokemon_info["name"]}")
        print(f"id: {pokemon_info["id"]}")
        print(f"height: {pokemon_info["height"]}")
        print(f"weight: {pokemon_info["weight"]}")
    

if __name__ == "__main__":
    main()
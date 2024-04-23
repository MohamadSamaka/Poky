from pokemonCollector import PokemonCollector

if __name__ == "__main__":
    while True:
        answer = input("Would  you like to draw a pokemon? (Y/N) ").upper()
        
        if answer.lower() == 'y':
            PokemonCollector()
        elif answer.lower() == 'n':
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid input! Please enter 'Y' for yes or 'N' for no.")
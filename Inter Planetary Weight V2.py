import pickle

fPlanetGravityFactors = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Moon": 0.165,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 0.93,
    "Uranus": 0.92,
    "Neptune": 1.12,
    "Pluto": 0.066
}

def main():
    while True:
        sUser = input("Welcome! What is your name? (enter 'q' to quit): ")
        if sUser.lower() == 'q':
            break

        try:
            with open('dfPlanetaryWeights.db', 'rb') as file:
                dictPlanetHistory = pickle.load(file)
        except FileNotFoundError:
            dictPlanetHistory = {}

        sSeeHistory = input("Would you like to view your history of calculations? (Y/N): ")
        if sSeeHistory.lower() == 'y':
            if sUser in dictPlanetHistory:
                for sName, fWeights in dictPlanetHistory.items():
                    print(f"\n{sName}'s Planetary Weight History:")
                    for sPlanet, fWeight in fWeights.items():
                        print(f"{sPlanet:<10}: {fWeight:>10.2f}lbs")
            else:
                print(f"\nNo history found for '{sUser}'.\n")

        else:
            print(f"Okay then, {sUser}, let's move on.\n")

        while True:
            try:
                fEarthWeight = float(input("Enter your weight (lbs) on Earth: "))
                break
            except ValueError:
                print("Error. Please enter a numeric value.")

        print(f"\n     {sUser}'s Weight\n Across the Solar System")
        print("*************************")
        dictPersonWeights = {}
        for sPlanet, fGravityFactor in fPlanetGravityFactors.items():
            fPlanetWeight = fEarthWeight * fGravityFactor
            dictPersonWeights[sPlanet] = fPlanetWeight
            print(f"{sPlanet:<10}: {fPlanetWeight:>10.2f}lbs")

        dictPlanetHistory[sUser] = dictPersonWeights
        with open("dfPlanetaryWeights.db", "wb") as file:
            pickle.dump(dictPlanetHistory, file)

if __name__ == "__main__":
    main()
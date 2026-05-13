import math
import random
import time

# storing old calculations here
history = []

# total calculations counter
total_calculations = 0


def calculate_distance(p1, p2):

    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def get_coordinates(name):

    while True:

        try:
            print(f"\nEnter coordinates for {name} (in million km)")

            x = float(input("x: "))
            y = float(input("y: "))

            return (x, y)

        except ValueError:
            print("invalid input bro")


def choose_planets():

    planets = {
        1: ("Earth", (0, 0)),
        2: ("Mars", (225, 0)),
        3: ("Venus", (108, 0)),
        4: ("Jupiter", (778, 0)),
        5: ("Saturn", (1427, 0)),
        6: ("Uranus", (2871, 0)),
        7: ("Neptune", (4495, 0)),
        8: ("Mercury", (58, 0)),
        9: ("Pluto", (5906, 0))
    }

    print("\nAvailable planets:")

    for num, (name, _) in planets.items():
        print(f"{num}. {name}")

    # choosing planets here
    def pick(msg):

        while True:

            try:
                choice = int(input(msg))

                if choice in planets:
                    return planets[choice]

                else:
                    print("pick a valid number")

            except ValueError:
                print("numbers only pls")

    p1_name, p1 = pick("Choose planet 1: ")
    p2_name, p2 = pick("Choose planet 2: ")

    return p1_name, p1, p2_name, p2


def show_fun_fact():

    facts = [
        "Venus spins backwards",
        "Mars sunsets are blue",
        "Saturn could float in water",
        "Jupiter is insanely huge",
        "Neptune has crazy strong winds"
    ]

    print(f"\nfun fact: {random.choice(facts)}")


def show_space_event():

    events = [
        "☄️ comet detected nearby",
        "🌠 meteor shower active",
        "🛰️ signal received from deep space",
        "👽 aliens definitely watching"
    ]

    print(random.choice(events))


def random_space_weather():

    weather = [
        "☀️ solar activity calm today",
        "🌌 radiation levels normal",
        "☄️ asteroid traffic kinda high rn",
        "🛰️ satellites working fine"
    ]

    print(f"\nspace weather: {random.choice(weather)}")


def mission_status():

    missions = [
        "✅ mission completed successfully",
        "🚀 navigation systems online",
        "⚠️ fuel levels questionable",
        "🌌 deep space systems stable"
    ]

    print(random.choice(missions))


# NEW thing today
def detect_black_hole():

    chance = random.randint(1, 10)

    if chance == 1:
        print("🕳️ black hole detected nearby RUN")
    else:
        print("✅ no black holes nearby")


# NEW thing today
def oxygen_level():

    oxygen = random.randint(70, 100)

    print(f"🫁 oxygen levels: {oxygen}%")


def random_rank(distance):

    if distance > 5000:
        print("🏆 rank: intergalactic traveler")

    elif distance > 3000:
        print("🏆 rank: galaxy traveler")

    elif distance > 1000:
        print("🏆 rank: space explorer")

    elif distance > 300:
        print("🏆 rank: orbit runner")

    else:
        print("🏆 rank: moon walker")


def main():

    global total_calculations

    startup_messages = [
        "space calculator v9 ready",
        "doing questionable space math",
        "probably accurate enough",
        "welcome back commander"
    ]

    print("\n🌌 Space Distance Calculator")
    print(random.choice(startup_messages))

    while True:

        mode = input("\n1 planets | 2 custom | 3 history | 4 stats: ").strip()

        # history
        if mode == "3":

            if not history:
                print("no history yet")

            else:
                print("\nhistory:")

                for item in history:
                    print(item)

            continue

        # stats mode
        if mode == "4":

            print(f"\n📊 total calculations: {total_calculations}")
            print(f"📜 saved history count: {len(history)}")

            continue

        # custom mode
        if mode == "2":

            p1 = get_coordinates("Point 1")
            p2 = get_coordinates("Point 2")

            p1_name, p2_name = "Point 1", "Point 2"

        else:
            p1_name, p1, p2_name, p2 = choose_planets()

        print("\ncalculating distance...")
        time.sleep(1)

        distance = calculate_distance(p1, p2)

        distance_km = distance * 1_000_000

        result = f"{p1_name} ↔ {p2_name}: {distance:.2f} million km ({distance_km:.0f} km)"

        print(f"\nDistance: {result}")

        history.append(result)

        total_calculations += 1

        # saving history
        with open("history.txt", "a") as file:
            file.write(result + "\n")

        # light speed
        light_speed = 299_792

        time_seconds = distance_km / light_speed
        time_minutes = time_seconds / 60

        print(f"⚡ light travel time: {time_seconds:.2f} sec ({time_minutes:.2f} min)")

        # spaceship speed
        ship_speed = 50000

        ship_hours = distance_km / ship_speed

        print(f"🚀 spaceship travel time: {ship_hours:.2f} hours")

        # earth comparison
        earth_trips = distance_km / 40075

        print(f"🌍 that's around Earth {earth_trips:.0f} times")

        # reactions
        if distance > 3000:
            print("😱 that's insanely insanely far")

        elif distance > 1000:
            print("😳 pretty far ngl")

        else:
            print("🚀 kinda close actually")

        show_fun_fact()
        show_space_event()
        random_space_weather()
        mission_status()
        detect_black_hole()
        oxygen_level()
        random_rank(distance)

        # random exploration score
        score = random.randint(1, 100)

        print(f"⭐ exploration score: {score}/100")

        # tiny easter eggs
        secret = input("\nsecret code? (press enter to skip): ")

        if secret.lower() == "apollo":
            print("🚀 moon mission unlocked")

        elif secret.lower() == "mars":
            print("🔴 welcome to mars commander")

        elif secret.lower() == "saturn":
            print("🪐 ring system access granted")

        elif secret.lower() == "pluto":
            print("❄️ tiny planet mode activated")

        again = input("\nrun again? (y/n): ").lower()

        if again != "y":
            print("ok bye")
            break


if __name__ == "__main__":
    main()

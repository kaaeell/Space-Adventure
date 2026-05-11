import math
import random
import time

# storing old calculations here
history = []


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
        8: ("Mercury", (58, 0))
    }

    print("\nAvailable planets:")

    for num, (name, _) in planets.items():
        print(f"{num}. {name}")

    # planet picking thing
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
        "Jupiter is so big it could fit all planets inside it 😳",
        "Venus spins backwards",
        "Saturn could float in water",
        "Mars sunsets are blue",
        "Space is completely silent"
    ]

    print(f"\nfun fact: {random.choice(facts)}")


def show_space_event():

    events = [
        "☄️ a comet just passed by",
        "🛰️ strange signal detected",
        "🌠 meteor shower nearby",
        "👽 aliens definitely watching"
    ]

    print(random.choice(events))


# added today because it sounded cool
def random_space_weather():

    weather = [
        "☀️ solar activity is calm today",
        "🌌 cosmic radiation levels normal",
        "☄️ asteroid traffic kinda high rn",
        "🛰️ satellite network stable",
        "🌠 meteor activity detected"
    ]

    print(f"\nspace weather: {random.choice(weather)}")


# NEW
def gravity_level():

    gravity = [
        "🪐 gravity levels stable",
        "⚠️ small gravity fluctuations detected",
        "🌍 earth gravity feeling normal",
        "🛰️ low gravity zone nearby"
    ]

    print(random.choice(gravity))


# NEW
def random_rank(distance):

    if distance > 3000:
        print("🏆 rank: galaxy traveler")

    elif distance > 1000:
        print("🏆 rank: space explorer")

    elif distance > 300:
        print("🏆 rank: orbit runner")

    else:
        print("🏆 rank: moon walker")


def main():

    startup_messages = [
        "welcome back space traveler",
        "doing space math again huh",
        "probably accurate enough",
        "space calculator v7 ready"
    ]

    print("\n🌌 Space Distance Calculator")
    print(random.choice(startup_messages))

    while True:

        mode = input("\n1 planets | 2 custom | 3 history: ").strip()

        # history stuff
        if mode == "3":

            if not history:
                print("no history yet")

            else:
                print("\nhistory:")

                for item in history:
                    print(item)

            continue

        # custom coords mode
        if mode == "2":

            p1 = get_coordinates("Point 1")
            p2 = get_coordinates("Point 2")

            p1_name, p2_name = "Point 1", "Point 2"

        else:
            p1_name, p1, p2_name, p2 = choose_planets()

        print("\ncalculating distance...")
        time.sleep(1)

        distance = calculate_distance(p1, p2)

        # million km -> km
        distance_km = distance * 1_000_000

        result = f"{p1_name} ↔ {p2_name}: {distance:.2f} million km ({distance_km:.0f} km)"

        print(f"\nDistance: {result}")

        history.append(result)

        # save history into txt file
        with open("history.txt", "a") as file:
            file.write(result + "\n")

        # light speed thing
        light_speed = 299_792

        time_seconds = distance_km / light_speed
        time_minutes = time_seconds / 60

        print(f"⚡ light travel time: {time_seconds:.2f} sec ({time_minutes:.2f} min)")

        # fake spaceship speed lol
        ship_speed = 50000

        ship_hours = distance_km / ship_speed

        print(f"🚀 spaceship travel time: {ship_hours:.2f} hours")

        # compare with earth laps
        earth_trips = distance_km / 40075

        print(f"🌍 that's around Earth {earth_trips:.0f} times")

        # reactions
        if distance > 1000:
            print("😱 insanely far")

        elif distance > 300:
            print("😳 pretty far ngl")

        else:
            print("🚀 kinda close actually")

        show_fun_fact()
        show_space_event()
        random_space_weather()
        gravity_level()
        random_rank(distance)

        # NEW tiny random score thing
        score = random.randint(1, 100)
        print(f"⭐ exploration score: {score}/100")

        # easter egg
        secret = input("\nsecret code? (press enter to skip): ")

        if secret.lower() == "apollo":
            print("🚀 moon mission unlocked")

        elif secret.lower() == "mars":
            print("🔴 welcome to mars commander")

        again = input("\nrun again? (y/n): ").lower()

        if again != "y":
            print("ok bye")
            break


if __name__ == "__main__":
    main()

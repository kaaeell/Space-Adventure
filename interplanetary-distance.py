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
        7: ("Neptune", (4495, 0))
    }

    print("\nAvailable planets:")

    for num, (name, _) in planets.items():
        print(f"{num}. {name}")

    # picking planets
    def pick(msg):
        while True:
            try:
                choice = int(input(msg))

                if choice in planets:
                    return planets[choice]

                else:
                    print("pick a real number")

            except ValueError:
                print("numbers only pls")

    p1_name, p1 = pick("Choose planet 1: ")
    p2_name, p2 = pick("Choose planet 2: ")

    return p1_name, p1, p2_name, p2


def show_fun_fact():

    facts = [
        "Jupiter is so big it could fit all planets inside it 😳",
        "A day on Venus is longer than a year there",
        "Saturn could float in water",
        "Mars sunsets are blue",
        "Space is completely silent"
    ]

    print(f"\nfun fact: {random.choice(facts)}")


def show_space_event():

    events = [
        "☄️ a comet just passed by",
        "🛰️ weird satellite signal detected",
        "🌠 meteor shower nearby",
        "👽 aliens definitely saw that calculation"
    ]

    print(random.choice(events))


# new tiny feature for today
def random_space_weather():

    weather = [
        "☀️ solar activity is calm today",
        "🌌 cosmic radiation levels normal",
        "☄️ asteroid traffic kinda high rn",
        "🛰️ satellite network stable",
        "🌠 small meteor activity detected"
    ]

    print(f"\nspace weather: {random.choice(weather)}")


def main():

    startup_messages = [
        "welcome back space traveler",
        "doing space math again huh",
        "probably accurate enough",
        "space calculator v6 ready"
    ]

    print("\n🌌 Space Distance Calculator")
    print(random.choice(startup_messages))

    while True:

        mode = input("\n1 planets | 2 custom | 3 history: ").strip()

        # history mode
        if mode == "3":

            if not history:
                print("no history yet")

            else:
                print("\nhistory:")

                for item in history:
                    print(item)

            continue

        # custom coordinates
        if mode == "2":

            p1 = get_coordinates("Point 1")
            p2 = get_coordinates("Point 2")

            p1_name, p2_name = "Point 1", "Point 2"

        else:
            p1_name, p1, p2_name, p2 = choose_planets()

        print("\ncalculating distance...")
        time.sleep(1)

        distance = calculate_distance(p1, p2)

        # converting million km into normal km
        distance_km = distance * 1_000_000

        result = f"{p1_name} ↔ {p2_name}: {distance:.2f} million km ({distance_km:.0f} km)"

        print(f"\nDistance: {result}")

        history.append(result)

        # saving history into txt file
        with open("history.txt", "a") as file:
            file.write(result + "\n")

        # light speed because space
        light_speed = 299_792

        time_seconds = distance_km / light_speed
        time_minutes = time_seconds / 60

        print(f"⚡ light travel time: {time_seconds:.2f} sec ({time_minutes:.2f} min)")

        # random spaceship speed
        ship_speed = 50000  # km per hour

        ship_hours = distance_km / ship_speed

        print(f"🚀 spaceship travel time: {ship_hours:.2f} hours")

        # compare to earth trips
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

        # tiny easter egg
        secret = input("\nsecret code? (press enter to skip): ")

        if secret.lower() == "apollo":
            print("🚀 moon mission unlocked")

        again = input("\nrun again? (y/n): ").lower()

        if again != "y":
            print("ok bye")
            break


if __name__ == "__main__":
    main()

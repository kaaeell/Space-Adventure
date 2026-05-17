import math
import random
import time
from datetime import datetime

# storing old calculations here
history = []

# total calculations counter
total_calculations = 0

# highest distance tracker
highest_distance = 0

# missions completed
missions_completed = 0

# random galaxy names
galaxy_names = [
    "Milky Way",
    "Andromeda",
    "Sombrero Galaxy",
    "Whirlpool Galaxy",
    "Black Eye Galaxy",
    "Cartwheel Galaxy"
]

# astronaut names
astronauts = [
    "Neil",
    "Buzz",
    "Sally",
    "Yuri",
    "Mae",
    "Chris",
    "Valentina"
]

# spaceship names
spaceships = [
    "StarRunner",
    "NovaX",
    "Galaxy Rider",
    "Void Explorer",
    "Cosmic Storm",
    "Nebula One"
]

space_pets = [
    "space dog",
    "robot cat",
    "alien hamster",
    "tiny moon dragon"
]

badges = [
    "🌟 rookie pilot badge",
    "🚀 master explorer badge",
    "🪐 galaxy navigator badge",
    "☄️ asteroid survivor badge"
]


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
        9: ("Pluto", (5906, 0)),
        10: ("Moon", (1, 0))
    }

    print("\nAvailable planets:")

    for num, (name, _) in planets.items():
        print(f"{num}. {name}")

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
        "Neptune has crazy strong winds",
        "A day on Venus is longer than a year there"
    ]

    print(f"\nfun fact: {random.choice(facts)}")


def show_space_event():

    events = [
        "☄️ comet detected nearby",
        "🌠 meteor shower active",
        "🛰️ signal received from deep space",
        "👽 aliens definitely watching",
        "🪐 strange rings detected nearby"
    ]

    print(random.choice(events))


def random_space_weather():

    weather = [
        "☀️ solar activity calm today",
        "🌌 radiation levels normal",
        "☄️ asteroid traffic kinda high rn",
        "🛰️ satellites working fine",
        "⚡ solar storm warning active"
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


def detect_black_hole():

    chance = random.randint(1, 12)

    if chance == 1:
        print("🕳️ black hole detected nearby RUN")

    else:
        print("✅ no black holes nearby")


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


def random_galaxy():

    galaxy = random.choice(galaxy_names)

    print(f"🌌 nearby galaxy detected: {galaxy}")


def random_astronaut():

    print(f"👨‍🚀 astronaut online: {random.choice(astronauts)}")


def random_spaceship():

    print(f"🛸 active spaceship: {random.choice(spaceships)}")


def distance_category(distance):

    if distance < 100:
        print("📍 category: super short trip")

    elif distance < 1000:
        print("📍 category: medium trip")

    elif distance < 3000:
        print("📍 category: long trip")

    else:
        print("📍 category: extreme space travel")


def random_signal():

    signals = [
        "📡 strange radio signal detected",
        "📡 signal strength stable",
        "📡 communication delay increased",
        "📡 deep space signal lost briefly"
    ]

    print(random.choice(signals))


def moon_phase():

    phases = [
        "🌕 full moon tonight",
        "🌗 half moon detected",
        "🌑 new moon phase active",
        "🌙 crescent moon visible"
    ]

    print(random.choice(phases))


def crew_mood():

    moods = [
        "😄 crew feeling great",
        "😴 crew tired but working",
        "🤖 robots handling repairs",
        "🧑‍🚀 crew excited for mission"
    ]

    print(random.choice(moods))


def temperature_check():

    temp = random.randint(-150, 120)

    print(f"🌡️ nearby temperature: {temp}°C")


def danger_level():

    levels = [
        "🟢 danger level: low",
        "🟡 danger level: medium",
        "🟠 danger level: high",
        "🔴 danger level: critical"
    ]

    print(random.choice(levels))


def daily_space_tip():

    tips = [
        "💡 tip: always double check coordinates",
        "💡 tip: keep fuel above 30%",
        "💡 tip: avoid black holes if possible",
        "💡 tip: deep space signals can be delayed"
    ]

    print(random.choice(tips))


def main():

    global total_calculations
    global highest_distance
    global missions_completed

    startup_messages = [
        "space calculator v11 ready",
        "doing questionable space math",
        "probably accurate enough",
        "welcome back commander"
    ]

    print("\n🌌 Space Distance Calculator")
    print(random.choice(startup_messages))

    today = datetime.now()

    print(f"📅 date: {today.strftime('%Y-%m-%d')}")
    print(f"🕒 time: {today.strftime('%H:%M:%S')}")

    while True:

        mode = input("\n1 planets | 2 custom | 3 history | 4 stats | 5 clear history: ").strip()

        # history
        if mode == "3":

            if not history:
                print("no history yet")

            else:
                print("\nhistory:")

                for item in history:
                    print(item)

            continue

        # stats
        if mode == "4":

            print(f"\n📊 total calculations: {total_calculations}")
            print(f"📜 saved history count: {len(history)}")
            print(f"🏆 highest distance recorded: {highest_distance:.2f} million km")
            print(f"🚀 missions completed: {missions_completed}")

            continue

        # clear history
        if mode == "5":

            history.clear()

            with open("history.txt", "w") as file:
                file.write("")

            print("🗑️ history cleared")

            continue

        # custom mode
        if mode == "2":

            p1 = get_coordinates("Point 1")
            p2 = get_coordinates("Point 2")

            p1_name, p2_name = "Point 1", "Point 2"

        else:
            p1_name, p1, p2_name, p2 = choose_planets()

        # launch sequence
        print("\nlaunch sequence")

        for i in range(3, 0, -1):
            print(i)
            time.sleep(0.5)

        print("🚀 launch")

        # loading effect
        print("\ncalculating", end="")

        for i in range(3):
            time.sleep(0.5)
            print(".", end="")

        print()

        distance = calculate_distance(p1, p2)

        if distance > highest_distance:
            highest_distance = distance
            print("🏅 new distance record reached")

        distance_km = distance * 1_000_000

        result = f"{p1_name} ↔ {p2_name}: {distance:.2f} million km ({distance_km:.0f} km)"

        print(f"\nDistance: {result}")

        history.append(result)

        total_calculations += 1
        missions_completed += 1

        # save history
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

        # fuel
        fuel = random.randint(20, 100)

        print(f"⛽ spaceship fuel: {fuel}%")

        # random outputs
        show_fun_fact()
        show_space_event()
        random_space_weather()
        mission_status()
        detect_black_hole()
        oxygen_level()
        random_rank(distance)
        random_galaxy()
        random_astronaut()
        random_spaceship()
        distance_category(distance)
        random_signal()
        moon_phase()
        crew_mood()
        temperature_check()
        danger_level()
        daily_space_tip()

        # exploration score
        score = random.randint(1, 100)

        print(f"⭐ exploration score: {score}/100")

        # easter eggs
        secret = input("\nsecret code? (press enter to skip): ")

        if secret.lower() == "apollo":
            print("🚀 moon mission unlocked")

        elif secret.lower() == "mars":
            print("🔴 welcome to mars commander")

        elif secret.lower() == "saturn":
            print("🪐 ring system access granted")

        elif secret.lower() == "pluto":
            print("❄️ tiny planet mode activated")

        elif secret.lower() == "galaxy":
            print("🌌 galaxy mode activated")

        again = input("\nrun again? (y/n): ").lower()

        if again != "y":
            print("\nthanks for using space calculator")
            print("made by commander")
            break


def random_space_pet():

    print(f"🐾 companion detected: {random.choice(space_pets)}")


def random_badge():

    print(f"🎖️ badge earned: {random.choice(badges)}")


def signal_strength():

    strength = random.randint(40, 100)

    print(f"📶 signal strength: {strength}%")


def credits():

    credits_amount = random.randint(100, 5000)

    print(f"💰 space credits earned: {credits_amount}")


def asteroid_scan():

    asteroids = random.randint(0, 12)

    print(f"🪨 asteroids nearby: {asteroids}")


if __name__ == "__main__":
    main()

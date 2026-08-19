"""
🚀 SPACE ADVENTURE
A space game I made for fun - explore, trade, hunt bounties!
"""

import math, random, time, json, os
from datetime import datetime

you = {
    "fuel": 5000, "credits": 1000, "missions": 0, "streak": 0,
    "morale": 80, "research": 0, "rank": 1, "record": 0,
    "total_distance": 0, "achievements": [], "inventory": [], "pets": [],
    "luck": 0, "last_played": None, "pirates_killed": 0,
    "nebulae_visited": 0, "jokes_told": 0, "sessions": 0,
    "ship_name": "Star Explorer", "visited_planets": [],
    "total_fuel_collected": 0, "biggest_treasure": 0,
    "crew_happiness": 80, "asteroids_mined": 0,
    "aliens_met": 0, "quests_completed": 0,
    "space_pizza_eaten": 0, "stars_observed": 0,
    "black_holes_escaped": 0
}

crew = [
    {"name": "Rex", "role": "Captain", "level": 1, "xp": 0},
    {"name": "Jen", "role": "Engineer", "level": 1, "xp": 0},
    {"name": "Zoe", "role": "Navigator", "level": 1, "xp": 0},
    {"name": "Kim", "role": "Scientist", "level": 1, "xp": 0},
    {"name": "Mack", "role": "Gunner", "level": 1, "xp": 0}
]

PLANETS = {
    1: ("Earth", (0,0)), 2: ("Mars", (225,0)), 3: ("Venus", (108,0)),
    4: ("Jupiter", (778,0)), 5: ("Saturn", (1427,0)), 6: ("Uranus", (2871,0)),
    7: ("Neptune", (4495,0)), 8: ("Mercury", (58,0)), 9: ("Pluto", (5906,0))
}

BOUNTIES = [
    {"name":"Red Pirate","reward":500,"level":1,"hp":3},
    {"name":"Shadow Corsair","reward":1000,"level":2,"hp":5},
    {"name":"Void Reaver","reward":2000,"level":3,"hp":7},
    {"name":"Galactic Menace","reward":3500,"level":4,"hp":10}
]

TECH = {
    "Fuel Efficiency":{"cost":100,"owned":False},
    "Warp Drive":{"cost":200,"owned":False},
    "Shield Tech":{"cost":150,"owned":False},
    "Scanner Range":{"cost":120,"owned":False}
}

ACHIEVEMENTS = {
    "first_mission":"First mission!",
    "explorer":"Traveled 2000+ km!",
    "fuel_finder":"Found fuel in nebula!",
    "millionaire":"Earned 10,000 credits!",
    "legend":"50 missions!",
    "streak":"5 in a row!",
    "bounty_hunter":"Defeated a bounty!",
    "researcher":"All research!",
    "pet_finder":"Found a pet!",
    "lucky":"Lucky day!",
    "traveler":"10000 km total!",
    "pirate_slayer":"10 pirates!",
    "nebula_expert":"5 nebulae!",
    "comedian":"10 jokes!",
    "collector":"10 items!",
    "ship_namer":"Named your ship!",
    "planet_lover":"All planets!",
    "fuel_horder":"5000 fuel!",
    "miner":"50 asteroids!",
    "alien_friend":"10 aliens!",
    "quest_master":"10 quests!",
    "pizza_lover":"Ate 10 pizzas!",
    "star_gazer":"Observed 50 stars!",
    "black_hole_survivor":"Escaped 5 black holes!"
}

PETS = ["Space Dog","Robot Cat","Alien Hamster","Tiny Dragon",
        "Quantum Fox","Space Penguin","Star Octopus","Nebula Unicorn"]

JOKES = [
    "Why did the star go to school? To get brighter!",
    "What do astronauts use for pants? An asteroid belt!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key? The space bar!",
    "Why did the alien cross the galaxy? To get to the other side!",
    "What do you call a space cow? A milky way!"
]

NEBULAE = {
    "Orion":(1340,-220), "Eagle":(7000,0), "Helix":(695,280),
    "Crab":(6500,190), "Skull":(4200,-500)
}

SHOP = {
    "Dark Crystal":500, "Warp Core":2000, "Quantum Shield":1500,
    "Space Pizza":50, "Anomaly Scanner":800, "Research Data":400,
    "Telescope":300, "Black Hole Map":600
}

SHIP_NAMES = ["Star Explorer","Cosmic Wanderer","Nebula Rider",
              "Void Seeker","Galaxy Hopper","Starlight","Dark Star"]

SPACE_FACTS = [
    "A day on Venus is longer than a year.",
    "Saturn's rings are made of ice and rock.",
    "Jupiter is the largest planet.",
    "Space is completely silent.",
    "There are more stars than grains of sand.",
    "The sun is actually white, not yellow.",
    "Black holes are invisible!"
]

SPACE_WEATHER = [
    "Solar winds are calm ☀️",
    "Cosmic radiation is normal",
    "A solar flare just passed!",
    "Perfect conditions for travel!",
    "Auroras visible today!",
    "Magnetic field is stable",
    "Warning: Black hole nearby!"
]

GREETINGS = [
    "Good to see you, Captain!",
    "Ready for another adventure?",
    "The stars are calling!",
    "Welcome back to space!",
    "Another day, another galaxy!"
]

STARS = ["Sirius","Betelgeuse","Rigel","Vega","Proxima Centauri",
         "Alpha Centauri","Polaris","Aldebaran","Antares","Capella"]

quest = {"name":"Fly 500 km","type":"distance","goal":500,"reward":200}
quest_progress = 0

def new_quest():
    global quest, quest_progress
    qs = [
        {"name":"Fly 500 km","type":"distance","goal":500,"reward":200},
        {"name":"Earn 1000 credits","type":"credits","goal":1000,"reward":300},
        {"name":"Mine 100 fuel","type":"mine","goal":100,"reward":250},
        {"name":"Visit 2 planets","type":"planets","goal":2,"reward":150},
        {"name":"Tell 3 jokes","type":"jokes","goal":3,"reward":100},
        {"name":"Eat 2 space pizzas","type":"pizza","goal":2,"reward":150},
        {"name":"Observe 5 stars","type":"stars","goal":5,"reward":200},
        {"name":"Escape a black hole","type":"blackhole","goal":1,"reward":300}
    ]
    quest = random.choice(qs)
    quest_progress = 0

def show_quest():
    print(f"\n📋 QUEST: {quest['name']} ({quest_progress}/{quest['goal']}) - Reward: {quest['reward']}cr")

def check_quest():
    global quest_progress, quest
    if quest_progress >= quest["goal"]:
        print(f"\n🎯 QUEST COMPLETE! +{quest['reward']} credits!")
        you["credits"] += quest["reward"]
        you["quests_completed"] += 1
        if you["quests_completed"] >= 10:
            unlock_ach("quest_master")
        new_quest()

def black_hole():
    global quest_progress
    header("🌀 BLACK HOLE ENCOUNTER")
    print("🚨 WARNING: You've encountered a black hole!")
    print("Gravity is pulling your ship in...")
    time.sleep(1)
    
    if "Black Hole Map" in you["inventory"]:
        print("\n🗺️ Your Black Hole Map shows a safe escape route!")
        escape_chance = 0.9
    else:
        print("\n💫 You need to escape quickly!")
        escape_chance = 0.6 + (you["luck"] * 0.03)
    
    print(f"🔄 Escape chance: {escape_chance*100:.0f}%")
    
    if random.random() < escape_chance:
        print("\n✅ You escaped the black hole!")
        you["black_holes_escaped"] += 1
        reward = random.randint(100, 300)
        you["credits"] += reward
        print(f"💰 +{reward} credits for surviving!")
        you["morale"] = min(100, you["morale"] + 10)
        print("😊 Morale +10!")
        if you["black_holes_escaped"] >= 5:
            unlock_ach("black_hole_survivor")
        if quest["type"] == "blackhole":
            quest_progress += 1
            check_quest()
    else:
        print("\n💥 The black hole damaged your ship!")
        damage = random.randint(100, 300)
        you["fuel"] = max(0, you["fuel"] - damage)
        you["morale"] = max(0, you["morale"] - 10)
        print(f"⛽ Lost {damage} fuel!")
        print("😞 Morale -10!")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(text):
    print("\n" + "=" * 50 + f"\n  {text}\n" + "=" * 50)

def dist(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def unlock_ach(key):
    if key in ACHIEVEMENTS and key not in you["achievements"]:
        you["achievements"].append(key)
        print(f"\n🎉 {ACHIEVEMENTS[key]} 🎉\n")
        time.sleep(0.8)

def crew_xp(amount):
    for m in crew:
        m["xp"] += amount
        if m["xp"] >= m["level"] * 100:
            m["xp"] = 0
            m["level"] += 1
            print(f"\n🌟 {m['name']} is now level {m['level']}!")
            you["credits"] += random.randint(100, 300)

def check_luck():
    today = datetime.now().date()
    if you["last_played"] != str(today):
        you["luck"] = random.randint(1, 10)
        you["last_played"] = str(today)
        print(f"\n🍀 Luck: {'⭐' * you['luck']}")
        if you["luck"] >= 8:
            print("🌟 Lucky day!")
            unlock_ach("lucky")
        elif you["luck"] >= 5:
            print("✨ Good day")
        else:
            print("🌙 Quiet day")
        time.sleep(0.5)

def find_pet():
    pet = random.choice(PETS)
    if pet not in you["pets"]:
        you["pets"].append(pet)
        print(f"\n🐾 A {pet} joined your crew!")
        unlock_ach("pet_finder")
        you["morale"] = min(100, you["morale"] + 10)
        you["crew_happiness"] = min(100, you.get("crew_happiness", 80) + 5)

def tell_joke():
    print(f"\n😂 {random.choice(JOKES)}")
    you["morale"] = min(100, you["morale"] + 5)
    you["crew_happiness"] = min(100, you.get("crew_happiness", 80) + 3)
    you["jokes_told"] += 1
    if you["jokes_told"] >= 10:
        unlock_ach("comedian")

def get_input(prompt, default=None):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\n👋 Later!")
        exit()

def show_morale():
    filled = int(20 * you["morale"] / 100)
    bar = "█" * filled + "░" * (20 - filled)
    mood = "😄" if you["morale"] > 70 else "😐" if you["morale"] > 40 else "😞"
    print(f"😊 Morale: [{bar}] {you['morale']}% {mood}")

def get_planet_name(coords):
    for name, c in PLANETS.values():
        if c == coords:
            return name
    return "Unknown"

def show_happiness():
    filled = int(20 * you.get("crew_happiness", 80) / 100)
    bar = "█" * filled + "░" * (20 - filled)
    print(f"👥 Happiness: [{bar}] {you.get('crew_happiness', 80)}%")

def alien_encounter():
    print("\n👽 A friendly alien appears!")
    time.sleep(0.5)
    alien = random.choice(["Zorg","Blip","Nova","Kratos","Glimmer"])
    print(f"The alien is {alien}.")
    you["aliens_met"] += 1
    if you["aliens_met"] >= 10:
        unlock_ach("alien_friend")
    gift = random.choice(["Crystal","Hat","Flower","Candy","Space Gem"])
    print(f"\n🎁 {alien} gives you: {gift}!")
    you["inventory"].append(gift)
    you["credits"] += random.randint(20, 80)

def name_ship():
    header("🚢 NAME YOUR SHIP")
    print(f"Current: {you['ship_name']}")
    for i, name in enumerate(SHIP_NAMES, 1):
        print(f"{i}. {name}")
    print(f"{len(SHIP_NAMES)+1}. Custom")
    choice = get_input("Choice: ", "1")
    if choice.isdigit() and 1 <= int(choice) <= len(SHIP_NAMES):
        you["ship_name"] = SHIP_NAMES[int(choice)-1]
        print(f"\n✅ Ship renamed to {you['ship_name']}!")
        unlock_ach("ship_namer")
    elif choice == str(len(SHIP_NAMES)+1):
        new_name = get_input("Enter name: ")
        if new_name.strip():
            you["ship_name"] = new_name.strip()
            print(f"\n✅ Ship renamed to {you['ship_name']}!")
            unlock_ach("ship_namer")

def observe_stars():
    global quest_progress
    header("🔭 STAR GAZING")
    if "Telescope" not in you["inventory"]:
        print("\n❌ You need a Telescope!")
        print("💡 Buy one from the alien trader!")
        return
    print("\n🔭 Pointing your telescope at the sky...")
    time.sleep(1)
    stars_seen = random.randint(1, 5)
    you["stars_observed"] += stars_seen
    star_names = random.sample(STARS, min(stars_seen, len(STARS)))
    print(f"\n✨ You observed {stars_seen} stars:")
    for star in star_names:
        print(f"  • {star}")
    gain = random.randint(3, 8)
    you["morale"] = min(100, you["morale"] + gain)
    you["crew_happiness"] = min(100, you.get("crew_happiness", 80) + 2)
    print(f"\n😊 Stargazing boosted morale +{gain}!")
    if random.random() < 0.1:
        print("\n🌟 You discovered a new star!")
        new_star = random.choice(["Nova","Solara","Lumina","Vela"])
        print(f"📝 Welcome to the universe, {new_star}!")
        reward = random.randint(50, 150)
        you["credits"] += reward
        print(f"💰 The astronomy society pays you {reward} credits!")
    if you["stars_observed"] >= 50:
        unlock_ach("star_gazer")
    if quest["type"] == "stars":
        quest_progress += stars_seen
        check_quest()

def view_inventory():
    header("📦 INVENTORY")
    if you["inventory"]:
        print("\nYour items:")
        for i, item in enumerate(you["inventory"], 1):
            print(f"{i}. {item}")
        print(f"\nTotal: {len(you['inventory'])} items")
    else:
        print("\nYour inventory is empty!")

def eat_pizza():
    global quest_progress
    if "Space Pizza" in you["inventory"]:
        you["inventory"].remove("Space Pizza")
        you["space_pizza_eaten"] += 1
        you["morale"] = min(100, you["morale"] + 5)
        you["crew_happiness"] = min(100, you.get("crew_happiness", 80) + 3)
        print("\n🍕 You eat a delicious Space Pizza!")
        print(f"😊 Morale +5! (Now: {you['morale']}%)")
        if you["space_pizza_eaten"] >= 10:
            unlock_ach("pizza_lover")
        if quest["type"] == "pizza":
            quest_progress += 1
            check_quest()
    else:
        print("\n❌ You don't have any Space Pizza!")

def use_item():
    header("🔧 USE ITEM")
    if not you["inventory"]:
        print("\nYou have nothing to use!")
        return
    print("\nYour items:")
    for i, item in enumerate(you["inventory"], 1):
        print(f"{i}. {item}")
    choice = get_input("\nChoose item (number or q): ", "q")
    if choice.lower() == 'q':
        return
    if choice.isdigit() and 1 <= int(choice) <= len(you["inventory"]):
        item = you["inventory"][int(choice)-1]
        if "Pizza" in item:
            eat_pizza()
        elif "Crystal" in item or "Gem" in item:
            you["inventory"].remove(item)
            value = random.randint(50, 150)
            you["credits"] += value
            print(f"\n💎 Sold {item} for {value} credits!")
        elif "Telescope" in item:
            observe_stars()
        elif "Black Hole Map" in item:
            print("\n🗺️ You study the Black Hole Map...")
            print("💡 You now have a better chance of escaping black holes!")
        else:
            print(f"\n❌ Can't use {item} right now.")

def pick_planets():
    print("\n🪐 WHERE TO?")
    for n, (name, _) in PLANETS.items():
        print(f"{n}. {name}")
    def choose(q):
        while True:
            try:
                c = int(get_input(q, "1"))
                if c in PLANETS:
                    return PLANETS[c]
                print("Invalid!")
            except ValueError:
                print("Enter a number!")
    start = choose("Start: ")
    end = choose("Destination: ")
    return get_planet_name(start), start, get_planet_name(end), end

def mission():
    global quest_progress
    check_luck()
    header(f"🚀 {you['ship_name']} - LAUNCH")
    print("1. Known planets  2. Unknown  3. Back")
    choice = get_input("Choice: ", "3")
    if choice == "3":
        return
    elif choice == "1":
        start_name, start, end_name, end = pick_planets()
    elif choice == "2":
        try:
            print("\n📡 Coordinates (million km)")
            start = (float(get_input("x: ", "0")), float(get_input("y: ", "0")))
            end = (float(get_input("x: ", "100")), float(get_input("y: ", "100")))
            start_name, end_name = "Unknown", "Unknown"
        except ValueError:
            print("Invalid!")
            return
    else:
        print("Invalid!")
        return

    distance = dist(start, end)
    you["total_distance"] += distance
    print(f"\n📏 Distance: {distance:,.0f} million km")
    quest_progress += distance

    if distance > you["record"]:
        you["record"] = distance
        print("🏆 New record!")

    if random.random() < 0.25 + (you["luck"] * 0.01):
        event = random.choice(["wormhole","treasure","pet","joke","alien","blackhole"])
        if event == "wormhole":
            distance *= 0.6
            print("🌀 Wormhole shortcut!")
        elif event == "treasure":
            bonus = random.randint(100, 300) + (you["luck"] * 10)
            you["credits"] += bonus
            if bonus > you["biggest_treasure"]:
                you["biggest_treasure"] = bonus
                print(f"💰 BIGGEST TREASURE! +{bonus}cr!")
            else:
                print(f"💰 Found treasure! +{bonus}cr!")
        elif event == "pet":
            find_pet()
        elif event == "joke":
            tell_joke()
        elif event == "alien":
            alien_encounter()
        elif event == "blackhole":
            black_hole()

    fuel_needed = distance * 0.5
    if TECH["Fuel Efficiency"]["owned"]:
        fuel_needed *= 0.9
        print("⛽ Fuel efficiency active!")

    if you["fuel"] < fuel_needed:
        print(f"\n⛽ Need {fuel_needed:.0f} fuel, have {you['fuel']:.0f}")
        print("1. Mine  2. Buy  3. Abort")
        choice = get_input("Choice: ", "3")
        if choice == "3":
            print("Aborted.")
            return
        elif choice == "1":
            if random.random() < 0.6 + (you["luck"] * 0.02):
                gained = random.randint(200, 800)
                you["fuel"] += gained
                you["total_fuel_collected"] += gained
                you["asteroids_mined"] += 1
                print(f"✅ Mined {gained} fuel!")
                if you["total_fuel_collected"] >= 5000:
                    unlock_ach("fuel_horder")
                if you["asteroids_mined"] >= 50:
                    unlock_ach("miner")
            else:
                lost = random.randint(50, 200)
                you["fuel"] = max(0, you["fuel"] - lost)
                print(f"💥 Lost {lost} fuel!")
        elif choice == "2":
            try:
                amount = int(get_input("How much? ", "100"))
                cost = amount * 2
                if you["credits"] >= cost:
                    you["credits"] -= cost
                    you["fuel"] += amount
                    print(f"✅ Bought {amount} fuel!")
                else:
                    print("Not enough credits!")
            except ValueError:
                print("Invalid!")
        return

    you["fuel"] -= fuel_needed
    earned = int(distance * 0.8 + 50 + (you["luck"] * 2))
    you["credits"] += earned
    you["missions"] += 1
    you["streak"] += 1
    you["morale"] = min(100, you["morale"] + random.randint(5, 15))
    you["crew_happiness"] = min(100, you.get("crew_happiness", 80) + 3)

    header("✅ MISSION COMPLETE")
    print(f"💰 +{earned} credits")
    print(f"⛽ Fuel left: {you['fuel']:.0f}")
    show_morale()
    show_happiness()
    print(f"📊 Missions: {you['missions']} | Streak: {you['streak']}")

    if you["missions"] == 1:
        unlock_ach("first_mission")
    if you["credits"] >= 10000:
        unlock_ach("millionaire")
    if you["missions"] >= 50:
        unlock_ach("legend")
    if you["streak"] >= 5:
        unlock_ach("streak")
    if you["record"] >= 2000:
        unlock_ach("explorer")
    if you["total_distance"] >= 10000:
        unlock_ach("traveler")
    if len(you["inventory"]) >= 10:
        unlock_ach("collector")

    if start_name != "Unknown" and start_name not in you["visited_planets"]:
        you["visited_planets"].append(start_name)
    if end_name != "Unknown" and end_name not in you["visited_planets"]:
        you["visited_planets"].append(end_name)
    
    all_planets = [name for name, _ in PLANETS.values()]
    if len(set(you["visited_planets"]) & set(all_planets)) >= len(all_planets):
        unlock_ach("planet_lover")

    check_quest()
    crew_xp(20)

def bounty():
    check_luck()
    header("💰 BOUNTY HUNTING")
    print(f"🏆 Rank: {you['rank']}")
    available = [b for b in BOUNTIES if b["level"] <= you["rank"] + 1]
    if not available:
        print("No bounties!")
        return
    print("\n🎯 TARGETS:")
    for i, t in enumerate(available[:4], 1):
        print(f"{i}. {t['name']} - 💰 {t['reward']} (Lv.{t['level']})")
    choice = get_input("Choose: ", "1")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(available[:4]):
        return
    target = available[int(choice)-1]
    print(f"\n⚔️ FIGHTING {target['name']}...")
    time.sleep(0.5)
    my_hp = target["hp"] + (you["luck"] // 3)
    enemy_hp = target["hp"]
    if TECH["Shield Tech"]["owned"]:
        my_hp += 2
        print("🛡️ Shield active!")
    while my_hp > 0 and enemy_hp > 0:
        print(f"\n❤️ You: {my_hp} | {target['name']}: {enemy_hp}")
        action = get_input("1. Attack  2. Dodge  3. Use item: ", "1")
        if action == "1":
            dmg = random.randint(2, 6) + (you["luck"] // 5)
            if TECH["Warp Drive"]["owned"]:
                dmg += 1
            enemy_hp -= dmg
            print(f"⚡ Hit for {dmg}!")
            if enemy_hp > 0:
                counter = random.randint(1, 4)
                if TECH["Shield Tech"]["owned"]:
                    counter = max(1, counter - 1)
                my_hp -= counter
                print(f"💥 Took {counter} damage!")
        elif action == "2":
            if random.random() < 0.5 + (you["luck"] * 0.02):
                print("🛡️ Dodged!")
            else:
                counter = random.randint(2, 5)
                my_hp -= counter
                print(f"💥 Took {counter} damage!")
        elif action == "3":
            if "Space Pizza" in you["inventory"]:
                you["inventory"].remove("Space Pizza")
                heal = random.randint(3, 8)
                max_hp = target["hp"] + (you["luck"] // 3)
                if TECH["Shield Tech"]["owned"]:
                    max_hp += 2
                my_hp = min(max_hp, my_hp + heal)
                print(f"💊 Healed {heal} health!")
            else:
                print("❌ No items!")
    if my_hp > 0:
        bonus = int(target["reward"] * (1 + you["luck"] * 0.01))
        you["credits"] += bonus
        you["pirates_killed"] += 1
        print(f"\n🎉 VICTORY! +{bonus} credits!")
        if target["level"] == you["rank"]:
            you["rank"] += 1
            print(f"🏆 Rank up! Now {you['rank']}")
        unlock_ach("bounty_hunter")
        if you["pirates_killed"] >= 10:
            unlock_ach("pirate_slayer")
        crew_xp(30)
    else:
        print("\n💀 Defeated! Lost 100 credits")
        you["credits"] = max(0, you["credits"] - 100)

def research():
    header("🧪 RESEARCH")
    print(f"📚 Points: {you['research']}\n")
    for i, (name, data) in enumerate(TECH.items(), 1):
        status = "✅" if data["owned"] else f"💰 {data['cost']}pts"
        print(f"{i}. {name} - {status}")
    print("\n5. Convert 100cr → 20pts  6. Back")
    choice = get_input("Choice: ", "6")
    if choice == "6":
        return
    elif choice.isdigit() and 1 <= int(choice) <= 4:
        name, data = list(TECH.items())[int(choice)-1]
        if not data["owned"] and you["research"] >= data["cost"]:
            you["research"] -= data["cost"]
            data["owned"] = True
            print(f"\n✨ Unlocked {name}!")
            if all(t["owned"] for t in TECH.values()):
                unlock_ach("researcher")
        else:
            print("❌ Not enough points or already owned!")
    elif choice == "5":
        if you["credits"] >= 100:
            you["credits"] -= 100
            you["research"] += 20
            print("✅ Converted!")
        else:
            print("❌ Not enough credits!")

def trade():
    header("👽 ALIEN TRADE")
    print(f"💰 Credits: {you['credits']}\n")
    for i, (item, price) in enumerate(SHOP.items(), 1):
        print(f"{i}. {item} - {price}cr")
    choice = get_input("Buy (number or q): ", "q")
    if choice.lower() == 'q':
        return
    elif choice.isdigit() and 1 <= int(choice) <= len(SHOP):
        item, price = list(SHOP.items())[int(choice)-1]
        if you["credits"] >= price:
            you["credits"] -= price
            you["inventory"].append(item)
            print(f"\n✨ Bought {item}!")
            if len(you["inventory"]) >= 10:
                unlock_ach("collector")
        else:
            print("❌ Not enough credits!")

def nebula():
    header("🌌 NEBULA EXPLORATION")
    for i, name in enumerate(NEBULAE.keys(), 1):
        print(f"{i}. {name}")
    choice = get_input("Choose: ", "1")
    if choice.isdigit() and 1 <= int(choice) <= len(NEBULAE):
        name = list(NEBULAE.keys())[int(choice)-1]
        print(f"\n🚀 Entering {name}...")
        time.sleep(1)
        you["nebulae_visited"] += 1
        if you["nebulae_visited"] >= 5:
            unlock_ach("nebula_expert")
        roll = random.random()
        if roll < 0.6 + (you["luck"] * 0.02):
            fuel = random.randint(300, 1500) + (you["luck"] * 10)
            you["fuel"] += fuel
            you["total_fuel_collected"] += fuel
            print(f"⛽ Found {fuel} fuel!")
            if you["total_fuel_collected"] >= 5000:
                unlock_ach("fuel_horder")
            unlock_ach("fuel_finder")
        elif roll < 0.8:
            treasure = random.choice(["Ancient Relic","Crystal Shard","Star Chart"])
            you["inventory"].append(treasure)
            print(f"🔮 Found {treasure}!")
            you["research"] += 20 + (you["luck"] * 2)
            if len(you["inventory"]) >= 10:
                unlock_ach("collector")
        else:
            print("💨 Empty nebula...")
        if random.random() < 0.08:
            find_pet()
    else:
        print("Invalid!")

def random_fun():
    header("🎲 RANDOM FUN")
    action = random.choice(["joke","pet","luck","treasure","dance","fact","weather","alien","pizza","stargaze","blackhole"])
    if action == "joke":
        tell_joke()
    elif action == "pet":
        find_pet()
    elif action == "luck":
        check_luck()
    elif action == "treasure":
        treasure = random.randint(50, 200) + (you["luck"] * 5)
        you["credits"] += treasure
        print(f"\n💰 Found {treasure} credits!")
    elif action == "dance":
        gain = random.randint(3, 10)
        you["morale"] = min(100, you["morale"] + gain)
        you["crew_happiness"] = min(100, you.get("crew_happiness", 80) + 2)
        print(f"\n💃 Dance party! Morale +{gain}!")
    elif action == "fact":
        print(f"\n📚 {random.choice(SPACE_FACTS)}")
    elif action == "weather":
        print(f"\n🌦️ {random.choice(SPACE_WEATHER)}")
    elif action == "alien":
        alien_encounter()
    elif action == "pizza":
        eat_pizza()
    elif action == "stargaze":
        observe_stars()
    elif action == "blackhole":
        black_hole()

def help():
    header("📖 CAPTAIN'S GUIDE")
    print(f"\n🚢 Ship: {you['ship_name']}")
    print("""
🎮 HOW TO PLAY:
   • Missions for credits and fuel
   • Research tech upgrades
   • Hunt bounties for rewards
   • Explore nebulae for treasures
   • Trade with aliens
   • Collect pets!

💡 TIPS:
   • Save often
   • Check daily luck
   • Keep fuel above 30%
   • Level up your crew
   • Eat pizza for morale! 🍕
   • Buy a telescope to see stars! 🔭
   • Get a Black Hole Map for safety! 🌀

🚀 HAVE FUN!
    """)

def stats():
    header("📊 YOUR STATS")
    print(f"🚢 Ship: {you['ship_name']}")
    print(f"🚀 Missions: {you['missions']} | 🔥 Streak: {you['streak']}")
    print(f"⛽ Fuel: {you['fuel']:.0f} | 💰 Credits: {you['credits']}")
    print(f"📚 Research: {you['research']}")
    show_morale()
    show_happiness()
    print(f"🏆 Rank: {you['rank']} | 📏 Furthest: {you['record']:,.0f} km")
    print(f"🍀 Luck: {'⭐'*you['luck']} | 🏅 Achievements: {len(you['achievements'])}")
    print(f"🪐 Planets: {len(you.get('visited_planets', []))}")
    print(f"⛽ Fuel Collected: {you.get('total_fuel_collected', 0)}")
    print(f"💎 Biggest Treasure: {you.get('biggest_treasure', 0)}")
    print(f"🪨 Asteroids: {you.get('asteroids_mined', 0)}")
    print(f"👽 Aliens: {you.get('aliens_met', 0)}")
    print(f"📋 Quests: {you.get('quests_completed', 0)}")
    print(f"🍕 Pizzas Eaten: {you.get('space_pizza_eaten', 0)}")
    print(f"✨ Stars Observed: {you.get('stars_observed', 0)}")
    print(f"🌀 Black Holes Escaped: {you.get('black_holes_escaped', 0)}")

    if you["achievements"]:
        print("\n🏅 Achievements:")
        for a in you["achievements"]:
            print(f"  • {ACHIEVEMENTS[a]}")
    if you["pets"]:
        print("\n🐾 Pets:")
        for pet in you["pets"]:
            print(f"  • {pet}")
    if you["inventory"]:
        print("\n📦 Inventory:")
        for item in you["inventory"]:
            print(f"  • {item}")

def view_crew():
    header("👥 YOUR CREW")
    for m in crew:
        print(f"\n🌟 {m['name']} - Lv.{m['level']} ({m['role']})")
        print(f"   XP: {m['xp']}/{m['level']*100}")
        if m['level'] * 100 > 0:
            prog = int((m['xp'] / (m['level'] * 100)) * 10)
            print(f"   [{ '█'*prog }{ '░'*(10-prog) }]")
        else:
            print(f"   [░░░░░░░░░░]")

def save():
    data = {k: v for k, v in you.items() if k not in ["achievements","inventory","pets","visited_planets"]}
    data.update({"achievements":you["achievements"],"inventory":you["inventory"],"pets":you["pets"],"visited_planets":you.get("visited_planets",[])})
    data["crew"] = crew
    data["tech"] = TECH
    try:
        with open("save.json", "w") as f:
            json.dump(data, f)
        print("\n💾 Saved!")
    except:
        print("❌ Save failed!")

def load():
    global you, crew, TECH
    try:
        with open("save.json", "r") as f:
            data = json.load(f)
        for key in data:
            if key in you and key not in ["achievements","inventory","pets","visited_planets"]:
                you[key] = data[key]
        you["achievements"] = data.get("achievements", [])
        you["inventory"] = data.get("inventory", [])
        you["pets"] = data.get("pets", [])
        you["visited_planets"] = data.get("visited_planets", [])
        if "crew" in data:
            for i, m in enumerate(data["crew"]):
                if i < len(crew):
                    crew[i] = m
        if "tech" in data:
            for name, vals in data["tech"].items():
                if name in TECH:
                    TECH[name]["owned"] = vals.get("owned", False)
        print("\n📀 Loaded!")
        return True
    except:
        print("❌ No save found!")
        return False

def main():
    new_quest()
    you["sessions"] = you.get("sessions", 0) + 1
    clear()

    print("""
    ╔════════════════════════════════════════════╗
    ║   🚀 SPACE ADVENTURE                     ║
    ║        A game I made for fun             ║
    ║     "The cosmos is yours to explore!"    ║
    ╚════════════════════════════════════════════╝
    """)

    print(f"🌟 {random.choice(GREETINGS)}")
    print(f"🚢 Ship: {you['ship_name']}")
    print("💫 Let's explore!\n")
    time.sleep(0.5)
    check_luck()
    show_quest()

    while True:
        print("\n" + "=" * 40)
        print("🌟 MAIN MENU")
        print("=" * 40)
        print("1. 🚀 Mission    2. 📊 Stats    3. 👥 Crew")
        print("4. 🧪 Research   5. 💰 Bounty   6. 👽 Trade")
        print("7. 🌌 Nebula     8. 💾 Save     9. 📀 Load")
        print("10. 🎲 Random    11. 📖 Help    12. 🚢 Name")
        print("13. 📋 Quest     14. 📦 Inventory")
        print("15. 🔭 Stargaze  16. 🌀 Black Hole")
        print("17. ❌ Quit")
        print("=" * 40)
        
        print(f"\n📊 Quick: Fuel: {you['fuel']:.0f} | Credits: {you['credits']} | Missions: {you['missions']}")

        choice = get_input("\nChoice: ", "17")

        if choice == "1": mission()
        elif choice == "2": stats()
        elif choice == "3": view_crew()
        elif choice == "4": research()
        elif choice == "5": bounty()
        elif choice == "6": trade()
        elif choice == "7": nebula()
        elif choice == "8": save()
        elif choice == "9": load()
        elif choice == "10": random_fun()
        elif choice == "11": help()
        elif choice == "12": name_ship()
        elif choice == "13": show_quest()
        elif choice == "14": view_inventory()
        elif choice == "15": observe_stars()
        elif choice == "16": black_hole()
        elif choice == "17":
            print("\n👋 See you later, Captain!")
            print("⭐ The stars will be waiting.")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

"""
🚀 SPACE ADVENTURE
A fun space game - explore, trade, hunt bounties!
"""

import math, random, time, json, os
from datetime import datetime

# ============================================
# Player data
# ============================================

p = {
    "fuel": 5000, "credits": 1000, "missions": 0, "streak": 0,
    "morale": 80, "research": 0, "rank": 1, "record": 0,
    "total_distance": 0, "achievements": [], "inventory": [], "pets": [],
    "luck": 0, "last_played": None, "pirates_killed": 0,
    "nebulae_visited": 0, "jokes_told": 0, "sessions": 0,
    "ship_name": "Star Explorer", "visited_planets": [],
    "total_fuel_collected": 0, "biggest_treasure": 0,
    "crew_happiness": 80, "asteroids_mined": 0,
    "aliens_met": 0, "quests_completed": 0
}

# ============================================
# Crew
# ============================================

crew = [
    {"name": "Rex", "role": "Captain", "level": 1, "xp": 0},
    {"name": "Jen", "role": "Engineer", "level": 1, "xp": 0},
    {"name": "Zoe", "role": "Navigator", "level": 1, "xp": 0},
    {"name": "Kim", "role": "Scientist", "level": 1, "xp": 0},
    {"name": "Mack", "role": "Gunner", "level": 1, "xp": 0}
]

# ============================================
# Game data
# ============================================

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
    "quest_master":"10 quests!"
}

PETS = ["Space Dog","Robot Cat","Alien Hamster","Tiny Dragon",
        "Quantum Fox","Space Penguin","Star Octopus","Nebula Unicorn"]

JOKES = [
    "Why did the star go to school? To get brighter!",
    "What do astronauts use for pants? An asteroid belt!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key? The space bar!"
]

NEBULAE = {"Orion":(1340,-220),"Eagle":(7000,0),"Helix":(695,280),
           "Crab":(6500,190),"Skull":(4200,-500)}

SHOP = {"Dark Crystal":500,"Warp Core":2000,"Quantum Shield":1500,
        "Space Pizza":50,"Anomaly Scanner":800,"Research Data":400}

SHIP_NAMES = ["Star Explorer","Cosmic Wanderer","Nebula Rider",
              "Void Seeker","Galaxy Hopper","Starlight","Dark Star"]

SPACE_FACTS = [
    "A day on Venus is longer than a year.",
    "Saturn's rings are made of ice and rock.",
    "Jupiter is the largest planet.",
    "Space is completely silent.",
    "There are more stars than grains of sand."
]

SPACE_WEATHER = [
    "Solar winds are calm ☀️",
    "Cosmic radiation is normal",
    "A solar flare just passed!",
    "Perfect conditions for travel!",
    "Auroras visible today!"
]

# ============================================
# Quest system
# ============================================

quest = {"name":"Fly 500 km","type":"distance","goal":500,"reward":200}
quest_progress = 0

def gen_quest():
    global quest, quest_progress
    qs = [
        {"name":"Fly 500 km","type":"distance","goal":500,"reward":200},
        {"name":"Earn 1000 credits","type":"credits","goal":1000,"reward":300},
        {"name":"Mine 100 fuel","type":"mine","goal":100,"reward":250},
        {"name":"Visit 2 planets","type":"planets","goal":2,"reward":150},
        {"name":"Tell 3 jokes","type":"jokes","goal":3,"reward":100}
    ]
    quest = random.choice(qs)
    quest_progress = 0

def show_quest():
    print(f"\n📋 QUEST: {quest['name']} ({quest_progress}/{quest['goal']}) - Reward: {quest['reward']}cr")

def check_quest():
    global quest_progress, quest
    if quest_progress >= quest["goal"]:
        print(f"\n🎯 QUEST COMPLETE! +{quest['reward']} credits!")
        p["credits"] += quest["reward"]
        p["quests_completed"] += 1
        if p["quests_completed"] >= 10:
            unlock_ach("quest_master")
        gen_quest()

# ============================================
# Helper functions
# ============================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(text):
    print("\n" + "=" * 50 + f"\n  {text}\n" + "=" * 50)

def dist(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def unlock_ach(key):
    if key in ACHIEVEMENTS and key not in p["achievements"]:
        p["achievements"].append(key)
        print(f"\n🎉 {ACHIEVEMENTS[key]} 🎉\n")
        time.sleep(0.8)

def crew_xp(amount):
    for m in crew:
        m["xp"] += amount
        if m["xp"] >= m["level"] * 100:
            m["xp"] = 0
            m["level"] += 1
            print(f"\n🌟 {m['name']} is now level {m['level']}!")
            p["credits"] += random.randint(100, 300)

def check_luck():
    today = datetime.now().date()
    if p["last_played"] != str(today):
        p["luck"] = random.randint(1, 10)
        p["last_played"] = str(today)
        print(f"\n🍀 Luck: {'⭐' * p['luck']}")
        if p["luck"] >= 8:
            print("🌟 Lucky day!")
            unlock_ach("lucky")
        elif p["luck"] >= 5:
            print("✨ Good day")
        else:
            print("🌙 Quiet day")
        time.sleep(0.5)

def find_pet():
    pet = random.choice(PETS)
    if pet not in p["pets"]:
        p["pets"].append(pet)
        print(f"\n🐾 A {pet} joined your crew!")
        unlock_ach("pet_finder")
        p["morale"] = min(100, p["morale"] + 10)
        p["crew_happiness"] = min(100, p.get("crew_happiness", 80) + 5)

def tell_joke():
    print(f"\n😂 {random.choice(JOKES)}")
    p["morale"] = min(100, p["morale"] + 5)
    p["crew_happiness"] = min(100, p.get("crew_happiness", 80) + 3)
    p["jokes_told"] += 1
    if p["jokes_told"] >= 10:
        unlock_ach("comedian")

def get_input(prompt, default=None):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\n👋 Later!")
        exit()

def show_morale():
    filled = int(20 * p["morale"] / 100)
    bar = "█" * filled + "░" * (20 - filled)
    mood = "😄" if p["morale"] > 70 else "😐" if p["morale"] > 40 else "😞"
    print(f"😊 Morale: [{bar}] {p['morale']}% {mood}")

def get_planet_name(coords):
    for name, c in PLANETS.values():
        if c == coords:
            return name
    return "Unknown"

def show_happiness():
    filled = int(20 * p.get("crew_happiness", 80) / 100)
    bar = "█" * filled + "░" * (20 - filled)
    print(f"👥 Happiness: [{bar}] {p.get('crew_happiness', 80)}%")

def alien_encounter():
    print("\n👽 A friendly alien appears!")
    time.sleep(0.5)
    alien = random.choice(["Zorg","Blip","Nova","Kratos"])
    print(f"The alien is {alien}.")
    p["aliens_met"] += 1
    if p["aliens_met"] >= 10:
        unlock_ach("alien_friend")
    gift = random.choice(["Crystal","Hat","Flower","Candy"])
    print(f"\n🎁 {alien} gives you: {gift}!")
    p["inventory"].append(gift)
    p["credits"] += random.randint(20, 80)

def name_ship():
    header("🚢 NAME YOUR SHIP")
    print(f"Current: {p['ship_name']}")
    for i, name in enumerate(SHIP_NAMES, 1):
        print(f"{i}. {name}")
    print(f"{len(SHIP_NAMES)+1}. Custom")
    choice = get_input("Choice: ", "1")
    if choice.isdigit() and 1 <= int(choice) <= len(SHIP_NAMES):
        p["ship_name"] = SHIP_NAMES[int(choice)-1]
        print(f"\n✅ Ship renamed to {p['ship_name']}!")
        unlock_ach("ship_namer")
    elif choice == str(len(SHIP_NAMES)+1):
        new_name = get_input("Enter name: ")
        if new_name.strip():
            p["ship_name"] = new_name.strip()
            print(f"\n✅ Ship renamed to {p['ship_name']}!")
            unlock_ach("ship_namer")

# ============================================
# Game functions
# ============================================

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
    header(f"🚀 {p['ship_name']} - LAUNCH")
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
    p["total_distance"] += distance
    print(f"\n📏 Distance: {distance:,.0f} million km")
    quest_progress += distance

    if distance > p["record"]:
        p["record"] = distance
        print("🏆 New record!")

    if random.random() < 0.25 + (p["luck"] * 0.01):
        event = random.choice(["wormhole","treasure","pet","joke","alien"])
        if event == "wormhole":
            distance *= 0.6
            print("🌀 Wormhole shortcut!")
        elif event == "treasure":
            bonus = random.randint(100, 300) + (p["luck"] * 10)
            p["credits"] += bonus
            if bonus > p["biggest_treasure"]:
                p["biggest_treasure"] = bonus
                print(f"💰 BIGGEST TREASURE! +{bonus}cr!")
            else:
                print(f"💰 Found treasure! +{bonus}cr!")
        elif event == "pet":
            find_pet()
        elif event == "joke":
            tell_joke()
        elif event == "alien":
            alien_encounter()

    fuel_needed = distance * 0.5
    if TECH["Fuel Efficiency"]["owned"]:
        fuel_needed *= 0.9
        print("⛽ Fuel efficiency active!")

    if p["fuel"] < fuel_needed:
        print(f"\n⛽ Need {fuel_needed:.0f} fuel, have {p['fuel']:.0f}")
        print("1. Mine  2. Buy  3. Abort")
        choice = get_input("Choice: ", "3")
        if choice == "3":
            print("Aborted.")
            return
        elif choice == "1":
            if random.random() < 0.6 + (p["luck"] * 0.02):
                gained = random.randint(200, 800)
                p["fuel"] += gained
                p["total_fuel_collected"] += gained
                p["asteroids_mined"] += 1
                print(f"✅ Mined {gained} fuel!")
                if p["total_fuel_collected"] >= 5000:
                    unlock_ach("fuel_horder")
                if p["asteroids_mined"] >= 50:
                    unlock_ach("miner")
            else:
                lost = random.randint(50, 200)
                p["fuel"] = max(0, p["fuel"] - lost)
                print(f"💥 Lost {lost} fuel!")
        elif choice == "2":
            try:
                amount = int(get_input("How much? ", "100"))
                cost = amount * 2
                if p["credits"] >= cost:
                    p["credits"] -= cost
                    p["fuel"] += amount
                    print(f"✅ Bought {amount} fuel!")
                else:
                    print("Not enough credits!")
            except ValueError:
                print("Invalid!")
        return

    p["fuel"] -= fuel_needed
    earned = int(distance * 0.8 + 50 + (p["luck"] * 2))
    p["credits"] += earned
    p["missions"] += 1
    p["streak"] += 1
    p["morale"] = min(100, p["morale"] + random.randint(5, 15))
    p["crew_happiness"] = min(100, p.get("crew_happiness", 80) + 3)

    header("✅ MISSION COMPLETE")
    print(f"💰 +{earned} credits")
    print(f"⛽ Fuel left: {p['fuel']:.0f}")
    show_morale()
    show_happiness()
    print(f"📊 Missions: {p['missions']} | Streak: {p['streak']}")

    if p["missions"] == 1:
        unlock_ach("first_mission")
    if p["credits"] >= 10000:
        unlock_ach("millionaire")
    if p["missions"] >= 50:
        unlock_ach("legend")
    if p["streak"] >= 5:
        unlock_ach("streak")
    if p["record"] >= 2000:
        unlock_ach("explorer")
    if p["total_distance"] >= 10000:
        unlock_ach("traveler")
    if len(p["inventory"]) >= 10:
        unlock_ach("collector")

    if start_name != "Unknown" and start_name not in p["visited_planets"]:
        p["visited_planets"].append(start_name)
    if end_name != "Unknown" and end_name not in p["visited_planets"]:
        p["visited_planets"].append(end_name)
    
    all_planets = [name for name, _ in PLANETS.values()]
    if len(set(p["visited_planets"]) & set(all_planets)) >= len(all_planets):
        unlock_ach("planet_lover")

    check_quest()
    crew_xp(20)

def bounty():
    check_luck()
    header("💰 BOUNTY HUNTING")
    print(f"🏆 Rank: {p['rank']}")
    available = [b for b in BOUNTIES if b["level"] <= p["rank"] + 1]
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
    my_hp = target["hp"] + (p["luck"] // 3)
    enemy_hp = target["hp"]
    if TECH["Shield Tech"]["owned"]:
        my_hp += 2
        print("🛡️ Shield active!")
    while my_hp > 0 and enemy_hp > 0:
        print(f"\n❤️ You: {my_hp} | {target['name']}: {enemy_hp}")
        action = get_input("1. Attack  2. Dodge  3. Use item: ", "1")
        if action == "1":
            dmg = random.randint(2, 6) + (p["luck"] // 5)
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
            if random.random() < 0.5 + (p["luck"] * 0.02):
                print("🛡️ Dodged!")
            else:
                counter = random.randint(2, 5)
                my_hp -= counter
                print(f"💥 Took {counter} damage!")
        elif action == "3":
            if "Space Pizza" in p["inventory"]:
                p["inventory"].remove("Space Pizza")
                heal = random.randint(3, 8)
                max_hp = target["hp"] + (p["luck"] // 3)
                if TECH["Shield Tech"]["owned"]:
                    max_hp += 2
                my_hp = min(max_hp, my_hp + heal)
                print(f"💊 Healed {heal} health!")
            else:
                print("❌ No items!")
    if my_hp > 0:
        bonus = int(target["reward"] * (1 + p["luck"] * 0.01))
        p["credits"] += bonus
        p["pirates_killed"] += 1
        print(f"\n🎉 VICTORY! +{bonus} credits!")
        if target["level"] == p["rank"]:
            p["rank"] += 1
            print(f"🏆 Rank up! Now {p['rank']}")
        unlock_ach("bounty_hunter")
        if p["pirates_killed"] >= 10:
            unlock_ach("pirate_slayer")
        crew_xp(30)
    else:
        print("\n💀 Defeated! Lost 100 credits")
        p["credits"] = max(0, p["credits"] - 100)

def research():
    header("🧪 RESEARCH")
    print(f"📚 Points: {p['research']}\n")
    for i, (name, data) in enumerate(TECH.items(), 1):
        status = "✅" if data["owned"] else f"💰 {data['cost']}pts"
        print(f"{i}. {name} - {status}")
    print("\n5. Convert 100cr → 20pts  6. Back")
    choice = get_input("Choice: ", "6")
    if choice == "6":
        return
    elif choice.isdigit() and 1 <= int(choice) <= 4:
        name, data = list(TECH.items())[int(choice)-1]
        if not data["owned"] and p["research"] >= data["cost"]:
            p["research"] -= data["cost"]
            data["owned"] = True
            print(f"\n✨ Unlocked {name}!")
            if all(t["owned"] for t in TECH.values()):
                unlock_ach("researcher")
        else:
            print("❌ Not enough points or already owned!")
    elif choice == "5":
        if p["credits"] >= 100:
            p["credits"] -= 100
            p["research"] += 20
            print("✅ Converted!")
        else:
            print("❌ Not enough credits!")

def trade():
    header("👽 ALIEN TRADE")
    print(f"💰 Credits: {p['credits']}\n")
    for i, (item, price) in enumerate(SHOP.items(), 1):
        print(f"{i}. {item} - {price}cr")
    choice = get_input("Buy (number or q): ", "q")
    if choice.lower() == 'q':
        return
    elif choice.isdigit() and 1 <= int(choice) <= len(SHOP):
        item, price = list(SHOP.items())[int(choice)-1]
        if p["credits"] >= price:
            p["credits"] -= price
            p["inventory"].append(item)
            print(f"\n✨ Bought {item}!")
            if len(p["inventory"]) >= 10:
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
        p["nebulae_visited"] += 1
        if p["nebulae_visited"] >= 5:
            unlock_ach("nebula_expert")
        roll = random.random()
        if roll < 0.6 + (p["luck"] * 0.02):
            fuel = random.randint(300, 1500) + (p["luck"] * 10)
            p["fuel"] += fuel
            p["total_fuel_collected"] += fuel
            print(f"⛽ Found {fuel} fuel!")
            if p["total_fuel_collected"] >= 5000:
                unlock_ach("fuel_horder")
            unlock_ach("fuel_finder")
        elif roll < 0.8:
            treasure = random.choice(["Ancient Relic","Crystal Shard","Star Chart"])
            p["inventory"].append(treasure)
            print(f"🔮 Found {treasure}!")
            p["research"] += 20 + (p["luck"] * 2)
            if len(p["inventory"]) >= 10:
                unlock_ach("collector")
        else:
            print("💨 Empty nebula...")
        if random.random() < 0.08:
            find_pet()
    else:
        print("Invalid!")

def random_fun():
    header("🎲 RANDOM FUN")
    action = random.choice(["joke","pet","luck","treasure","dance","fact","weather","alien"])
    if action == "joke":
        tell_joke()
    elif action == "pet":
        find_pet()
    elif action == "luck":
        check_luck()
    elif action == "treasure":
        treasure = random.randint(50, 200) + (p["luck"] * 5)
        p["credits"] += treasure
        print(f"\n💰 Found {treasure} credits!")
    elif action == "dance":
        gain = random.randint(3, 10)
        p["morale"] = min(100, p["morale"] + gain)
        p["crew_happiness"] = min(100, p.get("crew_happiness", 80) + 2)
        print(f"\n💃 Dance party! Morale +{gain}!")
    elif action == "fact":
        print(f"\n📚 {random.choice(SPACE_FACTS)}")
    elif action == "weather":
        print(f"\n🌦️ {random.choice(SPACE_WEATHER)}")
    elif action == "alien":
        alien_encounter()

def help():
    header("📖 CAPTAIN'S GUIDE")
    print(f"\n🚢 Ship: {p['ship_name']}")
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

🚀 HAVE FUN!
    """)

# ============================================
# Display
# ============================================

def stats():
    header("📊 YOUR STATS")
    print(f"🚢 Ship: {p['ship_name']}")
    print(f"🚀 Missions: {p['missions']} | 🔥 Streak: {p['streak']}")
    print(f"⛽ Fuel: {p['fuel']:.0f} | 💰 Credits: {p['credits']}")
    print(f"📚 Research: {p['research']}")
    show_morale()
    show_happiness()
    print(f"🏆 Rank: {p['rank']} | 📏 Furthest: {p['record']:,.0f} km")
    print(f"🍀 Luck: {'⭐'*p['luck']} | 🏅 Achievements: {len(p['achievements'])}")
    print(f"🪐 Planets: {len(p.get('visited_planets', []))}")
    print(f"⛽ Fuel Collected: {p.get('total_fuel_collected', 0)}")
    print(f"💎 Biggest Treasure: {p.get('biggest_treasure', 0)}")
    print(f"🪨 Asteroids: {p.get('asteroids_mined', 0)}")
    print(f"👽 Aliens: {p.get('aliens_met', 0)}")
    print(f"📋 Quests: {p.get('quests_completed', 0)}")

    if p["achievements"]:
        print("\n🏅 Achievements:")
        for a in p["achievements"]:
            print(f"  • {ACHIEVEMENTS[a]}")
    if p["pets"]:
        print("\n🐾 Pets:")
        for pet in p["pets"]:
            print(f"  • {pet}")
    if p["inventory"]:
        print("\n📦 Inventory:")
        for item in p["inventory"]:
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

# ============================================
# Save/Load
# ============================================

def save():
    data = {k: v for k, v in p.items() if k not in ["achievements","inventory","pets","visited_planets"]}
    data.update({"achievements":p["achievements"],"inventory":p["inventory"],"pets":p["pets"],"visited_planets":p.get("visited_planets",[])})
    data["crew"] = crew
    data["tech"] = TECH
    try:
        with open("save.json", "w") as f:
            json.dump(data, f)
        print("\n💾 Saved!")
    except:
        print("❌ Save failed!")

def load():
    global p, crew, TECH
    try:
        with open("save.json", "r") as f:
            data = json.load(f)
        for key in data:
            if key in p and key not in ["achievements","inventory","pets","visited_planets"]:
                p[key] = data[key]
        p["achievements"] = data.get("achievements", [])
        p["inventory"] = data.get("inventory", [])
        p["pets"] = data.get("pets", [])
        p["visited_planets"] = data.get("visited_planets", [])
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

# ============================================
# Main
# ============================================

def main():
    gen_quest()
    p["sessions"] = p.get("sessions", 0) + 1
    clear()

    print("""
    ╔════════════════════════════════════════════╗
    ║   🚀 SPACE ADVENTURE                     ║
    ║        A game I made for fun             ║
    ║     "The cosmos is yours to explore!"    ║
    ╚════════════════════════════════════════════╝
    """)

    print(f"🌟 Hey, Captain!")
    print(f"🚢 Ship: {p['ship_name']}")
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
        print("13. 📋 Quest     14. ❌ Quit")
        print("=" * 40)
        
        print(f"\n📊 Quick: Fuel: {p['fuel']:.0f} | Credits: {p['credits']} | Missions: {p['missions']}")

        choice = get_input("\nChoice: ", "14")

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
        elif choice == "14":
            print("\n👋 See you later, Captain!")
            print("⭐ The stars will be waiting.")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

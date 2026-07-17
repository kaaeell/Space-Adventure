"""
🚀 SPACE ADVENTURE
A space game I made for fun - explore, trade, hunt bounties!
"""

import math
import random
import time
import json
import os
from datetime import datetime

# ============================================
# Player data
# ============================================

player = {
    "fuel": 5000,
    "credits": 1000,
    "missions": 0,
    "streak": 0,
    "morale": 80,
    "research": 0,
    "rank": 1,
    "record": 0,
    "total_distance": 0,
    "achievements": [],
    "inventory": [],
    "pets": [],
    "luck": 0,
    "last_played": None,
    "pirates_killed": 0,
    "nebulae_visited": 0,
    "jokes_told": 0,
    "sessions": 0,
    "ship_name": "Star Explorer",
    "favorite_planet": "Earth"  # NEW
}

# ============================================
# Your crew
# ============================================

crew = [
    {"name": "Rex", "role": "Captain", "level": 1, "xp": 0},
    {"name": "Jen", "role": "Engineer", "level": 1, "xp": 0},
    {"name": "Zoe", "role": "Navigator", "level": 1, "xp": 0},
    {"name": "Kim", "role": "Scientist", "level": 1, "xp": 0},
    {"name": "Mack", "role": "Gunner", "level": 1, "xp": 0}
]

# ============================================
# Game world
# ============================================

PLANETS = {
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

BOUNTIES = [
    {"name": "Red Pirate", "reward": 500, "level": 1, "hp": 3},
    {"name": "Shadow Corsair", "reward": 1000, "level": 2, "hp": 5},
    {"name": "Void Reaver", "reward": 2000, "level": 3, "hp": 7},
    {"name": "Galactic Menace", "reward": 3500, "level": 4, "hp": 10}
]

TECH = {
    "Fuel Efficiency": {"cost": 100, "owned": False},
    "Warp Drive": {"cost": 200, "owned": False},
    "Shield Tech": {"cost": 150, "owned": False},
    "Scanner Range": {"cost": 120, "owned": False}
}

ACHIEVEMENTS = {
    "first_mission": "Completed your first mission!",
    "explorer": "Traveled over 2000 million km!",
    "fuel_finder": "Found fuel in a nebula!",
    "millionaire": "Earned 10,000 credits!",
    "legend": "Completed 50 missions!",
    "streak": "5 missions in a row!",
    "bounty_hunter": "Defeated a bounty target!",
    "researcher": "Unlocked all research!",
    "pet_finder": "Found a space pet!",
    "lucky": "Had a lucky day!",
    "traveler": "Traveled 10000 km total!",
    "pirate_slayer": "Killed 10 pirates!",
    "nebula_expert": "Visited 5 nebulae!",
    "comedian": "Told 10 jokes!",
    "collector": "Collected 10 items!",
    "ship_namer": "Named your ship!",
    "planet_lover": "Visited all planets!"  # NEW
}

PETS = ["Space Dog", "Robot Cat", "Alien Hamster", "Tiny Dragon",
        "Quantum Fox", "Space Penguin", "Star Octopus", "Nebula Unicorn"]

JOKES = [
    "Why did the star go to school? To get brighter!",
    "What do astronauts use for pants? An asteroid belt!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key? The space bar!",
    "Why did the alien cross the galaxy? To get to the other side!"
]

NEBULAE = {"Orion": (1340,-220), "Eagle": (7000,0), "Helix": (695,280),
           "Crab": (6500,190), "Skull": (4200,-500)}

SHOP = {"Dark Crystal": 500, "Warp Core": 2000, "Quantum Shield": 1500,
        "Space Pizza": 50, "Anomaly Scanner": 800, "Research Data": 400}

SHIP_NAMES = [
    "Star Explorer", "Cosmic Wanderer", "Nebula Rider", 
    "Void Seeker", "Galaxy Hopper", "Starlight", "Dark Star"
]

# NEW: Fun facts about space
SPACE_FACTS = [
    "A day on Venus is longer than a year on Venus.",
    "Saturn's rings are made of ice and rock.",
    "Jupiter is the largest planet in our solar system.",
    "The sun is actually white, not yellow.",
    "Space is completely silent - no air to carry sound!",
    "One million Earths could fit inside the sun."
]

# NEW: Weather in space
SPACE_WEATHER = [
    "Solar winds are calm today ☀️",
    "Cosmic radiation levels are normal",
    "A solar flare just passed by!",
    "The magnetic field is stable",
    "Perfect conditions for space travel!"
]

# ============================================
# Helper functions
# ============================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(text):
    print("\n" + "=" * 50)
    print(f"  {text}")
    print("=" * 50)

def calc_distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def unlock_achievement(key):
    if key in ACHIEVEMENTS and key not in player["achievements"]:
        player["achievements"].append(key)
        print(f"\n🎉 {ACHIEVEMENTS[key]} 🎉\n")
        time.sleep(0.8)

def give_crew_xp(amount):
    for member in crew:
        member["xp"] += amount
        if member["xp"] >= member["level"] * 100:
            member["xp"] = 0
            member["level"] += 1
            print(f"\n🌟 {member['name']} reached level {member['level']}!")
            player["credits"] += random.randint(100, 300)

def check_luck():
    today = datetime.now().date()
    if player["last_played"] != str(today):
        player["luck"] = random.randint(1, 10)
        player["last_played"] = str(today)
        print(f"\n🍀 Luck: {'⭐' * player['luck']}")
        if player["luck"] >= 8:
            print("🌟 Lucky day!")
            unlock_achievement("lucky")
        elif player["luck"] >= 5:
            print("✨ Good day for adventures")
        else:
            print("🌙 Quiet day...")
        time.sleep(0.5)

def find_pet():
    pet = random.choice(PETS)
    if pet not in player["pets"]:
        player["pets"].append(pet)
        print(f"\n🐾 A {pet} joined your crew!")
        unlock_achievement("pet_finder")
        player["morale"] = min(100, player["morale"] + 10)

def tell_joke():
    print(f"\n😂 {random.choice(JOKES)}")
    player["morale"] = min(100, player["morale"] + 5)
    player["jokes_told"] = player.get("jokes_told", 0) + 1
    if player["jokes_told"] >= 10:
        unlock_achievement("comedian")

def get_input(prompt, default=None):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\n👋 Later!")
        exit()

def show_morale():
    filled = int(20 * player["morale"] / 100)
    bar = "█" * filled + "░" * (20 - filled)
    mood = "😄" if player["morale"] > 70 else "😐" if player["morale"] > 40 else "😞"
    print(f"😊 Morale: [{bar}] {player['morale']}% {mood}")

def get_planet_name(coords):
    for name, c in PLANETS.values():
        if c == coords:
            return name
    return "Unknown"

# ============================================
# NEW: Space facts and weather
# ============================================

def show_space_fact():
    print(f"\n📚 Did you know? {random.choice(SPACE_FACTS)}")

def check_space_weather():
    print(f"\n🌦️ Space Weather: {random.choice(SPACE_WEATHER)}")

# ============================================
# Ship naming
# ============================================

def name_ship():
    show_header("🚢 NAME YOUR SHIP")
    print(f"Current name: {player['ship_name']}")
    print("\nChoose a name:")
    for i, name in enumerate(SHIP_NAMES, 1):
        print(f"{i}. {name}")
    print(f"{len(SHIP_NAMES)+1}. Custom name")
    
    choice = get_input("Choice: ", "1")
    if choice.isdigit() and 1 <= int(choice) <= len(SHIP_NAMES):
        player["ship_name"] = SHIP_NAMES[int(choice)-1]
        print(f"\n✅ Ship renamed to {player['ship_name']}!")
        unlock_achievement("ship_namer")
    elif choice == str(len(SHIP_NAMES)+1):
        new_name = get_input("Enter ship name: ")
        if new_name.strip():
            player["ship_name"] = new_name.strip()
            print(f"\n✅ Ship renamed to {player['ship_name']}!")
            unlock_achievement("ship_namer")
        else:
            print("❌ Invalid name!")

# ============================================
# Quick stats
# ============================================

def show_quick_stats():
    print(f"\n📊 Quick Stats:")
    print(f"  Fuel: {player['fuel']:.0f} | Credits: {player['credits']}")
    print(f"  Missions: {player['missions']} | Ship: {player['ship_name']}")

# ============================================
# Game functions
# ============================================

def pick_planets():
    print("\n🪐 WHERE TO?")
    for n, (name, _) in PLANETS.items():
        print(f"{n}. {name}")

    def choose_planet(prompt):
        while True:
            try:
                choice = int(get_input(prompt, "1"))
                if choice in PLANETS:
                    return PLANETS[choice]
                print("Invalid choice!")
            except ValueError:
                print("Enter a number!")

    start = choose_planet("Starting planet: ")
    end = choose_planet("Destination: ")
    return get_planet_name(start), start, get_planet_name(end), end

def do_mission():
    check_luck()
    show_header(f"🚀 {player['ship_name']} - LAUNCH")
    print("1. Known planets")
    print("2. Unknown coordinates")
    print("3. Go back")

    choice = get_input("Choice: ", "3")

    if choice == "3":
        return
    elif choice == "1":
        start_name, start, end_name, end = pick_planets()
    elif choice == "2":
        try:
            print("\n📡 Enter coordinates (million km)")
            start = (float(get_input("Start x: ", "0")), float(get_input("Start y: ", "0")))
            end = (float(get_input("End x: ", "100")), float(get_input("End y: ", "100")))
            start_name, end_name = "Unknown", "Unknown"
        except ValueError:
            print("Invalid coordinates!")
            return
    else:
        print("Invalid choice!")
        return

    distance = calc_distance(start, end)
    player["total_distance"] += distance
    print(f"\n📏 Distance: {distance:,.0f} million km")

    if distance > player["record"]:
        player["record"] = distance
        print("🏆 New record!")

    # Random events
    if random.random() < 0.25 + (player["luck"] * 0.01):
        event = random.choice(["wormhole", "treasure", "pet", "joke"])
        if event == "wormhole":
            distance *= 0.6
            print("🌀 Wormhole shortcut!")
        elif event == "treasure":
            bonus = random.randint(100, 300) + (player["luck"] * 10)
            player["credits"] += bonus
            print(f"💰 Found treasure! +{bonus} credits!")
        elif event == "pet":
            find_pet()
        elif event == "joke":
            tell_joke()

    fuel_needed = distance * 0.5
    if TECH["Fuel Efficiency"]["owned"]:
        fuel_needed *= 0.9
        print("⛽ Fuel efficiency active!")

    if player["fuel"] < fuel_needed:
        print(f"\n⛽ Need {fuel_needed:.0f} fuel, have {player['fuel']:.0f}")
        print("1. Mine asteroid")
        print("2. Buy fuel")
        print("3. Abort")
        choice = get_input("Choice: ", "3")

        if choice == "3":
            print("Mission aborted.")
            return
        elif choice == "1":
            if random.random() < 0.6 + (player["luck"] * 0.02):
                gained = random.randint(200, 800)
                player["fuel"] += gained
                print(f"✅ Mined {gained} fuel!")
            else:
                lost = random.randint(50, 200)
                player["fuel"] = max(0, player["fuel"] - lost)
                print(f"💥 Lost {lost} fuel!")
        elif choice == "2":
            try:
                amount = int(get_input("How much? ", "100"))
                cost = amount * 2
                if player["credits"] >= cost:
                    player["credits"] -= cost
                    player["fuel"] += amount
                    print(f"✅ Bought {amount} fuel!")
                else:
                    print("Not enough credits!")
            except ValueError:
                print("Invalid amount!")
        return

    player["fuel"] -= fuel_needed
    earned = int(distance * 0.8 + 50 + (player["luck"] * 2))
    player["credits"] += earned
    player["missions"] += 1
    player["streak"] += 1
    player["morale"] = min(100, player["morale"] + random.randint(5, 15))

    show_header("✅ MISSION COMPLETE")
    print(f"💰 +{earned} credits")
    print(f"⛽ Fuel left: {player['fuel']:.0f}")
    show_morale()
    print(f"📊 Missions: {player['missions']} | Streak: {player['streak']}")

    # Check achievements
    if player["missions"] == 1:
        unlock_achievement("first_mission")
    if player["credits"] >= 10000:
        unlock_achievement("millionaire")
    if player["missions"] >= 50:
        unlock_achievement("legend")
    if player["streak"] >= 5:
        unlock_achievement("streak")
    if player["record"] >= 2000:
        unlock_achievement("explorer")
    if player["total_distance"] >= 10000:
        unlock_achievement("traveler")
    if len(player["inventory"]) >= 10:
        unlock_achievement("collector")

    # NEW: Track visited planets
    if start_name != "Unknown" and start_name not in player.get("visited_planets", []):
        if "visited_planets" not in player:
            player["visited_planets"] = []
        player["visited_planets"].append(start_name)
    if end_name != "Unknown" and end_name not in player.get("visited_planets", []):
        if "visited_planets" not in player:
            player["visited_planets"] = []
        player["visited_planets"].append(end_name)
    
    # Check if all planets visited
    all_planets = [name for name, _ in PLANETS.values()]
    visited = player.get("visited_planets", [])
    if len(set(visited) & set(all_planets)) >= len(all_planets):
        unlock_achievement("planet_lover")

    give_crew_xp(20)

def hunt_bounty():
    check_luck()
    show_header("💰 BOUNTY HUNTING")
    print(f"🏆 Rank: {player['rank']}")

    available = [b for b in BOUNTIES if b["level"] <= player["rank"] + 1]
    if not available:
        print("No bounties available!")
        return

    print("\n🎯 TARGETS:")
    for i, target in enumerate(available[:4], 1):
        print(f"{i}. {target['name']} - 💰 {target['reward']} (Lv.{target['level']})")

    choice = get_input("Choose: ", "1")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(available[:4]):
        return

    target = available[int(choice)-1]
    print(f"\n⚔️ FIGHTING {target['name']}...")
    time.sleep(0.5)

    my_hp = target["hp"] + (player["luck"] // 3)
    enemy_hp = target["hp"]

    if TECH["Shield Tech"]["owned"]:
        my_hp += 2
        print("🛡️ Shield active!")

    while my_hp > 0 and enemy_hp > 0:
        print(f"\n❤️ You: {my_hp} | {target['name']}: {enemy_hp}")
        action = get_input("1. Attack  2. Dodge  3. Use item: ", "1")

        if action == "1":
            damage = random.randint(2, 6) + (player["luck"] // 5)
            if TECH["Warp Drive"]["owned"]:
                damage += 1
            enemy_hp -= damage
            print(f"⚡ Hit for {damage}!")
            if enemy_hp > 0:
                counter = random.randint(1, 4)
                if TECH["Shield Tech"]["owned"]:
                    counter = max(1, counter - 1)
                my_hp -= counter
                print(f"💥 Took {counter} damage!")
        elif action == "2":
            if random.random() < 0.5 + (player["luck"] * 0.02):
                print("🛡️ Dodged!")
            else:
                counter = random.randint(2, 5)
                my_hp -= counter
                print(f"💥 Took {counter} damage!")
        elif action == "3":
            if "Space Pizza" in player["inventory"]:
                player["inventory"].remove("Space Pizza")
                heal = random.randint(3, 8)
                max_hp = target["hp"] + (player["luck"] // 3)
                if TECH["Shield Tech"]["owned"]:
                    max_hp += 2
                my_hp = min(max_hp, my_hp + heal)
                print(f"💊 Healed {heal} health!")
            else:
                print("❌ No items!")

    if my_hp > 0:
        bonus = int(target["reward"] * (1 + player["luck"] * 0.01))
        player["credits"] += bonus
        player["pirates_killed"] = player.get("pirates_killed", 0) + 1
        print(f"\n🎉 VICTORY! +{bonus} credits!")
        if target["level"] == player["rank"]:
            player["rank"] += 1
            print(f"🏆 Rank up! Now {player['rank']}")
        unlock_achievement("bounty_hunter")
        if player["pirates_killed"] >= 10:
            unlock_achievement("pirate_slayer")
        give_crew_xp(30)
    else:
        print("\n💀 Defeated! Lost 100 credits")
        player["credits"] = max(0, player["credits"] - 100)

def research_lab():
    show_header("🧪 RESEARCH")
    print(f"📚 Points: {player['research']}\n")

    for i, (name, data) in enumerate(TECH.items(), 1):
        status = "✅" if data["owned"] else f"💰 {data['cost']}pts"
        print(f"{i}. {name} - {status}")

    print("\n5. Convert 100 credits → 20 points")
    print("6. Back")

    choice = get_input("Choice: ", "6")
    if choice == "6":
        return
    elif choice.isdigit() and 1 <= int(choice) <= 4:
        name, data = list(TECH.items())[int(choice)-1]
        if not data["owned"] and player["research"] >= data["cost"]:
            player["research"] -= data["cost"]
            data["owned"] = True
            print(f"\n✨ Unlocked {name}!")
            if all(t["owned"] for t in TECH.values()):
                unlock_achievement("researcher")
        else:
            print("❌ Not enough points or already owned!")
    elif choice == "5":
        if player["credits"] >= 100:
            player["credits"] -= 100
            player["research"] += 20
            print("✅ Converted!")
        else:
            print("❌ Not enough credits!")

def trade():
    show_header("👽 ALIEN TRADE")
    print(f"💰 Credits: {player['credits']}\n")

    for i, (item, price) in enumerate(SHOP.items(), 1):
        print(f"{i}. {item} - {price} credits")

    choice = get_input("Buy (number or q): ", "q")
    if choice.lower() == 'q':
        return
    elif choice.isdigit() and 1 <= int(choice) <= len(SHOP):
        item, price = list(SHOP.items())[int(choice)-1]
        if player["credits"] >= price:
            player["credits"] -= price
            player["inventory"].append(item)
            print(f"\n✨ Bought {item}!")
            if len(player["inventory"]) >= 10:
                unlock_achievement("collector")
        else:
            print("❌ Not enough credits!")

def explore_nebula():
    show_header("🌌 NEBULA EXPLORATION")
    for i, name in enumerate(NEBULAE.keys(), 1):
        print(f"{i}. {name}")

    choice = get_input("Choose: ", "1")
    if choice.isdigit() and 1 <= int(choice) <= len(NEBULAE):
        name = list(NEBULAE.keys())[int(choice)-1]
        print(f"\n🚀 Entering {name}...")
        time.sleep(1)

        player["nebulae_visited"] = player.get("nebulae_visited", 0) + 1
        if player["nebulae_visited"] >= 5:
            unlock_achievement("nebula_expert")

        roll = random.random()
        if roll < 0.6 + (player["luck"] * 0.02):
            fuel = random.randint(300, 1500) + (player["luck"] * 10)
            player["fuel"] += fuel
            print(f"⛽ Found {fuel} fuel!")
            unlock_achievement("fuel_finder")
        elif roll < 0.8:
            treasure = random.choice(["Ancient Relic", "Crystal Shard", "Star Chart"])
            player["inventory"].append(treasure)
            print(f"🔮 Found {treasure}!")
            player["research"] += 20 + (player["luck"] * 2)
            if len(player["inventory"]) >= 10:
                unlock_achievement("collector")
        else:
            print("💨 Empty nebula...")

        if random.random() < 0.08:
            find_pet()
    else:
        print("Invalid!")

def random_activity():
    show_header("🎲 RANDOM FUN")
    action = random.choice(["joke", "pet", "luck", "treasure", "dance", "fact", "weather"])
    
    if action == "joke":
        tell_joke()
    elif action == "pet":
        find_pet()
    elif action == "luck":
        check_luck()
    elif action == "treasure":
        treasure = random.randint(50, 200) + (player["luck"] * 5)
        player["credits"] += treasure
        print(f"\n💰 Found {treasure} credits!")
    elif action == "dance":
        gain = random.randint(3, 10)
        player["morale"] = min(100, player["morale"] + gain)
        print(f"\n💃 Dance party! Morale +{gain}!")
    elif action == "fact":
        show_space_fact()
    elif action == "weather":
        check_space_weather()

def show_help():
    show_header("📖 CAPTAIN'S GUIDE")
    print(f"\n🚢 Your ship: {player['ship_name']}")
    print("""
🎮 HOW TO PLAY:
   • Do missions for credits and fuel
   • Research tech upgrades
   • Hunt bounties for big rewards
   • Explore nebulae for treasures
   • Trade with aliens
   • Collect pets!

💡 TIPS:
   • Save often
   • Check daily luck
   • Keep fuel above 30%
   • Level up your crew
   • Get achievements!

🌌 NEW FEATURES:
   • Space facts to learn!
   • Space weather updates!
   • Visit all planets for an achievement!
   • Random fun has more activities!

🚀 HAVE FUN!
    """)

# ============================================
# Display functions
# ============================================

def show_stats():
    show_header("📊 YOUR STATS")
    print(f"🚢 Ship: {player['ship_name']}")
    print(f"🚀 Missions: {player['missions']} | 🔥 Streak: {player['streak']}")
    print(f"⛽ Fuel: {player['fuel']:.0f} | 💰 Credits: {player['credits']}")
    print(f"📚 Research: {player['research']}")
    show_morale()
    print(f"🏆 Rank: {player['rank']} | 📏 Furthest: {player['record']:,.0f} km")
    print(f"🍀 Luck: {'⭐'*player['luck']} | 🏅 Achievements: {len(player['achievements'])}")
    print(f"🪐 Planets Visited: {len(player.get('visited_planets', []))}")

    if player["achievements"]:
        print("\n🏅 Achievements:")
        for a in player["achievements"]:
            print(f"  • {ACHIEVEMENTS[a]}")
    if player["pets"]:
        print("\n🐾 Pets:")
        for p in player["pets"]:
            print(f"  • {p}")
    if player["inventory"]:
        print("\n📦 Inventory:")
        for i in player["inventory"]:
            print(f"  • {i}")

def show_crew():
    show_header("👥 YOUR CREW")
    for member in crew:
        print(f"\n🌟 {member['name']} - Lv.{member['level']} ({member['role']})")
        print(f"   XP: {member['xp']}/{member['level']*100}")
        if member['level'] * 100 > 0:
            prog = int((member['xp'] / (member['level'] * 100)) * 10)
            bar = "█" * prog + "░" * (10 - prog)
            print(f"   [{bar}]")
        else:
            print(f"   [░░░░░░░░░░]")

# ============================================
# Save/Load
# ============================================

def save_game():
    data = {
        "fuel": player["fuel"],
        "credits": player["credits"],
        "missions": player["missions"],
        "streak": player["streak"],
        "morale": player["morale"],
        "research": player["research"],
        "rank": player["rank"],
        "record": player["record"],
        "total_distance": player["total_distance"],
        "achievements": player["achievements"],
        "inventory": player["inventory"],
        "pets": player["pets"],
        "luck": player["luck"],
        "last_played": player["last_played"],
        "pirates_killed": player.get("pirates_killed", 0),
        "nebulae_visited": player.get("nebulae_visited", 0),
        "jokes_told": player.get("jokes_told", 0),
        "sessions": player.get("sessions", 0),
        "ship_name": player.get("ship_name", "Star Explorer"),
        "visited_planets": player.get("visited_planets", []),
        "crew": crew,
        "tech": TECH
    }
    try:
        with open("save.json", "w") as f:
            json.dump(data, f)
        print("\n💾 Saved!")
    except Exception as e:
        print(f"❌ Save failed: {e}")

def load_game():
    global player, crew, TECH
    try:
        with open("save.json", "r") as f:
            data = json.load(f)

        for key in data:
            if key in player and key not in ["achievements", "inventory", "pets"]:
                player[key] = data[key]

        player["achievements"] = data.get("achievements", [])
        player["inventory"] = data.get("inventory", [])
        player["pets"] = data.get("pets", [])
        player["visited_planets"] = data.get("visited_planets", [])

        if "crew" in data:
            for i, member in enumerate(data["crew"]):
                if i < len(crew):
                    crew[i] = member

        if "tech" in data:
            for name, values in data["tech"].items():
                if name in TECH:
                    TECH[name]["owned"] = values.get("owned", False)

        print("\n📀 Loaded!")
        return True
    except FileNotFoundError:
        print("❌ No save found!")
        return False
    except Exception as e:
        print(f"❌ Load failed: {e}")
        return False

# ============================================
# Main game loop
# ============================================

def main():
    player["sessions"] = player.get("sessions", 0) + 1
    clear_screen()

    print("""
    ╔════════════════════════════════════════════╗
    ║                                          ║
    ║   🚀 SPACE ADVENTURE                     ║
    ║        A game I made for fun             ║
    ║                                          ║
    ║     "The cosmos is yours to explore!"    ║
    ║                                          ║
    ╚════════════════════════════════════════════╝
    """)

    print("🌟 Hey there, Captain!")
    print(f"🚢 Your ship: {player['ship_name']}")
    print("💫 Let's explore the stars.\n")
    time.sleep(0.5)
    check_luck()

    while True:
        print("\n" + "=" * 40)
        print("🌟 MAIN MENU")
        print("=" * 40)
        print("1. 🚀 Mission")
        print("2. 📊 Stats")
        print("3. 👥 Crew")
        print("4. 🧪 Research")
        print("5. 💰 Bounty")
        print("6. 👽 Trade")
        print("7. 🌌 Nebula")
        print("8. 💾 Save")
        print("9. 📀 Load")
        print("10. 🎲 Random")
        print("11. 📖 Help")
        print("12. 🚢 Name Ship")
        print("13. ❌ Quit")
        print("=" * 40)
        
        show_quick_stats()

        choice = get_input("\nChoice: ", "13")

        if choice == "1":
            do_mission()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            show_crew()
        elif choice == "4":
            research_lab()
        elif choice == "5":
            hunt_bounty()
        elif choice == "6":
            trade()
        elif choice == "7":
            explore_nebula()
        elif choice == "8":
            save_game()
        elif choice == "9":
            load_game()
        elif choice == "10":
            random_activity()
        elif choice == "11":
            show_help()
        elif choice == "12":
            name_ship()
        elif choice == "13":
            print("\n👋 See you later, Captain!")
            print("⭐ The stars will be waiting.")
            break
        else:
            print("❌ Not a valid choice!")

if __name__ == "__main__":
    main()

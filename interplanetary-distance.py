"""
🚀 SPACE DISTANCE CALCULATOR
A space adventure game where you explore, trade, and hunt bounties!
"""

import math
import random
import time
import json
import os
from datetime import datetime

# ============================================
# PLAYER DATA
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
    "trophies": [],
    "inventory": [],
    "pets": [],
    "luck": 0,
    "last_play": None
}

# ============================================
# CREW
# ============================================

crew = [
    {"name": "Captain Rex", "skill": "Leadership", "level": 1, "xp": 0},
    {"name": "Engineer Jen", "skill": "Mechanics", "level": 1, "xp": 0},
    {"name": "Navigator Zoe", "skill": "Astrogation", "level": 1, "xp": 0},
    {"name": "Scientist Kim", "skill": "Research", "level": 1, "xp": 0},
    {"name": "Gunner Mack", "skill": "Combat", "level": 1, "xp": 0}
]

# ============================================
# GAME DATA
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
    {"name": "Void Reaver", "reward": 2000, "level": 3, "hp": 7}
]

TECH = {
    "Fuel Efficiency": {"cost": 100, "owned": False},
    "Warp Drive": {"cost": 200, "owned": False},
    "Shield Tech": {"cost": 150, "owned": False}
}

ACHIEVEMENTS = {
    "first": "🌱 First space trip!",
    "explorer": "🌌 Traveled over 2000 million km!",
    "fuel": "⛽ Found fuel in a nebula!",
    "rich": "💰 Space millionaire!",
    "legend": "⭐ Completed 50 missions!",
    "streak": "🔥 5 missions in a row!",
    "bounty": "💰 Defeated a bounty target!",
    "research": "🧠 Unlocked all research!",
    "pet": "🐾 Found a space pet!",
    "lucky": "🍀 Had a lucky day!"
}

PETS = ["🐶 Space Dog", "🐱 Robot Cat", "🐹 Alien Hamster", "🐉 Tiny Dragon", "🦊 Quantum Fox", "🐧 Space Penguin"]

JOKES = [
    "Why did the star go to school? To get brighter!",
    "What do astronauts use for pants? An asteroid belt!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key? The space bar!",
    "Why did the alien cross the galaxy? To get to the other side!"
]

NEBULAE = {"Orion Nebula": (1340, -220), "Eagle Nebula": (7000, 0), "Helix Nebula": (695, 280)}

# ============================================
# HELPER FUNCTIONS
# ============================================

def distance(p1, p2):
    """Calculate distance between two points"""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def unlock_achievement(key):
    """Unlock an achievement"""
    if key in ACHIEVEMENTS and key not in player["trophies"]:
        player["trophies"].append(key)
        print(f"\n🎉 {ACHIEVEMENTS[key]} 🎉\n")
        time.sleep(0.5)

def gain_crew_xp(amount):
    """Give XP to crew members"""
    for member in crew:
        member["xp"] += amount
        if member["xp"] >= member["level"] * 100:
            member["xp"] = 0
            member["level"] += 1
            print(f"\n🎉 {member['name']} reached level {member['level']}!")
            player["credits"] += random.randint(100, 300)

def check_daily_luck():
    """Check and update daily luck"""
    today = datetime.now().date()
    if player["last_play"] != str(today):
        player["luck"] = random.randint(1, 10)
        player["last_play"] = str(today)
        print(f"\n🍀 Today's luck: {'⭐' * player['luck']}")
        if player["luck"] >= 8:
            print("🌟 You feel extra lucky today!")
            unlock_achievement("lucky")
        elif player["luck"] >= 5:
            print("✨ It's a good day for adventures!")
        else:
            print("🌙 Maybe stay safe today...")
        time.sleep(0.5)

def find_pet():
    """Find a space pet"""
    pet = random.choice(PETS)
    if pet not in player["pets"]:
        player["pets"].append(pet)
        print(f"\n🐾 A {pet} joined your crew!")
        unlock_achievement("pet")
        player["morale"] = min(100, player["morale"] + 10)
    else:
        print(f"\n🐾 {pet} is already part of your crew!")

def tell_joke():
    """Tell a joke"""
    joke = random.choice(JOKES)
    print(f"\n😂 {joke}")
    player["morale"] = min(100, player["morale"] + 5)
    print(f"😊 Crew morale +5! (Now: {player['morale']}%)")

# ============================================
# MAIN GAME FUNCTIONS
# ============================================

def pick_planet():
    """Choose two planets"""
    print("\n🪐 WHERE TO?")
    for num, (name, _) in PLANETS.items():
        print(f"{num}. {name}")

    def choose(question):
        while True:
            try:
                choice = int(input(question))
                if choice in PLANETS:
                    return PLANETS[choice]
                print("Invalid choice! Try again.")
            except ValueError:
                print("Please enter a number!")

    start = choose("Starting planet: ")
    end = choose("Destination planet: ")
    
    # Get planet names
    start_name = "Earth"
    end_name = "Destination"
    for num, (name, coords) in PLANETS.items():
        if coords == start:
            start_name = name
        if coords == end:
            end_name = name
    
    return start_name, start, end_name, end

def start_mission():
    """Start a space mission"""
    check_daily_luck()

    print("\n🚀 PREPARING FOR LAUNCH!")
    print("1. Travel to known planets")
    print("2. Explore unknown coordinates")

    choice = input("Choice: ")

    if choice == "1":
        start_name, start, end_name, end = pick_planet()
    elif choice == "2":
        try:
            start = (float(input("Start x: ")), float(input("Start y: ")))
            end = (float(input("End x: ")), float(input("End y: ")))
            start_name, end_name = "Unknown", "Unknown"
        except ValueError:
            print("❌ Invalid coordinates!")
            return
    else:
        print("❌ Invalid choice!")
        return

    # Calculate distance
    dist = distance(start, end)
    print(f"\n📏 {start_name} to {end_name}: {dist:.0f} million km")

    # Check for new record
    if dist > player["record"]:
        player["record"] = dist
        print("🏆 That's your longest trip yet!")

    # Random events
    if random.random() < 0.25 + (player["luck"] * 0.01):
        event = random.choice(["wormhole", "treasure", "pet", "joke"])
        if event == "wormhole":
            dist *= 0.6
            print("🌀 You found a wormhole shortcut!")
        elif event == "treasure":
            bonus = random.randint(100, 300) + (player["luck"] * 10)
            player["credits"] += bonus
            print(f"💰 Found treasure! +{bonus} credits!")
        elif event == "pet":
            find_pet()
        elif event == "joke":
            tell_joke()

    # Fuel check
    fuel_needed = dist * 0.5
    if player["fuel"] < fuel_needed:
        print(f"\n⛽ Need {fuel_needed:.0f} fuel, have {player['fuel']:.0f}")
        print("1. Mine asteroid (risky)")
        print("2. Buy fuel (2 credits/unit)")
        choice = input("Choice: ")

        if choice == "1":
            if random.random() < 0.6 + (player["luck"] * 0.02):
                gained = random.randint(200, 800)
                player["fuel"] += gained
                print(f"✅ Mined {gained} fuel!")
            else:
                lost = random.randint(50, 200)
                player["fuel"] = max(0, player["fuel"] - lost)
                print(f"💥 Asteroid damaged ship! Lost {lost} fuel")
        elif choice == "2":
            try:
                amount = int(input("How much fuel? "))
                cost = amount * 2
                if player["credits"] >= cost:
                    player["credits"] -= cost
                    player["fuel"] += amount
                    print(f"✅ Bought {amount} fuel!")
                else:
                    print("❌ Not enough credits!")
            except ValueError:
                print("❌ Invalid amount!")
        return

    # Complete mission
    player["fuel"] -= fuel_needed
    earned = int(dist * 0.8 + 50 + (player["luck"] * 2))
    player["credits"] += earned
    player["missions"] += 1
    player["streak"] += 1
    player["morale"] = min(100, player["morale"] + random.randint(5, 15))

    print(f"\n✅ MISSION COMPLETE! +{earned} credits")
    print(f"⛽ Fuel remaining: {player['fuel']:.0f}")
    print(f"😊 Crew morale: {player['morale']}%")

    # Check achievements
    if player["missions"] == 1:
        unlock_achievement("first")
    if player["credits"] >= 10000:
        unlock_achievement("rich")
    if player["missions"] >= 50:
        unlock_achievement("legend")
    if player["streak"] >= 5:
        unlock_achievement("streak")
    if player["record"] >= 2000:
        unlock_achievement("explorer")

    gain_crew_xp(20)

def hunt_bounty():
    """Hunt a bounty target"""
    check_daily_luck()

    print("\n💰 BOUNTY HUNTING")
    print(f"🏆 Your rank: {player['rank']}")

    available = [b for b in BOUNTIES if b["level"] <= player["rank"] + 1]
    if not available:
        print("No bounties available. Complete more missions!")
        return

    print("\n🎯 WANTED:")
    for i, target in enumerate(available[:3], 1):
        print(f"{i}. {target['name']} - 💰 {target['reward']}")

    choice = input("Choose target (number): ")
    if not choice.isdigit() or int(choice) > len(available[:3]):
        return

    target = available[int(choice) - 1]
    print(f"\n⚔️ FIGHTING {target['name']}...")
    time.sleep(0.5)

    # Combat with luck bonus
    my_hp = target["hp"] + (player["luck"] // 3)
    enemy_hp = target["hp"]

    print(f"💪 Luck bonus: +{player['luck']//3} extra health!")

    while my_hp > 0 and enemy_hp > 0:
        print(f"\n❤️ Your health: {my_hp} | {target['name']}: {enemy_hp}")
        action = input("1. Attack  2. Dodge: ")

        if action == "1":
            damage = random.randint(2, 6) + (player["luck"] // 5)
            enemy_hp -= damage
            print(f"⚡ You hit for {damage} damage!")
            if enemy_hp > 0:
                counter = random.randint(1, 4)
                my_hp -= counter
                print(f"💥 They hit back for {counter} damage!")
        elif action == "2":
            if random.random() < 0.5 + (player["luck"] * 0.02):
                print("🛡️ You dodged the attack!")
            else:
                counter = random.randint(2, 5)
                my_hp -= counter
                print(f"💥 Too slow! You took {counter} damage!")
        else:
            print("Invalid action!")

    if my_hp > 0:
        reward_bonus = int(target["reward"] * (1 + player["luck"] * 0.01))
        player["credits"] += reward_bonus
        print(f"\n🎉 VICTORY! +{reward_bonus} credits!")
        if target["level"] == player["rank"]:
            player["rank"] += 1
            print(f"🏆 Rank up! Now {player['rank']}")
        unlock_achievement("bounty")
        gain_crew_xp(30)
    else:
        print("\n💀 Defeated! Lost 100 credits")
        player["credits"] = max(0, player["credits"] - 100)

def do_research():
    """Research new technology"""
    print("\n🧪 RESEARCH LAB")
    print(f"📚 Research points: {player['research']}")

    for i, (name, data) in enumerate(TECH.items(), 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']}pts"
        print(f"{i}. {name} - {status}")
    print("4. Convert 100 credits → 20 research points")

    choice = input("Choose: ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        name, data = list(TECH.items())[int(choice) - 1]
        if not data["owned"]:
            if player["research"] >= data["cost"]:
                player["research"] -= data["cost"]
                data["owned"] = True
                print(f"✨ UNLOCKED {name}!")
                if all(t["owned"] for t in TECH.values()):
                    unlock_achievement("research")
            else:
                print("❌ Not enough research points!")
        else:
            print("❌ Already owned!")
    elif choice == "4":
        if player["credits"] >= 100:
            player["credits"] -= 100
            player["research"] += 20
            print("✅ Converted credits to research points!")
        else:
            print("❌ Not enough credits!")

def trade_with_aliens():
    """Trade with aliens"""
    print("\n👽 ALIEN TRADE")
    print(f"💰 Your credits: {player['credits']}")

    items = {
        "🌌 Dark Crystal": 500,
        "💫 Warp Core": 2000,
        "🔮 Shield": 1500,
        "🍕 Space Pizza": 50
    }

    for i, (item, price) in enumerate(items.items(), 1):
        print(f"{i}. {item} - {price} credits")

    choice = input("Buy (number) or 'q': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        item, price = list(items.items())[int(choice) - 1]
        if player["credits"] >= price:
            player["credits"] -= price
            player["inventory"].append(item)
            print(f"✨ Bought {item}!")
        else:
            print("❌ Not enough credits!")

def explore_nebula():
    """Explore a nebula"""
    print("\n🌌 NEBULA EXPLORATION")
    for i, name in enumerate(NEBULAE.keys(), 1):
        print(f"{i}. {name}")

    choice = input("Choose: ")
    if choice.isdigit() and 1 <= int(choice) <= len(NEBULAE):
        name = list(NEBULAE.keys())[int(choice) - 1]
        print(f"\n🚀 Flying into {name}...")
        time.sleep(1)

        if random.random() < 0.6 + (player["luck"] * 0.02):
            fuel_found = random.randint(300, 1500) + (player["luck"] * 10)
            player["fuel"] += fuel_found
            print(f"⛽ Found {fuel_found} fuel!")
            unlock_achievement("fuel")
        else:
            treasure = random.choice(["Ancient Relic", "Crystal Shard", "Star Chart"])
            player["inventory"].append(treasure)
            print(f"🔮 Found {treasure}!")
            player["research"] += 20 + (player["luck"] * 2)

        if random.random() < 0.08:
            find_pet()
    else:
        print("Invalid choice!")

def random_activity():
    """Do something random for fun"""
    print("\n🎲 RANDOM ACTIVITY!")
    options = ["tell_joke", "find_pet", "check_luck", "find_treasure"]
    action = random.choice(options)

    if action == "tell_joke":
        tell_joke()
    elif action == "find_pet":
        find_pet()
    elif action == "check_luck":
        check_daily_luck()
    elif action == "find_treasure":
        treasure = random.randint(50, 200) + (player["luck"] * 5)
        player["credits"] += treasure
        print(f"\n💰 Found {treasure} credits floating in space!")

# ============================================
# DISPLAY FUNCTIONS
# ============================================

def show_stats():
    """Display all player stats"""
    print("\n" + "=" * 50)
    print("📊 YOUR SPACE STATISTICS")
    print("=" * 50)
    print(f"🚀 Missions completed: {player['missions']}")
    print(f"🔥 Current streak: {player['streak']}")
    print(f"⛽ Fuel remaining: {player['fuel']:.0f}")
    print(f"💰 Credits: {player['credits']}")
    print(f"📚 Research points: {player['research']}")
    print(f"😊 Crew morale: {player['morale']}%")
    print(f"🏆 Bounty rank: {player['rank']}")
    print(f"📏 Furthest distance: {player['record']:.0f} million km")
    print(f"🍀 Today's luck: {'⭐' * player['luck']}")
    print(f"🏅 Achievements: {len(player['trophies'])}")

    if player["trophies"]:
        print("\n🏅 Your achievements:")
        for t in player["trophies"]:
            print(f"  • {ACHIEVEMENTS[t]}")

    if player["pets"]:
        print("\n🐾 Your space pets:")
        for pet in player["pets"]:
            print(f"  • {pet}")

    if player["inventory"]:
        print("\n📦 Your inventory:")
        for item in player["inventory"]:
            print(f"  • {item}")

def show_crew():
    """Display crew information"""
    print("\n👥 YOUR CREW")
    print("=" * 40)
    for member in crew:
        print(f"• {member['name']} - Level {member['level']} ({member['skill']})")
        print(f"  XP: {member['xp']}/{member['level'] * 100}")

# ============================================
# SAVE/LOAD FUNCTIONS
# ============================================

def save_game():
    """Save game progress"""
    data = {
        "fuel": player["fuel"],
        "credits": player["credits"],
        "missions": player["missions"],
        "streak": player["streak"],
        "morale": player["morale"],
        "research": player["research"],
        "rank": player["rank"],
        "record": player["record"],
        "trophies": player["trophies"],
        "inventory": player["inventory"],
        "pets": player["pets"],
        "luck": player["luck"],
        "last_play": player["last_play"],
        "crew": crew,
        "tech": TECH
    }
    try:
        with open("space_save.json", "w") as f:
            json.dump(data, f)
        print("💾 Game saved successfully!")
    except:
        print("❌ Save failed!")

def load_game():
    """Load game progress"""
    global player, crew, TECH
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)

        for key in data:
            if key in player and key not in ["trophies", "inventory", "pets"]:
                player[key] = data[key]
        player["trophies"] = data.get("trophies", [])
        player["inventory"] = data.get("inventory", [])
        player["pets"] = data.get("pets", [])
        crew[:] = data.get("crew", crew)
        
        if "tech" in data:
            for name, values in data["tech"].items():
                if name in TECH:
                    TECH[name]["owned"] = values.get("owned", False)

        print("📀 Game loaded successfully!")
        return True
    except FileNotFoundError:
        print("❌ No save file found!")
        return False
    except Exception as e:
        print(f"❌ Load failed: {e}")
        return False

# ============================================
# MAIN GAME LOOP
# ============================================

def main():
    print("""
    ╔════════════════════════════════════════════╗
    ║   🚀 SPACE DISTANCE CALCULATOR 🚀         ║
    ║           The Space Adventure             ║
    ║               Version 3.5                 ║
    ║                                          ║
    ║     "Explore the cosmos!"                ║
    ╚════════════════════════════════════════════╝
    """)

    print("🌟 Welcome, Captain! The galaxy awaits you!\n")
    check_daily_luck()

    while True:
        print("\n" + "=" * 40)
        print("🌟 MAIN MENU")
        print("=" * 40)
        print("1. 🚀 Start Mission")
        print("2. 📊 View Stats")
        print("3. 👥 View Crew")
        print("4. 🧪 Research Lab")
        print("5. 💰 Hunt Bounty")
        print("6. 👽 Trade with Aliens")
        print("7. 🌌 Explore Nebula")
        print("8. 💾 Save Game")
        print("9. 📀 Load Game")
        print("10. 🎲 Random Fun")
        print("11. ❌ Quit")

        choice = input("\nYour choice: ")

        if choice == "1":
            start_mission()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            show_crew()
        elif choice == "4":
            do_research()
        elif choice == "5":
            hunt_bounty()
        elif choice == "6":
            trade_with_aliens()
        elif choice == "7":
            explore_nebula()
        elif choice == "8":
            save_game()
        elif choice == "9":
            load_game()
        elif choice == "10":
            random_activity()
        elif choice == "11":
            print("\n👋 Farewell, Captain!")
            print("⭐ Live long and prosper! 🖖")
            break
        else:
            print("❌ Invalid choice, Captain!")

if __name__ == "__main__":
    main()

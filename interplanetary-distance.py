"""
🚀 SPACE DISTANCE CALCULATOR
The Friendly Space Adventure Game
Version 3.7 - FINAL

A simple, fun space game made with love and Python.
Fly missions, hunt bounties, collect pets, and explore the cosmos!
"""

import math
import random
import time
import json
import os
from datetime import datetime

# ============================================
# YOUR SHIP'S DATA
# ============================================

you = {
    "fuel": 5000,
    "credits": 1000,
    "missions": 0,
    "streak": 0,
    "morale": 80,
    "research": 0,
    "rank": 1,
    "record": 0,
    "total_distance": 0,
    "trophies": [],
    "inventory": [],
    "pets": [],
    "luck": 0,
    "last_play": None,
    "pirates_defeated": 0,
    "nebula_explored": 0,
    "jokes_told": 0,
    "games_played": 0
}

# ============================================
# YOUR CREW
# ============================================

crew = [
    {"name": "Captain Rex", "skill": "Leadership", "level": 1, "xp": 0},
    {"name": "Engineer Jen", "skill": "Mechanics", "level": 1, "xp": 0},
    {"name": "Navigator Zoe", "skill": "Astrogation", "level": 1, "xp": 0},
    {"name": "Scientist Kim", "skill": "Research", "level": 1, "xp": 0},
    {"name": "Gunner Mack", "skill": "Combat", "level": 1, "xp": 0}
]

# ============================================
# THE UNIVERSE
# ============================================

PLANETS = {
    1: ("🌍 Earth", (0, 0)),
    2: ("🔴 Mars", (225, 0)),
    3: ("🟡 Venus", (108, 0)),
    4: ("🟠 Jupiter", (778, 0)),
    5: ("🪐 Saturn", (1427, 0)),
    6: ("🔵 Uranus", (2871, 0)),
    7: ("🔷 Neptune", (4495, 0)),
    8: ("⚪ Mercury", (58, 0)),
    9: ("⚫ Pluto", (5906, 0))
}

BOUNTIES = [
    {"name": "🏴‍☠️ Red Pirate", "reward": 500, "level": 1, "hp": 3},
    {"name": "🌑 Shadow Corsair", "reward": 1000, "level": 2, "hp": 5},
    {"name": "💀 Void Reaver", "reward": 2000, "level": 3, "hp": 7},
    {"name": "👾 Galactic Menace", "reward": 3500, "level": 4, "hp": 10}
]

TECH = {
    "⛽ Fuel Efficiency": {"cost": 100, "owned": False, "desc": "Use 10% less fuel"},
    "⚡ Warp Drive": {"cost": 200, "owned": False, "desc": "20% faster travel"},
    "🛡️ Shield Tech": {"cost": 150, "owned": False, "desc": "Take less damage"},
    "🔭 Scanner Range": {"cost": 120, "owned": False, "desc": "Find more treasures"}
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
    "lucky": "🍀 Had a lucky day!",
    "traveler": "🌠 Traveled 10000 million km total!",
    "pirate_hunter": "⚔️ Defeated 10 pirates!",
    "nebula_expert": "🌌 Explored 5 nebulae!",
    "jokester": "😂 Told 10 jokes!",
    "collector": "📦 Collected 10 items!"
}

PETS = [
    "🐶 Space Dog", "🐱 Robot Cat", "🐹 Alien Hamster", 
    "🐉 Tiny Dragon", "🦊 Quantum Fox", "🐧 Space Penguin", 
    "🐙 Star Octopus", "🦄 Nebula Unicorn", "🐼 Panda-stronaut"
]

JOKES = [
    "Why did the star go to school? To get brighter!",
    "What do astronauts use for pants? An asteroid belt!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key? The space bar!",
    "Why did the alien cross the galaxy? To get to the other side!",
    "What do you call a lazy astronaut? A space cadet!",
    "Why is space so clean? Because nobody dusts!",
    "What do you call a flying cow? A spaceship!"
]

NEBULAE = {
    "🌌 Orion Nebula": (1340, -220),
    "🦅 Eagle Nebula": (7000, 0),
    "🌀 Helix Nebula": (695, 280),
    "🦀 Crab Nebula": (6500, 190),
    "💀 Skull Nebula": (4200, -500)
}

ALIEN_ITEMS = {
    "🌌 Dark Crystal": 500,
    "💫 Warp Core": 2000,
    "🔮 Quantum Shield": 1500,
    "🍕 Space Pizza": 50,
    "📡 Anomaly Scanner": 800,
    "🧪 Research Data": 400,
    "🎵 Space Radio": 150
}

WELCOME_MESSAGES = [
    "The stars are calling!",
    "Adventure awaits!",
    "Time to explore the cosmos!",
    "Another day, another galaxy!",
    "The universe is your playground!"
]

FAREWELL_MESSAGES = [
    "The stars will remember you!",
    "Come back soon, space cowboy!",
    "May the force be with you!",
    "To infinity and beyond!",
    "Live long and prosper!"
]

# ============================================
# HELPER FUNCTIONS
# ============================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    print("\n" + "=" * 50)
    print(f"  {text}")
    print("=" * 50)

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def unlock_achievement(key):
    if key in ACHIEVEMENTS and key not in you["trophies"]:
        you["trophies"].append(key)
        print(f"\n🎉 {'='*40}")
        print(f"🎉 {ACHIEVEMENTS[key]}")
        print(f"🎉 {'='*40}\n")
        time.sleep(0.8)
        return True
    return False

def gain_crew_xp(amount):
    for member in crew:
        member["xp"] += amount
        if member["xp"] >= member["level"] * 100:
            member["xp"] = 0
            member["level"] += 1
            print(f"\n🌟 {member['name']} reached level {member['level']}!")
            bonus = random.randint(100, 300)
            you["credits"] += bonus
            print(f"💰 Crew celebration! +{bonus} credits!")

def check_daily_luck():
    today = datetime.now().date()
    if you["last_play"] != str(today):
        you["luck"] = random.randint(1, 10)
        you["last_play"] = str(today)
        
        print("\n" + "─" * 40)
        print(f"🍀 Today's Luck: {'⭐' * you['luck']}")
        
        if you["luck"] >= 8:
            print("🌟 The stars are aligned in your favor!")
            unlock_achievement("lucky")
        elif you["luck"] >= 5:
            print("✨ The cosmos smiles upon you today")
        else:
            print("🌙 The universe feels... quiet today")
        print("─" * 40 + "\n")
        time.sleep(0.5)

def find_pet():
    pet = random.choice(PETS)
    if pet not in you["pets"]:
        you["pets"].append(pet)
        print(f"\n🐾 A wild {pet} appeared and joined your crew!")
        print("💕 It looks at you with adorable eyes...")
        unlock_achievement("pet")
        you["morale"] = min(100, you["morale"] + 10)
    else:
        print(f"\n🐾 {pet} is already part of your space family!")

def tell_joke():
    joke = random.choice(JOKES)
    print(f"\n😂 {joke}")
    you["morale"] = min(100, you["morale"] + 5)
    you["jokes_told"] = you.get("jokes_told", 0) + 1
    print(f"😊 The crew chuckles. Morale +5! (Now: {you['morale']}%)")
    
    if you["jokes_told"] >= 10:
        unlock_achievement("jokester")

def get_planet_name(coords):
    for num, (name, c) in PLANETS.items():
        if c == coords:
            return name
    return "📍 Unknown"

def safe_input(prompt, default=None):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted! See you later, Captain!")
        exit()
    except EOFError:
        return default if default is not None else ""

def show_morale_bar():
    bar_length = 20
    filled = int(bar_length * you["morale"] / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    mood = "😄" if you["morale"] > 70 else "😐" if you["morale"] > 40 else "😞"
    print(f"😊 Morale: [{bar}] {you['morale']}% {mood}")

# ============================================
# MAIN GAME FUNCTIONS
# ============================================

def pick_planet():
    print("\n🪐 WHERE TO?")
    print("─" * 30)
    for num, (name, _) in PLANETS.items():
        print(f"{num}. {name}")
    print("─" * 30)

    def choose(question):
        while True:
            try:
                choice = int(safe_input(question, "1"))
                if choice in PLANETS:
                    return PLANETS[choice]
                print("❌ Invalid choice! Try again.")
            except ValueError:
                print("❌ Please enter a number!")

    start = choose("🌍 Starting planet: ")
    end = choose("🎯 Destination planet: ")
    
    start_name = get_planet_name(start)
    end_name = get_planet_name(end)
    
    return start_name, start, end_name, end

def start_mission():
    check_daily_luck()

    print_header("🚀 PREPARING FOR LAUNCH")
    print("1. 📍 Travel to known planets")
    print("2. 🗺️ Explore unknown coordinates")
    print("3. ↩️ Return to menu")

    choice = safe_input("\nChoice: ", "3")

    if choice == "3":
        return
    elif choice == "1":
        start_name, start, end_name, end = pick_planet()
    elif choice == "2":
        try:
            print("\n📡 Enter coordinates (in million km)")
            start = (float(safe_input("Start x: ", "0")), float(safe_input("Start y: ", "0")))
            end = (float(safe_input("End x: ", "100")), float(safe_input("End y: ", "100")))
            start_name, end_name = "🚀 Unknown", "📍 Unknown"
        except ValueError:
            print("❌ Invalid coordinates!")
            return
    else:
        print("❌ Invalid choice!")
        return

    dist = distance(start, end)
    you["total_distance"] += dist
    print(f"\n📏 Distance: {dist:,.0f} million km")
    print(f"📊 Total distance traveled: {you['total_distance']:,.0f} million km")

    if dist > you["record"]:
        you["record"] = dist
        print("🏆 NEW RECORD DISTANCE!")

    if random.random() < 0.25 + (you["luck"] * 0.01):
        event = random.choice(["wormhole", "treasure", "pet", "joke", "alien_signal", "shooting_star"])
        if event == "wormhole":
            dist *= 0.6
            print("🌀 You found a wormhole shortcut!")
            print(f"📏 New distance: {dist:,.0f} million km")
        elif event == "treasure":
            bonus = random.randint(100, 300) + (you["luck"] * 10)
            you["credits"] += bonus
            print(f"💰 You found a floating treasure pod! +{bonus} credits!")
        elif event == "pet":
            find_pet()
        elif event == "joke":
            tell_joke()
        elif event == "alien_signal":
            print("📡 You picked up a mysterious alien signal...")
            if random.random() < 0.5:
                gift = random.randint(50, 150)
                you["credits"] += gift
                print(f"👽 The aliens send you a gift! +{gift} credits!")
            else:
                print("👽 The signal fades away...")
        elif event == "shooting_star":
            print("🌠 You see a shooting star! Make a wish!")
            wish_bonus = random.randint(20, 80)
            you["morale"] = min(100, you["morale"] + wish_bonus // 10)
            print(f"✨ Your wish gave you +{wish_bonus//10} morale!")

    fuel_needed = dist * 0.5
    if TECH["⛽ Fuel Efficiency"]["owned"]:
        fuel_needed *= 0.9
        print("⛽ Fuel Efficiency active! Using less fuel.")
    
    if you["fuel"] < fuel_needed:
        print(f"\n⛽ INSUFFICIENT FUEL!")
        print(f"   Need: {fuel_needed:.0f} fuel")
        print(f"   Have: {you['fuel']:.0f} fuel")
        print("\n1. Mine asteroid (risky but free)")
        print("2. Buy fuel (2 credits/unit)")
        print("3. Abort mission")
        choice = safe_input("Choice: ", "3")

        if choice == "3":
            print("🔄 Mission aborted. Returning to base.")
            return
        elif choice == "1":
            if random.random() < 0.6 + (you["luck"] * 0.02):
                gained = random.randint(200, 800)
                you["fuel"] += gained
                print(f"✅ Successfully mined {gained} fuel!")
            else:
                lost = random.randint(50, 200)
                you["fuel"] = max(0, you["fuel"] - lost)
                print(f"💥 Asteroid collision! Lost {lost} fuel!")
        elif choice == "2":
            try:
                amount = int(safe_input("How much fuel? ", "100"))
                cost = amount * 2
                if you["credits"] >= cost:
                    you["credits"] -= cost
                    you["fuel"] += amount
                    print(f"✅ Purchased {amount} fuel!")
                else:
                    print("❌ Not enough credits!")
            except ValueError:
                print("❌ Invalid amount!")
        return

    you["fuel"] -= fuel_needed
    earned = int(dist * 0.8 + 50 + (you["luck"] * 2))
    you["credits"] += earned
    you["missions"] += 1
    you["streak"] += 1
    morale_gain = random.randint(5, 15)
    you["morale"] = min(100, you["morale"] + morale_gain)

    print_header("✅ MISSION COMPLETE")
    print(f"💰 Credits earned: +{earned}")
    print(f"⛽ Fuel remaining: {you['fuel']:.0f}")
    show_morale_bar()
    print(f"📊 Total missions: {you['missions']}")
    print(f"🔥 Current streak: {you['streak']}")

    if you["missions"] == 1:
        unlock_achievement("first")
    if you["credits"] >= 10000:
        unlock_achievement("rich")
    if you["missions"] >= 50:
        unlock_achievement("legend")
    if you["streak"] >= 5:
        unlock_achievement("streak")
    if you["record"] >= 2000:
        unlock_achievement("explorer")
    if you["total_distance"] >= 10000:
        unlock_achievement("traveler")
    if len(you["inventory"]) >= 10:
        unlock_achievement("collector")

    gain_crew_xp(20)

def hunt_bounty():
    check_daily_luck()

    print_header("💰 BOUNTY HUNTING")
    print(f"🏆 Your rank: {you['rank']}")

    available = [b for b in BOUNTIES if b["level"] <= you["rank"] + 1]
    if not available:
        print("❌ No bounties available at your rank.")
        print("💡 Complete more missions to unlock harder targets!")
        return

    print("\n🎯 AVAILABLE TARGETS:")
    for i, target in enumerate(available[:4], 1):
        print(f"{i}. {target['name']}")
        print(f"   💰 Reward: {target['reward']} | Level: {target['level']}")

    choice = safe_input("\nChoose target (number): ", "1")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(available[:4]):
        return

    target = available[int(choice) - 1]
    print(f"\n⚔️ ENGAGING {target['name']}...")
    time.sleep(0.5)

    my_hp = target["hp"] + (you["luck"] // 3)
    enemy_hp = target["hp"]
    
    if TECH["🛡️ Shield Tech"]["owned"]:
        my_hp += 2
        print("🛡️ Shield Tech active! Extra protection!")
    
    print(f"💪 Bonus health: +{you['luck']//3}")
    print(f"❤️ Your health: {my_hp} | Enemy health: {enemy_hp}")

    while my_hp > 0 and enemy_hp > 0:
        print(f"\n❤️ You: {my_hp} | {target['name']}: {enemy_hp}")
        action = safe_input("1. ⚔️ Attack  2. 🛡️ Dodge  3. 💊 Use item: ", "1")

        if action == "1":
            damage = random.randint(2, 6) + (you["luck"] // 5)
            if TECH["⚡ Warp Drive"]["owned"]:
                damage += 1
                print("⚡ Warp Drive gives extra damage!")
            enemy_hp -= damage
            print(f"⚡ You strike for {damage} damage!")
            if enemy_hp > 0:
                counter = random.randint(1, 4)
                if TECH["🛡️ Shield Tech"]["owned"]:
                    counter = max(1, counter - 1)
                my_hp -= counter
                print(f"💥 They counter for {counter} damage!")
        elif action == "2":
            if random.random() < 0.5 + (you["luck"] * 0.02):
                print("🛡️ You gracefully dodge the attack!")
            else:
                counter = random.randint(2, 5)
                my_hp -= counter
                print(f"💥 Too slow! You took {counter} damage!")
        elif action == "3":
            if "🍕 Space Pizza" in you["inventory"]:
                you["inventory"].remove("🍕 Space Pizza")
                heal = random.randint(3, 8)
                max_hp = target["hp"] + (you["luck"] // 3)
                if TECH["🛡️ Shield Tech"]["owned"]:
                    max_hp += 2
                my_hp = min(max_hp, my_hp + heal)
                print(f"💊 You ate Space Pizza! Healed {heal} health!")
            else:
                print("❌ No Space Pizza available!")
                if you["inventory"]:
                    print(f"📦 You have: {', '.join(you['inventory'])}")
                else:
                    print("📦 Your inventory is empty!")
        else:
            print("Invalid action!")

    if my_hp > 0:
        reward_bonus = int(target["reward"] * (1 + you["luck"] * 0.01))
        you["credits"] += reward_bonus
        you["pirates_defeated"] = you.get("pirates_defeated", 0) + 1
        print(f"\n🎉 VICTORY!")
        print(f"💰 Collected {reward_bonus} credits!")
        if target["level"] == you["rank"]:
            you["rank"] += 1
            print(f"🏆 Rank up! You are now level {you['rank']}")
        unlock_achievement("bounty")
        
        if you["pirates_defeated"] >= 10:
            unlock_achievement("pirate_hunter")
        
        gain_crew_xp(30)
    else:
        print("\n💀 You were defeated!")
        print("💸 Lost 100 credits")
        you["credits"] = max(0, you["credits"] - 100)

def do_research():
    print_header("🧪 RESEARCH LAB")
    print(f"📚 Research points: {you['research']}\n")

    for i, (name, data) in enumerate(TECH.items(), 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} pts"
        print(f"{i}. {name}")
        print(f"   {data['desc']} - {status}")

    print("\n5. 💰 Convert 100 credits → 20 research points")
    print("6. ↩️ Back to menu")

    choice = safe_input("\nChoice: ", "6")
    if choice == "6":
        return
    elif choice.isdigit() and 1 <= int(choice) <= 4:
        name, data = list(TECH.items())[int(choice) - 1]
        if not data["owned"]:
            if you["research"] >= data["cost"]:
                you["research"] -= data["cost"]
                data["owned"] = True
                print(f"\n✨ RESEARCH COMPLETE!")
                print(f"🔬 {name} unlocked!")
                if all(t["owned"] for t in TECH.values()):
                    unlock_achievement("research")
            else:
                print("❌ Not enough research points!")
        else:
            print("❌ Already researched!")
    elif choice == "5":
        if you["credits"] >= 100:
            you["credits"] -= 100
            you["research"] += 20
            print("✅ Converted credits to research points!")
        else:
            print("❌ Not enough credits!")

def trade_with_aliens():
    print_header("👽 ALIEN TRADE")
    print(f"💰 Your credits: {you['credits']}\n")

    print("🛒 AVAILABLE ITEMS:")
    for i, (item, price) in enumerate(ALIEN_ITEMS.items(), 1):
        print(f"{i}. {item} - {price} credits")

    choice = safe_input("\nBuy (number) or 'q' to quit: ", "q")
    if choice.lower() == 'q':
        return
    elif choice.isdigit() and 1 <= int(choice) <= len(ALIEN_ITEMS):
        item, price = list(ALIEN_ITEMS.items())[int(choice) - 1]
        if you["credits"] >= price:
            you["credits"] -= price
            you["inventory"].append(item)
            print(f"\n✨ Purchased {item}!")
            print(f"💰 Remaining credits: {you['credits']}")
            if len(you["inventory"]) >= 10:
                unlock_achievement("collector")
        else:
            print("❌ Not enough credits!")

def explore_nebula():
    print_header("🌌 NEBULA EXPLORATION")
    
    for i, name in enumerate(NEBULAE.keys(), 1):
        print(f"{i}. {name}")

    choice = safe_input("\nChoose: ", "1")
    if choice.isdigit() and 1 <= int(choice) <= len(NEBULAE):
        name = list(NEBULAE.keys())[int(choice) - 1]
        print(f"\n🚀 Entering {name}...")
        time.sleep(1)

        you["nebula_explored"] = you.get("nebula_explored", 0) + 1
        
        if you["nebula_explored"] >= 5:
            unlock_achievement("nebula_expert")

        roll = random.random()
        if roll < 0.6 + (you["luck"] * 0.02):
            fuel_found = random.randint(300, 1500) + (you["luck"] * 10)
            you["fuel"] += fuel_found
            print(f"⛽ Discovered {fuel_found} fuel in the nebula!")
            unlock_achievement("fuel")
        elif roll < 0.8:
            treasure = random.choice(["Ancient Relic", "Crystal Shard", "Star Chart", "Alien Artifact"])
            you["inventory"].append(treasure)
            print(f"🔮 Found {treasure}!")
            you["research"] += 20 + (you["luck"] * 2)
            if len(you["inventory"]) >= 10:
                unlock_achievement("collector")
        else:
            print("💨 The nebula is empty... but you enjoy the view!")

        if random.random() < 0.08:
            find_pet()
    else:
        print("Invalid choice!")

def random_activity():
    print_header("🎲 RANDOM FUN")
    
    options = ["tell_joke", "find_pet", "check_luck", "find_treasure", "meditate", "dance"]
    action = random.choice(options)

    if action == "tell_joke":
        tell_joke()
    elif action == "find_pet":
        find_pet()
    elif action == "check_luck":
        check_daily_luck()
    elif action == "find_treasure":
        treasure = random.randint(50, 200) + (you["luck"] * 5)
        you["credits"] += treasure
        print(f"\n💰 You found {treasure} credits floating in space!")
    elif action == "meditate":
        gain = random.randint(5, 15)
        you["morale"] = min(100, you["morale"] + gain)
        print(f"\n🧘‍♂️ Your crew meditates in zero-gravity.")
        print(f"😊 Morale +{gain}! (Now: {you['morale']}%)")
    elif action == "dance":
        gain = random.randint(3, 10)
        you["morale"] = min(100, you["morale"] + gain)
        print(f"\n💃 The crew has a zero-gravity dance party!")
        print(f"😊 Morale +{gain}! (Now: {you['morale']}%)")

def view_help():
    print_header("📖 CAPTAIN'S GUIDE")
    print("""
🎮 HOW TO PLAY:
   • Fly missions to earn credits and fuel
   • Research technology for ship upgrades
   • Hunt bounties for big rewards
   • Explore nebulae for rare finds
   • Trade with aliens for special items
   • Collect space pets for morale boosts

💡 TIPS:
   • Save your game regularly
   • Check daily luck before missions
   • Keep at least 30% fuel reserve
   • Level up crew for better bonuses
   • Complete achievements for bragging rights

🚀 GOOD LUCK, CAPTAIN!
    """)

# ============================================
# DISPLAY FUNCTIONS
# ============================================

def show_stats():
    print_header("📊 YOUR SPACE STATISTICS")
    
    print(f"🚀 Missions:     {you['missions']}")
    print(f"🔥 Streak:       {you['streak']}")
    print(f"⛽ Fuel:         {you['fuel']:.0f}")
    print(f"💰 Credits:      {you['credits']}")
    print(f"📚 Research:     {you['research']}")
    show_morale_bar()
    print(f"🏆 Bounty Rank:  {you['rank']}")
    print(f"📏 Furthest:     {you['record']:,.0f} million km")
    print(f"🌠 Total Dist.:  {you['total_distance']:,.0f} million km")
    print(f"🍀 Luck:         {'⭐' * you['luck']} ({you['luck']}/10)")
    print(f"⚔️ Pirates Def.: {you.get('pirates_defeated', 0)}")
    print(f"🌌 Nebulae Exp.: {you.get('nebula_explored', 0)}")
    print(f"😂 Jokes Told:   {you.get('jokes_told', 0)}")
    print(f"🏅 Achievements: {len(you['trophies'])}")

    if you["trophies"]:
        print("\n🏅 ACHIEVEMENTS:")
        for t in you["trophies"]:
            print(f"  • {ACHIEVEMENTS[t]}")

    if you["pets"]:
        print("\n🐾 SPACE PETS:")
        for pet in you["pets"]:
            print(f"  • {pet}")

    if you["inventory"]:
        print("\n📦 INVENTORY:")
        for item in you["inventory"]:
            print(f"  • {item}")

def show_crew():
    print_header("👥 YOUR CREW")
    
    for member in crew:
        print(f"\n🌟 {member['name']}")
        print(f"   Skill: {member['skill']}")
        print(f"   Level: {member['level']}")
        print(f"   XP: {member['xp']}/{member['level'] * 100}")
        if member['level'] * 100 > 0:
            progress = int((member['xp'] / (member['level'] * 100)) * 10)
            bar = "█" * progress + "░" * (10 - progress)
            print(f"   Progress: [{bar}]")
        else:
            print(f"   Progress: [░░░░░░░░░░]")

# ============================================
# SAVE/LOAD FUNCTIONS
# ============================================

def save_game():
    data = {
        "fuel": you["fuel"],
        "credits": you["credits"],
        "missions": you["missions"],
        "streak": you["streak"],
        "morale": you["morale"],
        "research": you["research"],
        "rank": you["rank"],
        "record": you["record"],
        "total_distance": you["total_distance"],
        "trophies": you["trophies"],
        "inventory": you["inventory"],
        "pets": you["pets"],
        "luck": you["luck"],
        "last_play": you["last_play"],
        "pirates_defeated": you.get("pirates_defeated", 0),
        "nebula_explored": you.get("nebula_explored", 0),
        "jokes_told": you.get("jokes_told", 0),
        "games_played": you.get("games_played", 0),
        "crew": crew,
        "tech": TECH
    }
    try:
        with open("space_save.json", "w") as f:
            json.dump(data, f)
        print("\n💾 Game saved successfully!")
        print(f"📅 Saved at: {datetime.now().strftime('%H:%M:%S')}")
        return True
    except Exception as e:
        print(f"❌ Save failed: {e}")
        return False

def load_game():
    global you, crew, TECH
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)

        for key in data:
            if key in you and key not in ["trophies", "inventory", "pets"]:
                you[key] = data[key]
        
        you["trophies"] = data.get("trophies", [])
        you["inventory"] = data.get("inventory", [])
        you["pets"] = data.get("pets", [])
        you["games_played"] = data.get("games_played", 0)
        
        if "crew" in data:
            for i, member in enumerate(data["crew"]):
                if i < len(crew):
                    crew[i] = member
        
        if "tech" in data:
            for name, values in data["tech"].items():
                if name in TECH:
                    TECH[name]["owned"] = values.get("owned", False)

        print("\n📀 Game loaded successfully!")
        print(f"👋 Welcome back, Captain!")
        return True
    except FileNotFoundError:
        print("❌ No save file found!")
        print("💡 Start a new adventure!")
        return False
    except Exception as e:
        print(f"❌ Load failed: {e}")
        return False

# ============================================
# MAIN GAME LOOP
# ============================================

def main():
    you["games_played"] = you.get("games_played", 0) + 1
    clear_screen()
    
    print("""
    ╔════════════════════════════════════════════╗
    ║                                          ║
    ║   🚀 SPACE DISTANCE CALCULATOR 🚀        ║
    ║                                          ║
    ║        The Friendly Space Adventure      ║
    ║                                          ║
    ║           Version 3.7 - FINAL            ║
    ║                                          ║
    ║     "The cosmos is yours to explore!"    ║
    ║                                          ║
    ╚════════════════════════════════════════════╝
    """)
    
    print(f"🌟 Welcome, Captain!")
    print(f"💫 {random.choice(WELCOME_MESSAGES)}\n")
    print(f"🎮 Game session #{you['games_played']}")
    time.sleep(1)
    
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
       

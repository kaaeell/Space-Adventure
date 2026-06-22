"""
🚀 SPACE ADVENTURE - The Friendly Edition
A cozy space game where you explore, trade, and become a legend!
Just you, your crew, and the infinite cosmos.
"""

import math, random, time, json, os

# ============================================
# YOUR SHIP - Your home in the stars
# ============================================
you = {
    "fuel": 5000,        # Gas to fly!
    "credits": 1000,     # Space money
    "missions": 0,       # How many trips
    "streak": 0,         # Hot streak!
    "morale": 80,        # Happy crew?
    "research": 0,       # Science points
    "rank": 1,           # Bounty hunter rank
    "record": 0,         # Furthest trip
    "trophies": [],      # Achievements
    "stuff": []          # Your treasures
}

# ============================================
# YOUR CREW - Your space family
# ============================================
crew = [
    {"name": "Captain Rex", "skill": "Leadership", "level": 1, "xp": 0},
    {"name": "Engineer Jen", "skill": "Mechanics", "level": 1, "xp": 0},
    {"name": "Navigator Zoe", "skill": "Astrogation", "level": 1, "xp": 0},
    {"name": "Scientist Kim", "skill": "Research", "level": 1, "xp": 0},
    {"name": "Gunner Mack", "skill": "Combat", "level": 1, "xp": 0}
]

# ============================================
# THE COSMOS - All the cool stuff
# ============================================

# Planets you can visit
PLANETS = {
    1: ("Earth", (0,0)), 2: ("Mars", (225,0)), 3: ("Venus", (108,0)),
    4: ("Jupiter", (778,0)), 5: ("Saturn", (1427,0)), 6: ("Uranus", (2871,0)),
    7: ("Neptune", (4495,0)), 8: ("Mercury", (58,0)), 9: ("Pluto", (5906,0))
}

# Bad guys to catch
bounties = [
    {"name": "Red Pirate", "reward": 500, "level": 1, "hp": 3},
    {"name": "Shadow Corsair", "reward": 1000, "level": 2, "hp": 5},
    {"name": "Void Reaver", "reward": 2000, "level": 3, "hp": 7}
]

# Tech to unlock
tech = {
    "Fuel Efficiency": {"cost": 100, "owned": False},
    "Warp Drive": {"cost": 200, "owned": False},
    "Shield Tech": {"cost": 150, "owned": False}
}

# Achievements to earn
trophies = {
    "first": "🌱 Your first space trip!",
    "explorer": "🌌 You traveled far!",
    "fuel": "⛽ You found fuel in a nebula!",
    "rich": "💰 You're a space millionaire!",
    "legend": "⭐ You're a space legend!",
    "streak": "🔥 You're on fire!",
    "bounty": "💰 You caught a criminal!",
    "research": "🧠 You're a genius!"
}

# ============================================
# HELPER MAGIC
# ============================================

def distance(p1, p2):
    """How far apart are two points in space?"""
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def celebrate(achievement):
    """You did something awesome!"""
    if achievement in trophies and achievement not in you["trophies"]:
        you["trophies"].append(achievement)
        print(f"\n🎉 {trophies[achievement]} 🎉\n")
        time.sleep(0.3)

def crew_growth(amount):
    """Your crew learns and grows!"""
    for person in crew:
        person["xp"] += amount
        if person["xp"] >= person["level"] * 100:
            person["xp"] = 0
            person["level"] += 1
            print(f"\n🎉 {person['name']} is now level {person['level']}!")
            you["credits"] += random.randint(100, 300)

# ============================================
# WHAT YOU CAN DO
# ============================================

def pick_destination():
    """Where do you want to go?"""
    print("\n🪐 WHERE TO?")
    for n, (name, _) in PLANETS.items():
        print(f"{n}. {name}")
    
    def choose(question):
        while True:
            try:
                choice = int(input(question))
                if choice in PLANETS:
                    return PLANETS[choice]
                print("That planet doesn't exist!")
            except:
                print("Please enter a number!")
    
    start = choose("Where are you starting from? ")
    end = choose("Where are you going to? ")
    return start, end

def go_on_mission():
    """Your main adventure!"""
    print("\n🚀 PREPARING FOR LAUNCH!")
    print("1. Travel to known planets")
    print("2. Explore unknown space")
    
    if input("Choice: ") == "1":
        start_name, start = pick_destination()
        end_name, end = pick_destination()
    else:
        start = (float(input("Start x: ")), float(input("Start y: ")))
        end = (float(input("End x: ")), float(input("End y: ")))
        start_name, end_name = "Unknown", "Unknown"
    
    # Calculate your journey
    dist = distance(start, end)
    print(f"\n📏 {start_name} to {end_name}: {dist:.0f} million km")
    
    # New record?
    if dist > you["record"]:
        you["record"] = dist
        print("🏆 That's your longest trip yet!")
    
    # Space surprises!
    if random.random() < 0.25:
        if random.random() < 0.5:
            dist *= 0.6
            print("🌀 You found a wormhole shortcut!")
        else:
            bonus = random.randint(100, 300)
            you["credits"] += bonus
            print(f"💰 Found space treasure! +{bonus} credits!")
    
    # Fuel check
    needed = dist * 0.5
    if you["fuel"] < needed:
        print(f"\n⛽ Uh oh! Need {needed:.0f} fuel, have {you['fuel']:.0f}")
        if input("1. Mine asteroid  2. Buy fuel: ") == "1":
            if random.random() < 0.6:
                you["fuel"] += random.randint(200, 800)
                print("✅ Mined some fuel!")
            else:
                you["fuel"] = max(0, you["fuel"] - random.randint(50, 200))
                print("💥 Ouch! Asteroid damaged your ship!")
        else:
            amount = int(input("How much fuel? "))
            cost = amount * 2
            if you["credits"] >= cost:
                you["credits"] -= cost
                you["fuel"] += amount
                print(f"✅ Bought {amount} fuel!")
        return
    
    # Mission success!
    you["fuel"] -= needed
    earned = int(dist * 0.8 + 50)
    you["credits"] += earned
    you["missions"] += 1
    you["streak"] += 1
    you["morale"] = min(100, you["morale"] + random.randint(5, 15))
    
    print(f"\n✅ MISSION COMPLETE! +{earned} credits")
    print(f"⛽ Fuel left: {you['fuel']:.0f}")
    print(f"😊 Crew morale: {you['morale']}%")
    
    # Check for achievements
    if you["missions"] == 1: celebrate("first")
    if you["credits"] >= 10000: celebrate("rich")
    if you["missions"] >= 50: celebrate("legend")
    if you["streak"] >= 5: celebrate("streak")
    
    crew_growth(20)

def hunt_bounty():
    """Catch space criminals for money!"""
    print("\n💰 BOUNTY HUNTING")
    print(f"🏆 Your rank: {you['rank']}")
    
    available = [b for b in bounties if b["level"] <= you["rank"] + 1]
    if not available:
        print("No bounties right now. Do more missions!")
        return
    
    print("\n🎯 WANTED:")
    for i, target in enumerate(available[:3], 1):
        print(f"{i}. {target['name']} - 💰 {target['reward']}")
    
    choice = input("Who do you want? ")
    if not choice.isdigit() or int(choice) > len(available[:3]):
        return
    
    target = available[int(choice)-1]
    print(f"\n⚔️ FIGHTING {target['name']}...")
    time.sleep(0.5)
    
    my_hp = target["hp"]
    their_hp = target["hp"]
    
    while my_hp > 0 and their_hp > 0:
        print(f"\n❤️ You: {my_hp} | {target['name']}: {their_hp}")
        action = input("1. Attack  2. Dodge: ")
        
        if action == "1":
            damage = random.randint(2, 6)
            their_hp -= damage
            print(f"⚡ You hit for {damage}!")
            counter = random.randint(1, 4)
            my_hp -= counter
            print(f"💥 They hit back for {counter}!")
        else:
            if random.random() < 0.5:
                print("🛡️ You dodged!")
            else:
                counter = random.randint(2, 5)
                my_hp -= counter
                print(f"💥 Too slow! Took {counter} damage!")
    
    if my_hp > 0:
        you["credits"] += target["reward"]
        print(f"\n🎉 VICTORY! +{target['reward']} credits!")
        if target["level"] == you["rank"]:
            you["rank"] += 1
            print(f"🏆 Rank up! Now {you['rank']}")
        celebrate("bounty")
        crew_growth(30)
    else:
        print("\n💀 You lost! Lost 100 credits")
        you["credits"] = max(0, you["credits"] - 100)

def do_research():
    """Unlock cool technology!"""
    print("\n🧪 RESEARCH LAB")
    print(f"📚 Points: {you['research']}")
    
    for i, (name, data) in enumerate(tech.items(), 1):
        status = "✅" if data["owned"] else f"💰 {data['cost']}pts"
        print(f"{i}. {name} - {status}")
    print("4. Convert 100 credits → 20 points")
    
    choice = input("What to research? ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        name, data = list(tech.items())[int(choice)-1]
        if not data["owned"] and you["research"] >= data["cost"]:
            you["research"] -= data["cost"]
            data["owned"] = True
            print(f"✨ UNLOCKED {name}!")
            celebrate("research")
        else:
            print("❌ Not enough points!")
    elif choice == "4" and you["credits"] >= 100:
        you["credits"] -= 100
        you["research"] += 20
        print("✅ Converted credits to research!")

def trade_with_aliens():
    """Meet space friends and trade!"""
    print("\n👽 ALIEN ENCOUNTER!")
    print(f"💰 Credits: {you['credits']}")
    
    items = {
        "🌌 Crystal": 500,
        "💫 Warp Core": 2000,
        "🔮 Shield": 1500,
        "🍕 Space Pizza": 50
    }
    
    for i, (item, price) in enumerate(items.items(), 1):
        print(f"{i}. {item} - {price}")
    
    choice = input("Buy (number) or 'q': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        item, price = list(items.items())[int(choice)-1]
        if you["credits"] >= price:
            you["credits"] -= price
            you["stuff"].append(item)
            print(f"✨ Bought {item}!")

def explore_nebula():
    """Fly into colorful space clouds!"""
    nebulae = {"Orion": (1340,-220), "Eagle": (7000,0), "Helix": (695,280)}
    
    print("\n🌌 NEBULA EXPLORATION")
    for i, name in enumerate(nebulae.keys(), 1):
        print(f"{i}. {name}")
    
    choice = input("Where to? ")
    if choice.isdigit() and 1 <= int(choice) <= len(nebulae):
        name = list(nebulae.keys())[int(choice)-1]
        print(f"\n🚀 Flying into {name}...")
        time.sleep(1)
        
        if random.random() < 0.6:
            fuel_found = random.randint(300, 1500)
            you["fuel"] += fuel_found
            print(f"⛽ Found {fuel_found} fuel!")
            celebrate("fuel")
        else:
            treasure = random.choice(["relic", "crystal", "chart"])
            you["stuff"].append(treasure)
            print(f"🔮 Found {treasure}!")
            you["research"] += 20

def show_stats():
    """How's your space journey going?"""
    print("\n" + "="*50)
    print("📊 YOUR SPACE JOURNEY")
    print("="*50)
    print(f"🚀 Missions: {you['missions']}")
    print(f"🔥 Streak: {you['streak']}")
    print(f"⛽ Fuel: {you['fuel']:.0f}")
    print(f"💰 Credits: {you['credits']}")
    print(f"📚 Research: {you['research']}")
    print(f"😊 Morale: {you['morale']}%")
    print(f"🏆 Bounty Rank: {you['rank']}")
    print(f"📏 Furthest: {you['record']:.0f} million km")
    print(f"🏅 Achievements: {len(you['trophies'])}")
    
    if you["trophies"]:
        print("\n🏅 Your trophies:")
        for t in you["trophies"]:
            print(f"  • {trophies[t]}")
    
    if you["stuff"]:
        print("\n📦 Your stuff:")
        for item in you["stuff"]:
            print(f"  • {item}")

def show_crew():
    """Meet your space family!"""
    print("\n👥 YOUR CREW")
    for person in crew:
        print(f"• {person['name']} - Level {person['level']} ({person['skill']})")
        print(f"  XP: {person['xp']}/{person['level']*100}")

def save_game():
    """Save your adventure to continue later"""
    data = {
        "fuel": you["fuel"], "credits": you["credits"],
        "missions": you["missions"], "streak": you["streak"],
        "morale": you["morale"], "research": you["research"],
        "rank": you["rank"], "record": you["record"],
        "trophies": you["trophies"], "stuff": you["stuff"],
        "crew": crew
    }
    with open("space_save.json", "w") as f:
        json.dump(data, f)
    print("💾 Adventure saved!")

def load_game():
    """Continue your space journey"""
    global you, crew
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)
        
        for key in data:
            if key in you:
                you[key] = data[key]
        crew[:] = data.get("crew", crew)
        
        print("📀 Welcome back, Captain!")
        return True
    except:
        print("❌ No saved game found!")
        return False

# ============================================
# LET'S GO!
# ============================================

def main():
    print("""
    ╔══════════════════════════════════════════╗
    ║   🚀 SPACE DISTANCE CALCULATOR 🚀       ║
    ║      The Friendly Space Adventure!      ║
    ║                                         ║
    ║   "The cosmos is yours to explore!"     ║
    ╚══════════════════════════════════════════╝
    """)
    
    print("🌟 Welcome, Captain! The galaxy awaits!\n")
    
    while True:
        print("\n" + "="*40)
        print("🌟 WHAT'S NEXT?")
        print("="*40)
        print("1. 🚀 Fly a mission")
        print("2. 📊 Check stats")
        print("3. 👥 Meet crew")
        print("4. 🧪 Research")
        print("5. 💰 Hunt bounty")
        print("6. 👽 Trade with aliens")
        print("7. 🌌 Explore nebula")
        print("8. 💾 Save")
        print("9. 📀 Load")
        print("10. ❌ Quit")
        
        choice = input("\nYour choice: ")
        
        if choice == "1": go_on_mission()
        elif choice == "2": show_stats()
        elif choice == "3": show_crew()
        elif choice == "4": do_research()
        elif choice == "5": hunt_bounty()
        elif choice == "6": trade_with_aliens()
        elif choice == "7": explore_nebula()
        elif choice == "8": save_game()
        elif choice == "9": load_game()
        elif choice == "10":
            print("\n👋 Farewell, Captain! The stars will miss you!")
            print("⭐ Live long and prosper! 🖖")
            break
        else:
            print("❌ Hmm, that's not a valid choice. Try again!")

if __name__ == "__main__":
    main()

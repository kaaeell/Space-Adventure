"""
🚀 SPACE ADVENTURE
A friendly space game where you explore, trade, and hunt bounties!
"""

import math
import random
import time
import json
import os
from datetime import datetime

# ========== YOUR SHIP ==========
you = {
    "fuel": 5000, "credits": 1000, "missions": 0, "streak": 0,
    "morale": 80, "research": 0, "rank": 1, "record": 0,
    "total_distance": 0, "trophies": [], "inventory": [], "pets": [],
    "luck": 0, "last_play": None, "pirates_defeated": 0,
    "nebula_explored": 0, "jokes_told": 0, "games_played": 0
}

# ========== YOUR CREW ==========
crew = [
    {"name": "Captain Rex", "skill": "Leadership", "level": 1, "xp": 0},
    {"name": "Engineer Jen", "skill": "Mechanics", "level": 1, "xp": 0},
    {"name": "Navigator Zoe", "skill": "Astrogation", "level": 1, "xp": 0},
    {"name": "Scientist Kim", "skill": "Research", "level": 1, "xp": 0},
    {"name": "Gunner Mack", "skill": "Combat", "level": 1, "xp": 0}
]

# ========== THE UNIVERSE ==========
PLANETS = {
    1: ("🌍 Earth", (0, 0)), 2: ("🔴 Mars", (225, 0)),
    3: ("🟡 Venus", (108, 0)), 4: ("🟠 Jupiter", (778, 0)),
    5: ("🪐 Saturn", (1427, 0)), 6: ("🔵 Uranus", (2871, 0)),
    7: ("🔷 Neptune", (4495, 0)), 8: ("⚪ Mercury", (58, 0)),
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
    "first": "🌱 First space trip!", "explorer": "🌌 Traveled 2000+ km!",
    "fuel": "⛽ Found fuel in nebula!", "rich": "💰 Space millionaire!",
    "legend": "⭐ 50 missions!", "streak": "🔥 5 in a row!",
    "bounty": "💰 Defeated a bounty!", "research": "🧠 All research!",
    "pet": "🐾 Found a pet!", "lucky": "🍀 Lucky day!",
    "traveler": "🌠 10000 km total!", "pirate_hunter": "⚔️ 10 pirates!",
    "nebula_expert": "🌌 5 nebulae!", "jokester": "😂 10 jokes!",
    "collector": "📦 10 items!"
}

PETS = ["🐶 Space Dog", "🐱 Robot Cat", "🐹 Alien Hamster", "🐉 Tiny Dragon", 
        "🦊 Quantum Fox", "🐧 Space Penguin", "🐙 Star Octopus", "🦄 Nebula Unicorn"]

JOKES = [
    "Why did the star go to school? To get brighter!",
    "What do astronauts use for pants? An asteroid belt!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key? The space bar!"
]

NEBULAE = {"🌌 Orion": (1340,-220), "🦅 Eagle": (7000,0), "🌀 Helix": (695,280),
           "🦀 Crab": (6500,190), "💀 Skull": (4200,-500)}

ALIEN_ITEMS = {"🌌 Dark Crystal": 500, "💫 Warp Core": 2000, "🔮 Quantum Shield": 1500,
               "🍕 Space Pizza": 50, "📡 Anomaly Scanner": 800, "🧪 Research Data": 400}

WELCOME = ["The stars are calling!", "Adventure awaits!", "Explore the cosmos!"]
FAREWELL = ["The stars will remember you!", "Come back soon!", "Live long and prosper!"]

# ========== HELPERS ==========
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(text):
    print("\n" + "=" * 50 + f"\n  {text}\n" + "=" * 50)

def dist(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def unlock(key):
    if key in ACHIEVEMENTS and key not in you["trophies"]:
        you["trophies"].append(key)
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

def daily_luck():
    today = datetime.now().date()
    if you["last_play"] != str(today):
        you["luck"] = random.randint(1, 10)
        you["last_play"] = str(today)
        print(f"\n🍀 Luck: {'⭐' * you['luck']}")
        if you["luck"] >= 8:
            print("🌟 Lucky day!")
            unlock("lucky")
        elif you["luck"] >= 5:
            print("✨ Good day!")
        else:
            print("🌙 Quiet day...")
        time.sleep(0.5)

def find_pet():
    pet = random.choice(PETS)
    if pet not in you["pets"]:
        you["pets"].append(pet)
        print(f"\n🐾 {pet} joined your crew!")
        unlock("pet")
        you["morale"] = min(100, you["morale"] + 10)

def tell_joke():
    print(f"\n😂 {random.choice(JOKES)}")
    you["morale"] = min(100, you["morale"] + 5)
    you["jokes_told"] += 1
    if you["jokes_told"] >= 10:
        unlock("jokester")

def safe_input(prompt, default=None):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\n👋 Later, Captain!")
        exit()

def morale_bar():
    filled = int(20 * you["morale"] / 100)
    bar = "█" * filled + "░" * (20 - filled)
    mood = "😄" if you["morale"] > 70 else "😐" if you["morale"] > 40 else "😞"
    print(f"😊 Morale: [{bar}] {you['morale']}% {mood}")

# ========== GAME ACTIONS ==========
def pick_planet():
    print("\n🪐 WHERE TO?")
    for n, (name, _) in PLANETS.items():
        print(f"{n}. {name}")
    
    def choose(q):
        while True:
            try:
                c = int(safe_input(q, "1"))
                if c in PLANETS:
                    return PLANETS[c]
                print("Invalid!")
            except ValueError:
                print("Enter a number!")
    
    start = choose("🌍 Starting: ")
    end = choose("🎯 Destination: ")
    
    start_name = end_name = "Unknown"
    for n, (name, coords) in PLANETS.items():
        if coords == start:
            start_name = name
        if coords == end:
            end_name = name
    return start_name, start, end_name, end

def mission():
    daily_luck()
    header("🚀 LAUNCH")
    print("1. Known planets  2. Unknown space  3. Back")
    choice = safe_input("Choice: ", "3")
    
    if choice == "3":
        return
    elif choice == "1":
        start_name, start, end_name, end = pick_planet()
    elif choice == "2":
        try:
            print("\n📡 Coordinates (million km)")
            start = (float(safe_input("Start x: ", "0")), float(safe_input("Start y: ", "0")))
            end = (float(safe_input("End x: ", "100")), float(safe_input("End y: ", "100")))
            start_name, end_name = "Unknown", "Unknown"
        except ValueError:
            print("Invalid!")
            return
    else:
        print("Invalid!")
        return
    
    d = dist(start, end)
    you["total_distance"] += d
    print(f"\n📏 Distance: {d:,.0f} million km")
    
    if d > you["record"]:
        you["record"] = d
        print("🏆 New record!")
    
    # Random events
    if random.random() < 0.25 + (you["luck"] * 0.01):
        event = random.choice(["wormhole", "treasure", "pet", "joke"])
        if event == "wormhole":
            d *= 0.6
            print("🌀 Wormhole shortcut!")
        elif event == "treasure":
            bonus = random.randint(100, 300) + (you["luck"] * 10)
            you["credits"] += bonus
            print(f"💰 Found treasure! +{bonus} credits!")
        elif event == "pet":
            find_pet()
        elif event == "joke":
            tell_joke()
    
    fuel_needed = d * 0.5
    if TECH["⛽ Fuel Efficiency"]["owned"]:
        fuel_needed *= 0.9
        print("⛽ Fuel efficiency active!")
    
    if you["fuel"] < fuel_needed:
        print(f"\n⛽ Need {fuel_needed:.0f} fuel, have {you['fuel']:.0f}")
        print("1. Mine asteroid  2. Buy fuel  3. Abort")
        choice = safe_input("Choice: ", "3")
        if choice == "3":
            print("Mission aborted.")
            return
        elif choice == "1":
            if random.random() < 0.6 + (you["luck"] * 0.02):
                gained = random.randint(200, 800)
                you["fuel"] += gained
                print(f"✅ Mined {gained} fuel!")
            else:
                lost = random.randint(50, 200)
                you["fuel"] = max(0, you["fuel"] - lost)
                print(f"💥 Lost {lost} fuel!")
        elif choice == "2":
            try:
                amount = int(safe_input("How much? ", "100"))
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
    earned = int(d * 0.8 + 50 + (you["luck"] * 2))
    you["credits"] += earned
    you["missions"] += 1
    you["streak"] += 1
    you["morale"] = min(100, you["morale"] + random.randint(5, 15))
    
    header("✅ MISSION COMPLETE")
    print(f"💰 +{earned} credits")
    print(f"⛽ Fuel: {you['fuel']:.0f}")
    morale_bar()
    print(f"📊 Missions: {you['missions']} | Streak: {you['streak']}")
    
    # Achievements
    if you["missions"] == 1: unlock("first")
    if you["credits"] >= 10000: unlock("rich")
    if you["missions"] >= 50: unlock("legend")
    if you["streak"] >= 5: unlock("streak")
    if you["record"] >= 2000: unlock("explorer")
    if you["total_distance"] >= 10000: unlock("traveler")
    if len(you["inventory"]) >= 10: unlock("collector")
    
    crew_xp(20)

def bounty():
    daily_luck()
    header("💰 BOUNTY HUNTING")
    print(f"🏆 Rank: {you['rank']}")
    
    available = [b for b in BOUNTIES if b["level"] <= you["rank"] + 1]
    if not available:
        print("No bounties available!")
        return
    
    print("\n🎯 TARGETS:")
    for i, t in enumerate(available[:4], 1):
        print(f"{i}. {t['name']} - 💰 {t['reward']} (Lv.{t['level']})")
    
    choice = safe_input("Choose: ", "1")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(available[:4]):
        return
    
    target = available[int(choice)-1]
    print(f"\n⚔️ FIGHTING {target['name']}...")
    time.sleep(0.5)
    
    my_hp = target["hp"] + (you["luck"] // 3)
    enemy_hp = target["hp"]
    if TECH["🛡️ Shield Tech"]["owned"]:
        my_hp += 2
        print("🛡️ Shield active!")
    
    while my_hp > 0 and enemy_hp > 0:
        print(f"\n❤️ You: {my_hp} | {target['name']}: {enemy_hp}")
        action = safe_input("1. Attack  2. Dodge  3. Use item: ", "1")
        
        if action == "1":
            dmg = random.randint(2, 6) + (you["luck"] // 5)
            if TECH["⚡ Warp Drive"]["owned"]:
                dmg += 1
            enemy_hp -= dmg
            print(f"⚡ Hit for {dmg}!")
            if enemy_hp > 0:
                counter = random.randint(1, 4)
                if TECH["🛡️ Shield Tech"]["owned"]:
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
            if "🍕 Space Pizza" in you["inventory"]:
                you["inventory"].remove("🍕 Space Pizza")
                heal = random.randint(3, 8)
                max_hp = target["hp"] + (you["luck"] // 3)
                if TECH["🛡️ Shield Tech"]["owned"]:
                    max_hp += 2
                my_hp = min(max_hp, my_hp + heal)
                print(f"💊 Healed {heal} health!")
            else:
                print("❌ No items!")
    
    if my_hp > 0:
        bonus = int(target["reward"] * (1 + you["luck"] * 0.01))
        you["credits"] += bonus
        you["pirates_defeated"] += 1
        print(f"\n🎉 VICTORY! +{bonus} credits!")
        if target["level"] == you["rank"]:
            you["rank"] += 1
            print(f"🏆 Rank up! Now {you['rank']}")
        unlock("bounty")
        if you["pirates_defeated"] >= 10:
            unlock("pirate_hunter")
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
        print(f"   {data['desc']}")
    
    print("\n5. Convert 100 credits → 20 points")
    print("6. Back")
    
    choice = safe_input("Choice: ", "6")
    if choice == "6":
        return
    elif choice.isdigit() and 1 <= int(choice) <= 4:
        name, data = list(TECH.items())[int(choice)-1]
        if not data["owned"] and you["research"] >= data["cost"]:
            you["research"] -= data["cost"]
            data["owned"] = True
            print(f"\n✨ Unlocked {name}!")
            if all(t["owned"] for t in TECH.values()):
                unlock("research")
        else:
            print("❌ Not enough points or already owned!")
    elif choice == "5" and you["credits"] >= 100:
        you["credits"] -= 100
        you["research"] += 20
        print("✅ Converted!")

def trade():
    header("👽 ALIEN TRADE")
    print(f"💰 Credits: {you['credits']}\n")
    
    for i, (item, price) in enumerate(ALIEN_ITEMS.items(), 1):
        print(f"{i}. {item} - {price} credits")
    
    choice = safe_input("Buy (number or q): ", "q")
    if choice.lower() == 'q':
        return
    elif choice.isdigit() and 1 <= int(choice) <= len(ALIEN_ITEMS):
        item, price = list(ALIEN_ITEMS.items())[int(choice)-1]
        if you["credits"] >= price:
            you["credits"] -= price
            you["inventory"].append(item)
            print(f"\n✨ Bought {item}!")
            if len(you["inventory"]) >= 10:
                unlock("collector")
        else:
            print("❌ Not enough credits!")

def nebula():
    header("🌌 NEBULA EXPLORATION")
    for i, name in enumerate(NEBULAE.keys(), 1):
        print(f"{i}. {name}")
    
    choice = safe_input("Choose: ", "1")
    if choice.isdigit() and 1 <= int(choice) <= len(NEBULAE):
        name = list(NEBULAE.keys())[int(choice)-1]
        print(f"\n🚀 Entering {name}...")
        time.sleep(1)
        
        you["nebula_explored"] += 1
        if you["nebula_explored"] >= 5:
            unlock("nebula_expert")
        
        roll = random.random()
        if roll < 0.6 + (you["luck"] * 0.02):
            fuel = random.randint(300, 1500) + (you["luck"] * 10)
            you["fuel"] += fuel
            print(f"⛽ Found {fuel} fuel!")
            unlock("fuel")
        elif roll < 0.8:
            treasure = random.choice(["Ancient Relic", "Crystal Shard", "Star Chart"])
            you["inventory"].append(treasure)
            print(f"🔮 Found {treasure}!")
            you["research"] += 20 + (you["luck"] * 2)
            if len(you["inventory"]) >= 10:
                unlock("collector")
        else:
            print("💨 Empty nebula...")
        
        if random.random() < 0.08:
            find_pet()
    else:
        print("Invalid!")

def random_fun():
    header("🎲 RANDOM FUN")
    action = random.choice(["joke", "pet", "luck", "treasure", "dance"])
    
    if action == "joke":
        tell_joke()
    elif action == "pet":
        find_pet()
    elif action == "luck":
        daily_luck()
    elif action == "treasure":
        treasure = random.randint(50, 200) + (you["luck"] * 5)
        you["credits"] += treasure
        print(f"\n💰 Found {treasure} credits!")
    elif action == "dance":
        gain = random.randint(3, 10)
        you["morale"] = min(100, you["morale"] + gain)
        print(f"\n💃 Dance party! Morale +{gain}!")

def help():
    header("📖 CAPTAIN'S GUIDE")
    print("""
🎮 HOW TO PLAY:
   • Fly missions for credits and fuel
   • Research tech upgrades
   • Hunt bounties for big rewards
   • Explore nebulae for treasures
   • Trade with aliens
   • Collect pets!

💡 TIPS:
   • Save often
   • Check daily luck
   • Keep 30% fuel reserve
   • Level up your crew
   • Get achievements!

🚀 GOOD LUCK!
    """)

# ========== DISPLAY ==========
def stats():
    header("📊 YOUR STATS")
    print(f"🚀 Missions: {you['missions']} | 🔥 Streak: {you['streak']}")
    print(f"⛽ Fuel: {you['fuel']:.0f} | 💰 Credits: {you['credits']}")
    print(f"📚 Research: {you['research']}")
    morale_bar()
    print(f"🏆 Rank: {you['rank']} | 📏 Furthest: {you['record']:,.0f} km")
    print(f"🍀 Luck: {'⭐'*you['luck']} | 🏅 Achievements: {len(you['trophies'])}")
    
    if you["trophies"]:
        print("\n🏅 Achievements:")
        for t in you["trophies"]:
            print(f"  • {ACHIEVEMENTS[t]}")
    if you["pets"]:
        print("\n🐾 Pets:")
        for p in you["pets"]:
            print(f"  • {p}")
    if you["inventory"]:
        print("\n📦 Inventory:")
        for i in you["inventory"]:
            print(f"  • {i}")

def view_crew():
    header("👥 YOUR CREW")
    for m in crew:
        print(f"\n🌟 {m['name']} - Lv.{m['level']} ({m['skill']})")
        print(f"   XP: {m['xp']}/{m['level']*100}")
        if m['level'] * 100 > 0:
            prog = int((m['xp'] / (m['level'] * 100)) * 10)
            print(f"   [{ '█'*prog }{ '░'*(10-prog) }]")

# ========== SAVE/LOAD ==========
def save():
    data = {k: v for k, v in you.items() if k not in ["trophies", "inventory", "pets"]}
    data.update({"trophies": you["trophies"], "inventory": you["inventory"], "pets": you["pets"]})
    data["crew"] = crew
    data["tech"] = TECH
    try:
        with open("space_save.json", "w") as f:
            json.dump(data, f)
        print("\n💾 Saved!")
    except:
        print("❌ Save failed!")

def load():
    global you, crew, TECH
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)
        for k, v in data.items():
            if k in you and k not in ["trophies", "inventory", "pets"]:
                you[k] = v
        you["trophies"] = data.get("trophies", [])
        you["inventory"] = data.get("inventory", [])
        you["pets"] = data.get("pets", [])
        if "crew" in data:
            for i, m in enumerate(data["crew"]):
                if i < len(crew):
                    crew[i] = m
        if "tech" in data:
            for name, vals in data["tech"].items():
                if name in TECH:
                    TECH[name]["owned"] = vals.get("owned", False)
        print("\n📀 Loaded! Welcome back!")
        return True
    except FileNotFoundError:
        print("❌ No save found!")
        return False
    except:
        print("❌ Load failed!")
        return False

# ========== MAIN ==========
def main():
    you["games_played"] += 1
    clear()
    
    print("""
    ╔════════════════════════════════════════════╗
    ║   🚀 SPACE ADVENTURE 🚀                  ║
    ║        The Friendly Space Game           ║
    ║     "The cosmos is yours to explore!"    ║
    ╚════════════════════════════════════════════╝
    """)
    
    print(f"🌟 Welcome, Captain!")
    print(f"💫 {random.choice(WELCOME)}\n")
    time.sleep(0.5)
    daily_luck()

    while True:
        print("\n" + "=" * 40)
        print("🌟 MAIN MENU")
        print("=" * 40)
        print("1. 🚀 Mission    2. 📊 Stats    3. 👥 Crew")
        print("4. 🧪 Research   5. 💰 Bounty   6. 👽 Trade")
        print("7. 🌌 Nebula     8. 💾 Save     9. 📀 Load")
        print("10. 🎲 Random    11. 📖 Help    12. ❌ Quit")
        print("=" * 40)
        
        choice = safe_input("Choice: ", "12")
        
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
        elif choice == "12":
            print(f"\n👋 Farewell! {random.choice(FAREWELL)}")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

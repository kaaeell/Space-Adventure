"""
🚀 SPACE DISTANCE CALCULATOR - Compact Edition
A fun space adventure game
"""

import math, random, time, json, os

# ========== YOUR SHIP ==========
ship = {
    "fuel": 5000, "credits": 1000, "missions": 0, "streak": 0,
    "morale": 80, "research": 0, "bounty_rank": 1,
    "highest": 0, "achievements": [], "inventory": []
}

# ========== YOUR CREW ==========
crew = [
    {"name": "Captain Rex", "skill": "Leadership", "level": 1, "xp": 0},
    {"name": "Engineer Jen", "skill": "Mechanics", "level": 1, "xp": 0},
    {"name": "Navigator Zoe", "skill": "Astrogation", "level": 1, "xp": 0},
    {"name": "Scientist Kim", "skill": "Research", "level": 1, "xp": 0},
    {"name": "Gunner Mack", "skill": "Combat", "level": 1, "xp": 0}
]

# ========== GAME DATA ==========
bounties = [
    {"name": "Red Pirate", "bounty": 500, "level": 1, "health": 3},
    {"name": "Shadow Corsair", "bounty": 1000, "level": 2, "health": 5},
    {"name": "Void Reaver", "bounty": 2000, "level": 3, "health": 7}
]

tech = {
    "Fuel Efficiency": {"cost": 100, "owned": False},
    "Warp Drive": {"cost": 200, "owned": False},
    "Shield Tech": {"cost": 150, "owned": False}
}

achievements = {
    "first": "🌱 Your first mission!",
    "explorer": "🌌 Travel 2000+ million km",
    "fuel": "⛽ Collect fuel from a nebula",
    "rich": "💰 Earn 10,000 credits",
    "legend": "⭐ Complete 50 missions",
    "streak": "🔥 5 missions in a row",
    "bounty": "💰 Defeat a bounty",
    "research": "🧠 Unlock 3 upgrades"
}

# ========== HELPERS ==========
def dist(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def unlock(key):
    if key in achievements and key not in ship["achievements"]:
        ship["achievements"].append(key)
        print(f"\n🎉 {achievements[key]} 🎉\n")
        time.sleep(0.3)

def crew_xp(amount):
    for m in crew:
        m["xp"] += amount
        if m["xp"] >= m["level"] * 100:
            m["xp"] = 0
            m["level"] += 1
            print(f"\n🎉 {m['name']} is now level {m['level']}!")
            ship["credits"] += random.randint(100, 300)

# ========== PLANETS ==========
PLANETS = {
    1: ("Earth", (0,0)), 2: ("Mars", (225,0)), 3: ("Venus", (108,0)),
    4: ("Jupiter", (778,0)), 5: ("Saturn", (1427,0)), 6: ("Uranus", (2871,0)),
    7: ("Neptune", (4495,0)), 8: ("Mercury", (58,0)), 9: ("Pluto", (5906,0))
}

def pick_planet():
    print("\n🪐 WHERE TO?")
    for n, (name, _) in PLANETS.items():
        print(f"{n}. {name}")
    def choose(q):
        while True:
            try:
                c = int(input(q))
                if c in PLANETS: return PLANETS[c]
                print("Invalid!")
            except: print("Enter a number!")
    return choose("Start: "), choose("Destination: ")

# ========== MISSIONS ==========
def mission():
    print("\n🚀 LAUNCH!")
    print("1. Known planets  2. Custom coordinates")
    if input("Choice: ") == "1":
        s_name, s = pick_planet()
        e_name, e = pick_planet()
    else:
        s = (float(input("Start x: ")), float(input("Start y: ")))
        e = (float(input("End x: ")), float(input("End y: ")))
        s_name, e_name = "Unknown", "Unknown"
    
    d = dist(s, e)
    print(f"\n📏 {s_name} → {e_name}: {d:.0f} million km")
    
    if d > ship["highest"]:
        ship["highest"] = d
        print("🏆 New record!")
    
    # Random events
    if random.random() < 0.25:
        if random.random() < 0.5:
            d *= 0.6
            print("🌀 Wormhole! Distance reduced!")
        else:
            bonus = random.randint(100, 300)
            ship["credits"] += bonus
            print(f"💰 Found treasure! +{bonus} credits!")
    
    # Fuel
    needed = d * 0.5
    if ship["fuel"] < needed:
        print(f"\n⛽ Need {needed:.0f} fuel, have {ship['fuel']:.0f}")
        if input("1. Mine asteroid  2. Buy fuel: ") == "1":
            if random.random() < 0.6:
                ship["fuel"] += random.randint(200, 800)
                print("✅ Mined fuel!")
            else:
                ship["fuel"] = max(0, ship["fuel"] - random.randint(50, 200))
                print("💥 Asteroid damaged ship!")
        else:
            amt = int(input("How much? "))
            cost = amt * 2
            if ship["credits"] >= cost:
                ship["credits"] -= cost
                ship["fuel"] += amt
                print(f"✅ Bought {amt} fuel!")
        return
    
    # Complete mission
    ship["fuel"] -= needed
    earned = int(d * 0.8 + 50)
    ship["credits"] += earned
    ship["missions"] += 1
    ship["streak"] += 1
    ship["morale"] = min(100, ship["morale"] + random.randint(5, 15))
    
    print(f"\n✅ Mission complete! +{earned} credits")
    print(f"⛽ Fuel: {ship['fuel']:.0f} | 😊 Morale: {ship['morale']}%")
    
    # Achievements
    if ship["missions"] == 1: unlock("first")
    if ship["credits"] >= 10000: unlock("rich")
    if ship["missions"] >= 50: unlock("legend")
    if ship["streak"] >= 5: unlock("streak")
    
    crew_xp(20)

# ========== BOUNTY HUNTING ==========
def bounty():
    print("\n💰 BOUNTY HUNTING")
    print(f"🏆 Rank: {ship['bounty_rank']}")
    
    avail = [b for b in bounties if b["level"] <= ship["bounty_rank"] + 1]
    if not avail:
        print("No bounties available!")
        return
    
    for i, t in enumerate(avail[:3], 1):
        print(f"{i}. {t['name']} - 💰 {t['bounty']}")
    
    choice = input("Choose: ")
    if not choice.isdigit() or int(choice) > len(avail[:3]):
        return
    
    target = avail[int(choice)-1]
    print(f"\n⚔️ Fighting {target['name']}...")
    time.sleep(0.5)
    
    hp = target["health"]
    enemy_hp = target["health"]
    
    while hp > 0 and enemy_hp > 0:
        print(f"\n❤️ You: {hp} | {target['name']}: {enemy_hp}")
        action = input("1. Attack  2. Dodge: ")
        
        if action == "1":
            dmg = random.randint(2, 6)
            enemy_hp -= dmg
            print(f"⚡ Hit for {dmg}!")
            counter = random.randint(1, 4)
            hp -= counter
            print(f"💥 Took {counter} damage!")
        else:
            if random.random() < 0.5:
                print("🛡️ Dodged!")
            else:
                counter = random.randint(2, 5)
                hp -= counter
                print(f"💥 Took {counter} damage!")
    
    if hp > 0:
        ship["credits"] += target["bounty"]
        print(f"\n🎉 VICTORY! +{target['bounty']} credits!")
        if target["level"] == ship["bounty_rank"]:
            ship["bounty_rank"] += 1
            print(f"🏆 Rank up! Now {ship['bounty_rank']}")
        unlock("bounty")
        crew_xp(30)
    else:
        print("\n💀 Defeated! Lost 100 credits")
        ship["credits"] = max(0, ship["credits"] - 100)

# ========== RESEARCH ==========
def research():
    print("\n🧪 RESEARCH")
    print(f"📚 Points: {ship['research']}")
    for i, (name, data) in enumerate(tech.items(), 1):
        status = "✅" if data["owned"] else f"💰 {data['cost']}pts"
        print(f"{i}. {name} - {status}")
    print("4. Convert 100 credits → 20 RP")
    
    choice = input("Choose: ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        name, data = list(tech.items())[int(choice)-1]
        if not data["owned"] and ship["research"] >= data["cost"]:
            ship["research"] -= data["cost"]
            data["owned"] = True
            print(f"✨ Unlocked {name}!")
            unlock("research")
        else:
            print("❌ Not enough points!")
    elif choice == "4" and ship["credits"] >= 100:
        ship["credits"] -= 100
        ship["research"] += 20
        print("✅ Converted!")

# ========== ALIEN TRADE ==========
def trade():
    print("\n👽 ALIEN TRADE")
    print(f"💰 Credits: {ship['credits']}")
    items = {"🌌 Crystal": 500, "💫 Warp Core": 2000, "🔮 Shield": 1500, "🍕 Space Pizza": 50}
    for i, (item, price) in enumerate(items.items(), 1):
        print(f"{i}. {item} - {price}")
    
    choice = input("Buy (number) or 'q': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        item, price = list(items.items())[int(choice)-1]
        if ship["credits"] >= price:
            ship["credits"] -= price
            ship["inventory"].append(item)
            print(f"✨ Bought {item}!")

# ========== EXPLORE NEBULA ==========
def nebula():
    nebulae = {"Orion": (1340,-220), "Eagle": (7000,0), "Helix": (695,280)}
    print("\n🌌 NEBULA EXPLORATION")
    for i, name in enumerate(nebulae.keys(), 1):
        print(f"{i}. {name}")
    
    choice = input("Choose: ")
    if choice.isdigit() and 1 <= int(choice) <= len(nebulae):
        name = list(nebulae.keys())[int(choice)-1]
        print(f"\n🚀 Exploring {name}...")
        time.sleep(1)
        
        if random.random() < 0.6:
            gained = random.randint(300, 1500)
            ship["fuel"] += gained
            print(f"⛽ Found {gained} fuel!")
            unlock("fuel")
        else:
            artifact = random.choice(["relic", "crystal", "chart"])
            ship["inventory"].append(artifact)
            print(f"🔮 Found {artifact}!")
            ship["research"] += 20

# ========== STATS ==========
def stats():
    print("\n" + "="*50)
    print("📊 YOUR STATS")
    print("="*50)
    print(f"🚀 Missions: {ship['missions']} | 🔥 Streak: {ship['streak']}")
    print(f"⛽ Fuel: {ship['fuel']:.0f} | 💰 Credits: {ship['credits']}")
    print(f"📚 Research: {ship['research']} | 😊 Morale: {ship['morale']}%")
    print(f"🏆 Bounty Rank: {ship['bounty_rank']}")
    print(f"📏 Furthest: {ship['highest']:.0f} million km")
    print(f"🏅 Achievements: {len(ship['achievements'])}")
    
    if ship["achievements"]:
        print("\n🏅 Achievements:")
        for a in ship["achievements"]:
            print(f"  • {achievements[a]}")
    if ship["inventory"]:
        print("\n📦 Inventory:")
        for item in ship["inventory"]:
            print(f"  • {item}")

# ========== SAVE/LOAD ==========
def save():
    data = {k: v for k, v in ship.items() if k != "achievements"}
    data["achievements"] = ship["achievements"]
    data["crew"] = crew
    with open("space_save.json", "w") as f:
        json.dump(data, f)
    print("💾 Saved!")

def load():
    global ship, crew
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)
        for k, v in data.items():
            if k in ship and k != "achievements":
                ship[k] = v
        ship["achievements"] = data.get("achievements", [])
        crew[:] = data.get("crew", crew)
        print("📀 Loaded!")
        return True
    except:
        print("❌ No save found!")
        return False

# ========== CREW VIEW ==========
def view_crew():
    print("\n👥 CREW")
    for m in crew:
        print(f"• {m['name']} - Lv.{m['level']} ({m['skill']}) XP: {m['xp']}/{m['level']*100}")

# ========== MAIN ==========
def main():
    print("""
    ╔═══════════════════════════════════════╗
    ║   🚀 SPACE DISTANCE CALCULATOR 🚀    ║
    ║         Compact Edition v3.4         ║
    ║   "To infinity and beyond!"          ║
    ╚═══════════════════════════════════════╝
    """)
    
    while True:
        print("\n" + "="*40)
        print("🌟 MAIN MENU")
        print("="*40)
        print("1. 🚀 Mission   2. 📊 Stats   3. 👥 Crew")
        print("4. 🧪 Research  5. 💰 Bounty  6. 👽 Trade")
        print("7. 🌌 Nebula    8. 💾 Save    9. 📀 Load")
        print("10. ❌ Quit")
        
        choice = input("\nChoice: ")
        
        if choice == "1": mission()
        elif choice == "2": stats()
        elif choice == "3": view_crew()
        elif choice == "4": research()
        elif choice == "5": bounty()
        elif choice == "6": trade()
        elif choice == "7": nebula()
        elif choice == "8": save()
        elif choice == "9": load()
        elif choice == "10":
            print("\n👋 Farewell, Captain! Live long and prosper! 🖖")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

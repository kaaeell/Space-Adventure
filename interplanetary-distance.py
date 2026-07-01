"""
🚀 SPACE DISTANCE CALCULATOR
The Friendly Space Adventure Game
Version 3.6 - FINAL
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
    "total_distance": 0,
    "trophies": [],
    "inventory": [],
    "pets": [],
    "luck": 0,
    "last_play": None,
    "pirates_defeated": 0,
    "nebula_explored": 0,
    "jokes_told": 0
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
    "jokester": "😂 Told 10 jokes!"
}

PETS = [
    "🐶 Space Dog", "🐱 Robot Cat", "🐹 Alien Hamster", 
    "🐉 Tiny Dragon", "🦊 Quantum Fox", "🐧 Space Penguin", 
    "🐙 Star Octopus", "🦄 Nebula Unicorn"
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
    "🧪 Research Data": 400
}

WELCOME_MESSAGES = [
    "The stars are calling!",
    "Adventure awaits!",
    "Time to explore the cosmos!",
    "Another day, another galaxy!",
    "The universe is your playground!"
]

# ============================================
# HELPER FUNCTIONS
# ============================================

def clear_screen():
    """Clear the screen for cleaner display"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Print a styled header"""
    print("\n" + "=" * 50)
    print(f"  {text}")
    print("=" * 50)

def distance(p1, p2):
    """Calculate distance between two points"""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def unlock_achievement(key):
    """Unlock an achievement with celebration"""
    if key in ACHIEVEMENTS and key not in player["trophies"]:
        player["trophies"].append(key)
        print(f"\n🎉 {'='*40}")
        print(f"🎉 {ACHIEVEMENTS[key]}")
        print(f"🎉 {'='*40}\n")
        time.sleep(0.8)

def gain_crew_xp(amount):
    """Give XP to crew members and check for level ups"""
    for member in crew:
        member["xp"] += amount
        if member["xp"] >= member["level"] * 100:
            member["xp"] = 0
            member["level"] += 1
            print(f"\n🌟 {member['name']} reached level {member['level']}!")
            bonus = random.randint(100, 300)
            player["credits"] += bonus
            print(f"💰 Crew celebration! +{bonus} credits!")

def check_daily_luck():
    """Check and update daily luck"""
    today = datetime.now().date()
    if player["last_play"] != str(today):
        player["luck"] = random.randint(1, 10)
        player["last_play"] = str(today)
        
        print("\n" + "─" * 40)
        print(f"🍀 Today's Luck: {'⭐' * player['luck']}")
        
        if player["luck"] >= 8:
            print("🌟 The stars are aligned in your favor!")
            unlock_achievement("lucky")
        elif player["luck"] >= 5:
            print("✨ The cosmos smiles upon you today")
        else:
            print("🌙 The universe feels... quiet today")
        print("─" * 40 + "\n")
        time.sleep(0.5)

def find_pet():
    """Find a space pet"""
    pet = random.choice(PETS)
    if pet not in player["pets"]:
        player["pets"].append(pet)
        print(f"\n🐾 A wild {pet} appeared and joined your crew!")
        print("💕 It looks at you with adorable eyes...")
        unlock_achievement("pet")
        player["morale"] = min(100, player["morale"] + 10)
    else:
        print(f"\n🐾 {pet} is already part of your space family!")

def tell_joke():
    """Tell a joke and boost morale"""
    joke = random.choice(JOKES)
    print(f"\n😂 {joke}")
    player["morale"] = min(100, player["morale"] + 5)
    player["jokes_told"] += 1
    print(f"😊 The crew chuckles. Morale +5! (Now: {player['morale']}%)")
    
    if player["jokes_told"] >= 10:
        unlock_achievement("jokester")

# ============================================
# MAIN GAME FUNCTIONS
# ============================================

def pick_planet():
    """Choose two planets"""
    print("\n🪐 WHERE TO?")
    print("─" * 30)
    for num, (name, _) in PLANETS.items():
        print(f"{num}. {name}")
    print("─" * 30)

    def choose(question):
        while True:
            try:
                choice = int(input(question))
                if choice in PLANETS:
                    return PLANETS[choice]
                print("❌ Invalid choice! Try again.")
            except ValueError:
                print("❌ Please enter a number!")

    start = choose("🌍 Starting planet: ")
    end = choose("🎯 Destination planet: ")
    
    # Get planet names
    start_name = "🌍 Earth"
    end_name = "📍 Destination"
    for num, (name, coords) in PLANETS.items():
        if coords == start:
            start_name = name
        if coords == end:
            end_name = name
    
    return start_name, start, end_name, end

def start_mission():
    """Start a space mission"""
    check_daily_luck()

    print_header("🚀 PREPARING FOR LAUNCH")
    print("1. 📍 Travel to known planets")
    print("2. 🗺️ Explore unknown coordinates")
    print("3. ↩️ Return to menu")

    choice = input("\nChoice: ")

    if choice == "3":
        return
    elif choice == "1":
        start_name, start, end_name, end = pick_planet()
    elif choice == "2":
        try:
            print("\n📡 Enter coordinates (in million km)")
            start = (float(input("Start x: ")), float(input("Start y: ")))
            end = (float(input("End x: ")), float(input("End y: ")))
            start_name, end_name = "🚀 Unknown", "📍 Unknown"
        except ValueError:
            print("❌ Invalid coordinates!")
            return
    else:
        print("❌ Invalid choice!")
        return

    # Calculate distance
    dist = distance(start, end)
    player["total_distance"] += dist
    print(f"\n📏 Distance: {dist:,.0f} million km")
    print(f"📊 Total distance traveled: {player['total_distance']:,.0f} million km")

    if dist > player["record"]:
        player["record"] = dist
        print("🏆 NEW RECORD DISTANCE!")

    # Random events
    if random.random() < 0.25 + (player["luck"] * 0.01):
        event = random.choice(["wormhole", "treasure", "pet", "joke", "alien_signal"])
        if event == "wormhole":
            dist *= 0.6
            print("🌀 You found a wormhole shortcut!")
            print(f"📏 New distance: {dist:,.0f} million km")
        elif event == "treasure":
            bonus = random.randint(100, 300) + (player["luck"] * 10)
            player["credits"] += bonus
            print(f"💰 You found a floating treasure pod! +{bonus} credits!")
        elif event == "pet":
            find_pet()
        elif event == "joke":
            tell_joke()
        elif event == "alien_signal":
            print("📡 You picked up a mysterious alien signal...")
            if random.random() < 0.5:
                gift = random.randint(50, 150)
                player["credits"] += gift
                print(f"👽 The aliens send you a gift! +{gift} credits!")
            else:
                print("👽 The signal fades away...")

    # Fuel check
    fuel_needed = dist * 0.5
    if TECH["⛽ Fuel Efficiency"]["owned"]:
        fuel_needed *= 0.9
        print("⛽ Fuel Efficiency active! Using less fuel.")
    
    if player["fuel"] < fuel_needed:
        print(f"\n⛽ INSUFFICIENT FUEL!")
        print(f"   Need: {fuel_needed:.0f} fuel")
        print(f"   Have: {player['fuel']:.0f} fuel")
        print("\n1. Mine asteroid (risky but free)")
        print("2. Buy fuel (2 credits/unit)")
        print("3. Abort mission")
        choice = input("Choice: ")

        if choice == "3":
            print("🔄 Mission aborted. Returning to base.")
            return
        elif choice == "1":
            if random.random() < 0.6 + (player["luck"] * 0.02):
                gained = random.randint(200, 800)
                player["fuel"] += gained
                print(f"✅ Successfully mined {gained} fuel!")
            else:
                lost = random.randint(50, 200)
                player["fuel"] = max(0, player["fuel"] - lost)
                print(f"💥 Asteroid collision! Lost {lost} fuel!")
        elif choice == "2":
            try:
                amount = int(input("How much fuel? "))
                cost = amount * 2
                if player["credits"] >= cost:
                    player["credits"] -= cost
                    player["fuel"] += amount
                    print(f"✅ Purchased {amount} fuel!")
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
    morale_gain = random.randint(5, 15)
    player["morale"] = min(100, player["morale"] + morale_gain)

    print_header("✅ MISSION COMPLETE")
    print(f"💰 Credits earned: +{earned}")
    print(f"⛽ Fuel remaining: {player['fuel']:.0f}")
    print(f"😊 Crew morale: {player['morale']}% (+{morale_gain})")
    print(f"📊 Total missions: {player['missions']}")
    print(f"🔥 Current streak: {player['streak']}")

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
    if player["total_distance"] >= 10000:
        unlock_achievement("traveler")

    gain_crew_xp(20)

def hunt_bounty():
    """Hunt a bounty target"""
    check_daily_luck()

    print_header("💰 BOUNTY HUNTING")
    print(f"🏆 Your rank: {player['rank']}")

    available = [b for b in BOUNTIES if b["level"] <= player["rank"] + 1]
    if not available:
        print("❌ No bounties available at your rank.")
        print("💡 Complete more missions to unlock harder targets!")
        return

    print("\n🎯 AVAILABLE TARGETS:")
    for i, target in enumerate(available[:4], 1):
        print(f"{i}. {target['name']}")
        print(f"   💰 Reward: {target['reward']} | Level: {target['level']}")

    choice = input("\nChoose target (number): ")
    if not choice.isdigit() or int(choice) > len(available[:4]):
        return

    target = available[int(choice) - 1]
    print(f"\n⚔️ ENGAGING {target['name']}...")
    time.sleep(0.5)

    # Combat
    my_hp = target["hp"] + (player["luck"] // 3)
    enemy_hp = target["hp"]
    
    if TECH["🛡️ Shield Tech"]["owned"]:
        my_hp += 2
        print("🛡️ Shield Tech active! Extra protection!")
    
    print(f"💪 Bonus health: +{player['luck']//3}")
    print(f"❤️ Your health: {my_hp} | Enemy health: {enemy_hp}")

    while my_hp > 0 and enemy_hp > 0:
        print(f"\n❤️ You: {my_hp} | {target['name']}: {enemy_hp}")
        action = input("1. ⚔️ Attack  2. 🛡️ Dodge  3. 💊 Use item: ")

        if action == "1":
            damage = random.randint(2, 6) + (player["luck"] // 5)
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
            if random.random() < 0.5 + (player["luck"] * 0.02):
                print("🛡️ You gracefully dodge the attack!")
            else:
                counter = random.randint(2, 5)
                my_hp -= counter
                print(f"💥 Too slow! You took {counter} damage!")
        elif action == "3":
            # Check if player has any consumable items
            consumable_items = ["🍕 Space Pizza"]
            found_item = None
            for item in consumable_items:
                if item in player["inventory"]:
                    found_item = item
                    break
            
            if found_item:
                player["inventory"].remove(found_item)
                heal = random.randint(3, 8)
                max_hp = target["hp"] + (player["luck"] // 3)
                my_hp = min(max_hp, my_hp + heal)
                print(f"💊 You used {found_item}! Healed {heal} health!")
            else:
                print("❌ No items available! You have: " + ", ".join(player["inventory"]) if player["inventory"] else "Nothing")
        else:
            print("Invalid action!")

    if my_hp > 0:
        reward_bonus = int(target["reward"] * (1 + player["luck"] * 0.01))
        player["credits"] += reward_bonus
        player["pirates_defeated"] += 1
        print(f"\n🎉 VICTORY!")
        print(f"💰 Collected {reward_bonus} credits!")
        if target["level"] == player["rank"]:
            player["rank"] += 1
            print(f"🏆 Rank up! You are now level {player['rank']}")
        unlock_achievement("bounty")
        
        if player["pirates_defeated"] >= 10:
            unlock_achievement("pirate_hunter")
        
        gain_crew_xp(30)
    else:
        print("\n💀 You were defeated!")
        print("💸 Lost 100 credits")
        player["credits"] = max(0, player["credits"] - 100)

def do_research():
    """Research new technology"""
    print_header("🧪 RESEARCH LAB")
    print(f"📚 Research points: {player['research']}\n")

    for i, (name, data) in enumerate(TECH.items(), 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} pts"
        print(f"{i}. {name}")
        print(f"   {data['desc']} - {status}")

    print("\n5. 💰 Convert 100 credits → 20 research points")
    print("6. ↩️ Back to menu")

    choice = input("\nChoice: ")
    if choice == "6":
        return
    elif choice.isdigit() and 1 <= int(choice) <= 4:
        name, data = list(TECH.items())[int(choice) - 1]
        if not data["owned"]:
            if player["research"] >= data["cost"]:
                player["research"] -= data["cost"]
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
        if player["credits"] >= 100:
            player["credits"] -= 100
            player["research"] += 20
            print("✅ Converted credits to research points!")
        else:
            print("❌ Not enough credits!")

def trade_with_aliens():
    """Trade with aliens"""
    print_header("👽 ALIEN TRADE")
    print(f"💰 Your credits: {player['credits']}\n")

    print("🛒 AVAILABLE ITEMS:")
    for i, (item, price) in enumerate(ALIEN_ITEMS.items(), 1):
        print(f"{i}. {item} - {price} credits")

    choice = input("\nBuy (number) or 'q' to quit: ")
    if choice == 'q' or choice == 'Q':
        return
    elif choice.isdigit() and 1 <= int(choice) <= len(ALIEN_ITEMS):
        item, price = list(ALIEN_ITEMS.items())[int(choice) - 1]
        if player["credits"] >= price:
            player["credits"] -= price
            player["inventory"].append(item)
            print(f"\n✨ Purchased {item}!")
            print(f"💰 Remaining credits: {player['credits']}")
        else:
            print("❌ Not enough credits!")

def explore_nebula():
    """Explore a nebula"""
    print_header("🌌 NEBULA EXPLORATION")
    
    for i, name in enumerate(NEBULAE.keys(), 1):
        print(f"{i}. {name}")

    choice = input("\nChoose: ")
    if choice.isdigit() and 1 <= int(choice) <= len(NEBULAE):
        name = list(NEBULAE.keys())[int(choice) - 1]
        print(f"\n🚀 Entering {name}...")
        time.sleep(1)

        player["nebula_explored"] += 1
        
        if player["nebula_explored"] >= 5:
            unlock_achievement("nebula_expert")

        roll = random.random()
        if roll < 0.6 + (player["luck"] * 0.02):
            fuel_found = random.randint(300, 1500) + (player["luck"] * 10)
            player["fuel"] += fuel_found
            print(f"⛽ Discovered {fuel_found} fuel in the nebula!")
            unlock_achievement("fuel")
        elif roll < 0.8:
            treasure = random.choice(["Ancient Relic", "Crystal Shard", "Star Chart", "Alien Artifact"])
            player["inventory"].append(treasure)
            print(f"🔮 Found {treasure}!")
            player["research"] += 20 + (player["luck"] * 2)
        else:
            print("💨 The nebula is empty... but you enjoy the view!")

        if random.random() < 0.08:
            find_pet()
    else:
        print("Invalid choice!")

def random_activity():
    """Do something random for fun"""
    print_header("🎲 RANDOM FUN")
    
    options = ["tell_joke", "find_pet", "check_luck", "find_treasure", "meditate"]
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
        print(f"\n💰 You found {treasure} credits floating in space!")
    elif action == "meditate":
        gain = random.randint(5, 15)
        player["morale"] = min(100, player["morale"] + gain)
        print(f"\n🧘‍♂️ Your crew meditates in zero-gravity.")
        print(f"😊 Morale +{gain}! (Now: {player['morale']}%)")

def view_help():
    """Show helpful tips"""
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
    """Display all player stats"""
    print_header("📊 YOUR SPACE STATISTICS")
    
    print(f"🚀 Missions:     {player['missions']}")
    print(f"🔥 Streak:       {player['streak']}")
    print(f"⛽ Fuel:         {player['fuel']:.0f}")
    print(f"💰 Credits:      {player['credits']}")
    print(f"📚 Research:     {player['research']}")
    print(f"😊 Morale:       {player['morale']}%")
    print(f"🏆 Bounty Rank:  {player['rank']}")
    print(f"📏 Furthest:     {player['record']:,.0f} million km")
    print(f"🌠 Total Dist.:  {player['total_distance']:,.0f} million km")
    print(f"🍀 Luck:         {'⭐' * player['luck']} ({player['luck']}/10)")
    print(f"⚔️ Pirates Def.: {player['pirates_defeated']}")
    print(f"🌌 Nebulae Exp.: {player['nebula_explored']}")
    print(f"😂 Jokes Told:   {player['jokes_told']}")
    print(f"🏅 Achievements: {len(player['trophies'])}")

    if player["trophies"]:
        print("\n🏅 ACHIEVEMENTS:")
        for t in player["trophies"]:
            print(f"  • {ACHIEVEMENTS[t]}")

    if player["pets"]:
        print("\n🐾 SPACE PETS:")
        for pet in player["pets"]:
            print(f"  • {pet}")

    if player["inventory"]:
        print("\n📦 INVENTORY:")
        for item in player["inventory"]:
            print(f"  • {item}")

def show_crew():
    """Display crew information"""
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
        "total_distance": player["total_distance"],
        "trophies": player["trophies"],
        "inventory": player["inventory"],
        "pets": player["pets"],
        "luck": player["luck"],
        "last_play": player["last_play"],
        "pirates_defeated": player["pirates_defeated"],
        "nebula_explored": player["nebula_explored"],
        "jokes_told": player["jokes_told"],
        "crew": crew,
        "tech": TECH
    }
    try:
        with open("space_save.json", "w") as f:
            json.dump(data, f)
        print("\n💾 Game saved successfully!")
        print(f"📅 Saved at: {datetime.now().strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"❌ Save failed: {e}")

def load_game():
    """Load game progress"""
    global player, crew, TECH
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)

        # Load player data
        for key in data:
            if key in player and key not in ["trophies", "inventory", "pets"]:
                player[key] = data[key]
        
        # Load lists
        player["trophies"] = data.get("trophies", [])
        player["inventory"] = data.get("inventory", [])
        player["pets"] = data.get("pets", [])
        
        # Load crew
        if "crew" in data:
            for i, member in enumerate(data["crew"]):
                if i < len(crew):
                    crew[i] = member
        
        # Load tech
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
    """Main game entry point"""
    clear_screen()
    
    print("""
    ╔════════════════════════════════════════════╗
    ║                                          ║
    ║   🚀 SPACE DISTANCE CALCULATOR 🚀        ║
    ║                                          ║
    ║        The Friendly Space Adventure      ║
    ║                                          ║
    ║           Version 3.6 - FINAL            ║
    ║                                          ║
    ║     "The cosmos is yours to explore!"    ║
    ║                                          ║
    ╚════════════════════════════════════════════╝
    """)
    
    print(f"🌟 Welcome, Captain!")
    print(f"💫 {random.choice(WELCOME_MESSAGES)}\n")
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
        print("6. 👽 Trade with Aliens")
        print("7. 🌌 Explore Nebula")
        print("8. 💾 Save Game")
        print("9. 📀 Load Game")
        print("10. 🎲 Random Fun")
        print("11. 📖 Help")
        print("12. ❌ Quit")
        print("=" * 40)

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
            view_help()
        elif choice == "12":
            print("\n" + "=" * 40)
            print("👋 Farewell, Captain!")
            print("⭐ Live long and prosper! 🖖")
            print("=" * 40 + "\n")
            break
        else:
            print("❌ Invalid choice, Captain!")

if __name__ == "__main__":
    main()

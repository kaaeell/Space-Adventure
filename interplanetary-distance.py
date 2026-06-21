"""
🚀 SPACE DISTANCE CALCULATOR - The Friendly Space Adventure
=============================================================
A fun, interactive space exploration game where you travel between planets,
hunt bounties, research technology, and build your crew!

Created by: A Space Enthusiast
Version: 3.4 (The Friendly Edition)
License: MIT

How to play:
- Run the game and follow the menu
- Fly missions to earn credits and research points
- Upgrade your ship and crew
- Hunt bounties and explore nebulae
- Save your progress and continue later!

Let the adventure begin! 🚀
"""

import math
import random
import time
from datetime import datetime
import json
import os

# ============================================================================
# YOUR SPACE JOURNEY STARTS HERE
# ============================================================================

# These are your spaceship's current stats - you start as a rookie space captain!
ship = {
    "fuel": 5000,              # You need fuel to fly!
    "credits": 1000,           # Space money for upgrades and supplies
    "missions": 0,             # How many missions you've completed
    "streak": 0,               # Consecutive missions without failure
    "morale": 80,              # How happy your crew is (0-100)
    "research": 0,             # Science points for unlocking cool tech
    "bounty_rank": 1,          # Your reputation as a bounty hunter
    "highest_distance": 0,     # Furthest you've ever traveled
    "achievements": [],        # Trophies you've earned
    "inventory": []            # Stuff you've collected
}

# Your crew members - each has special skills!
crew = [
    {"name": "Captain Rex", "skill": "Leadership", "level": 1, "xp": 0},
    {"name": "Engineer Jen", "skill": "Mechanics", "level": 1, "xp": 0},
    {"name": "Navigator Zoe", "skill": "Astrogation", "level": 1, "xp": 0},
    {"name": "Scientist Kim", "skill": "Research", "level": 1, "xp": 0},
    {"name": "Gunner Mack", "skill": "Combat", "level": 1, "xp": 0}
]

# ============================================================================
# THE SPACE UNIVERSE - All the cool stuff you can find
# ============================================================================

# Strange phenomena you might discover while flying
anomalies = {
    "Time Dilation Field": {"effect": "research", "reward": 50},
    "Quantum Rift": {"effect": "teleport", "reward": None},
    "Sentient Nebula": {"effect": "credits", "reward": 300},
    "Space Whale Song": {"effect": "morale", "reward": 20}
}

# Bad guys you can hunt for money
bounties = [
    {"name": "Red Pirate", "bounty": 500, "level": 1, "health": 3},
    {"name": "Shadow Corsair", "bounty": 1000, "level": 2, "health": 5},
    {"name": "Void Reaver", "bounty": 2000, "level": 3, "health": 7}
]

# Tech upgrades you can research
tech_upgrades = {
    "Fuel Efficiency": {"cost": 100, "owned": False},
    "Warp Drive": {"cost": 200, "owned": False},
    "Shield Tech": {"cost": 150, "owned": False}
}

# Cool achievements to unlock
achievement_list = {
    "first_step": "🌱 Your first space mission!",
    "explorer": "🌌 Travel over 2000 million km",
    "fuel_hunter": "⛽ Collect fuel from a nebula",
    "millionaire": "💰 Earn 10,000 credits",
    "legend": "⭐ Complete 50 missions",
    "streak": "🔥 Complete 5 missions in a row",
    "bounty_hunter": "💰 Defeat a bounty target",
    "researcher": "🧠 Unlock 3 research upgrades"
}

# ============================================================================
# HELPER FUNCTIONS - The math and magic behind the scenes
# ============================================================================

def distance_between(point1, point2):
    """Calculates how far apart two points are in space using math"""
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

def unlock_achievement(ach_key):
    """Celebrates when you earn a new achievement - makes you feel special!"""
    if ach_key in achievement_list and ach_key not in ship["achievements"]:
        ship["achievements"].append(ach_key)
        print(f"\n🎉 ACHIEVEMENT UNLOCKED: {achievement_list[ach_key]} 🎉\n")
        time.sleep(0.5)

def give_crew_xp(amount):
    """Your crew learns and grows from adventures - they get better over time!"""
    for member in crew:
        member["xp"] += amount
        # Level up when they've learned enough
        if member["xp"] >= member["level"] * 100:
            member["xp"] = 0
            member["level"] += 1
            print(f"\n🎉 {member['name']} is now level {member['level']}! They're getting really good at {member['skill']}!")
            ship["credits"] += random.randint(100, 300)  # Bonus for leveling up!

def show_your_status():
    """Shows how your space adventure is going - your personal dashboard!"""
    print("\n" + "="*50)
    print("📊 YOUR SPACE STATUS")
    print("="*50)
    print(f"🚀 Missions: {ship['missions']} | 🔥 Streak: {ship['streak']}")
    print(f"⛽ Fuel: {ship['fuel']:.0f} | 💰 Credits: {ship['credits']}")
    print(f"📚 Research: {ship['research']} | 😊 Morale: {ship['morale']}%")
    print(f"🏆 Bounty Rank: {ship['bounty_rank']}")
    print(f"📏 Furthest Traveled: {ship['highest_distance']:.0f} million km")
    print("="*50)

# ============================================================================
# THE FUN STUFF - All the things you can do in the game
# ============================================================================

def pick_a_planet():
    """You choose where to travel in space - like a cosmic travel agent!"""
    planets = {
        1: ("Earth", (0,0)), 
        2: ("Mars", (225,0)), 
        3: ("Venus", (108,0)),
        4: ("Jupiter", (778,0)), 
        5: ("Saturn", (1427,0)), 
        6: ("Uranus", (2871,0)),
        7: ("Neptune", (4495,0)), 
        8: ("Mercury", (58,0)), 
        9: ("Pluto", (5906,0))
    }
    
    print("\n🪐 WHERE DO YOU WANT TO GO?")
    for num, (name, _) in planets.items():
        print(f"{num}. {name}")
    
    def choose_planet(question):
        while True:
            try:
                choice = int(input(question))
                if choice in planets:
                    return planets[choice]
                print("That planet doesn't exist! Try again.")
            except ValueError:
                print("Please enter a number!")
    
    start_name, start = choose_planet("Where are you starting from? ")
    end_name, end = choose_planet("Where are you going to? ")
    return start_name, start, end_name, end

def start_mission():
    """Your main adventure - flying through space! This is where the fun begins!"""
    print("\n🚀 PREPARING FOR LAUNCH... 🚀")
    print("="*40)
    
    # Choose your destination
    print("1. Travel between known planets")
    print("2. Explore unknown coordinates")
    choice = input("What do you want to do? ")
    
    if choice == "1":
        start_name, start, end_name, end = pick_a_planet()
    else:
        print("\n📡 Enter coordinates (in million km)")
        start = (float(input("Start x: ")), float(input("Start y: ")))
        end = (float(input("Destination x: ")), float(input("Destination y: ")))
        start_name, end_name = "Unknown", "Unknown"
    
    # Calculate the journey - this is the core math!
    distance = distance_between(start, end)
    print(f"\n📏 The journey from {start_name} to {end_name} is {distance:.0f} million km")
    
    # Update your records - you're becoming a legend!
    if distance > ship["highest_distance"]:
        ship["highest_distance"] = distance
        print("🏆 That's your longest journey yet!")
    
    # Random space events - space is full of surprises!
    if random.random() < 0.3:
        event = random.choice(["🌀 WORMHOLE!", "✨ COSMIC CACHE!", "📡 MYSTERY SIGNAL"])
        print(f"\n⚠️ SURPRISE! {event}")
        if "WORMHOLE" in event:
            distance *= 0.6
            print(f"🔄 You found a shortcut! Distance reduced to {distance:.0f} million km!")
            unlock_achievement("wormhole_rider")
        elif "CACHE" in event:
            bonus = random.randint(100, 300)
            ship["credits"] += bonus
            print(f"💰 You found floating treasure! +{bonus} credits!")
    
    # Fuel check - you need gas to fly!
    fuel_needed = distance * 0.5
    if ship["fuel"] < fuel_needed:
        print(f"\n⛽ Uh oh! You need {fuel_needed:.0f} fuel but only have {ship['fuel']:.0f}")
        emergency_fuel()
        return start_mission()  # Try again with more fuel
    
    # Take off! You're flying through space!
    ship["fuel"] -= fuel_needed
    earned = int(distance * 0.8 + 50)
    ship["credits"] += earned
    
    # Mission success! Time to celebrate!
    ship["missions"] += 1
    ship["streak"] += 1
    ship["morale"] = min(100, ship["morale"] + random.randint(5, 15))
    
    print(f"\n✅ MISSION SUCCESSFUL!")
    print(f"💰 Earned {earned} credits")
    print(f"⛽ Fuel remaining: {ship['fuel']:.0f}")
    print(f"😊 Crew morale: {ship['morale']}%")
    
    # Check for achievements - you might have earned some!
    if ship["missions"] == 1:
        unlock_achievement("first_step")
    if ship["credits"] >= 10000:
        unlock_achievement("millionaire")
    if ship["missions"] >= 50:
        unlock_achievement("legend")
    if ship["streak"] >= 5:
        unlock_achievement("streak")
    
    # Your crew learns from the experience - they're getting smarter!
    give_crew_xp(20)

def emergency_fuel():
    """When you're stranded in space - time to get creative!"""
    global ship
    print("\n🆘 EMERGENCY FUEL RESCUE")
    print("1. Mine an asteroid (risky but free!)")
    print("2. Buy fuel (2 credits per unit)")
    
    choice = input("What's your plan? ")
    if choice == "1":
        if random.random() < 0.6:
            gained = random.randint(200, 800)
            ship["fuel"] += gained
            print(f"✅ Success! You mined {gained} fuel!")
        else:
            damage = random.randint(50, 200)
            ship["fuel"] = max(0, ship["fuel"] - damage)
            print(f"💥 Ouch! The asteroid damaged your ship! Lost {damage} fuel")
    elif choice == "2":
        amount = int(input("How much fuel do you need? "))
        cost = amount * 2
        if ship["credits"] >= cost:
            ship["credits"] -= cost
            ship["fuel"] += amount
            print(f"✅ Fuel purchased! You now have {ship['fuel']:.0f} fuel")
        else:
            print("❌ Not enough credits! Maybe try mining?")

def hunt_bounties():
    """Track down space criminals for reward money - become a legendary bounty hunter!"""
    print("\n💰 BOUNTY HUNTING")
    print(f"🏆 Your current rank: {ship['bounty_rank']}")
    
    # Show available targets
    available = [b for b in bounties if b["level"] <= ship["bounty_rank"] + 1]
    if not available:
        print("No bounties available at your rank. Complete more missions!")
        return
    
    print("\n🎯 WANTED CRIMINALS:")
    for i, target in enumerate(available[:3], 1):
        print(f"{i}. {target['name']} - 💰 {target['bounty']} credits (Level {target['level']})")
    
    choice = input("Who do you want to hunt? ")
    if choice.isdigit() and 1 <= int(choice) <= len(available[:3]):
        target = available[int(choice)-1]
        
        print(f"\n⚔️ Tracking {target['name']}...")
        time.sleep(1)
        
        # Combat mini-game - fight like a true space warrior!
        player_health = target["health"]
        enemy_health = target["health"]
        
        print(f"🔫 FIGHT!")
        while player_health > 0 and enemy_health > 0:
            print(f"\n❤️ Your health: {player_health} | {target['name']}: {enemy_health}")
            action = input("1. Attack | 2. Dodge: ")
            
            if action == "1":
                damage = random.randint(2, 6)
                enemy_health -= damage
                print(f"⚡ You hit for {damage} damage!")
                
                counter = random.randint(1, 4)
                player_health -= counter
                print(f"💥 {target['name']} hits back for {counter} damage!")
            else:
                if random.random() < 0.5:
                    print("🛡️ You dodged the attack!")
                else:
                    counter = random.randint(2, 5)
                    player_health -= counter
                    print(f"💥 Too slow! You took {counter} damage!")
        
        # Victory or defeat - every battle teaches you something!
        if player_health > 0:
            reward = target["bounty"]
            ship["credits"] += reward
            print(f"\n🎉 YOU WIN! Defeated {target['name']}!")
            print(f"💰 Collected {reward} credits!")
            
            if target["level"] == ship["bounty_rank"]:
                ship["bounty_rank"] += 1
                print(f"🏆 Your bounty rank increased to {ship['bounty_rank']}!")
            
            unlock_achievement("bounty_hunter")
            give_crew_xp(30)
        else:
            print(f"\n💀 You were defeated! Lost 100 credits")
            ship["credits"] = max(0, ship["credits"] - 100)

def research_lab():
    """Unlock cool technology for your ship - become a space scientist!"""
    print("\n🧪 RESEARCH LAB")
    print(f"📚 Research points: {ship['research']}")
    print("\nAvailable technologies:")
    
    # Show upgrades
    for i, (name, data) in enumerate(tech_upgrades.items(), 1):
        status = "✅ Owned" if data["owned"] else f"💰 {data['cost']} points"
        print(f"{i}. {name} - {status}")
    
    print("\n4. Convert credits to research (100 credits → 20 points)")
    
    choice = input("\nWhat do you want to research? ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        name, data = list(tech_upgrades.items())[int(choice)-1]
        if not data["owned"]:
            if ship["research"] >= data["cost"]:
                ship["research"] -= data["cost"]
                data["owned"] = True
                print(f"✨ RESEARCH COMPLETE! You now have {name}!")
                unlock_achievement("researcher")
            else:
                print("❌ Not enough research points! Do more missions to earn them.")
    elif choice == "4":
        if ship["credits"] >= 100:
            ship["credits"] -= 100
            ship["research"] += 20
            print("✅ Converted credits to research points!")

def alien_trade():
    """Meet aliens and trade with them - make friends across the galaxy!"""
    print("\n👽 ALIEN ENCOUNTER!")
    print(f"💰 Your credits: {ship['credits']}")
    
    items = {
        "🌌 Dark Matter Crystal": 500,
        "💫 Warp Core Upgrade": 2000,
        "🔮 Quantum Shield": 1500,
        "🍕 Exotic Space Pizza": 50
    }
    
    print("\nWhat do you want to buy?")
    for i, (item, price) in enumerate(items.items(), 1):
        print(f"{i}. {item} - {price} credits")
    
    choice = input("Choose (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        item, price = list(items.items())[int(choice)-1]
        if ship["credits"] >= price:
            ship["credits"] -= price
            ship["inventory"].append(item)
            print(f"✨ You bought {item}!")
            unlock_achievement("alien_friend")
        else:
            print("❌ Not enough credits!")

def explore_nebula():
    """Fly into a nebula to find treasures - explore the mysterious cosmos!"""
    nebulae = {
        "Orion Nebula": (1340, -220),
        "Eagle Nebula": (7000, 0),
        "Helix Nebula": (695, 280)
    }
    
    print("\n🌌 NEBULA EXPLORATION")
    print("Where do you want to explore?")
    for i, name in enumerate(nebulae.keys(), 1):
        print(f"{i}. {name}")
    
    choice = input("Choose: ")
    if choice.isdigit() and 1 <= int(choice) <= len(nebulae):
        name = list(nebulae.keys())[int(choice)-1]
        print(f"\n🚀 Flying into {name}...")
        time.sleep(1)
        
        # Random discovery - what will you find?
        if random.random() < 0.6:
            fuel_gained = random.randint(300, 1500)
            ship["fuel"] += fuel_gained
            print(f"⛽ You found {fuel_gained} fuel in the nebula!")
            unlock_achievement("fuel_hunter")
        else:
            artifact = random.choice(["ancient relic", "crystal shard", "star chart"])
            ship["inventory"].append(artifact)
            print(f"🔮 You discovered an {artifact}!")
            ship["research"] += 20

def show_stats():
    """See how your space adventure is going - your complete report card!"""
    print("\n" + "="*50)
    print("📊 YOUR SPACE ADVENTURE STATS")
    print("="*50)
    print(f"🚀 Missions completed: {ship['missions']}")
    print(f"🏆 Furthest distance: {ship['highest_distance']:.0f} million km")
    print(f"⛽ Current fuel: {ship['fuel']:.0f}")
    print(f"💰 Credits: {ship['credits']}")
    print(f"📚 Research points: {ship['research']}")
    print(f"😊 Crew morale: {ship['morale']}%")
    print(f"🏆 Bounty rank: {ship['bounty_rank']}")
    print(f"🏅 Achievements: {len(ship['achievements'])}")
    
    if ship["achievements"]:
        print("\n🏅 Your achievements:")
        for ach in ship["achievements"]:
            print(f"  • {achievement_list[ach]}")
    
    if ship["inventory"]:
        print("\n📦 Your inventory:")
        for item in ship["inventory"]:
            print(f"  • {item}")

def save_game():
    """Save your progress so you can continue later - don't lose your adventure!"""
    data = {
        "missions": ship["missions"],
        "fuel": ship["fuel"],
        "credits": ship["credits"],
        "achievements": ship["achievements"],
        "inventory": ship["inventory"],
        "morale": ship["morale"],
        "research": ship["research"],
        "bounty_rank": ship["bounty_rank"],
        "highest_distance": ship["highest_distance"],
        "crew": crew
    }
    with open("space_save.json", "w") as f:
        json.dump(data, f)
    print("💾 Your adventure has been saved!")

def load_game():
    """Continue your space adventure from where you left off - welcome back!"""
    global ship, crew
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)
        
        ship["missions"] = data.get("missions", 0)
        ship["fuel"] = data.get("fuel", 5000)
        ship["credits"] = data.get("credits", 1000)
        ship["achievements"] = data.get("achievements", [])
        ship["inventory"] = data.get("inventory", [])
        ship["morale"] = data.get("morale", 80)
        ship["research"] = data.get("research", 0)
        ship["bounty_rank"] = data.get("bounty_rank", 1)
        ship["highest_distance"] = data.get("highest_distance", 0)
        crew = data.get("crew", crew)
        
        print("📀 Welcome back, Captain! Your game is loaded.")
        return True
    except FileNotFoundError:
        print("❌ No saved game found! Start a new adventure.")
        return False

def welcome_message():
    """A friendly welcome to start your space adventure!"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║   🚀 SPACE DISTANCE CALCULATOR 🚀                       ║
    ║         The Friendly Space Adventure!                   ║
    ║                                                         ║
    ║   "To infinity and beyond!" - Buzz Lightyear           ║
    ║                                                         ║
    ║   Welcome, Captain! The galaxy is waiting for you.     ║
    ║   Explore, trade, fight, and become a space legend!    ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    print("🌟 QUICK TIPS:")
    print("• Fly missions to earn credits and fuel")
    print("• Research technology to upgrade your ship")
    print("• Hunt bounties for big rewards")
    print("• Save your game regularly!")
    print("• Have fun exploring the cosmos!\n")

def main():
    """The main game loop - where all the magic happens!"""
    welcome_message()
    
    while True:
        print("\n" + "="*50)
        print("🌟 WHAT DO YOU WANT TO DO?")
        print("="*50)
        print("1. 🚀 Fly on a mission")
        print("2. 📊 Check your stats")
        print("3. 👥 Meet your crew")
        print("4. 🧪 Research technology")
        print("5. 💰 Hunt bounties")
        print("6. 👽 Trade with aliens")
        print("7. 🌌 Explore a nebula")
        print("8. 💾 Save your game")
        print("9. 📀 Load your game")
        print("10. ❌ Quit")
        
        choice = input("\nYour choice: ")
        
        if choice == "1":
            start_mission()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("\n👥 YOUR CREW")
            print("="*40)
            for member in crew:
                print(f"• {member['name']} - Level {member['level']} ({member['skill']})")
                print(f"  XP: {member['xp']}/{member['level']*100}")
        elif choice == "4":
            research_lab()
        elif choice == "5":
            hunt_bounties()
        elif choice == "6":
            alien_trade()
        elif choice == "7":
            explore_nebula()
        elif choice == "8":
            save_game()
        elif choice == "9":
            load_game()
        elif choice == "10":
            print("\n👋 Farewell, Captain! The stars will miss you!")
            print("⭐ Live long and prosper! 🖖")
            break
        else:
            print("❌ That's not a valid option, Captain. Try again!")

# Start the adventure!
if __name__ == "__main__":
    main()

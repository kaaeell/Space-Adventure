import math
import random
import time
from datetime import datetime
import json
import os

# SPACE DISTANCE CALCULATOR - ULTIMATE EDITION v3.4

# ============= PLAYER DATA =============
history = []
total_calculations = 0
highest_distance = 0
missions_completed = 0
fuel = 5000
credits_total = 1000
achievements = []
inventory = []
crew_morale = 80
consecutive_missions = 0
research_points = 0
bounty_hunting_level = 1
discovered_anomalies = []

# ============= CREW SYSTEM =============
crew_members = [
    {"name": "Captain", "skill": "Leadership", "level": 1, "xp": 0, "bonus": "morale"},
    {"name": "Engineer", "skill": "Mechanics", "level": 1, "xp": 0, "bonus": "fuel_saving"},
    {"name": "Navigator", "skill": "Astrogation", "level": 1, "xp": 0, "bonus": "distance_bonus"},
    {"name": "Scientist", "skill": "Research", "level": 1, "xp": 0, "bonus": "rp_bonus"},
    {"name": "Gunner", "skill": "Combat", "level": 1, "xp": 0, "bonus": "combat_damage"}
]

# ============= GAME DATA =============
space_jokes = [
    "Why did the star go to school? To get a little brighter!",
    "What do astronauts use to keep their pants up? An asteroid belt!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key? The space bar!"
]

space_anomalies = {
    "Time Dilation Field": {"effect": "bonus_research", "reward": 50},
    "Quantum Rift": {"effect": "teleport", "reward": None},
    "Sentient Nebula": {"effect": "gift", "reward": 300},
    "Micro Black Hole": {"effect": "danger", "damage": 150},
    "Space Whale Song": {"effect": "morale_boost", "reward": 20}
}

bounty_targets = [
    {"name": "Red Pirate", "bounty": 500, "level": 1, "health": 3},
    {"name": "Shadow Corsair", "bounty": 1000, "level": 2, "health": 5},
    {"name": "Void Reaver", "bounty": 2000, "level": 3, "health": 7}
]

research_upgrades = {
    "Fuel Efficiency": {"cost": 100, "owned": False},
    "Warp Drive": {"cost": 200, "owned": False},
    "Shield Tech": {"cost": 150, "owned": False}
}

achievement_list = {
    "first_step": "🌱 Complete your first mission",
    "milky_way_tourist": "🌌 Travel over 2000 million km",
    "fuel_hunter": "⛽ Collect fuel from a nebula",
    "millionaire": "💰 Earn 10,000 credits",
    "galaxy_legend": "⭐ Complete 50 missions",
    "streak_master": "🔥 Complete 5 missions in a row",
    "bounty_hunter": "💰 Defeat a bounty target",
    "research_genius": "🧠 Unlock 3 research upgrades"
}

# ============= HELPER FUNCTIONS =============
def calculate_distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def check_achievement(achievement_key):
    global achievements
    if achievement_key in achievement_list and achievement_key not in achievements:
        achievements.append(achievement_key)
        print(f"\n🏆 ACHIEVEMENT UNLOCKED: {achievement_list[achievement_key]} 🏆\n")

def gain_crew_xp(xp_amount):
    global credits_total
    for member in crew_members:
        member['xp'] += xp_amount
        if member['xp'] >= member['level'] * 100:
            member['xp'] = 0
            member['level'] += 1
            print(f"\n🎉 {member['name']} leveled up to level {member['level']}!")
            credits_total += random.randint(100, 300)
            if member['level'] >= 5:
                check_achievement("crew_trainer")

# ============= GAME FUNCTIONS =============
def show_status():
    print("\n" + "="*40)
    print(f"🚀 Missions: {missions_completed} | 🔥 Streak: {consecutive_missions}")
    print(f"⛽ Fuel: {fuel:.1f} | 💰 Credits: {credits_total}")
    print(f"📚 Research: {research_points} | 😊 Morale: {crew_morale}%")
    print(f"🏆 Bounty Rank: {bounty_hunting_level}")
    print("="*40)

def choose_planets():
    planets = {
        1: ("Earth", (0,0)), 2: ("Mars", (225,0)), 3: ("Venus", (108,0)),
        4: ("Jupiter", (778,0)), 5: ("Saturn", (1427,0)), 6: ("Uranus", (2871,0)),
        7: ("Neptune", (4495,0)), 8: ("Mercury", (58,0)), 9: ("Pluto", (5906,0))
    }
    print("\n📋 Available planets:")
    for num, (name, _) in planets.items():
        print(f"{num}. {name}")
    
    def pick(msg):
        while True:
            try:
                choice = int(input(msg))
                if choice in planets:
                    return planets[choice]
                print("Invalid choice!")
            except ValueError:
                print("Enter a number!")
    
    p1_name, p1 = pick("Choose planet 1: ")
    p2_name, p2 = pick("Choose planet 2: ")
    return p1_name, p1, p2_name, p2

def do_mission():
    global missions_completed, fuel, credits_total, crew_morale, consecutive_missions, highest_distance
    
    print("\n🚀 STARTING NEW MISSION 🚀")
    print("1. Choose planets")
    print("2. Enter custom coordinates")
    
    choice = input("Choose: ")
    if choice == "1":
        p1_name, p1, p2_name, p2 = choose_planets()
    else:
        p1 = get_coordinates("Start")
        p2 = get_coordinates("Destination")
        p1_name, p2_name = "Start", "Destination"
    
    distance = calculate_distance(p1, p2)
    total_calculations += 1
    
    print(f"\n📏 Distance from {p1_name} to {p2_name}: {distance:.2f} million km")
    
    if distance > highest_distance:
        highest_distance = distance
        print("🏆 New record distance!")
    
    # Random events
    if random.random() < 0.3:
        event = random.choice([
            ("🌀 WORMHOLE!", 0.6),
            ("✨ COSMIC CACHE!", 1.0)
        ])
        print(f"\n⚠️ {event[0]}")
        if "WORMHOLE" in event[0]:
            distance *= 0.6
            print(f"🔄 Distance reduced to {distance:.2f} million km!")
            check_achievement("wormhole_rider")
    
    # Fuel check
    fuel_needed = distance * 0.5
    if fuel < fuel_needed:
        print(f"\n⚠️ Not enough fuel! Need {fuel_needed:.1f}, have {fuel:.1f}")
        collect_emergency_fuel()
        return do_mission()
    
    fuel -= fuel_needed
    credits_earned = int(distance * 0.8 + 50)
    credits_total += credits_earned
    
    missions_completed += 1
    consecutive_missions += 1
    crew_morale = min(100, crew_morale + random.randint(5, 15))
    
    print(f"\n✅ Mission Complete! +{credits_earned} credits")
    print(f"⛽ Fuel remaining: {fuel:.1f}")
    print(f"😊 Crew morale: {crew_morale}%")
    
    if missions_completed == 1:
        check_achievement("first_step")
    if credits_total >= 10000:
        check_achievement("millionaire")
    if missions_completed >= 50:
        check_achievement("galaxy_legend")
    if consecutive_missions >= 5:
        check_achievement("streak_master")
    
    gain_crew_xp(20)

def collect_emergency_fuel():
    global fuel, credits_total
    print("\n🔄 EMERGENCY FUEL COLLECTION")
    print("1. Mine asteroid (risky)")
    print("2. Buy fuel (2 credits/unit)")
    
    choice = input("Choose: ")
    if choice == "1":
        if random.random() < 0.6:
            gained = random.randint(200, 800)
            fuel += gained
            print(f"✅ +{gained} fuel!")
        else:
            damage = random.randint(50, 200)
            fuel = max(0, fuel - damage)
            print(f"💥 Lost {damage} fuel!")
    elif choice == "2":
        amount = int(input("Amount to buy: "))
        cost = amount * 2
        if credits_total >= cost:
            credits_total -= cost
            fuel += amount
            print(f"✅ Bought {amount} fuel!")

def get_coordinates(name):
    while True:
        try:
            print(f"\nEnter coordinates for {name} (in million km)")
            x = float(input("x: "))
            y = float(input("y: "))
            return (x, y)
        except ValueError:
            print("Invalid input!")

def bounty_hunting():
    global credits_total, bounty_hunting_level
    
    print("\n💰 BOUNTY HUNTING")
    print(f"🏆 Rank: {bounty_hunting_level}")
    
    available = [t for t in bounty_targets if t["level"] <= bounty_hunting_level + 1]
    if not available:
        print("No bounties available!")
        return
    
    print("\nAvailable bounties:")
    for i, target in enumerate(available[:3], 1):
        print(f"{i}. {target['name']} - 💰 {target['bounty']} credits")
    
    choice = input("Select bounty: ")
    if choice.isdigit() and 1 <= int(choice) <= len(available[:3]):
        target = available[int(choice)-1]
        
        print(f"\n⚔️ Hunting {target['name']}...")
        time.sleep(1)
        
        # Simple combat
        player_health = target['health']
        target_health = target['health']
        
        while player_health > 0 and target_health > 0:
            print(f"\n❤️ You: {player_health} | {target['name']}: {target_health}")
            action = input("1. Attack | 2. Dodge: ")
            
            if action == "1":
                damage = random.randint(2, 6)
                target_health -= damage
                print(f"⚡ Dealt {damage} damage!")
                enemy_damage = random.randint(1, 4)
                player_health -= enemy_damage
                print(f"💥 Took {enemy_damage} damage!")
            else:
                if random.random() < 0.5:
                    print("🛡️ Dodged!")
                else:
                    enemy_damage = random.randint(2, 5)
                    player_health -= enemy_damage
                    print(f"💥 Took {enemy_damage} damage!")
        
        if player_health > 0:
            credits_total += target['bounty']
            print(f"\n🎉 VICTORY! +{target['bounty']} credits!")
            if target["level"] == bounty_hunting_level:
                bounty_hunting_level += 1
                print(f"🏆 Bounty rank increased to {bounty_hunting_level}!")
            check_achievement("bounty_hunter")
            gain_crew_xp(30)
        else:
            print("\n💀 Defeated! Lost 100 credits")
            credits_total = max(0, credits_total - 100)

def research_lab():
    global research_points, credits_total
    
    print("\n🧪 RESEARCH LAB")
    print(f"📚 Research Points: {research_points}\n")
    
    for i, (name, data) in enumerate(research_upgrades.items(), 1):
        status = "✅" if data["owned"] else f"💰 {data['cost']} RP"
        print(f"{i}. {name} - {status}")
    
    print("\n4. Convert 100 credits → 20 RP")
    
    choice = input("\nChoose: ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        upgrade_name, upgrade_data = list(research_upgrades.items())[int(choice)-1]
        if not upgrade_data["owned"]:
            if research_points >= upgrade_data["cost"]:
                research_points -= upgrade_data["cost"]
                upgrade_data["owned"] = True
                print(f"✨ Unlocked {upgrade_name}!")
                check_achievement("research_genius")
            else:
                print("❌ Not enough research points!")
    elif choice == "4":
        if credits_total >= 100:
            credits_total -= 100
            research_points += 20
            print("✅ Converted credits to research points!")

def alien_encounter():
    global credits_total, inventory
    
    print("\n👽 ALIEN ENCOUNTER!")
    print(f"Credits: {credits_total}")
    
    items = {
        "🌌 dark matter crystal": 500,
        "💫 warp core": 2000,
        "🔮 quantum shield": 1500,
        "🍕 space pizza": 50
    }
    
    for i, (item, price) in enumerate(items.items(), 1):
        print(f"{i}. {item} - {price} credits")
    
    choice = input("Buy (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        item, price = list(items.items())[int(choice)-1]
        if credits_total >= price:
            credits_total -= price
            inventory.append(item)
            print(f"✨ Bought {item}!")
            check_achievement("alien_friend")
        else:
            print("❌ Not enough credits!")

def explore_nebula():
    global fuel, research_points
    
    nebulae = {
        "Orion Nebula": (1340, -220),
        "Eagle Nebula": (7000, 0),
        "Helix Nebula": (695, 280)
    }
    
    print("\n🌌 NEBULA EXPLORATION")
    for i, name in enumerate(nebulae.keys(), 1):
        print(f"{i}. {name}")
    
    choice = input("Explore (number): ")
    if choice.isdigit() and 1 <= int(choice) <= len(nebulae):
        neb_name = list(nebulae.keys())[int(choice)-1]
        print(f"\n🚀 Exploring {neb_name}...")
        time.sleep(1)
        
        if random.random() < 0.6:
            fuel_gained = random.randint(300, 1500)
            fuel += fuel_gained
            print(f"⛽ Collected {fuel_gained} fuel!")
            check_achievement("fuel_hunter")
        else:
            artifact = random.choice(["ancient relic", "crystal shard", "star chart"])
            inventory.append(artifact)
            print(f"🔮 Found {artifact}!")
            research_points += 20

def view_stats():
    print("\n📊 SPACE STATISTICS")
    print("="*40)
    print(f"🚀 Missions: {missions_completed}")
    print(f"📏 Total Calculations: {total_calculations}")
    print(f"🏆 Highest Distance: {highest_distance:.2f} million km")
    print(f"⛽ Fuel: {fuel:.1f}")
    print(f"💰 Credits: {credits_total}")
    print(f"📚 Research Points: {research_points}")
    print(f"😊 Crew Morale: {crew_morale}%")
    print(f"🏆 Bounty Rank: {bounty_hunting_level}")
    print(f"🏅 Achievements: {len(achievements)}")
    print("\nAchievements:")
    for ach in achievements:
        print(f"  {achievement_list[ach]}")
    print("\nInventory:")
    if inventory:
        for item in inventory:
            print(f"  • {item}")
    else:
        print("  Empty")

def daily_bonus():
    global credits_total, fuel, research_points
    print("\n🎁 DAILY BONUS!")
    bonus = random.randint(200, 500)
    credits_total += bonus
    print(f"💰 +{bonus} credits!")

def save_game():
    data = {
        "missions_completed": missions_completed,
        "fuel": fuel,
        "credits_total": credits_total,
        "achievements": achievements,
        "inventory": inventory,
        "crew_morale": crew_morale,
        "research_points": research_points,
        "bounty_hunting_level": bounty_hunting_level,
        "crew_members": crew_members,
        "highest_distance": highest_distance
    }
    with open("space_save.json", "w") as f:
        json.dump(data, f)
    print("💾 Game saved!")

def load_game():
    global missions_completed, fuel, credits_total, achievements, inventory
    global crew_morale, research_points, bounty_hunting_level, crew_members, highest_distance
    
    try:
        with open("space_save.json", "r") as f:
            data = json.load(f)
        
        missions_completed = data.get("missions_completed", 0)
        fuel = data.get("fuel", 5000)
        credits_total = data.get("credits_total", 1000)
        achievements = data.get("achievements", [])
        inventory = data.get("inventory", [])
        crew_morale = data.get("crew_morale", 80)
        research_points = data.get("research_points", 0)
        bounty_hunting_level = data.get("bounty_hunting_level", 1)
        crew_members = data.get("crew_members", crew_members)
        highest_distance = data.get("highest_distance", 0)
        
        print("📀 Game loaded!")
        return True
    except FileNotFoundError:
        print("❌ No save file found!")
        return False

# ============= MAIN GAME =============
def main():
    print("""
    ╔═══════════════════════════════════════╗
    ║   🚀 SPACE DISTANCE CALCULATOR 🚀    ║
    ║         ULTIMATE EDITION v3.4         ║
    ╚═══════════════════════════════════════╝
    """)
    
    while True:
        print("\n" + "="*40)
        print("🌟 MAIN MENU")
        print("="*40)
        print("1. 🚀 Start Mission")
        print("2. 📊 View Stats")
        print("3. 👥 Crew Management")
        print("4. 🧪 Research Lab")
        print("5. 💰 Bounty Hunting")
        print("6. 👽 Alien Trade")
        print("7. 🌌 Explore Nebula")
        print("8. 🎁 Daily Bonus")
        print("9. 💾 Save/Load")
        print("10. ❌ Exit")
        
        choice = input("\nChoose option: ")
        
        if choice == "1":
            do_mission()
        elif choice == "2":
            view_stats()
        elif choice == "3":
            print("\n👥 CREW MEMBERS")
            for member in crew_members:
                print(f"{member['name']} - Level {member['level']} ({member['skill']})")
                print(f"  XP: {member['xp']}/{member['level']*100}")
        elif choice == "4":
            research_lab()
        elif choice == "5":
            bounty_hunting()
        elif choice == "6":
            alien_encounter()
        elif choice == "7":
            explore_nebula()
        elif choice == "8":
            daily_bonus()
        elif choice == "9":
            print("\n1. Save Game")
            print("2. Load Game")
            sub_choice = input("Choose: ")
            if sub_choice == "1":
                save_game()
            elif sub_choice == "2":
                load_game()
        elif choice == "10":
            print("\n👋 Thanks for playing! Live long and prosper! 🖖")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

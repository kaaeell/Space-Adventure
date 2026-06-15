import math
import random
import time
from datetime import datetime
import json
import os

# SPACE DISTANCE CALCULATOR - ULTIMATE EDITION v3.1
# New today: Space anomalies, research system, bounty hunting, CREW SKILL SYSTEM, 
# SPACE STOCK MARKET, SPACE MINING, DIPLOMATIC RELATIONS, PLANETARY COLONIZATION, 
# BLACK MARKET, and SPACE RACING LEAGUE!


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
last_pirate_defeated = None

# ============= NEW: SPACE RACING LEAGUE =============
race_tracks = [
    {"name": "Asteroid Field Dash", "difficulty": 1, "prize": 300, "record": 60.0},
    {"name": "Saturn's Ring Circuit", "difficulty": 2, "prize": 600, "record": 90.0},
    {"name": "Nebula Run", "difficulty": 3, "prize": 1000, "record": 120.0},
    {"name": "Black Hole Slingshot", "difficulty": 4, "prize": 2000, "record": 150.0},
    {"name": "Galactic Grand Prix", "difficulty": 5, "prize": 5000, "record": 180.0}
]

racing_upgrades = {
    "Nitro Boost": {"owned": False, "cost": 500, "bonus": 0.2},
    "Aero Wings": {"owned": False, "cost": 300, "bonus": 0.1},
    "Quantum Engine": {"owned": False, "cost": 1000, "bonus": 0.3},
    "Shield Deflector": {"owned": False, "cost": 700, "bonus": 0.15}
}

racing_stats = {
    "races_entered": 0,
    "races_won": 0,
    "best_time": 999.0,
    "total_winnings": 0
}

# ============= PLANETARY COLONIZATION =============
colonies = []
available_planets = [
    {"name": "Mars", "cost": 2000, "income": 100, "hazards": ["dust_storms"], "colonized": False},
    {"name": "Europa", "cost": 3000, "income": 150, "hazards": ["ice_cracks"], "colonized": False},
    {"name": "Titan", "cost": 2500, "income": 120, "hazards": ["methane_lakes"], "colonized": False},
    {"name": "Kepler-22b", "cost": 5000, "income": 300, "hazards": ["alien_wildlife"], "colonized": False},
    {"name": "Proxima Centauri b", "cost": 8000, "income": 500, "hazards": ["solar_flares"], "colonized": False}
]

colonization_upgrades = {
    "Defense System": {"cost": 1000, "owned": False, "bonus": 50},
    "Research Lab": {"cost": 800, "owned": False, "bonus": 30},
    "Trade Hub": {"cost": 1500, "owned": False, "bonus": 100},
    "Mining Facility": {"cost": 1200, "owned": False, "bonus": 75}
}

# ============= BLACK MARKET =============
black_market_items = {
    "Stolen Research Data": {"price": 300, "risk": 20, "reward": "research", "value": 80},
    "Illegal Weapons": {"price": 500, "risk": 40, "reward": "combat", "value": 150},
    "Alien Tech": {"price": 1000, "risk": 60, "reward": "tech", "value": 300},
    "Black Hole Fragment": {"price": 2000, "risk": 80, "reward": "special", "value": 800},
    "Forgotten Map": {"price": 400, "risk": 30, "reward": "treasure", "value": 200}
}

smuggling_heat = 0
black_market_access = False

# ============= DIPLOMATIC RELATIONS =============
alien_factions = {
    "Crystal Collective": {"relation": 50, "benefits": [], "trade_discount": 0},
    "Nebula Nomads": {"relation": 50, "benefits": [], "trade_discount": 0},
    "Star Empire": {"relation": 50, "benefits": [], "trade_discount": 0},
    "Void Syndicate": {"relation": 50, "benefits": [], "trade_discount": 0}
}

# ============= CREW SKILL SYSTEM =============
crew_members = [
    {"name": "Captain", "skill": "Leadership", "level": 1, "xp": 0, "bonus": "morale"},
    {"name": "Engineer", "skill": "Mechanics", "level": 1, "xp": 0, "bonus": "fuel_saving"},
    {"name": "Navigator", "skill": "Astrogation", "level": 1, "xp": 0, "bonus": "distance_bonus"},
    {"name": "Scientist", "skill": "Research", "level": 1, "xp": 0, "bonus": "rp_bonus"},
    {"name": "Gunner", "skill": "Combat", "level": 1, "xp": 0, "bonus": "combat_damage"}
]

# ============= SPACE STOCK MARKET =============
stock_market = {
    "Space Fuel": {"price": 100, "volatility": 0.15, "owned": 0},
    "Dark Matter": {"price": 500, "volatility": 0.25, "owned": 0},
    "Alien Artifacts": {"price": 300, "volatility": 0.2, "owned": 0},
    "Quantum Chips": {"price": 200, "volatility": 0.18, "owned": 0},
    "Nebula Gas": {"price": 80, "volatility": 0.12, "owned": 0}
}

market_news = [
    "📰 New mining operation discovered!",
    "📰 Alien trade routes disrupted!",
    "📰 Space pirates attacking convoys!",
    "📰 Research breakthrough announced!",
    "📰 Government subsidies approved!",
    "📰 Supply shortage reported!"
]

# ============= SPACE MINING SYSTEM =============
mining_resources = {
    "Iron Ore": {"value": 50, "difficulty": 1, "yield": (10, 30)},
    "Titanium": {"value": 120, "difficulty": 2, "yield": (5, 20)},
    "Gold": {"value": 300, "difficulty": 3, "yield": (3, 12)},
    "Platinum": {"value": 500, "difficulty": 4, "yield": (2, 8)},
    "Dark Matter Crystal": {"value": 1000, "difficulty": 5, "yield": (1, 4)}
}

mining_upgrades = {
    "Laser Drill": {"owned": False, "cost": 500, "bonus": 0.2},
    "Shield Generator": {"owned": False, "cost": 800, "bonus": 0.3},
    "Cargo Expander": {"owned": False, "cost": 400, "bonus": 0.5}
}

total_mined = 0

# ============= DATA SETS =============
galaxy_names = ["Milky Way","Andromeda","Sombrero Galaxy","Whirlpool Galaxy","Black Eye Galaxy","Cartwheel Galaxy","Triangulum Galaxy","Pinwheel Galaxy"]
astronauts = ["Neil","Buzz","Sally","Yuri","Mae","Chris","Valentina","Jose","Priya","Chen"]
spaceships = ["StarRunner","NovaX","Galaxy Rider","Void Explorer","Cosmic Storm","Nebula One","Quantum Leap","Starlight"]
space_pets = ["space dog","robot cat","alien hamster","tiny moon dragon","quantum parrot","zero-g fish"]
badges = ["🌟 rookie pilot","🚀 master explorer","🪐 galaxy navigator","☄️ asteroid survivor","🔭 deep space observer","⚡ speed champion"]
alien_names = ["Zorg","Xenon","Blip","Nova","Kratos","Glimmer","Vortex","Stardust"]
space_foods = ["freeze dried pizza","space tacos","galaxy noodles","moon burgers","asteroid ice cream","nebula smoothie"]
space_jobs = ["pilot","engineer","galaxy scout","alien translator","space mechanic","astrobiologist","warp specialist"]
planet_conditions = ["lava storms","ice surface","heavy gravity","safe landing","radioactive atmosphere","crystal caves","underwater cities"]

comet_names = ["Halley","Encke","Hale-Bopp","Swift-Tuttle","Neowise","Lovejoy","ISON"]
space_jokes = [
    "Why did the star go to school? To get a little brighter!",
    "What do astronauts use to keep their pants up? An asteroid belt!",
    "Why don't aliens visit our solar system? They read the reviews… only one star!",
    "How do you organize a space party? You planet!",
    "What's an astronaut's favorite key on a keyboard? The space bar!"
]
alien_greetings = ["👽 Blip blop!","👾 Greetings Earthling!","🛸 Take me to your leader!","🛸 Beep boop!","🌌 We come in peace!","✨ Hello from Andromeda!"]


space_anomalies = {
    "🔄 Time Dilation Field": {
        "description": "Time moves differently here!",
        "effect": "bonus_research",
        "reward": 50
    },
    "🌀 Quantum Rift": {
        "description": "Reality is unstable!",
        "effect": "teleport",
        "reward": None
    },
    "✨ Sentient Nebula": {
        "description": "The nebula is alive!",
        "effect": "gift",
        "reward": 300
    },
    "⚫ Micro Black Hole": {
        "description": "Tiny but dangerous!",
        "effect": "danger",
        "damage": 150
    },
    "🎵 Space Whale Song": {
        "description": "Beautiful cosmic whales singing!",
        "effect": "morale_boost",
        "reward": 20
    },
    "📜 Ancient Ruins": {
        "description": "Remains of an old civilization!",
        "effect": "artifact",
        "reward": None
    },
    "💎 Crystal Asteroid": {
        "description": "Asteroid made of rare crystals!",
        "effect": "mining_bonus",
        "reward": None
    }
}

bounty_targets = [
    {"name": "Red Pirate", "bounty": 500, "level": 1, "health": 3},
    {"name": "Shadow Corsair", "bounty": 1000, "level": 2, "health": 5},
    {"name": "Void Reaver", "bounty": 2000, "level": 3, "health": 7},
    {"name": "Star Eater", "bounty": 5000, "level": 4, "health": 10},
    {"name": "Galactic Menace", "bounty": 10000, "level": 5, "health": 15}
]

research_upgrades = {
    "Fuel Efficiency": {"cost": 100, "effect": "fuel_consumption", "value": 0.9, "owned": False},
    "Warp Drive": {"cost": 200, "effect": "speed_bonus", "value": 1.2, "owned": False},
    "Shield Tech": {"cost": 150, "effect": "damage_reduction", "value": 0.7, "owned": False},
    "Scanner Range": {"cost": 120, "effect": "credit_bonus", "value": 1.3, "owned": False},
    "Quantum Shields": {"cost": 300, "effect": "critical_protection", "value": 0.5, "owned": False}
}

achievement_list = {
    "first_step": "🌱 First Step - Complete your first mission",
    "milky_way_tourist": "🌌 Milky Way Tourist - Travel over 2000 million km",
    "fuel_hunter": "⛽ Fuel Hunter - Collect fuel from a nebula",
    "alien_friend": "👽 Alien Friend - Successfully trade with aliens",
    "millionaire": "💰 Space Millionaire - Earn 10,000 credits",
    "speed_demon": "⚡ Speed Demon - Complete a mission in under 30 seconds",
    "badge_collector": "🎖️ Badge Collector - Earn 5 different badges",
    "pet_lover": "🐾 Pet Lover - Adopt a space pet",
    "galaxy_legend": "⭐ Galaxy Legend - Complete 50 missions",
    "streak_master": "🔥 Streak Master - Complete 5 missions in a row",
    "wormhole_rider": "🌀 Wormhole Rider - Successfully use a wormhole",
    "anomaly_hunter": "🔭 Anomaly Hunter - Discover 3 space anomalies",
    "bounty_hunter": "💰 Bounty Hunter - Defeat a bounty target",
    "research_genius": "🧠 Research Genius - Unlock 3 research upgrades",
    "space_whisperer": "🐋 Space Whisperer - Find the space whales",
    "comet_chaser": "☄️ Comet Chaser - Track a comet",
    "galactic_hero": "🦸 Galactic Hero - Reach bounty rank 5",
    "crew_trainer": "🎓 Crew Trainer - Get a crew member to level 5",
    "stock_master": "📈 Stock Master - Make 5000 profit from stock market",
    "mining_baron": "⛏️ Mining Baron - Mine 50 total resources",
    "diplomat": "🤝 Diplomat - Reach 90+ relation with any faction",
    "colonizer": "🏠 Colonizer - Establish your first colony",
    "smuggler": "🕶️ Smuggler - Successfully use the black market 5 times",
    "racing_champion": "🏆 Racing Champion - Win 10 space races"
}

nebulae = {
    "Orion Nebula": (1340, -220),
    "Eagle Nebula": (7000, 0),
    "Helix Nebula": (695, 280),
    "Crab Nebula": (6500, 190),
    "Tarantula Nebula": (160000, 5000),
    "Horsehead Nebula": (1500, -300),
    "Cat's Eye Nebula": (3000, 400)
}

alien_items = {
    "🌌 dark matter crystal": 500,
    "💫 warp core upgrade": 2000,
    "🔮 quantum shield": 1500,
    "🍕 exotic space pizza": 50,
    "🐉 baby space dragon egg": 3000,
    "📡 anomaly scanner": 800,
    "🔭 research data": 400
}

random_events = [
    {"name": "🌀 WORMHOLE!", "effect": "shortcut", "message": "You found a wormhole! Distance reduced by 40%!", "modifier": 0.6},
    {"name": "🏴‍☠️ SPACE PIRATES!", "effect": "danger", "message": "Space pirates attacked! Lost 200 fuel and 100 credits!", "fuel": -200, "credits": -100},
    {"name": "✨ COSMIC CACHE", "effect": "reward", "message": "Found a floating cargo pod! +300 credits and +150 fuel!", "fuel": 150, "credits": 300},
    {"name": "🌊 SOLAR FLARE", "effect": "danger", "message": "Solar flare damaged shields! Lost 100 fuel!", "fuel": -100},
    {"name": "🤝 FRIENDLY ALIENS", "effect": "reward", "message": "Friendly aliens gave you a gift! +250 credits!", "credits": 250},
    {"name": "📡 MYSTERY SIGNAL", "effect": "anomaly", "message": "Strange signal detected!", "anomaly": True},
    {"name": "☄️ COMET FLYBY", "effect": "comet", "message": "A comet is passing by!", "comet": True}
]

# ============= NEW: SPACE RACING LEAGUE =============
def space_racing():
    global credits_total, fuel, crew_morale
    
    print("\n🏁 SPACE RACING LEAGUE 🏁")
    print("=" * 50)
    print(f"🏆 Races Entered: {racing_stats['races_entered']}")
    print(f"🏆 Races Won: {racing_stats['races_won']}")
    print(f"⭐ Best Time: {racing_stats['best_time']:.2f} seconds")
    print(f"💰 Total Winnings: {racing_stats['total_winnings']} credits")
    
    print("\nAvailable Tracks:")
    for i, track in enumerate(race_tracks, 1):
        record_emoji = "🏆" if racing_stats['best_time'] < track['record'] else "📝"
        print(f"{i}. {track['name']} - Difficulty: {'⭐'*track['difficulty']}")
        print(f"   Prize: {track['prize']} credits | Record: {track['record']:.1f}s {record_emoji}")
    
    print("\n6. Buy Racing Upgrades")
    print("7. View Racing Stats")
    print("8. Back")
    
    choice = input("\nChoose option: ")
    
    if choice == "6":
        buy_racing_upgrades()
    elif choice == "7":
        view_racing_stats()
    elif choice.isdigit() and 1 <= int(choice) <= len(race_tracks):
        race(int(choice)-1)

def race(track_index):
    global credits_total, fuel, crew_morale, racing_stats
    
    track = race_tracks[track_index]
    
    print(f"\n🏁 STARTING RACE: {track['name']} 🏁")
    print("=" * 40)
    
    # Calculate ship performance
    ship_bonus = 1.0
    for member in crew_members:
        if member['bonus'] == 'distance_bonus':
            ship_bonus += member['level'] * 0.05
    
    # Apply racing upgrades
    for upgrade, data in racing_upgrades.items():
        if data["owned"]:
            ship_bonus += data["bonus"]
            print(f"✅ {upgrade} active! +{int(data['bonus']*100)}% speed")
    
    # Crew morale affects performance
    morale_bonus = 1 + (crew_morale / 200)
    
    print("\nPress ENTER as fast as you can when you see 'GO!'")
    input("Ready? Press ENTER...")
    
    # Random countdown
    countdown = random.uniform(1, 4)
    time.sleep(countdown)
    print("🏁 GO! 🏁")
    
    start_time = time.time()
    input()
    reaction_time = time.time() - start_time
    
    # Calculate race time
    base_time = track['record'] * (0.8 + random.random() * 0.4)
    reaction_penalty = reaction_time * 5
    difficulty_penalty = track['difficulty'] * 3
    
    race_time = base_time + reaction_penalty + difficulty_penalty
    race_time = race_time / (ship_bonus * morale_bonus)
    
    print(f"\n⏱️ Your reaction time: {reaction_time:.3f}s")
    print(f"⏱️ Total race time: {race_time:.2f}s")
    print(f"🏆 Track record: {track['record']:.2f}s")
    
    # Check if won
    if race_time < track['record']:
        print("\n🎉 NEW TRACK RECORD! 🎉")
        track['record'] = race_time
        if race_time < racing_stats['best_time']:
            racing_stats['best_time'] = race_time
        racing_stats['races_won'] += 1
        
        prize_multiplier = 2
        print(f"🌟 Bonus for beating record! x{prize_multiplier}")
    elif race_time < track['record'] * 1.2:
        print("\n✅ You won the race!")
        prize_multiplier = 1
        racing_stats['races_won'] += 1
    elif race_time < track['record'] * 1.5:
        print("\n🥈 You placed 2nd!")
        prize_multiplier = 0.5
    else:
        print("\n😔 You lost the race...")
        prize_multiplier = 0
    
    if prize_multiplier > 0:
        winnings = int(track['prize'] * prize_multiplier)
        credits_total += winnings
        racing_stats['total_winnings'] += winnings
        print(f"💰 Won {winnings} credits!")
        
        # Fuel consumption
        fuel_cost = track['difficulty'] * 30
        fuel = max(0, fuel - fuel_cost)
        print(f"⛽ Race consumed {fuel_cost} fuel")
        
        # Crew XP gain
        gain_crew_xp(15 * track['difficulty'])
        
        # Check racing champion achievement
        if racing_stats['races_won'] >= 10:
            check_achievement("racing_champion")
    else:
        # Repair costs
        repair_cost = track['difficulty'] * 50
        credits_total = max(0, credits_total - repair_cost)
        print(f"🔧 Repairs cost {repair_cost} credits")
    
    racing_stats['races_entered'] += 1
    update_crew_morale(0, prize_multiplier > 0)

def buy_racing_upgrades():
    global credits_total
    
    print("\n🔧 RACING UPGRADE SHOP 🔧")
    print(f"💰 Credits: {credits_total}")
    print("\nAvailable upgrades:")
    
    upgrades_list = list(racing_upgrades.items())
    for i, (name, data) in enumerate(upgrades_list, 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} credits"
        print(f"{i}. {name} - {status} (+{int(data['bonus']*100)}% speed)")
    
    choice = input("\nSelect upgrade (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(upgrades_list):
        upgrade_name, upgrade_data = upgrades_list[int(choice)-1]
        if not upgrade_data["owned"]:
            if credits_total >= upgrade_data["cost"]:
                credits_total -= upgrade_data["cost"]
                upgrade_data["owned"] = True
                print(f"✨ Purchased {upgrade_name}! ✨")
                print(f"⚡ Speed increased by {int(upgrade_data['bonus']*100)}%")
            else:
                print(f"❌ Need {upgrade_data['cost']} credits!")
        else:
            print("❌ Already owned!")

def view_racing_stats():
    print("\n🏆 RACING STATISTICS 🏆")
    print("=" * 40)
    print(f"Races Entered: {racing_stats['races_entered']}")
    print(f"Races Won: {racing_stats['races_won']}")
    print(f"Win Rate: {(racing_stats['races_won']/racing_stats['races_entered']*100) if racing_stats['races_entered'] > 0 else 0:.1f}%")
    print(f"Best Time: {racing_stats['best_time']:.2f}s")
    print(f"Total Winnings: {racing_stats['total_winnings']} credits")
    
    print("\n🔧 Owned Upgrades:")
    upgrades_owned = [name for name, data in racing_upgrades.items() if data["owned"]]
    if upgrades_owned:
        for upgrade in upgrades_owned:
            print(f"  ✅ {upgrade}")
    else:
        print("  None")
    
    print("\n📝 Track Records:")
    for track in race_tracks:
        print(f"  {track['name']}: {track['record']:.2f}s")

# ============= PLANETARY COLONIZATION =============
def colonization_system():
    global credits_total, research_points
    
    print("\n🏠 PLANETARY COLONIZATION SYSTEM 🏠")
    print("=" * 50)
    
    print("\nYour Colonies:")
    if colonies:
        for colony in colonies:
            print(f"  🪐 {colony['name']} - Income: {colony['income']}/turn | Population: {colony['population']}")
    else:
        print("  No colonies yet!")
    
    print("\nAvailable Planets for Colonization:")
    for i, planet in enumerate(available_planets, 1):
        if not planet["colonized"]:
            print(f"{i}. {planet['name']} - Cost: {planet['cost']} credits | Base Income: {planet['income']}/mission")
            print(f"   Hazards: {', '.join(planet['hazards'])}")
    
    print("\n" + "-" * 50)
    print("1. Establish New Colony")
    print("2. Upgrade Colonies")
    print("3. Collect Colony Income")
    print("4. View Colony Details")
    print("5. Back to Main Menu")
    
    choice = input("\nChoose option: ")
    
    if choice == "1":
        establish_colony()
    elif choice == "2":
        upgrade_colonies()
    elif choice == "3":
        collect_colony_income()
    elif choice == "4":
        view_colony_details()

def establish_colony():
    global credits_total, research_points
    
    print("\n🌍 ESTABLISH NEW COLONY")
    for i, planet in enumerate(available_planets, 1):
        if not planet["colonized"]:
            print(f"{i}. {planet['name']} - {planet['cost']} credits")
    
    choice = input("Select planet (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(available_planets):
        planet = available_planets[int(choice)-1]
        if not planet["colonized"]:
            if credits_total >= planet["cost"]:
                credits_total -= planet["cost"]
                planet["colonized"] = True
                
                colony = {
                    "name": planet["name"],
                    "income": planet["income"],
                    "population": 100,
                    "hazards": planet["hazards"],
                    "upgrades": []
                }
                colonies.append(colony)
                print(f"✅ Colony established on {planet['name']}!")
                print(f"🏠 Population: 100 | Income: {planet['income']} credits per collection")
                check_achievement("colonizer")
                gain_crew_xp(50)
            else:
                print(f"❌ Need {planet['cost']} credits!")

def upgrade_colonies():
    global credits_total
    
    if not colonies:
        print("No colonies to upgrade!")
        return
    
    print("\n🔧 COLONY UPGRADES")
    print(f"💰 Credits: {credits_total}")
    print("\nAvailable Upgrades:")
    
    upgrades_list = list(colonization_upgrades.items())
    for i, (name, data) in enumerate(upgrades_list, 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} credits"
        print(f"{i}. {name} - {status} (+{data['bonus']} income)")
    
    choice = input("\nSelect upgrade (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(upgrades_list):
        upgrade_name, upgrade_data = upgrades_list[int(choice)-1]
        if not upgrade_data["owned"]:
            if credits_total >= upgrade_data["cost"]:
                credits_total -= upgrade_data["cost"]
                upgrade_data["owned"] = True
                
                for colony in colonies:
                    colony["income"] += upgrade_data["bonus"]
                    if upgrade_name not in colony["upgrades"]:
                        colony["upgrades"].append(upgrade_name)
                
                print(f"✅ Purchased {upgrade_name} for all colonies!")
                print(f"📈 Colony income increased by {upgrade_data['bonus']}!")
            else:
                print(f"❌ Need {upgrade_data['cost']} credits!")

def collect_colony_income():
    global credits_total
    
    if not colonies:
        print("No colonies to collect income from!")
        return
    
    total_income = 0
    for colony in colonies:
        hazard_multiplier = 1.0
        if random.random() < 0.3:
            hazard = random.choice(colony["hazards"])
            if hazard == "dust_storms":
                hazard_multiplier = 0.7
                print(f"⚠️ Dust storms on {colony['name']} reduced income!")
            elif hazard == "ice_cracks":
                hazard_multiplier = 0.8
                print(f"⚠️ Ice cracks on {colony['name']} caused issues!")
            elif hazard == "methane_lakes":
                hazard_multiplier = 0.75
                print(f"⚠️ Methane lakes on {colony['name']} caused problems!")
            elif hazard == "alien_wildlife":
                hazard_multiplier = 0.6
                print(f"⚠️ Alien wildlife attacked {colony['name']}!")
            elif hazard == "solar_flares":
                hazard_multiplier = 0.65
                print(f"⚠️ Solar flares disrupted {colony['name']}!")
        
        income = int(colony["income"] * hazard_multiplier)
        total_income += income
        print(f"🪐 {colony['name']}: +{income} credits")
        colony["population"] += random.randint(5, 20)
    
    credits_total += total_income
    print(f"\n💰 Total Colony Income: {total_income} credits")
    gain_crew_xp(20)

def view_colony_details():
    if not colonies:
        print("No colonies yet!")
        return
    
    print("\n📊 COLONY DETAILS")
    print("=" * 40)
    for colony in colonies:
        print(f"\n🪐 {colony['name']}")
        print(f"   Population: {colony['population']}")
        print(f"   Income: {colony['income']} credits/turn")
        print(f"   Upgrades: {', '.join(colony['upgrades']) if colony['upgrades'] else 'None'}")
        print(f"   Hazards: {', '.join(colony['hazards'])}")

# ============= BLACK MARKET =============
def black_market():
    global credits_total, smuggling_heat, black_market_access, research_points
    
    if missions_completed >= 10:
        black_market_access = True
    
    if not black_market_access:
        print("\n🔒 Black Market is locked! Complete 10 missions to unlock.")
        return
    
    print("\n🕶️ BLACK MARKET 🕶️")
    print(f"⚠️ Smuggling Heat: {smuggling_heat}/100")
    print(f"💰 Your Credits: {credits_total}")
    print("\nAvailable Items:")
    
    items_list = list(black_market_items.items())
    for i, (item, data) in enumerate(items_list, 1):
        print(f"{i}. {item} - {data['price']} credits")
        print(f"   Risk: {data['risk']}% | Reward: {data['reward']}")
    
    print("\n5. Reduce Heat (500 credits)")
    print("6. Back")
    
    choice = input("\nChoose option: ")
    
    if choice == "5":
        if credits_total >= 500:
            credits_total -= 500
            smuggling_heat = max(0, smuggling_heat - 30)
            print("✅ Heat reduced!")
        else:
            print("❌ Not enough credits!")
    
    elif choice.isdigit() and 1 <= int(choice) <= len(items_list):
        item_name, item_data = items_list[int(choice)-1]
        
        if credits_total >= item_data["price"]:
            if random.random() < (item_data["risk"] / 100) + (smuggling_heat / 200):
                print("\n🚨 CAUGHT BY AUTHORITIES! 🚨")
                penalty = item_data["price"] * 2
                credits_total = max(0, credits_total - penalty)
                smuggling_heat += 40
                print(f"💸 Fined {penalty} credits!")
                print(f"🔥 Smuggling heat increased to {smuggling_heat}")
            else:
                credits_total -= item_data["price"]
                smuggling_heat += item_data["risk"] // 5
                print(f"✅ Successfully acquired {item_name}!")
                
                if item_data["reward"] == "research":
                    research_points += item_data["value"]
                    print(f"🧠 +{item_data['value']} Research Points!")
                elif item_data["reward"] == "combat":
                    inventory.append("illegal_weapon_upgrade")
                    print(f"⚔️ Combat upgrade added to inventory!")
                elif item_data["reward"] == "tech":
                    inventory.append("alien_technology")
                    print(f"🔧 Alien Technology added to inventory!")
                elif item_data["reward"] == "special":
                    credits_total += item_data["value"] * 2
                    print(f"💰 Sold fragment for {item_data['value'] * 2} credits!")
                elif item_data["reward"] == "treasure":
                    treasure = random.randint(300, 800)
                    credits_total += treasure
                    print(f"💰 Found treasure worth {treasure} credits!")
                
                gain_crew_xp(15)
                
                if len([i for i in inventory if "illegal" in i or "alien" in i]) >= 5:
                    check_achievement("smuggler")
        else:
            print("❌ Not enough credits!")

# ============= SPACE MINING =============
def space_mining():
    global credits_total, fuel, total_mined
    
    print("\n⛏️ SPACE MINING OPERATION ⛏️")
    print("=" * 40)
    
    mining_bonus = 1.0
    cargo_bonus = 1.0
    for upgrade, data in mining_upgrades.items():
        if data["owned"]:
            if upgrade == "Laser Drill":
                mining_bonus += data["bonus"]
                print(f"⚡ Laser Drill active! +{int(data['bonus']*100)}% mining speed!")
            elif upgrade == "Shield Generator":
                print(f"🛡️ Shield Generator active! Safer mining!")
            elif upgrade == "Cargo Expander":
                cargo_bonus += data["bonus"]
                print(f"📦 Cargo Expander active! +{int(data['bonus']*100)}% cargo space!")
    
    print("\nAvailable mining locations:")
    resources_list = list(mining_resources.items())
    for i, (resource

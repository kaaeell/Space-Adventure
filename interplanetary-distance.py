import math
import random
import time
from datetime import datetime
import json
import os

# SPACE DISTANCE CALCULATOR - ULTIMATE EDITION v3.0
# New today: Space anomalies, research system, bounty hunting, CREW SKILL SYSTEM, 
# SPACE STOCK MARKET, SPACE MINING, DIPLOMATIC RELATIONS, PLANETARY COLONIZATION, and BLACK MARKET!


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

# ============= NEW: PLANETARY COLONIZATION =============
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

# ============= NEW: BLACK MARKET =============
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

diplomacy_actions = {
    "gift": {"cost": 200, "relation_gain": 10, "message": "You sent a diplomatic gift!"},
    "trade_agreement": {"cost": 500, "relation_gain": 20, "message": "Trade routes established!"},
    "alliance": {"cost": 1000, "relation_gain": 35, "message": "You formed an alliance!"}
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
    "smuggler": "🕶️ Smuggler - Successfully use the black market 5 times"
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

# ============= NEW: PLANETARY COLONIZATION =============
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
                
                # Apply diplomacy bonus for colonization cost
                discount = 1.0
                for faction in alien_factions.values():
                    if "trade_discount" in faction["benefits"]:
                        discount *= 0.95
                
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
                
                # Apply upgrade to all colonies
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
        # Random events affect colony income
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
        
        # Population growth
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

# ============= NEW: BLACK MARKET =============
def black_market():
    global credits_total, smuggling_heat, black_market_access, research_points
    
    # Unlock black market after 10 missions
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
            # Risk check
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
                
                # Check for smuggler achievement
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
    for i, (resource, data) in enumerate(resources_list, 1):
        print(f"{i}. {resource} - Value: {data['value']} credits | Difficulty: {data['difficulty']}")
    
    choice = input("\nSelect location to mine (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(resources_list):
        resource_name, resource_data = resources_list[int(choice)-1]
        
        print(f"\n⛏️ Mining {resource_name}...")
        time.sleep(1)
        
        engineer_bonus = 1
        for member in crew_members:
            if member['bonus'] == 'fuel_saving':
                engineer_bonus = 1 + (member['level'] * 0.1)
        
        success_chance = 0.8 - (resource_data['difficulty'] * 0.1)
        success_chance = min(0.95, success_chance * engineer_bonus)
        
        if random.random() < success_chance:
            yield_amount = random.randint(resource_data['yield'][0], resource_data['yield'][1])
            yield_amount = int(yield_amount * mining_bonus * cargo_bonus)
            value = yield_amount * resource_data['value']
            
            credits_total += value
            total_mined += yield_amount
            
            print(f"✅ Success! Mined {yield_amount} {resource_name}")
            print(f"💰 Sold for {value} credits!")
            
            if total_mined >= 50:
                check_achievement("mining_baron")
            
            gain_crew_xp(10)
            fuel_cost = resource_data['difficulty'] * 20
            fuel = max(0, fuel - fuel_cost)
            print(f"⛽ Mining consumed {fuel_cost} fuel")
        else:
            print(f"❌ Mining failed!")
            damage = random.randint(20, 80)
            fuel = max(0, fuel - damage)
            print(f"💥 Lost {damage} fuel escaping!")

def buy_mining_upgrade():
    global credits_total
    
    print("\n🔧 MINING UPGRADE SHOP 🔧")
    print(f"💰 Credits: {credits_total}")
    print("\nAvailable upgrades:")
    
    upgrades_list = list(mining_upgrades.items())
    for i, (name, data) in enumerate(upgrades_list, 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} credits"
        print(f"{i}. {name} - {status}")
    
    choice = input("\nSelect upgrade (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(upgrades_list):
        upgrade_name, upgrade_data = upgrades_list[int(choice)-1]
        if not upgrade_data["owned"]:
            if credits_total >= upgrade_data["cost"]:
                credits_total -= upgrade_data["cost"]
                upgrade_data["owned"] = True
                print(f"✨ Purchased {upgrade_name}! ✨")
            else:
                print(f"❌ Need {upgrade_data['cost']} credits!")
        else:
            print("❌ Already owned!")

# ============= DIPLOMATIC RELATIONS =============
def diplomacy_system():
    global credits_total, research_points
    
    print("\n🤝 DIPLOMATIC RELATIONS 🤝")
    print("=" * 50)
    
    factions_list = list(alien_factions.items())
    for i, (faction, data) in enumerate(factions_list, 1):
        relation = data["relation"]
        if relation >= 80:
            emoji = "😊"
        elif relation >= 50:
            emoji = "😐"
        elif relation >= 30:
            emoji = "😠"
        else:
            emoji = "💀"
        
        print(f"{i}. {faction} {emoji}")
        print(f"   Relation: {relation}/100")
        if data["benefits"]:
            print(f"   Benefits: {', '.join(data['benefits'])}")
        print()
    
    print("\nDiplomatic Actions:")
    print("1. Send Gift (200 credits) - +10 relation")
    print("2. Trade Agreement (500 credits) - +20 relation, trade discount")
    print("3. Form Alliance (1000 credits) - +35 relation, special benefits")
    print("4. Request Aid - Get help based on relation")
    print("5. Back")
    
    choice = input("\nChoose action: ")
    
    if choice == "1":
        print("\nChoose faction:")
        for i, (faction, data) in enumerate(factions_list, 1):
            print(f"{i}. {faction}")
        sub_choice = input("Select faction: ")
        if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(factions_list):
            faction_name, faction_data = factions_list[int(sub_choice)-1]
            if credits_total >= 200:
                credits_total -= 200
                faction_data["relation"] = min(100, faction_data["relation"] + 10)
                print(f"✅ Sent gift to {faction_name}!")
                print(f"📈 Relation now: {faction_data['relation']}")
                check_relation_benefits(faction_name, faction_data)
            else:
                print("❌ Not enough credits!")
    
    elif choice == "2":
        print("\nChoose faction:")
        for i, (faction, data) in enumerate(factions_list, 1):
            print(f"{i}. {faction}")
        sub_choice = input("Select faction: ")
        if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(factions_list):
            faction_name, faction_data = factions_list[int(sub_choice)-1]
            if credits_total >= 500:
                credits_total -= 500
                faction_data["relation"] = min(100, faction_data["relation"] + 20)
                if "trade_discount" not in faction_data["benefits"]:
                    faction_data["benefits"].append("trade_discount")
                    faction_data["trade_discount"] = 0.9
                print(f"✅ Trade agreement signed with {faction_name}!")
                print(f"📈 Relation now: {faction_data['relation']}")
                print(f"💰 Permanent 10% discount on all trades!")
                check_relation_benefits(faction_name, faction_data)
            else:
                print("❌ Not enough credits!")
    
    elif choice == "3":
        print("\nChoose faction:")
        for i, (faction, data) in enumerate(factions_list, 1):
            print(f"{i}. {faction}")
        sub_choice = input("Select faction: ")
        if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(factions_list):
            faction_name, faction_data = factions_list[int(sub_choice)-1]
            if credits_total >= 1000:
                credits_total -= 1000
                faction_data["relation"] = min(100, faction_data["relation"] + 35)
                if "alliance_bonus" not in faction_data["benefits"]:
                    faction_data["benefits"].append("alliance_bonus")
                print(f"✅ Alliance formed with {faction_name}!")
                print(f"📈 Relation now: {faction_data['relation']}")
                print(f"🌟 +5% bonus to all mission rewards!")
                check_relation_benefits(faction_name, faction_data)
                check_achievement("diplomat")
            else:
                print("❌ Not enough credits!")
    
    elif choice == "4":
        print("\nChoose faction to request aid from:")
        for i, (faction, data) in enumerate(factions_list, 1):
            print(f"{i}. {faction} (Relation: {data['relation']})")
        sub_choice = input("Select faction: ")
        if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(factions_list):
            faction_name, faction_data = factions_list[int(sub_choice)-1]
            request_aid(faction_name, faction_data)

def request_aid(faction_name, faction_data):
    global fuel, credits_total
    
    relation = faction_data["relation"]
    
    if relation >= 80:
        aid_type = random.choice(["fuel", "credits", "repair"])
        if aid_type == "fuel":
            amount = random.randint(300, 800)
            fuel += amount
            print(f"🛢️ {faction_name} gave you {amount} fuel!")
        elif aid_type == "credits":
            amount = random.randint(400, 1200)
            credits_total += amount
            print(f"💰 {faction_name} gifted you {amount} credits!")
        else:
            print(f"🔧 {faction_name} repaired your ship!")
    elif relation >= 50:
        amount = random.randint(100, 300)
        fuel += amount
        print(f"

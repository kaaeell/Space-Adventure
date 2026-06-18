import math
import random
import time
from datetime import datetime
import json
import os

# SPACE DISTANCE CALCULATOR - ULTIMATE EDITION v3.4
# New today: Space anomalies, research system, bounty hunting, CREW SKILL SYSTEM, 
# SPACE STOCK MARKET, SPACE MINING, DIPLOMATIC RELATIONS, PLANETARY COLONIZATION, 
# BLACK MARKET, SPACE RACING LEAGUE, SPACE CASINO, DAILY CHALLENGES, and PIRATE RAID DEFENSE!


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

# ============= NEW: PIRATE RAID DEFENSE =============
pirate_raids = []
defense_turrets = {
    "Laser Turret": {"owned": False, "cost": 500, "damage": 20},
    "Missile Battery": {"owned": False, "cost": 800, "damage": 35},
    "Shield Generator": {"owned": False, "cost": 600, "defense": 20},
    "Plasma Cannon": {"owned": False, "cost": 1200, "damage": 50}
}

pirate_raid_stats = {
    "raids_survived": 0,
    "raids_defeated": 0,
    "total_damage_dealt": 0,
    "total_loot": 0
}

raid_difficulties = [
    {"name": "Small Scout", "health": 50, "damage": 10, "loot": 200},
    {"name": "Marauder", "health": 100, "damage": 20, "loot": 500},
    {"name": "Raider Fleet", "health": 200, "damage": 35, "loot": 1000},
    {"name": "Pirate Lord", "health": 350, "damage": 50, "loot": 2000},
    {"name": "Armada", "health": 500, "damage": 75, "loot": 5000}
]

# ============= DAILY CHALLENGES =============
daily_challenges = []
last_challenge_date = None

challenge_templates = [
    {"name": "Distance Master", "description": "Travel 500 million km", "goal": 500, "reward": 300, "type": "distance"},
    {"name": "Fuel Collector", "description": "Collect 1000 fuel", "goal": 1000, "reward": 200, "type": "fuel"},
    {"name": "Bounty Hunter", "description": "Complete 3 bounties", "goal": 3, "reward": 500, "type": "bounty"},
    {"name": "Star Explorer", "description": "Visit 5 different planets", "goal": 5, "reward": 400, "type": "planets"},
    {"name": "Credit Grinder", "description": "Earn 2000 credits", "goal": 2000, "reward": 600, "type": "credits"},
    {"name": "Research Genius", "description": "Gain 100 research points", "goal": 100, "reward": 350, "type": "research"},
    {"name": "Race Champion", "description": "Win 2 races", "goal": 2, "reward": 450, "type": "races"},
    {"name": "Mining Pro", "description": "Mine 30 resources", "goal": 30, "reward": 400, "type": "mining"},
    {"name": "Colony Builder", "description": "Collect colony income twice", "goal": 2, "reward": 500, "type": "colony"},
    {"name": "Casino Winner", "description": "Win 1000 credits at casino", "goal": 1000, "reward": 300, "type": "casino"},
    {"name": "Pirate Slayer", "description": "Defeat 3 pirate raids", "goal": 3, "reward": 600, "type": "pirate"}
]

daily_progress = {
    "distance": 0,
    "fuel": 0,
    "bounty": 0,
    "planets": 0,
    "credits": 0,
    "research": 0,
    "races": 0,
    "mining": 0,
    "colony": 0,
    "casino": 0,
    "pirate": 0
}

# ============= SPACE CASINO =============
casino_games = {
    "Cosmic Slots": {"min_bet": 10, "max_bet": 500, "jackpot": 5000},
    "Alien Poker": {"min_bet": 20, "max_bet": 1000, "jackpot": 10000},
    "Roulette": {"min_bet": 5, "max_bet": 300, "jackpot": 3000},
    "Black Hole Blackjack": {"min_bet": 15, "max_bet": 800, "jackpot": 8000}
}

casino_stats = {
    "total_bet": 0,
    "total_won": 0,
    "biggest_win": 0,
    "games_played": 0
}

# ============= SPACE RACING LEAGUE =============
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
    "racing_champion": "🏆 Racing Champion - Win 10 space races",
    "casino_king": "👑 Casino King - Win 10000 credits at the casino",
    "lucky_streak": "🍀 Lucky Streak - Win 5 casino games in a row",
    "challenge_master": "🎯 Challenge Master - Complete 10 daily challenges",
    "pirate_hunter": "🏴‍☠️ Pirate Hunter - Defeat 50 pirate raids",
    "defense_genius": "🛡️ Defense Genius - Own all defense turrets"
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

# ============= PIRATE RAID DEFENSE =============
def pirate_raid_defense():
    global credits_total, fuel, crew_morale, pirate_raid_stats
    
    print("\n🏴‍☠️ PIRATE RAID DEFENSE SYSTEM 🏴‍☠️")
    print("=" * 50)
    print(f"⚔️ Raids Survived: {pirate_raid_stats['raids_survived']}")
    print(f"⚔️ Raids Defeated: {pirate_raid_stats['raids_defeated']}")
    print(f"💰 Total Loot: {pirate_raid_stats['total_loot']} credits")
    
    print("\n1. Defend Against Raid")
    print("2. Buy Defense Turrets")
    print("3. View Defense Stats")
    print("4. Back")
    
    choice = input("\nChoose option: ")
    
    if choice == "1":
        defend_raid()
    elif choice == "2":
        buy_defense_turrets()
    elif choice == "3":
        view_defense_stats()

def defend_raid():
    global credits_total, fuel, crew_morale, pirate_raid_stats
    
    # Select raid difficulty based on missions completed
    max_difficulty = min(missions_completed // 5 + 1, len(raid_difficulties))
    difficulty_index = random.randint(0, max_difficulty - 1)
    raid = raid_difficulties[difficulty_index]
    
    print(f"\n⚔️ RAID DETECTED: {raid['name']} ⚔️")
    print(f"Enemy Health: {raid['health']}")
    print(f"Enemy Damage: {raid['damage']}")
    print(f"Potential Loot: {raid['loot']} credits")
    
    # Calculate defense strength
    defense_strength = 0
    defense_health = 100
    
    for turret_name, turret_data in defense_turrets.items():
        if turret_data["owned"]:
            if "damage" in turret_data:
                defense_strength += turret_data["damage"]
                print(f"✅ {turret_name} active! +{turret_data['damage']} damage")
            elif "defense" in turret_data:
                defense_health += turret_data["defense"]
                print(f"✅ {turret_name} active! +{turret_data['defense']} health")
    
    # Apply gunner bonus
    gunner_bonus = 1
    for member in crew_members:
        if member['bonus'] == 'combat_damage':
            gunner_bonus = 1 + (member['level'] * 0.1)
            print(f"🔫 Gunner bonus: +{int((gunner_bonus-1)*100)}% damage")
    
    print("\n⚔️ COMBAT STARTING ⚔️")
    enemy_health = raid['health']
    
    while defense_health > 0 and enemy_health > 0:
        # Player attacks
        player_damage = random.randint(10, 30) + defense_strength
        player_damage = int(player_damage * gunner_bonus)
        enemy_health -= player_damage
        print(f"⚡ You dealt {player_damage} damage to the raid!")
        
        if enemy_health <= 0:
            break
        
        # Enemy attacks
        enemy_damage = random.randint(5, raid['damage'])
        # Apply shield research if owned
        if research_upgrades["Shield Tech"]["owned"]:
            enemy_damage = int(enemy_damage * research_upgrades["Shield Tech"]["value"])
            print(f"🛡️ Shields reduced damage to {enemy_damage}!")
        defense_health -= enemy_damage
        print(f"💥 Raid dealt {enemy_damage} damage to your defenses!")
        
        time.sleep(0.5)
    
    if enemy_health <= 0:
        print("\n🎉 RAID DEFEATED! 🎉")
        loot = raid['loot'] * random.uniform(0.8, 1.2)
        loot = int(loot)
        credits_total += loot
        pirate_raid_stats['raids_defeated'] += 1
        pirate_raid_stats['total_loot'] += loot
        print(f"💰 Loot collected: {loot} credits!")
        
        gain_crew_xp(30)
        update_daily_progress("pirate", 1)
        
        if pirate_raid_stats['raids_defeated'] >= 50:
            check_achievement("pirate_hunter")
    else:
        print("\n💀 Defenses breached! Raid escaped!")
        repair_cost = random.randint(100, 400)
        credits_total = max(0, credits_total - repair_cost)
        print(f"🔧 Repairs cost {repair_cost} credits")
    
    pirate_raid_stats['raids_survived'] += 1
    fuel -= random.randint(20, 60)
    fuel = max(0, fuel)
    print(f"⛽ Fuel remaining: {fuel}")
    
    # Crew morale effect
    if enemy_health <= 0:
        morale_change = random.randint(5, 15)
        crew_morale = min(100, crew_morale + morale_change)
        print(f"😊 Crew morale +{morale_change}! (Now: {crew_morale}%)")
    else:
        morale_change = random.randint(10, 20)
        crew_morale = max(0, crew_morale - morale_change)
        print(f"😞 Crew morale -{morale_change}! (Now: {crew_morale}%)")

def buy_defense_turrets():
    global credits_total
    
    print("\n🛡️ DEFENSE TURRET SHOP 🛡️")
    print(f"💰 Credits: {credits_total}")
    print("\nAvailable Turrets:")
    
    turrets_list = list(defense_turrets.items())
    for i, (name, data) in enumerate(turrets_list, 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} credits"
        stats = []
        if "damage" in data:
            stats.append(f"Damage: {data['damage']}")
        if "defense" in data:
            stats.append(f"Defense: +{data['defense']}")
        print(f"{i}. {name} - {status} | {' | '.join(stats)}")
    
    choice = input("\nSelect turret (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(turrets_list):
        turret_name, turret_data = turrets_list[int(choice)-1]
        if not turret_data["owned"]:
            if credits_total >= turret_data["cost"]:
                credits_total -= turret_data["cost"]
                turret_data["owned"] = True
                print(f"✨ Purchased {turret_name}! ✨")
                
                # Check if all turrets owned
                if all(t["owned"] for t in defense_turrets.values()):
                    check_achievement("defense_genius")
            else:
                print(f"❌ Need {turret_data['cost']} credits!")
        else:
            print("❌ Already owned!")

def view_defense_stats():
    print("\n📊 DEFENSE STATISTICS 📊")
    print("=" * 40)
    print(f"Raids Survived: {pirate_raid_stats['raids_survived']}")
    print(f"Raids Defeated: {pirate_raid_stats['raids_defeated']}")
    if pirate_raid_stats['raids_survived'] > 0:
        win_rate = (pirate_raid_stats['raids_defeated'] / pirate_raid_stats['raids_survived']) * 100
        print(f"Win Rate: {win_rate:.1f}%")
    print(f"Total Loot Collected: {pirate_raid_stats['total_loot']} credits")
    print(f"Total Damage Dealt: {pirate_raid_stats['total_damage_dealt']}")
    
    print("\n🛡️ Owned Turrets:")
    owned = [name for name, data in defense_turrets.items() if data["owned"]]
    if owned:
        for turret in owned:
            print(f"  ✅ {turret}")
    else:
        print("  None")

# ============= DAILY CHALLENGES =============
def generate_daily_challenges():
    global daily_challenges, last_challenge_date
    
    today = datetime.now().date()
    
    if last_challenge_date != today:
        daily_challenges = []
        available_templates = challenge_templates.copy()
        random.shuffle(available_templates)
        
        for template in available_templates[:4]:  # Increased to 4 challenges
            challenge = template.copy()
            challenge["progress"] = 0
            challenge["completed"] = False
            daily_challenges.append(challenge)
        
        last_challenge_date = today
        for key in daily_progress:
            daily_progress[key] = 0

def show_daily_challenges():
    generate_daily_challenges()
    
    print("\n🎯 DAILY CHALLENGES 🎯")
    print("=" * 40)
    print(f"📅 {datetime.now().strftime('%Y-%m-%d')}")
    
    if not daily_challenges:
        print("No challenges available today!")
        return
    
    print("\nToday's Challenges:")
    completed_count = 0
    for i, challenge in enumerate(daily_challenges, 1):
        status = "✅" if challenge["completed"] else "⬜"
        progress = challenge["progress"]
        goal = challenge["goal"]
        bar_length = 20
        filled = int(bar_length * progress / goal)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"{i}. {status} {challenge['name']}")
        print(f"   {challenge['description']}")
        print(f"   Progress: [{bar}] {progress}/{goal}")
        print(f"   Reward: {challenge['reward']} credits")
        if challenge["completed"]:
            completed_count += 1
        print()
    
    print(f"\nCompleted: {completed_count}/{len(daily_challenges)}")
    
    if completed_count == len(daily_challenges):
        print("🎉 All challenges completed! Great job! 🎉")
        check_achievement("challenge_master")

def update_daily_progress(challenge_type, amount):
    generate_daily_challenges()
    
    for challenge in daily_challenges:
        if challenge["type"] == challenge_type and not challenge["completed"]:
            challenge["progress"] = min(challenge["goal"], challenge["progress"] + amount)
            
            if challenge["progress"] >= challenge["goal"]:
                challenge["completed"] = True
                complete_challenge(challenge)

def complete_challenge(challenge):
    global credits_total, research_points
    
    print(f"\n🎯 CHALLENGE COMPLETED: {challenge['name']} 🎯")
    print(f"💰 Reward: {challenge['reward']} credits")
    
    credits_total += challenge['reward']
    research_points += challenge['reward'] // 10
    gain_crew_xp(20)
    
    if all(c["completed"] for c in daily_challenges):
        bonus = 500
        credits_total += bonus
        print(f"🌟 Bonus for completing all challenges: +{bonus} credits!")

# ============= SPACE CASINO =============
def space_casino():
    global credits_total, crew_morale
    
    print("\n🎰 SPACE CASINO 🎰")
    print("=" * 50)
    print(f"💰 Your Credits: {credits_total}")
    print(f"🎯 Biggest Win: {casino_stats['biggest_win']} credits")
    print("\nAvailable Games:")
    
    games_list = list(casino_games.items())
    for i, (game, data) in enumerate(games_list, 1):
        print(f"{i}. {game}")
        print(f"   Min Bet: {data['min_bet']} | Max Bet: {data['max_bet']} | Jackpot: {data['jackpot']}")
    
    print("\n5. View Casino Stats")
    print("6. Back")
    
    choice = input("\nChoose game: ")
    
    if choice == "5":
        view_casino_stats()
    elif choice.isdigit() and 1 <= int(choice) <= len(games_list):
        game_name, game_data = games_list[int(choice)-1]
        play_casino_game(game_name, game_data)

def play_casino_game(game_name, game_data):
    global credits_total, crew_morale, casino_stats
    
    print(f"\n🎮 PLAYING: {game_name} 🎮")
    print(f"💰 Your Credits: {credits_total}")
    
    bet = int(input(f"Enter bet ({game_data['min_bet']}-{game_data['max_bet']}): "))
    
    if bet < game_data['min_bet'] or bet > game_data['max_bet']:
        print("❌ Invalid bet amount!")
        return
    
    if bet > credits_total:
        print("❌ Not enough credits!")
        return
    
    credits_total -= bet
    casino_stats['total_bet'] += bet
    
    print("\n🔄 Spinning...")
    time.sleep(1.5)
    
    if game_name == "Cosmic Slots":
        result = play_slots(b

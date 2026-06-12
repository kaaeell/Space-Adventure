import math
import random
import time
from datetime import datetime
import json
import os

# SPACE DISTANCE CALCULATOR - ULTIMATE EDITION v2.1
# New today: Space anomalies, research system, bounty hunting, CREW SKILL SYSTEM, and SPACE STOCK MARKET!


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

# ============= NEW: CREW SKILL SYSTEM =============
crew_members = [
    {"name": "Captain", "skill": "Leadership", "level": 1, "xp": 0, "bonus": "morale"},
    {"name": "Engineer", "skill": "Mechanics", "level": 1, "xp": 0, "bonus": "fuel_saving"},
    {"name": "Navigator", "skill": "Astrogation", "level": 1, "xp": 0, "bonus": "distance_bonus"},
    {"name": "Scientist", "skill": "Research", "level": 1, "xp": 0, "bonus": "rp_bonus"},
    {"name": "Gunner", "skill": "Combat", "level": 1, "xp": 0, "bonus": "combat_damage"}
]

# ============= NEW: SPACE STOCK MARKET =============
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
    "📰 Supply shortage reported!",
    "📰 Overproduction causing price drop!"
]

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
    "stock_master": "📈 Stock Master - Make 5000 profit from stock market"
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

def calculate_distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def get_coordinates(name):
    while True:
        try:
            print(f"\nEnter coordinates for {name} (in million km)")
            x = float(input("x: "))
            y = float(input("y: "))
            return (x, y)
        except ValueError:
            print("invalid input")

def choose_planets():
    planets = {
        1: ("Earth",(0,0)), 2: ("Mars",(225,0)), 3: ("Venus",(108,0)), 4: ("Jupiter",(778,0)),
        5: ("Saturn",(1427,0)), 6: ("Uranus",(2871,0)), 7: ("Neptune",(4495,0)), 8: ("Mercury",(58,0)),
        9: ("Pluto",(5906,0)), 10: ("Moon",(1,0))
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
                else:
                    print("pick a valid number")
            except ValueError:
                print("numbers only")
    p1_name, p1 = pick("Choose planet 1: ")
    p2_name, p2 = pick("Choose planet 2: ")
    return p1_name, p1, p2_name, p2

# ============= NEW: SPACE STOCK MARKET =============
def update_stock_prices():
    for stock in stock_market.values():
        change = random.uniform(-stock["volatility"], stock["volatility"])
        stock["price"] = max(10, int(stock["price"] * (1 + change)))
        
        # Random news events affect specific stocks
        if random.random() < 0.2:
            news = random.choice(market_news)
            print(f"\n📢 MARKET NEWS: {news}")
            
            if "discovered" in news or "breakthrough" in news:
                for s in stock_market.values():
                    s["price"] = int(s["price"] * 1.3)
                print(f"   All prices surged!")
            elif "pirates" in news or "shortage" in news:
                for s in stock_market.values():
                    s["price"] = int(s["price"] * 1.2)
                print(f"   Prices increased due to scarcity!")
            elif "subsidies" in news or "overproduction" in news:
                for s in stock_market.values():
                    s["price"] = int(s["price"] * 0.85)
                print(f"   Prices dropped due to oversupply!")

def space_stock_market():
    global credits_total
    
    print("\n📈 SPACE STOCK MARKET 📈")
    print(f"💰 Your Credits: {credits_total}")
    print("\nCurrent Stock Prices:")
    print("-" * 50)
    
    stocks_list = list(stock_market.items())
    for i, (name, data) in enumerate(stocks_list, 1):
        print(f"{i}. {name}: {data['price']} credits")
        if data['owned'] > 0:
            print(f"   Owned: {data['owned']} shares | Value: {data['owned'] * data['price']} credits")
    
    print("\n" + "-" * 50)
    print("1. Buy shares")
    print("2. Sell shares")
    print("3. Update market prices")
    print("4. View portfolio")
    print("5. Back to main menu")
    
    choice = input("\nChoose option: ")
    
    if choice == "1":
        buy_stocks()
    elif choice == "2":
        sell_stocks()
    elif choice == "3":
        update_stock_prices()
        print("✅ Market prices updated!")
    elif choice == "4":
        show_portfolio()
    elif choice == "5":
        return

def buy_stocks():
    global credits_total
    
    print("\n💰 BUY SHARES")
    stocks_list = list(stock_market.items())
    for i, (name, data) in enumerate(stocks_list, 1):
        print(f"{i}. {name} - {data['price']} credits/share")
    
    choice = input("Select stock (number): ")
    if choice.isdigit() and 1 <= int(choice) <= len(stocks_list):
        stock_name, stock_data = stocks_list[int(choice)-1]
        shares = int(input(f"How many shares of {stock_name}? "))
        cost = shares * stock_data["price"]
        
        if credits_total >= cost:
            credits_total -= cost
            stock_data["owned"] += shares
            print(f"✅ Bought {shares} shares of {stock_name} for {cost} credits!")
            
            # Scientist gives trading bonus
            for member in crew_members:
                if member['bonus'] == 'rp_bonus' and random.random() < 0.3:
                    bonus = random.randint(10, 50)
                    research_points += bonus
                    print(f"🔬 Scientist found trading insights! +{bonus} RP")
        else:
            print(f"❌ Need {cost} credits, only have {credits_total}!")

def sell_stocks():
    global credits_total
    
    print("\n💰 SELL SHARES")
    stocks_list = list(stock_market.items())
    has_shares = False
    
    for i, (name, data) in enumerate(stocks_list, 1):
        if data['owned'] > 0:
            has_shares = True
            print(f"{i}. {name} - Owned: {data['owned']} | Current price: {data['price']}")
    
    if not has_shares:
        print("You don't own any shares!")
        return
    
    choice = input("Select stock to sell (number): ")
    if choice.isdigit() and 1 <= int(choice) <= len(stocks_list):
        stock_name, stock_data = stocks_list[int(choice)-1]
        if stock_data['owned'] > 0:
            shares = int(input(f"How many shares to sell? (Max: {stock_data['owned']}) "))
            if shares <= stock_data['owned']:
                revenue = shares * stock_data['price']
                credits_total += revenue
                stock_data['owned'] -= shares
                print(f"✅ Sold {shares} shares for {revenue} credits!")
                
                # Check for profit achievement
                if revenue - (shares * 100) > 5000:
                    check_achievement("stock_master")
            else:
                print("Not enough shares!")
        else:
            print("You don't own that stock!")

def show_portfolio():
    print("\n📊 YOUR PORTFOLIO")
    total_value = 0
    for name, data in stock_market.items():
        if data['owned'] > 0:
            value = data['owned'] * data['price']
            total_value += value
            print(f"{name}: {data['owned']} shares = {value} credits")
    
    print(f"\n💰 Total Portfolio Value: {total_value} credits")
    print(f"💵 Cash: {credits_total} credits")
    print(f"📈 Net Worth: {credits_total + total_value} credits")

# ============= CREW SKILL SYSTEM =============
def show_crew_skills():
    print("\n👥 CREW SKILL SYSTEM 👥")
    print("=" * 40)
    for i, member in enumerate(crew_members, 1):
        print(f"{i}. {member['name']} - {member['skill']}")
        print(f"   Level: {member['level']} | XP: {member['xp']}/{(member['level'] * 100)}")
        print(f"   Bonus: {member['bonus']}")
        print()
    
    print("\n💡 Crew members gain XP from missions!")
    print("   Higher levels = better bonuses!")

def gain_crew_xp(xp_amount):
    global credits_total, research_points
    
    for member in crew_members:
        member['xp'] += xp_amount
        # Level up check
        if member['xp'] >= member['level'] * 100:
            member['xp'] = 0
            member['level'] += 1
            print(f"\n🎉 {member['name']} leveled up to level {member['level']}! 🎉")
            
            # Special rewards on level up
            bonus = random.randint(100, 300)
            credits_total += bonus
            print(f"💰 Crew celebration! +{bonus} credits!")
            
            if member['level'] >= 5:
                check_achievement("crew_trainer")

def apply_crew_bonus(bonus_type, value):
    for member in crew_members:
        if member['bonus'] == bonus_type:
            bonus_multiplier = 1 + (member['level'] * 0.05)
            return value * bonus_multiplier
    return value

def train_crew():
    global credits_total
    
    print("\n📚 CREW TRAINING ACADEMY 📚")
    print(f"💰 Credits: {credits_total}")
    print("\nTraining options:")
    print("1. Basic Training (200 credits) - +30 XP to all crew")
    print("2. Advanced Training (500 credits) - +80 XP to all crew")
    print("3. Elite Training (1000 credits) - +200 XP to all crew")
    print("4. Specialization Course (800 credits) - +100 XP for one crew")
    
    choice = input("\nChoose training (1-4) or 'quit': ")
    
    if choice == "1" and credits_total >= 200:
        credits_total -= 200
        gain_crew_xp(30)
        print("✅ Basic training complete!")
    elif choice == "2" and credits_total >= 500:
        credits_total -= 500
        gain_crew_xp(80)
        print("✅ Advanced training complete!")
    elif choice == "3" and credits_total >= 1000:
        credits_total -= 1000
        gain_crew_xp(200)
        print("✅ Elite training complete!")
    elif choice == "4" and credits_total >= 800:
        credits_total -= 800
        print("\nChoose crew member:")
        for i, member in enumerate(crew_members, 1):
            print(f"{i}. {member['name']}")
        sub_choice = input("Select member: ")
        if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(crew_members):
            member = crew_members[int(sub_choice)-1]
            member['xp'] += 100
            print(f"✅ {member['name']} gained 100 XP!")
            if member['xp'] >= member['level'] * 100:
                member['xp'] = 0
                member['level'] += 1
                print(f"🎉 {member['name']} leveled up!")
    else:
        print("❌ Not enough credits or invalid choice!")

# ============= ANOMALY DISCOVERY SYSTEM =============
def discover_anomaly():
    global research_points, crew_morale, fuel, credits_total, inventory
    
    anomaly_name = random.choice(list(space_anomalies.keys()))
    anomaly = space_anomalies[anomaly_name]
    
    print(f"\n🔭 ANOMALY DISCOVERED: {anomaly_name} 🔭")
    print(f"📖 {anomaly['description']}")
    
    if anomaly_name not in discovered_anomalies:
        discovered_anomalies.append(anomaly_name)
        print(f"✨ New anomaly added to discovery log!")
        if len(discovered_anomalies) >= 3:
            check_achievement("anomaly_hunter")
    
    if anomaly["effect"] == "bonus_research":
        gain = anomaly["reward"]
        research_points += gain
        print(f"🧠 +{gain} research points!")
        
    elif anomaly["effect"] == "teleport":
        print("🌀 You've been teleported to a random location!")
        print("(Your next mission might be affected!)")
        
    elif anomaly["effect"] == "gift":
        gain = anomaly["reward"]
        credits_total += gain
        print(f"💰 The anomaly gave you {gain} credits!")
        
    elif anomaly["effect"] == "danger":
        damage = anomaly["damage"]
        if research_upgrades["Shield Tech"]["owned"]:
            damage = int(damage * research_upgrades["Shield Tech"]["value"])
            print(f"🛡️ Shields reduced damage to {damage}!")
        fuel = max(0, fuel - damage)
        print(f"💥 You lost {damage} fuel escaping!")
        
    elif anomaly["effect"] == "morale_boost":
        gain = anomaly["reward"]
        crew_morale = min(100, crew_morale + gain)
        print(f"😊 Crew morale +{gain}! (Now: {crew_morale}%)")
        if anomaly_name == "🎵 Space Whale Song":
            check_achievement("space_whisperer")
            
    elif anomaly["effect"] == "artifact":
        artifact = random.choice(["ancient tablet", "crystal skull", "energy orb", "star map"])
        inventory.append(artifact)
        print(f"🔮 You found an {artifact}!")
        research_points += 30
        print(f"🧠 +30 research points from studying the artifact!")

# ============= BOUNTY HUNTING SYSTEM =============
def bounty_hunting():
    global credits_total, fuel, bounty_hunting_level
    
    print("\n💰 BOUNTY HUNTING SYSTEM 💰")
    print(f"🏆 Your Bounty Rank: {bounty_hunting_level}")
    
    available_targets = [t for t in bounty_targets if t["level"] <= bounty_hunting_level + 1]
    
    if not available_targets:
        print("No available bounties at your rank! Complete more missions!")
        return
    
    print("\n🎯 AVAILABLE BOUNTIES:")
    for i, target in enumerate(available_targets[:3], 1):
        print(f"{i}. {target['name']} - 💰 {target['bounty']} credits (Level {target['level']})")
    
    choice = input("\nSelect bounty (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(available_targets[:3]):
        target = available_targets[int(choice)-1]
        
        print(f"\n🚀 Hunting {target['name']}...")
        time.sleep(1)
        
        print("⚔️ COMBAT MODE ⚔️")
        player_health = target['health']
        target_health = target['health']
        
        gunner_bonus = 1
        for member in crew_members:
            if member['bonus'] == 'combat_damage':
                gunner_bonus = 1 + (member['level'] * 0.1)
                print(f"🔫 Gunner bonus: +{int((gunner_bonus-1)*100)}% damage!")
        
        while player_health > 0 and target_health > 0:
            print(f"\n❤️ Your health: {player_health} | {target['name']} health: {target_health}")
            action = input("1. Attack | 2. Dodge | 3. Use item: ")
            
            if action == "1":
                damage = int(random.randint(2, 6) * gunner_bonus)
                target_health -= damage
                print(f"⚡ You dealt {damage} damage!")
                
                enemy_damage = random.randint(1, 5)
                player_health -= enemy_damage
                print(f"💥 {target['name']} dealt {enemy_damage} damage!")
                
            elif action == "2":
                if random.random() < 0.6:
                    print("🛡️ You dodged the attack!")
                else:
                    enemy_damage = random.randint(2, 6)
                    player_health -= enemy_damage
                    print(f"💥 Failed to dodge! Took {enemy_damage} damage!")
                    
            elif action == "3":
                print("🩹 Using repair kit...")
                heal = random.randint(3, 8)
                player_health = min(target['health'], player_health + heal)
                print(f"❤️ Restored {heal} health!")
        
        if player_health > 0:
            reward = target['bounty']
            credits_total += reward
            print(f"\n🎉 VICTORY! Defeated {target['name']}!")
            print(f"💰 Claimed {reward} credits!")
            gain_crew_xp(50)
            
            if target["level"] == bounty_hunting_level:
                bounty_hunting_level = min(5, bounty_hunting_level + 1)
                print(f"🏆 Bounty rank increased to {bounty_hunting_level}!")
                
            check_achievement("bounty_hunter")
            if bounty_hunting_level >= 5:
                check_achievement("galactic_hero")
        else:
            print(f"\n💀 Defeated by {target['name']}... Lost 200 credits")
            credits_total = max(0, credits_total - 200)

# ============= RESEARCH SYSTEM =============
def research_lab():
    global research_points, fuel, credits_total
    
    print("\n🧪 RESEARCH LAB 🧪")
    print(f"📚 Research Points: {research_points}")
    print("\nAvailable Upgrades:")
    
    rp_bonus = 1
    for member in crew_members:
        if member['bonus'] == 'rp_bonus':
            rp_bonus = 1 + (member['level'] * 0.05)
            print(f"🔬 Scientist bonus: +{int((rp_bonus-1)*100)}% research efficiency!")
    
    upgrades_list = list(research_upgrades.items())
    for i, (name, data) in enumerate(upgrades_list, 1):
        status = "✅ OWNED" if data["owned"] else f"💰 {data['cost']} RP"
        print(f"{i}. {name} - {status}")
    
    print("\n7. Convert credits to research points (100 credits = 20 RP)")
    print("8. 🎓 Train Crew")
    
    choice = input("\nSelect option (number) or 'quit': ")
    
    if choice == "8":
        train_crew()
    elif choice.isdigit() and 1 <= int(choice) <= len(upgrades_list):
        upgrade_name, upgrade_data = upgrades_list[int(choice)-1]
        if not upgrade_data["owned"]:
            cost = upgrade_data["cost"]
            if research_points >= cost:
                research_points -= cost
                upgrade_data["owned"] = True
                print(f"✨ Unlocked {upgrade_name}! ✨")
                check_achievement("research_genius")
                gain_crew_xp(25)
            else:
                print(f"❌ Need {cost} research points!")
        else:
            print("❌ Already owned!")
            
    elif choice == "7":
        amount = int(input("How many credits to convert? "))
        if amount >= 100:
            rp_gain = (amount // 100) * 20
            credits_total -= amount
            research_points += rp_gain
            print(f"✨ Converted {amount} credits into {rp_gain} research points!")

# ============= COMET TRACKING =============
def track_comet():
    global credits_total, research_points
    
    print("\n☄️ COMET TRACKING SYSTEM ☄️")
    comet = random.choice(comet_names)
    print(f"Tracking comet {comet}...")
    time.sleep(1)
    
    nav_bonus = 1
    for member in crew_members:
        if member['bonus'] == 'distance_bonus':
            nav_bonus = 1 - (member['level'] * 0.02)
            print(f"🧭 Navigator bonus: Easier tracking!")
    
    print("\nAdjust your telescope!")
    target_angle = random.randint(0, 360)
    print(f"Target angle: ???")
    
    guess = int(input("Your guess (0-360): "))
    difference = min(abs(guess - target_angle), 360 - abs(guess - target_angle))
    difference = int(difference * nav_bonus)
    
    if difference < 10:
        reward = 500
        print(f"🎯 PERFECT! You found comet {comet}!")
        print(f"💰 +{reward} credits!")
        credits_total += reward
        research_points += 30
        gain_crew_xp(40)
        check_achievement("comet_chaser")
    elif difference < 30:
        reward = 200
        print(f"👍 Good! You spotted comet {comet}!")
        print(f"💰 +{reward} credits!")
        credits_total += reward
        research_points += 15
        gain_crew_xp(15)
    else:
        print(f"😅 Missed it! The comet was at {target_angle}°")

# ============= SAVE/LOAD SYSTEM =============
def save_game():
    save_data = {
        "history": history,
        "total_calculations": total_calculations,
        "highest_distance": highest_distance,
        "missions_completed": missions_completed,
        "fuel": fuel,
        "credits_total": credits_total,
        "achievements": achievements,
        "inventory": inventory,
        "crew_morale": crew_morale,
        "consecutive_missions": consecutive_missions,
        "research_points": research_points,
        "bounty_hunting_level": bounty_hunting_level,
        "discovered_anomalies": discovered_anomalies,
        "research_upgrades_owned": {name: data["owned"] for name, data in research_upgrades.items()},
        "crew_members": crew_members,
        "stock_market": stock_market
    }
    
    with open("space_save.json", "w") as f:
        json.dump(save_data, f)
    print("💾 Game saved successfully!")

def load_game():
    global history, total_calculations, highest_distance, missions_completed, fuel, credits_total
    global achievements, inventory, crew_morale, consecutive_missions, research_points
    global bounty_hunting_level, discovered_anomalies, crew_members, stock_market
    
    try:
        with open("space_save.json", "r") as f:
            save_data = json.load(f)
        
        history = save_data.get("history", [])
        total_calculations = save_data.get("total_calculations", 0)
        highest_distance = save_data.get("highest_distance", 0)
        missions_completed = save_data.get("missions_completed", 0)
        fuel = save_data.get("fuel", 5000)
        credits_total = save_data.get("credits_total", 1000)
        achievements = save_data.get("achievements", [])
        inventory = save_data.get("inventory", [])
        crew_morale = save_data.get("crew_morale", 80)
        consecutive_missions = save_data.get("consecutive_missions", 0)
        research_points = save_data.get("research_points", 0)
        bounty_hunting_level = save_data.get("bounty_hunting_level", 1)
        discovered_anomalies = save_data.get("discovered_anomalies", [])
        crew_members = save_data.get("crew_members", crew_members)
        stock_market = save_data.get("stock_market", stock_market)
        
        upgrades_owned = save_data.get("research_upgrades_owned", {})
        for name, owned in upgrades_owned.items():
            if name in research_upgrades:
                research_upgrades[name]["owned"] = owned
        
        print("📀 Game loaded successfully!")
        return True
    except FileNotFoundError:
        print("❌ No save file found!")
        return False

# ============= FLUFF FUNCTIONS =============
def trigger_random_event():
    global fuel, credits_total, consecutive_missions
    
    if random.random() < 0.35:
        event = random.choice(random_events)
        print(f"\n⚠️ EVENT: {event['name']} ⚠️")
        print(event['message'])
        
        if event.get('anomaly'):
            discover_anomaly()
            return 1.0
            
        if event.get('comet'):
            track_comet()
            return 1.0
        
        if 'modifier' in event:
            return event['modifier']
            
        if 'fuel' in event:
            fuel = max(0, fuel + event['fuel'])
        if 'credits' in event:
            credits_total = max(0, credits_total + event['credits'])
        
        if event['name'] == "🌀 WORMHOLE!":
            check_achievement("wormhole_rider")
        
        return 1.0
    return 1.0

def update_crew_morale(distance, success=True):
    global crew_morale, consecutive_m

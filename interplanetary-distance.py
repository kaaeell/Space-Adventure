import math
import random
import time
from datetime import datetime
import os

# the code is getting EVEN BETTER today! ✨
# added: wormholes, space pirates, crew morale, and more surprises!
#this is really awesome

history = []
total_calculations = 0
highest_distance = 0
missions_completed = 0
fuel = 5000
credits_total = 1000
achievements = []
inventory = []
crew_morale = 80  # NEW: Crew morale system!
consecutive_missions = 0  # NEW: Streak counter

galaxy_names = ["Milky Way","Andromeda","Sombrero Galaxy","Whirlpool Galaxy","Black Eye Galaxy","Cartwheel Galaxy"]
astronauts = ["Neil","Buzz","Sally","Yuri","Mae","Chris","Valentina"]
spaceships = ["StarRunner","NovaX","Galaxy Rider","Void Explorer","Cosmic Storm","Nebula One"]
space_pets = ["space dog","robot cat","alien hamster","tiny moon dragon"]
badges = ["🌟 rookie pilot badge","🚀 master explorer badge","🪐 galaxy navigator badge","☄️ asteroid survivor badge"]
alien_names = ["Zorg","Xenon","Blip","Nova","Kratos"]
space_foods = ["freeze dried pizza","space tacos","galaxy noodles","moon burgers"]
space_jobs = ["pilot","engineer","galaxy scout","alien translator","space mechanic"]
planet_conditions = ["lava storms detected","ice surface detected","heavy gravity detected","safe landing conditions","radioactive atmosphere detected"]

comet_names = ["Halley","Encke","Hale-Bopp","Swift-Tuttle","Neowise"]
space_jokes = ["Why did the star go to school? To get a little brighter!","What do astronauts use to keep their pants up? An asteroid belt!","Why don't aliens visit our solar system? They read the reviews… only one star!"]
alien_greetings = ["👽 Blip blop!","👾 Greetings Earthling!","🛸 Take me to your leader!","🛸 Beep boop!"]

# NEW: Random events that can happen during missions
random_events = [
    {"name": "🌀 WORMHOLE!", "effect": "shortcut", "message": "You found a wormhole! Distance reduced by 40%!", "modifier": 0.6},
    {"name": "🏴‍☠️ SPACE PIRATES!", "effect": "danger", "message": "Space pirates attacked! Lost 200 fuel and 100 credits!", "fuel": -200, "credits": -100},
    {"name": "✨ COSMIC CACHE", "effect": "reward", "message": "Found a floating cargo pod! +300 credits and +150 fuel!", "fuel": 150, "credits": 300},
    {"name": "🌊 SOLAR FLARE", "effect": "danger", "message": "Solar flare damaged shields! Lost 100 fuel!", "fuel": -100},
    {"name": "🤝 FRIENDLY ALIENS", "effect": "reward", "message": "Friendly aliens gave you a gift! +250 credits!", "credits": 250}
]

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
    "streak_master": "🔥 Streak Master - Complete 5 missions in a row!",  # NEW
    "wormhole_rider": "🌀 Wormhole Rider - Successfully use a wormhole"  # NEW
}

nebulae = {
    "Orion Nebula": (1340, -220),
    "Eagle Nebula": (7000, 0),
    "Helix Nebula": (695, 280),
    "Crab Nebula": (6500, 190),
    "Tarantula Nebula": (160000, 5000)
}

alien_items = {
    "🌌 dark matter crystal": 500,
    "💫 warp core upgrade": 2000,
    "🔮 quantum shield": 1500,
    "🍕 exotic space pizza": 50,
    "🐉 baby space dragon egg": 3000
}

def calculate_distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def get_coordinates(name):
    while True:
        try:
            print(f"\nEnter coordinates for {name} (in million km)")
            x = float(input("x: "))
            y = float(input("y: "))
            return (x,y)
        except ValueError:
            print("invalid input")

def choose_planets():
    planets = {
        1: ("Earth",(0,0)),2: ("Mars",(225,0)),3: ("Venus",(108,0)),4: ("Jupiter",(778,0)),
        5: ("Saturn",(1427,0)),6: ("Uranus",(2871,0)),7: ("Neptune",(4495,0)),8: ("Mercury",(58,0)),
        9: ("Pluto",(5906,0)),10: ("Moon",(1,0))
    }
    print("\n📋 Available planets:")
    for num,(name,_) in planets.items():
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
    p1_name,p1 = pick("Choose planet 1: ")
    p2_name,p2 = pick("Choose planet 2: ")
    return p1_name,p1,p2_name,p2

# NEW: Random event trigger during missions
def trigger_random_event():
    global fuel, credits_total, consecutive_missions
    if random.random() < 0.3:  # 30% chance of random event
        event = random.choice(random_events)
        print(f"\n⚠️ EVENT: {event['name']} ⚠️")
        print(event['message'])
        
        if 'modifier' in event:
            return event['modifier']  # Return distance modifier
        if 'fuel' in event:
            fuel = max(0, fuel + event['fuel'])
        if 'credits' in event:
            credits_total = max(0, credits_total + event['credits'])
        
        if event['name'] == "🌀 WORMHOLE!":
            check_achievement("wormhole_rider")
        
        return 1.0  # No distance change
    return 1.0

# NEW: Crew morale system
def update_crew_morale(distance, success=True):
    global crew_morale, consecutive_missions
    if success:
        gain = random.randint(5, 15)
        crew_morale = min(100, crew_morale + gain)
        consecutive_missions += 1
        print(f"😊 Crew morale +{gain}! (Now: {crew_morale}%)")
        if consecutive_missions >= 5:
            check_achievement("streak_master")
    else:
        loss = random.randint(10, 25)
        crew_morale = max(0, crew_morale - loss)
        consecutive_missions = 0
        print(f"😞 Crew morale -{loss}! (Now: {crew_morale}%)")
    
    # Morale bonuses
    if crew_morale > 80:
        print("🎉 Crew is HYPED! +10% bonus to next mission!")
    elif crew_morale < 30:
        print("⚠️ Crew morale is critically low! Take a break or buy space pizza!")

# NEW: Show crew status bar
def show_crew_status():
    bar_length = 20
    filled = int(bar_length * crew_morale / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    mood_emoji = "😄" if crew_morale > 70 else "😐" if crew_morale > 40 else "😞"
    print(f"👥 Crew Morale: [{bar}] {crew_morale}% {mood_emoji}")

def check_fuel(distance):
    global fuel
    fuel_needed = distance * 0.5
    if fuel < fuel_needed:
        print(f"\n⚠️ INSUFFICIENT FUEL! Need {fuel_needed:.1f} units, have {fuel:.1f}")
        print("🎲 Attempting emergency fuel collection...")
        collect_emergency_fuel()
        return check_fuel(distance)
    else:
        fuel -= fuel_needed
        print(f"⛽ Fuel used: {fuel_needed:.1f} units | Remaining: {fuel:.1f}")
        return True

def collect_emergency_fuel():
    global fuel, credits_total
    print("\n🔄 EMERGENCY FUEL COLLECTION MODE 🔄")
    print("1. 🛸 Mine asteroid (risky but free)")
    print("2. 💰 Buy fuel (costs credits)")
    print("3. 🎲 Space casino (gamble!)")
    
    choice = input("Choose: ")
    
    if choice == "1":
        if random.random() < 0.6:
            gained = random.randint(200, 800)
            fuel += gained
            print(f"✅ +{gained} fuel")
        else:
            damage = random.randint(50, 200)
            fuel = max(0, fuel - damage)
            print(f"💥 Lost {damage} fuel")
    elif choice == "2":
        cost_per_unit = 2
        amount = int(input("How much fuel to buy? "))
        if credits_total >= amount * cost_per_unit:
            credits_total -= amount * cost_per_unit
            fuel += amount
            print(f"✅ Bought {amount} fuel!")
        else:
            print("❌ Not enough credits!")
    elif choice == "3":
        bet = int(input("Bet credits: "))
        if bet > credits_total:
            print("Not enough credits!")
            return
        if random.random() > 0.7:
            winnings = bet * random.uniform(1.5, 3)
            credits_total += winnings
            fuel += random.randint(100, 400)
            print(f"🎉 WIN! +{winnings:.0f} credits and fuel!")
        else:
            credits_total -= bet
            print(f"💀 Lost {bet} credits!")

def alien_trade():
    global credits_total, inventory
    print("\n🛸 ALIEN TRADING POST 🛸")
    print(f"💰 Credits: {credits_total}")
    items_list = list(alien_items.items())
    for i, (item, price) in enumerate(items_list, 1):
        print(f"{i}. {item} - {price} credits")
    
    choice = input("Buy (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= len(items_list):
        item, price = items_list[int(choice)-1]
        if credits_total >= price:
            credits_total -= price
            inventory.append(item)
            print(f"✨ Bought {item}!")
            check_achievement("alien_friend")
        else:
            print("❌ Need more credits!")

def explore_nebula():
    global fuel, achievements
    print("\n🌌 NEBULA EXPLORATION")
    neb_list = list(nebulae.items())
    for i, (name, coords) in enumerate(neb_list[:3], 1):  # Show first 3
        print(f"{i}. {name}")
    
    choice = input("Explore (number) or 'quit': ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        neb_name, coords = neb_list[int(choice)-1]
        print(f"\n🚀 Warping to {neb_name}...")
        time.sleep(1)
        
        if random.random() < 0.7:
            fuel_gained = random.randint(300, 1500)
            fuel += fuel_gained
            print(f"⛽ Collected {fuel_gained} fuel!")
            check_achievement("fuel_hunter")
        else:
            artifact = random.choice(["ancient artifact", "crystal", "energy core"])
            inventory.append(artifact)
            print(f"🔮 Found {artifact}!")

def space_race():
    global credits_total, fuel
    print("\n🏁 SPACE RACE CHALLENGE 🏁")
    print("Race from Earth to Mars!")
    
    input("Press ENTER when ready...")
    print("3... 2... 1... GO! 🚀")
    
    # Random delay before green light
    time.sleep(random.uniform(0.5, 2.0))
    print("🟢 GO NOW!")
    start = time.time()
    input()
    reaction = time.time() - start
    
    print(f"Your time: {reaction:.2f} seconds")
    
    if reaction < 0.5:
        winnings = 1000
        print(f"🏆 AMAZING! +{winnings} credits!")
        credits_total += winnings
        check_achievement("speed_demon")
    elif reaction < 1.0:
        winnings = 500
        print(f"👍 Good job! +{winnings} credits!")
        credits_total += winnings
    else:
        print("😅 Keep practicing!")

def check_achievement(achievement_key):
    global achievements
    if achievement_key in achievement_list and achievement_key not in achievements:
        achievements.append(achievement_key)
        print(f"\n🏆 ACHIEVEMENT: {achievement_list[achievement_key]} 🏆\n")

def daily_bonus():
    global credits_total, fuel
    print("\n🎁 DAILY BONUS! 🎁")
    bonus_credits = random.randint(200, 800)
    bonus_fuel = random.randint(100, 300)
    credits_total += bonus_credits
    fuel += bonus_fuel
    print(f"✨ +{bonus_credits} credits | +{bonus_fuel} fuel")

def show_fun_fact():
    facts = ["Venus spins backwards","Mars sunsets are blue","Saturn could float in water","Jupiter is insanely huge","Neptune has crazy strong winds","A day on Venus is longer than a year there"]
    print(f"\n📚 {random.choice(facts)}")

def show_space_event():
    events = ["☄️ comet nearby","🌠 meteor shower","🛰️ deep space signal","👽 aliens watching","🪐 strange rings"]
    print(f"✨ {random.choice(events)}")

def random_space_weather():
    weather = ["☀️ solar calm","🌌 radiation normal","☄️ asteroid traffic high","🛰️ satellites fine","⚡ solar storm warning"]
    print(f"\n🌦️ {random.choice(weather)}")

def mission_status():
    missions = ["✅ mission complete","🚀 nav online","⚠️ fuel questionable","🌌 systems stable"]
    print(f"📡 {random.choice(missions)}")

def detect_black_hole():
    if random.randint(1,12) == 1:
        print("🕳️ ⚠️ BLACK HOLE NEARBY! ⚠️")
        global fuel
        fuel -= random.randint(50, 200)
    else:
        print("✅ No black holes")

def oxygen_level():
    print(f"🫁 Oxygen: {random.randint(70,100)}%")

def random_rank(distance):
    if distance>5000: print("🏆 Intergalactic Traveler")
    elif distance>3000: print("🏆 Galaxy Traveler")
    elif distance>1000: print("🏆 Space Explorer")
    elif distance>300: print("🏆 Orbit Runner")
    else: print("🏆 Moon Walker")

def random_galaxy(): print(f"🌌 Galaxy: {random.choice(galaxy_names)}")
def random_astronaut(): print(f"👨‍🚀 Astronaut: {random.choice(astronauts)}")
def random_spaceship(): print(f"🛸 Ship: {random.choice(spaceships)}")

def distance_category(distance):
    if distance<100: print("📍 Short trip")
    elif distance<1000: print("📍 Medium trip")
    elif distance<3000: print("📍 Long trip")
    else: print("📍 Extreme travel")

def random_signal():
    signals = ["📡 Strange signal","📡 Signal stable","📡 Communication delay","📡 Signal lost"]
    print(random.choice(signals))

def moon_phase():
    phases = ["🌕 Full moon","🌗 Half moon","🌑 New moon","🌙 Crescent moon"]
    print(random.choice(phases))

def crew_mood():
    moods = ["😄 Crew great","😴 Crew tired","🤖 Robots working","🧑‍🚀 Crew excited"]
    print(random.choice(moods))

def temperature_check(): print(f"🌡️ Temp: {random.randint(-150,120)}°C")
def danger_level(): print(random.choice(["🟢 Low danger","🟡 Medium","🟠 High","🔴 Critical"]))
def daily_space_tip(): print(random.choice(["💡 Double-check coordinates","💡 Keep fuel above 30%","💡 Avoid black holes","💡 Nebulae = fuel"]))
def random_space_pet(): 
    pet = random.choice(space_pets)
    print(f"🐾 Pet: {pet}")
    if random.random() < 0.1:
        inventory.append(pet)
        print(f"🎉 {pet} joined your crew!")
        check_achievement("pet_lover")
def random_badge(): 
    badge = random.choice(badges)
    print(f"🎖️ Badge: {badge}")
def signal_strength(): print(f"📶 Signal: {random.randint(40,100)}%")
def credits_display(): print(f"💰 Credits: {credits_total}")
def asteroid_scan(): print(f"🪨 Asteroids: {random.randint(0,12)}")
def alien_encounter(): 
    if random.randint(1,5) == 1:
        print(f"👽 ALIEN: {random.choice(alien_names)} wants to trade!")
        alien_trade()
    else:
        print("👽 No aliens")
def space_food(): print(f"🍔 Meal: {random.choice(space_foods)}")
def engine_status(): print(random.choice(["🛠️ Engines perfect","⚠️ Engine heat high","🚀 Boosters ready","🔧 Maintenance needed"]))
def warp_drive(): print(f"💫 Warp: {random.randint(10,100)}%")
def random_space_job(): print(f"🧑‍🚀 Role: {random.choice(space_jobs)}")
def planet_condition(): print(f"🪐 Planet: {random.choice(planet_conditions)}")
def shield_status(): print(f"🛡️ Shields: {random.randint(20,100)}%")
def laser_power(): print(f"🔫 Lasers: {random.randint(10,100)}%")
def gravity_level(): print(f"🌍 Gravity: {round(random.uniform(0.2,5.0),2)}G")

def show_all_fluff(distance):
    print("\n" + "="*50)
    random_space_weather()
    show_space_event()
    random_galaxy()
    random_astronaut()
    random_spaceship()
    distance_category(distance)
    random_rank(distance)
    random_signal()
    moon_phase()
    crew_mood()
    temperature_check()
    danger_level()
    daily_space_tip()
    random_space_pet()
    random_badge()
    signal_strength()
    credits_display()
    asteroid_scan()
    alien_encounter()
    space_food()
    engine_status()
    warp_drive()
    random_space_job()
    planet_condition()
    shield_status()
    laser_power()
    gravity_level()
    detect_black_hole()
    oxygen_level()
    mission_status()
    show_fun_fact()
    print("="*50)

def show_stats_dashboard():
    print("\n" + "="*50)
    print("🚀 SPACE COMMANDER STATS 🚀")
    print("="*50)
    print(f"📊 Missions: {total_calculations}")
    print(f"📜 History: {len(history)}")
    print(f"🏆 Record: {highest_distance:.2f} million km")
    print(f"🚀 Complete: {missions_completed}")
    print(f"⛽ Fuel: {fuel:.1f}")
    print(f"💰 Credits: {credits_total}")
    print(f"🎖️ Achievements: {len(achievements)}/{len(achievement_list)}")
    print(f"🎒 Items: {len(inventory)}")
    print(f"🔥 Streak: {consecutive_missions}")
    show_crew_status()
    
    if inventory:
        print("\n🎒 Recent items:")
        for item in inventory[-3:]:
            print(f"  • {item}")
    
    if achievements:
        print("\n🏆 Achievements:")
        for ach in achievements[-3:]:
            print(f"  • {achievement_list[ach]}")
    print("="*50)

def main():
    global total_calculations, highest_distance, missions_completed, fuel, credits_total, crew_morale
    
    print("\n" + "🌌" * 20)
    print("🚀 SPACE CALCULATOR - TODAY'S EDITION 🚀")
    print("🌌" * 20)
    print(random.choice(["Ready for launch!","Space awaits!","Calculate the stars!","Mission control ready!"]))
    
    today = datetime.now()
    print(f"📅 {today.strftime('%Y-%m-%d')} 🕒 {today.strftime('%H:%M:%S')}")
    
    daily_bonus()
    show_crew_status()
    
    while True:
        print("\n" + "="*35)
        print("MAIN MENU")
        print("="*35)
        print("1️⃣  Planets | 2️⃣  Custom")
        print("3️⃣  History | 4️⃣  Stats")
        print("5️⃣  Clear | 6️⃣  Nebula")
        print("7️⃣  Trade | 8️⃣  Race")
        print("9️⃣  Inventory | 0️⃣  Exit")
        
        mode = input("\n➡️ ")
        
        if mode == "3":
            print("\n📜 HISTORY:")
            for item in history[-8:]:
                print(f"  {item}")
            continue
            
        if mode == "4":
            show_stats_dashboard()
            continue
            
        if mode == "5":
            history.clear()
            print("🧹 Cleared!")
            continue
            
        if mode == "6":
            explore_nebula()
            continue
            
        if mode == "7":
            alien_trade()
            continue
            
        if mode == "8":
            space_race()
            continue
            
        if mode == "9":
            print("\n🎒 INVENTORY:")
            if inventory:
                for item in inventory[-8:]:
                    print(f"  • {item}")
            else:
                print("  Empty!")
            continue
            
        if mode == "0":
            print(f"\n👋 Final: {missions_completed} missions | {len(achievements)} achievements")
            print("🖖 Live long and prosper!")
            break
            
        if mode == "1":
            p1_name, p1, p2_name, p2 = choose_planets()
            distance = calculate_distance(p1, p2)
            
            # Random event can modify distance!
            event_modifier = trigger_random_event()
            original_distance = distance
            distance = distance * event_modifier
            
            if event_modifier != 1.0:
                print(f"📏 Distance changed: {original_distance:.0f} → {distance:.0f} million km")
            
            if not check_fuel(distance):
                print("❌ Mission aborted!")
                update_crew_morale(distance, success=False)
                continue
            
        elif mode == "2":
            print("\n✨ CUSTOM MODE ✨")
            p1_name = input("Start: ") or "Start"
            p2_name = input("Dest: ") or "Dest"
            p1 = get_coordinates(p1_name)
            p2 = get_coordinates(p2_name)
            distance = calculate_distance(p1, p2)
            
            event_modifier = trigger_random_event()
            if event_modifier != 1.0:
                distance = distance * event_modifier
            
            if not check_fuel(distance):
                print("❌ Mission aborted!")
                update_crew_morale(distance, success=False)
                continue
            
        else:
            print("❌ Choose 0-9")
            continue
        
        # Mission success!
        total_calculations += 1
        missions_completed += 1
        
        reward = int(distance * 0.5) + random.randint(50, 200)
        credits_total += reward
        print(f"💰 +{reward} credits!")
        
        if distance > highest_distance:
            highest_distance = distance
            print("\n🎉 NEW RECORD! 🎉")
            if distance > 2000:
                check_achievement("milky_way_tourist")
        
        print(f"\n{'='*45}")
        print(f"📍 {p1_name} → {p2_name}")
        print(f"📏 {distance:.2f} million km")
        print(f"{'='*45}")
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        history.append(f"[{timestamp}] {p1_name} → {p2_name}: {distance:.2f}M km")
        
        show_all_fluff(distance)
        update_crew_morale(distance, success=True)
        
        if missions_completed == 1:
            check_achievement("first_step")
        if missions_completed % 5 == 0:
            print(f"\n🎉 {missions_completed} missions! 🎉")
            print(random.choice(alien_greetings))
        
        if credits_total >= 10000:
            check_achievement("millionaire")
        if missions_completed >= 50:
            check_achievement("galaxy_legend")

if __name__ == "__main__":
    main()

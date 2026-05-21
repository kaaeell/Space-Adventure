import math
import random
import time
from datetime import datetime

history = []
total_calculations = 0
highest_distance = 0
missions_completed = 0

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
    print("\nAvailable planets:")
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

def show_fun_fact():
    facts = ["Venus spins backwards","Mars sunsets are blue","Saturn could float in water","Jupiter is insanely huge","Neptune has crazy strong winds","A day on Venus is longer than a year there"]
    print(f"\nfun fact: {random.choice(facts)}")

def show_space_event():
    events = ["☄️ comet detected nearby","🌠 meteor shower active","🛰️ signal received from deep space","👽 aliens definitely watching","🪐 strange rings detected nearby"]
    print(random.choice(events))

def random_space_weather():
    weather = ["☀️ solar activity calm today","🌌 radiation levels normal","☄️ asteroid traffic kinda high rn","🛰️ satellites working fine","⚡ solar storm warning active"]
    print(f"\nspace weather: {random.choice(weather)}")

def mission_status():
    missions = ["✅ mission completed successfully","🚀 navigation systems online","⚠️ fuel levels questionable","🌌 deep space systems stable"]
    print(random.choice(missions))

def detect_black_hole():
    chance = random.randint(1,12)
    if chance==1:
        print("🕳️ black hole detected nearby RUN")
    else:
        print("✅ no black holes nearby")

def oxygen_level():
    oxygen = random.randint(70,100)
    print(f"🫁 oxygen levels: {oxygen}%")

def random_rank(distance):
    if distance>5000: print("🏆 rank: intergalactic traveler")
    elif distance>3000: print("🏆 rank: galaxy traveler")
    elif distance>1000: print("🏆 rank: space explorer")
    elif distance>300: print("🏆 rank: orbit runner")
    else: print("🏆 rank: moon walker")

def random_galaxy(): print(f"🌌 nearby galaxy detected: {random.choice(galaxy_names)}")
def random_astronaut(): print(f"👨‍🚀 astronaut online: {random.choice(astronauts)}")
def random_spaceship(): print(f"🛸 active spaceship: {random.choice(spaceships)}")

def distance_category(distance):
    if distance<100: print("📍 category: super short trip")
    elif distance<1000: print("📍 category: medium trip")
    elif distance<3000: print("📍 category: long trip")
    else: print("📍 category: extreme space travel")

def random_signal():
    signals = ["📡 strange radio signal detected","📡 signal strength stable","📡 communication delay increased","📡 deep space signal lost briefly"]
    print(random.choice(signals))

def moon_phase():
    phases = ["🌕 full moon tonight","🌗 half moon detected","🌑 new moon phase active","🌙 crescent moon visible"]
    print(random.choice(phases))

def crew_mood():
    moods = ["😄 crew feeling great","😴 crew tired but working","🤖 robots handling repairs","🧑‍🚀 crew excited for mission"]
    print(random.choice(moods))

def temperature_check(): print(f"🌡️ nearby temperature: {random.randint(-150,120)}°C")
def danger_level(): print(random.choice(["🟢 danger level: low","🟡 danger level: medium","🟠 danger level: high","🔴 danger level: critical"]))
def daily_space_tip(): print(random.choice(["💡 tip: always double check coordinates","💡 tip: keep fuel above 30%","💡 tip: avoid black holes if possible","💡 tip: deep space signals can be delayed"]))
def random_space_pet(): print(f"🐾 companion detected: {random.choice(space_pets)}")
def random_badge(): print(f"🎖️ badge earned: {random.choice(badges)}")
def signal_strength(): print(f"📶 signal strength: {random.randint(40,100)}%")
def credits(): print(f"💰 space credits earned: {random.randint(100,5000)}")
def asteroid_scan(): print(f"🪨 asteroids nearby: {random.randint(0,12)}")
def alien_encounter(): print(f"👽 alien encounter with {random.choice(alien_names)}" if random.randint(1,5)==1 else "👽 no aliens contacted today")
def space_food(): print(f"🍔 crew meal today: {random.choice(space_foods)}")
def engine_status(): print(random.choice(["🛠️ engines running perfectly","⚠️ engine heat slightly high","🚀 boosters ready","🔧 engine maintenance recommended"]))
def warp_drive(): print(f"💫 warp drive power: {random.randint(10,100)}%")
def random_space_job(): print(f"🧑‍🚀 current crew role: {random.choice(space_jobs)}")
def planet_condition(): print(f"🪐 planet scan: {random.choice(planet_conditions)}")
def shield_status(): print(f"🛡️ shield power: {random.randint(20,100)}%")
def laser_power(): print(f"🔫 laser system power: {random.randint(10,100)}%")
def gravity_level(): print(f"🌍 gravity level: {round(random.uniform(0.2,5.0),2)}G")

def main():
    global total_calculations, highest_distance, missions_completed
    print("\n🌌 Space Distance Calculator")
    print(random.choice(["space calculator v13 ready","doing questionable space math","probably accurate enough","welcome back commander"]))
    today=datetime.now()
    print(f"📅 date: {today.strftime('%Y-%m-%d')} 🕒 time: {today.strftime('%H:%M:%S')}")
    while True:
        mode=input("\n1 planets | 2 custom | 3 history | 4 stats | 5 clear history: ").strip()
        if mode=="3":
            print("\nhistory:" if history else "no history yet")
            for item in history: print(item)
            continue
        if mode=="4":
            print(f"\n📊 total calculations: {total_calculations}\n📜 saved history count: {len(history)}\n🏆 highest distance recorded: {highest_distance:.2f} million

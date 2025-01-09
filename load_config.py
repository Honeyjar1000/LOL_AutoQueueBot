import yaml
import random

RANDOM_CHAMPIONS = [
    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Ambessa", "Amumu", "Anivia", "Annie", "Aphelios", 
    "Ashe", "Aurelion Sol", "Aurora", "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Briar", 
    "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", 
    "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", 
    "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern", "Janna", 
    "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "K'Sante", "Kai'Sa", "Kalista", "Karma", "Karthus", 
    "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", 
    "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", 
    "Master Yi", "Milio", "Miss Fortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", 
    "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", 
    "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton", 
    "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", 
    "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Smolder", "Sona", "Soraka", "Swain", 
    "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", 
    "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", 
    "Vel'Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear" "Warwick" "Wukong" "Xayah" "Xerath" 
    "Xin Zhao" "Yasuo" "Yone" "Yorick" "Yuumi" "Zac" "Zed" "Zeri" "Ziggs" "Zilean" "Zoe" "Zyra"
]


def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_champion_preference(role, attempts):
    config = load_config()
    
    if attempts == 0:
        top_champion = config.get('top_champion_preference')
        jungle_champion = config.get('jungle_champion_preference')
        mid_champion = config.get('mid_champion_preference')
        bot_champion = config.get('bot_champion_preference')
        support_champion = config.get('support_champion_preference')
    elif attempts == 1:
        top_champion = config.get('top_second_champion_preference')
        jungle_champion = config.get('jungle_second_champion_preference')
        mid_champion = config.get('mid_second_champion_preference')
        bot_champion = config.get('bot_second_champion_preference')
        support_champion = config.get('support_second_champion_preference')
    else:
        return random.choice(RANDOM_CHAMPIONS)

    if role == 'top':
        return top_champion
    elif role == 'jungle':
        return jungle_champion
    elif role == 'mid':
        return mid_champion
    elif role == 'bot':
        return bot_champion
    elif role == 'support':
        return support_champion
    

    


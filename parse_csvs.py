from utils import read_csv_rows_to_dict
from champion import Champion

RESOURCES_PATH = 'resources/'
TOP_CSV_PATH = RESOURCES_PATH + 'top.csv'
JG_CSV_PATH = RESOURCES_PATH + 'jg.csv'
MID_CSV_PATH = RESOURCES_PATH + 'mid.csv'
BOT_CSV_PATH = RESOURCES_PATH + 'bot.csv'
SUPP_CSV_PATH = RESOURCES_PATH + 'support.csv'
TRAITS_PATH = RESOURCES_PATH + 'traits.csv'
SYNERGIES_PATH = RESOURCES_PATH + 'synergies.csv'
FOILS_PATH = RESOURCES_PATH + 'foils.csv'

def assemble_champion_map():
    # read from the roles sheets, the traits, synergies, and foils csvs

    top_laners_player_data = read_csv_rows_to_dict(TOP_CSV_PATH)
    jg_player_data = read_csv_rows_to_dict(JG_CSV_PATH)
    mid_laners_player_data = read_csv_rows_to_dict(MID_CSV_PATH)
    bot_laners_player_data = read_csv_rows_to_dict(BOT_CSV_PATH)
    supp_player_data = read_csv_rows_to_dict(SUPP_CSV_PATH)
    traits = read_csv_rows_to_dict(TRAITS_PATH)
    synergies = read_csv_rows_to_dict(SYNERGIES_PATH)
    foils = read_csv_rows_to_dict(FOILS_PATH)

    traits = convert_from_csv_form_to_a_dictionary_of_lists(traits)
    synergies = convert_from_csv_form_to_a_dictionary_of_lists(synergies)
    foils = convert_from_csv_form_to_a_dictionary_of_lists(foils)
    
    champion_objs = {}

    top_laners  = {}
    junglers = {}
    mid_laners = {}
    bot_laners = {}
    supports = {}

    # Create Champion objs for Top Laners as necessary and add Top Laners to Top Lane Role Map
    for top_laner in top_laners_player_data:
        add_champion_to_role_map_and_champion_map(
            top_laner, 
            top_laners, 
            champion_objs, 
            traits[top_laner['Champion']], 
            synergies[top_laner['Champion']], 
            foils[top_laner['Champion']] 
            )

    # Create Champion objs for Junglers as necessary and add Junglers to Jungle Role Map
    for jungler in jg_player_data:
        add_champion_to_role_map_and_champion_map(
            jungler,
            junglers,
            champion_objs, 
            traits[jungler['Champion']], 
            synergies[jungler['Champion']], 
            foils[jungler['Champion']]
            )
    
    # Create Champion objs for Mid Laners as necessary and add Mid Laners to Mid Lane Role Map
    for mid_laner in mid_laners_player_data:
        add_champion_to_role_map_and_champion_map(
            mid_laner,
            mid_laners,
            champion_objs, 
            traits[mid_laner['Champion']], 
            synergies[mid_laner['Champion']], 
            foils[mid_laner['Champion']]
            )
    
    # Create Champion objs for Bot Laners as necessary and add Bot Laners to Bot Lane Role Map
    for bot_laner in bot_laners_player_data:
        add_champion_to_role_map_and_champion_map(
            bot_laner,
            bot_laners,
            champion_objs, 
            traits[bot_laner['Champion']], 
            synergies[bot_laner['Champion']], 
            foils[bot_laner['Champion']]
            )
    
    # Create Champion objs for Supports as necessary and add Supports to Support Role Map
    for support in supp_player_data:
        add_champion_to_role_map_and_champion_map(
            support,
            supports,
            champion_objs, 
            traits[support['Champion']], 
            synergies[support['Champion']], 
            foils[support['Champion']]
            )
    return champion_objs, top_laners, junglers, mid_laners, bot_laners, supports

def add_champion_to_role_map_and_champion_map(champion, role_map, champion_map, traits, synergies, foils):
    if champion['Champion'] not in champion_map:
        champion_object = Champion(
            #Champion Name
            champion['Champion'],
            #Damage Spread
            {
            "magic": int(champion['% Magic Damage']),
            "physical": int(champion['% Physical Damage'])
            },
            #Is Tank
            champion['is Tank?'],
            #Has Engage
            champion['Has Engage?'],
            #Damage Scaling Factor,
            int(champion['Damage Scaling Factor']),
            #Traits
            set(traits),
            #Synergies
            set(synergies),
            #Foils
            set(foils)
        )
        champion_map[champion['Champion']] = champion_object
    role_map[champion['Champion']] = { 
            "skill": int(champion['Skill Level']),
            "happiness": int(champion['Happiness Level']),
            "matchup_spread": int(champion['Matchup Variance'])
    }
    

def convert_from_csv_form_to_a_dictionary_of_lists(feature_dict):
    feature_mapped_to_champion_names = {}
    for champion in feature_dict:
        feature_mapped_to_champion_names[champion['Champion']] = []
        for feature_key in champion:
            if feature_key == 'Champion' or champion[feature_key] is None or champion[feature_key] == '':
                pass
            else:
                feature_mapped_to_champion_names[champion['Champion']].append(champion[feature_key])
    return feature_mapped_to_champion_names
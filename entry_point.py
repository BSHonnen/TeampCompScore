import csv
from parse_csvs import assemble_champion_map
from comp import Comp
from four_drops import calculate_combinations_of_four
from sort_comps import sort_comps_into_combos_of_four
from filter import filter_out_bottom

def build_comps(top_laners, junglers, mid_laners, bot_laners, supports):
    comps = []
    for top_laner in top_laners:
        for jungler in junglers:
            for mid_laner in mid_laners:
                for bot_laner in bot_laners:
                    for support in supports:
                        comp = [top_laner, jungler, mid_laner, bot_laner, support]
                        if there_are_duplicate_champions(comp):
                            pass
                        else:
                            comps.append(comp)
    return comps


def there_are_duplicate_champions(comp):
    if len(comp) == len(set(comp)):
        return False
    else:
        return True


champion_objs, top_laners, junglers, mid_laners, bot_laners, supports = assemble_champion_map()
comps = build_comps(top_laners, junglers, mid_laners, bot_laners, supports)   
analyzed_comps = []
#[top_laner, jungler, mid_laner, bot_laner, support]
for comp in comps:
    sum_of_skill = top_laners[comp[0]]['skill'] + junglers[comp[1]]['skill'] + mid_laners[comp[2]]['skill']+bot_laners[comp[3]]['skill']+supports[comp[4]]['skill']
    sum_of_happiness = top_laners[comp[0]]['happiness'] + junglers[comp[1]]['happiness'] + mid_laners[comp[2]]['happiness']+bot_laners[comp[3]]['happiness']+supports[comp[4]]['happiness']
    sum_of_matchups = top_laners[comp[0]]['matchup_spread'] + junglers[comp[1]]['matchup_spread'] + mid_laners[comp[2]]['matchup_spread']+bot_laners[comp[3]]['matchup_spread']+supports[comp[4]]['matchup_spread']
    comp_under_analysis = Comp(
        champion_objs[comp[0]],
        champion_objs[comp[1]],
        champion_objs[comp[2]],
        champion_objs[comp[3]],
        champion_objs[comp[4]],
        sum_of_happiness,
        sum_of_skill,
        sum_of_matchups
        )
    analyzed_comps.append(comp_under_analysis)

champion_names = [top_laners,junglers,mid_laners,bot_laners,supports]

combos_of_four = calculate_combinations_of_four(champion_names)

sort_comps_into_combos_of_four(combos_of_four, analyzed_comps)

bottom_of_analyzed_comps = filter_out_bottom(combos_of_four, champion_names)

bad_comps = []

for groups_of_bottom in bottom_of_analyzed_comps:
    for comp in groups_of_bottom:
        bad_comps.append(comp)

bad_comps = list(set(bad_comps))

analyzed_comps = list(set(analyzed_comps))

for bad_comp in bad_comps:
    if bad_comp in analyzed_comps:
        analyzed_comps.remove(bad_comp)

analyzed_comps = sorted(analyzed_comps, key=lambda x: -int(x.total_synergy_score))

monolithic_csv_string = 'TOP,JUNGLE,MID,BOT,SUPPORT,DAMAGE_SPREAD,SYNERGY_SCORE, MATCHUP, SKILL, HAPPINESS\n'
for analyzed_comp in analyzed_comps:
    monolithic_csv_string += analyzed_comp.top.name + ',' + analyzed_comp.jg.name + ',' + analyzed_comp.mid.name + ',' + analyzed_comp.bot.name + ',' + analyzed_comp.support.name + ',' + 'M'+ str(analyzed_comp.magic_damage) +'/P'+ str(analyzed_comp.physical_damage) + ',' + str(analyzed_comp.total_synergy_score) + ',' + str(analyzed_comp.matchup) + ',' + str(analyzed_comp.skill) + ',' + str(analyzed_comp.happiness) + '\n'
text_file = open("output.csv", "w")
n = text_file.write(monolithic_csv_string)
text_file.close()
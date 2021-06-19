def sort_comps_into_combos_of_four(combos_of_four_hash_table, list_of_champs):
    for comp in list_of_champs:
        comp_1 = comp.top.name+","+comp.jg.name+","+comp.mid.name+","+comp.bot.name
        comp_2 = comp.jg.name+","+comp.mid.name+","+comp.bot.name+","+comp.support.name
        comp_3 = comp.top.name+","+comp.mid.name+","+comp.bot.name+","+comp.support.name
        comp_4 = comp.top.name+","+comp.jg.name+","+comp.bot.name+","+comp.support.name
        comp_5 = comp.top.name+","+comp.jg.name+","+comp.mid.name+","+comp.support.name
        
        comp_1_ranked_list = combos_of_four_hash_table.get_val(comp_1)
        comp_2_ranked_list = combos_of_four_hash_table.get_val(comp_2)
        comp_3_ranked_list = combos_of_four_hash_table.get_val(comp_3)
        comp_4_ranked_list = combos_of_four_hash_table.get_val(comp_4)
        comp_5_ranked_list = combos_of_four_hash_table.get_val(comp_5)

        comp_1_ranked_list.append(comp)
        comp_2_ranked_list.append(comp)
        comp_3_ranked_list.append(comp)
        comp_4_ranked_list.append(comp)
        comp_5_ranked_list.append(comp)

        combos_of_four_hash_table.set_val(comp_1, comp_1_ranked_list)
        combos_of_four_hash_table.set_val(comp_2, comp_2_ranked_list)
        combos_of_four_hash_table.set_val(comp_3, comp_3_ranked_list)
        combos_of_four_hash_table.set_val(comp_4, comp_4_ranked_list)
        combos_of_four_hash_table.set_val(comp_5, comp_5_ranked_list)

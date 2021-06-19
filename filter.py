def filter_out_bottom(combos_of_four, list_of_champions):
    final_list = []
    for i in range(len(list_of_champions)):
        restricted_list = list_of_champions.copy()
        restricted_list.pop(i)
        #  print(restricted_list)
        for i in restricted_list[0]:
            for j in restricted_list[1]:
                for k in restricted_list[2]:
                    for p in restricted_list[3]:
                        key_to_map = i+","+j+","+k+","+p
                        ranked_list = combos_of_four.get_val(key_to_map)
                        if ranked_list is None or ranked_list == []:
                            pass
                        else:
                            ranked_list_sorted = sorted(ranked_list, key=lambda x: -int(x.total_synergy_score))
                            ranked_list_slice = ranked_list_sorted[5:]
                            final_list.append(ranked_list_slice)

    return final_list
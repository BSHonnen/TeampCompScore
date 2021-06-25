from HashTable import HashTable

def calculate_combinations_of_four(list_of_lists_len_5):
    four_drops = HashTable(3000000)
    all_lists = []
    for i in range(len(list_of_lists_len_5)):
        restricted_list = list_of_lists_len_5.copy()
        restricted_list.pop(i)
        for i in restricted_list[0]:
            for j in restricted_list[1]:
                for k in restricted_list[2]:
                    for p in restricted_list[3]:
                        four_drops.set_val(i+","+j+","+k+","+p, [])
    return four_drops
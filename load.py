import csv
from HashMap import HashTable

with open('output.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

def get_synergy_score(data):
    return int(data[6])

# data.sort(key=get_synergy_score, reverse=True)

# file = open('output.csv', 'w+', newline ='')
  
# # writing the data into the file
# with file:    
#     write = csv.writer(file)
#     write.writerows(data)

top_champs = ["Riven", "Gwen", "Mordekaiser", "Wukong", "Camille","Shen","Gragas","Renekton","Nasus","Lee Sin","Yasuo","Irelia","Nocturne","Fiora"]
jg_champs = ["Evelynn","Diana","Xin Zhao","Fiddlesticks","Kyan (Blue)","Kayn (Red)","Nocturne","Skarner","Vi","J4","Volibear","Hecarim","Taliyah","Poppy","Elise"]
mid_champs = ["Yone","Sylas","Sett","Galio","Pantheon","Yasuo","Akali","Seraphine","Diana","Ryze","Cassiopeia","Zilean","Kassadin","J4","Lee Sin","Tristana","Lucian","Viego","Nocturne"]
bot_champs = ["Jinx","Xayah","Kai'sa","Miss Fortune","Ezreal","Sivir","Ashe","Jhin","Vayne","Tristana","Ziggs"]
supp_champs = ["Leona","Braum","Nautilus","Rakan","Rell","Alistar","Blitzcrank","Gragas","Pantheon","Shen","Taric","Brand","Maokai","Lulu","Sett","Poppy","Thresh"]

lists = [top_champs,jg_champs,mid_champs,bot_champs,supp_champs]

four_drops = HashTable(255000)
all_lists = []
for i in range(len(lists)):
  restricted_list = lists.copy()
  restricted_list.pop(i)
#  print(restricted_list)
  for i in restricted_list[0]:
    for j in restricted_list[1]:
       for k in restricted_list[2]:
         for p in restricted_list[3]:
            four_drops.set_val(i+","+j+","+k+","+p, [])

for comp in data:
    comp_1 = comp[0]+","+comp[1]+","+comp[2]+","+comp[3]
    comp_2 = comp[1]+","+comp[2]+","+comp[3]+","+comp[4]
    comp_3 = comp[0]+","+comp[2]+","+comp[3]+","+comp[4]
    comp_4 = comp[0]+","+comp[1]+","+comp[3]+","+comp[4]
    comp_5 = comp[0]+","+comp[1]+","+comp[2]+","+comp[4]
    
    comp_1_ranked_list = four_drops.get_val(comp_1)
    comp_2_ranked_list = four_drops.get_val(comp_2)
    comp_3_ranked_list = four_drops.get_val(comp_3)
    comp_4_ranked_list = four_drops.get_val(comp_4)
    comp_5_ranked_list = four_drops.get_val(comp_5)

    comp_1_ranked_list.append(comp)
    comp_2_ranked_list.append(comp)
    comp_3_ranked_list.append(comp)
    comp_4_ranked_list.append(comp)
    comp_5_ranked_list.append(comp)

    four_drops.set_val(comp_1, comp_1_ranked_list)
    four_drops.set_val(comp_2, comp_2_ranked_list)
    four_drops.set_val(comp_3, comp_3_ranked_list)
    four_drops.set_val(comp_4, comp_4_ranked_list)
    four_drops.set_val(comp_5, comp_5_ranked_list)

final_list = []
for i in range(len(lists)):
  restricted_list = lists.copy()
  restricted_list.pop(i)
#  print(restricted_list)
  for i in restricted_list[0]:
    for j in restricted_list[1]:
       for k in restricted_list[2]:
         for p in restricted_list[3]:
            key_to_map = i+","+j+","+k+","+p
            ranked_list = four_drops.get_val(key_to_map)
            if ranked_list is None or ranked_list == []:
                pass
            else:
                ranked_list_sorted = sorted(ranked_list, key=lambda x: -int(x[6]))
                top_5 = (tuple(t) for t in ranked_list_sorted[:5])
                final_list.append(top_5)

final_list_no_dupes = list(set(final_list))

final_final_list = [list(t) for t in final_list_no_dupes]

file = open('output2.csv', 'w+', newline ='')
  

with file:    
    write = csv.writer(file)
    write.writerows(final_final_list)



class Comp:
    def __init__(self, top, jg, mid, bot, support, happiness, skill, matchup):
        self.top = top
        self.jg = jg
        self.mid = mid
        self.bot = bot
        self.support = support
        self.comp = [top, jg, mid, bot, support]
        self.happiness = happiness
        self.skill = skill
        self.matchup = matchup
        self.analyze()

    def iterate_comp_and_initialize_metrics(self):
        self.number_of_tanks = 0
        self.number_of_engages = 0
        self.magic_damage = 0
        self.physical_damage = 0
        for champion in self.comp:
            if champion.is_tank:
                self.number_of_tanks += 1
            if champion.has_engage:
                self.number_of_engages += 1
            self.magic_damage += champion.damage_spread["magic"] * champion.damage_scaling
            self.physical_damage += champion.damage_spread["physical"] * champion.damage_scaling
        self.magic_damage = self.magic_damage/5
        self.physical_damage = self.physical_damage/5
    
    def pairwise_analysis(self):
        self.top_jg_synergies = self.compare_champions(self.top, self.jg)
        self.top_mid_synergies = self.compare_champions(self.top, self.mid)
        self.top_bot_synergies = self.compare_champions(self.top, self.bot)
        self.top_support_synergies = self.compare_champions(self.top, self.support)
        self.jg_mid_synergies = self.compare_champions(self.jg, self.mid)
        self.jg_bot_synergies = self.compare_champions(self.jg, self.bot) 
        self.jg_support_synergies = self.compare_champions(self.jg, self.support)
        self.mid_bot_synergies = self.compare_champions(self.mid, self.bot)
        self.mid_support_synergies = self.compare_champions(self.mid, self.support)
        self.bot_support_synergies = self.compare_champions(self.bot, self.support)
    
    def compare_champions(self, champ1, champ2):

        synergies_1 = champ1.traits.intersection(champ2.synergies)
        synergies_2 = champ2.traits.intersection(champ1.synergies)
        synergies = synergies_1 | synergies_2

        foils_1 = champ1.traits.intersection(champ2.foils)
        foils_2 = champ2.traits.intersection(champ1.foils)
        foils = foils_1 | foils_2

        synergy_score = len(synergies) - len(foils)

        return {"synergies": synergies, "foils": foils, "synergy_score": synergy_score}

    def calculate_total_synergy_score(self):
        self.total_synergy_score = self.top_jg_synergies["synergy_score"] + self.top_mid_synergies["synergy_score"] + self.top_bot_synergies["synergy_score"] + self.top_support_synergies["synergy_score"] + self.jg_mid_synergies["synergy_score"] + self.jg_bot_synergies["synergy_score"] + self.jg_support_synergies["synergy_score"] + self.mid_bot_synergies["synergy_score"] + self.mid_support_synergies["synergy_score"] + self.bot_support_synergies["synergy_score"]

    def analyze(self):
        self.iterate_comp_and_initialize_metrics()
        self.pairwise_analysis()
        self.calculate_total_synergy_score()
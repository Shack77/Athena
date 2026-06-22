from scenarios import SCENARIOS
import random

class ScenarioManager:

    def get_random_scenario(self):
        return random.choice(SCENARIOS)

    def get_all_scenarios(self):
        return SCENARIOS
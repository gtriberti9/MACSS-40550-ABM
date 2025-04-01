from mesa import Model
from agents import ConwayAgent
from mesa.space import SingleGrid

class ConwayModel(Model):
    def __init__(self, width = 100, height = 100, start_alive = 0.3, seed = None):
        super().__init__(seed = seed)

        # modify the grid so that the edges of the space do not wrap around.
        # for this change torus = True for False
        self.grid = SingleGrid(width, height, torus = False)
        for cont, (x, y) in self.grid.coord_iter():
            conway = ConwayAgent(self, (x, y))
            if self.random.random() < start_alive:
                conway.state = 1
            else:
                conway.state = 0
            self.grid.place_agent(conway, (x, y))
        self.running = True

    def step(self):
        self.agents.do("determine_next_state")
        self.agents.do("live_or_die") 

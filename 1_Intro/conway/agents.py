from mesa import Agent

class ConwayAgent(Agent):
    def __init__(self, model, pos, state = 0):
        super().__init__(model)
        # position
        self.x, self.y = pos
        self.state = None
        self.new_state = None

    def determine_next_state(self):

        # moore = True. For von-neuman neigborhoods moore = False
        live_neighbors = sum(neighbor.state for neighbor in self.model.grid.iter_neighbors((self.x, self.y), moore=False))
        # if self state is alive
        # if self.state == 1:
        #     # if it has different from 2 or 3 neighbors alive
        #     if live_neighbors < 2 or live_neighbors > 3:
        #         # it dies
        #         self.new_state = 0
        #     # else, remain alive
        #     else: self.new_state = 1

        ###### Change
        if self.state == 1:
            # Survive if 1 or 2 neighbors are alive
            if live_neighbors in [1, 2]:
                self.new_state = 1
            else:
                self.new_state = 0
        
        # if not alive
        else:
            # and has 3 neighbors alive
            # change for 2 neighbors
            if live_neighbors == 2:
                # revive
                self.new_state = 1
            else:
                # not alive
                self.new_state = 0

    # Determine the new state of the cell            
    def live_or_die(self):
        self.state = self.new_state
        

from mesa import Agent
import random

class SchellingAgent(Agent):
    ## Initiate agent instance, inherit model trait from parent class
    def __init__(self, model, agent_type):
        super().__init__(model)
        ## Set agent type
        self.type = agent_type
        self.threshold = random.randint(0, 1)
    ## Define basic decision rule
    def move(self):
        ## Get list of neighbors within range of sight
        neighbors = self.model.grid.get_neighbors(
            self.pos, moore=True, radius = self.model.radius, include_center = False)
        ## Count neighbors of same type as self
        similar_neighbors = sum(1 for neighbor in neighbors if self.type == neighbor.type)
        ## If an agent has any neighbors (to avoid division by zero), calculate share of neighbors of same type
        if neighbors:
            share_alike = similar_neighbors / len(neighbors)
        else:
            share_alike = 0
        ## If unhappy with neighbors, move to random empty slot. Otherwise add one to model count of happy agents.
        #if share_alike < self.model.desired_share_alike:
        if share_alike < self.threshold:
            self.model.grid.move_to_empty(self)
        else: 
            self.model.happy += 1     


# Maybe creating a different type of agent where some of them will like living with others
# and having a lower rate of share_alike can be better

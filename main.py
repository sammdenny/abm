# -*- coding: utf-8 -*-
"""
Spyder Editor

Phase 1:
create agent class
define agent attributes - position, selected neighbors
place agents on grid
agents need to be able to know about all neighbors
randomly choose two
use pythagorus to determine distance from each

Move:
    determine options for positions to move to
    agents cant move to an occupied space 

"""

# set up agent class

import random 


class Room():
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        
        self.agent_list = []

        
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    
    # list of agents in the room
    def add_agent(self, agent):
        self.agent_list.append(agent)
        
    
    def get_agent_list(self):
        return self.agent_list
    

    def print_agents(self):
        for agent in self.agent_list:
            print(str(agent))




class Agent():
    
    def __init__(self, room, identifier):
        
        self.room = room
        self.identifier = identifier
        
        # tell room about agent, add to list
        room.add_agent(self)


        # set initial coordinates off grid
        self.x = -1
        self.y = -1
        
        
    

        # set real starting position for agents
        occupied = True # assume occupied in order to generate 'new' coordinates
        while(occupied):
            destination_x = random.randint(0,self.room.get_width())
            destination_y = random.randint(0,self.room.get_height())
            
            occupied = self.is_occupied(destination_x, destination_y)
        
        # if destination location unoccupied, move there 
        self.x = destination_x
        self.y = destination_y


        # empty list for chosen neighbors
        self.chosen_neighbors = []
     

    
    # check whether location is already occupied by an agent
    def is_occupied(self, d_x, d_y):
        for agent in self.room.agent_list:
            if d_x == agent.x and d_y == agent.y:
                return True           
        return False
             
         
    def __str__(self):
        
        return(str(self.x) + ',' + str(self.y) + ' Neighbor 1: ' + 
               str(self.chosen_neighbors[0].identifier) + ' Neighbor 2: ' + 
                      str(self.chosen_neighbors[1].identifier))
        
 
    def choose_neighbors(self):
        neighbors = []
        neighbors.append(random.sample(room.agent_list, 2))
        self.chosen_neighbors.append(neighbors[0][0])
        self.chosen_neighbors.append(neighbors[0][1])
        
  
 

    def calculate_distance(self, neighbor):
        # calculate distance between self and each chosen neighbor
        return (((self.x - neighbor.x)**2) + ((self.y - neighbor.y)**2)**0.5)
        

        
    def move(self):
        # move to an adjacent cell that gets agent closer to equal distance
'''       





# main

room = Room(10, 5)


num_of_agents = 4


for i in range(num_of_agents):
    Agent(room, i)
    

agents = room.get_agent_list()

for agent in agents:
    agent.choose_neighbors()




room.print_agents()

















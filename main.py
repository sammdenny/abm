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
     
        # empty list for possible moves
        self.possible_moves = []
        
    
    # check whether location is already occupied by an agent
    def is_occupied(self, d_x, d_y):
        for agent in self.room.agent_list:
            if d_x == agent.x and d_y == agent.y:
                return True           
        return False
             
         
    def __str__(self):
        
        distances = self.agent_calculate_difference()
        
        return(str(self.x) + ',' + str(self.y) + ' Neighbor 1: ' + 
               str(self.chosen_neighbors[0].identifier) + ' Distance 1: ' + 
               str(distances[0]) + 
               ' Neighbor 2: ' + str(self.chosen_neighbors[1].identifier) +
               ' Distance 2: ' + 
               str(distances[1]) + 
               ' Difference: ' + str(distances[2]))
        
 
    def choose_neighbors(self):
        # remove self from list
        other_list = room.agent_list.copy()
        other_list.remove(self)
        
        # empty list for neighbors
        neighbors = []
        
        # randomly choose two neighbors
        neighbors.append(random.sample(other_list, 2))
        
        self.chosen_neighbors.append(neighbors[0][0])
        self.chosen_neighbors.append(neighbors[0][1])
 
        
    
    def agent_calculate_distance(self, neighbor):
        return(self.move_calculate_distance(neighbor, self.x, self.y))
    

    def move_calculate_distance(self, neighbor, x, y):
        # calculate distance between self and each chosen neighbor
        distance = (( ((x - neighbor.x)**2) + ((y - neighbor.y)**2) ) **0.5)
        return(distance)
    
    


    def agent_calculate_difference(self):
       return(self.move_calculate_difference(self.x, self.y))
        
    def move_calculate_difference(self, x, y):
       distance_1 = self.move_calculate_distance(self.chosen_neighbors[0], x, y)
       distance_2 = self.move_calculate_distance(self.chosen_neighbors[1], x, y)
      
       return([distance_1, distance_2, abs(distance_1 - distance_2)])




    def get_possible_moves(self):
    
        if self.x > 0:
            self.possible_moves.append((self.x-1, self.y))
            
        if self.x < room.get_width():
            self.possible_moves.append((self.x+1, self.y))
            
        if self.y > 0:
            self.possible_moves.append((self.x, self.y-1))
            
        if self.y < room.get_height():
            self.possible_moves.append((self.x, self.y+1))  




    def move(self):
        move_counter = 0
        
        
        possible_moves = self.get_possible_moves()
'''        
        if current_difference > 1:
            for move in possible_moves:
'''               
                
          





'''        

            
        

        
    def move(self):
        move_counter = 0
        
        # move to an adjacent cell that gets agent closer to equal distance
        distance_1 = self.calculate_distance(self.chosen_neighbors[0])
        distance_2 = self.calculate_distance(self.chosen_neighbors[1])
        
        possible_moves = self.get_possible_moves()
        
        current_difference = abs(distance_1 - distance_2)
        
        if current_difference > 1:
            for move in possible_moves:
                new_distance_1 = move.calculate_distance(self.chosen_neighbors[0])
                new_distance_2 = move.calculate_distance(self.chosen_neighbors[1])
                new_difference = abs(new_distance_1 - new_distance_2)
                if move.calculate_distance()
            
            
'''       






# main

room = Room(10, 5)


num_of_agents = 3


for i in range(num_of_agents):
    Agent(room, i)
    

agents = room.get_agent_list()

for agent in agents:
    agent.choose_neighbors()


for agent in agents:
    agent.get_possible_moves()
    
for agent in agents:
    agent.move()


room.print_agents()

















# -*- coding: utf-8 -*-
"""
Spyder Editor

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
        # empty list for possible moves
        possible_moves = []
        
        if self.x > 0:
            possible_moves.append([self.x-1, self.y])
            
        if self.x < room.get_width():
            possible_moves.append([self.x+1, self.y])
            
        if self.y > 0:
            possible_moves.append([self.x, self.y-1])
            
        if self.y < room.get_height():
            possible_moves.append([self.x, self.y+1])  

        # need to add in check if occupied

        return(possible_moves)



    def move(self):
        
        current_difference = self.agent_calculate_difference()[2]
        
        possible_moves = self.get_possible_moves()
     
        if current_difference > 0.5:
            for move in possible_moves:
                new_difference = self.move_calculate_difference(move[0],move[1])
                if new_difference[2] < current_difference:
                    self.x = move[0]
                    self.y = move[1]
                    return True
            return False
                
            




# main
import matplotlib.pyplot as plt 

room = Room(10, 5)

num_of_agents = 5


for i in range(num_of_agents):
    Agent(room, i)
    

agents = room.get_agent_list()

for agent in agents:
    agent.choose_neighbors()

room.print_agents()

plt.xlim(0, room.get_width())
plt.ylim(0, room.get_height())


end = False

while not end:
    
    for agent in agents:
        agent.get_possible_moves()
    
    
    end = True
    for agent in agents:
        has_moved = agent.move()
        if has_moved:
            end = False
        

    room.print_agents()
    


    for i in range(num_of_agents):
        plt.scatter(agents[i].x, agents[i].y)
    
    plt.show()













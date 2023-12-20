# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

# set up agent class

import random 
import numpy


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
        
        return(str(self.x) + ',' + str(self.y) + '  (' + 
               str(self.chosen_neighbors[0].x) + ',' + str(self.chosen_neighbors[0].y) + 
               ' , ' + str(self.chosen_neighbors[1].x) + ',' + str(self.chosen_neighbors[1].y) + ') '
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
        
        possible_moves = []
        # create local variables from methods to reuse
        w = room.get_width()
        h = room.get_height()
        
        # get 9 possible locations, remove off grid and occupied locations
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                temp_x = self.x + i
                temp_y = self.y + j
                if temp_x >= 0 and temp_x < w and temp_y >= 0 and temp_y < h and not self.is_occupied(temp_x, temp_y):
                    possible_moves.append([self.x + i, self.y + j])

        return(possible_moves)    




    def move(self):
        current_difference = self.agent_calculate_difference()[2]
        # margin of error for difference
        if current_difference <= 0.5:
            return False
        
        move_list = self.get_possible_moves()
        # if no valid moves exit
        if len(move_list) == 0:
            return False
        
        # list of new differences
        difference_list = []
        
        for move in move_list:
            new_difference = self.move_calculate_difference(move[0],move[1])
            difference_list.append(new_difference[2])

        # index for smallest difference    
        i = numpy.argmin(difference_list)
        
        best_move_difference = difference_list[i]
        
        # if best move better than current location then move                      
        if best_move_difference < current_difference:
            self.x = move_list[i][0]
            self.y = move_list[i][1]
          
            return True
        return False
                
            







# main
import matplotlib.pyplot as plt 

room = Room(25, 25)

num_of_agents = 10


for i in range(num_of_agents):
    Agent(room, i)
    

agents = room.get_agent_list()

for agent in agents:
    agent.choose_neighbors()

room.print_agents()

# set plot axes
w = room.get_width()
h = room.get_height()



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
    
    
    plt.xlim(0, w)
    plt.ylim(0, h)
    plt.show()













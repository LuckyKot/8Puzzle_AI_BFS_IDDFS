from queue import Queue
from queue import LifoQueue
import copy
import time

#Chain() class (chain because it has previous states list with "chaining" solution)
#each object holds current state (3x3 list), previous_states list that keeps all performed moves so far
#steps, the number of steps performed from initial state
#and initial state from the very beginning needed to assemble the solution in the end
class chain:
    def __init__(self,data,steps,init_state):
        self.data=data
        self.previous_states=[]
        self.steps=steps
        self.init_state=init_state
    
    def __del__(self):
        self.data=[]
        self.previous_states=[]
        self.steps=0
        
    def set_state(self,data):
        self.data=data
    
    def set_previous_states(self,previous_states):
        self.previous_states=copy.deepcopy(previous_states)        
    
    def append_previous_states(self,previous_states):
        self.previous_states.append(previous_states)
    
    def set_steps(self,steps):
        self.steps=steps
        
    def get_state(self):
        return self.data
    
    def get_previous_states(self):
        return self.previous_states
    
    def get_steps(self):
        return self.steps
    
    def get_init_state(self):
        return self.init_state
    
#helps transform 2d list to a string for the dictionary
def to_string(data):
    temp=''
    for i in data:
        for j in i:
            temp = temp+j
    return temp

#heler functions that perform the moves
#swaps 0 based on its coordinates
#also leaves a direction for the previous_states list
def move_up(data,zero_i,zero_j):
    direction='U'
    temp_data = copy.deepcopy(data.get_state())
    temp=temp_data[zero_i-1][zero_j]
    temp_data[zero_i-1][zero_j]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data,direction

def move_left(data,zero_i,zero_j):
    direction='L'
    temp_data = copy.deepcopy(data.get_state())
    temp=temp_data[zero_i][zero_j-1]
    temp_data[zero_i][zero_j-1]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data,direction

def move_right(data,zero_i,zero_j):
    direction='R'
    temp_data = copy.deepcopy(data.get_state())
    temp=temp_data[zero_i][zero_j+1]
    temp_data[zero_i][zero_j+1]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data,direction

def move_down(data,zero_i,zero_j):
    direction='D'
    temp_data = copy.deepcopy(data.get_state())
    temp=temp_data[zero_i+1][zero_j]
    temp_data[zero_i+1][zero_j]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data,direction



#the most important function
#determines the legal moves and then makes them
#takes chain objects as data, the dictionary as discovered_states, the queue as q and the dfs flag
#performes different actions that are more appropriate to DFS or BFS
#UPDATE - after changing dfs function DFS mode for actions() only slows it down
#use with false only
#improves performance for both (in terms of time)
#overall this function extremely inefficient due to repeating code, but it is very effective
def actions(data,discovered_states,q,dfs):
    temp=[]
    temp_dir=''
    #find zero, needed to determine legal moves and commit moves themselves
    for i in range(3):
        if '0' in data.get_state()[i]:
            zero_i=i
            for j in range(3):
                if data.get_state()[i][j]=='0':
                    zero_j=j
                    
    
    if zero_i != 0 and zero_i !=2 and zero_j != 0 and zero_j !=2:
            temp,temp_dir=move_up(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            temp,temp_dir=move_right(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            temp,temp_dir=move_down(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            temp,temp_dir=move_left(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
    if zero_i == 0:
        if zero_j == 0:
        #down        
            
            temp,temp_dir=move_down(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)
                
                q.put(tempdata)
                 
                del tempdata
                
        #right
            temp,temp_dir=move_right(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
                
        elif zero_j == 2:
        #down
            temp,temp_dir=move_down(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        #left
            temp,temp_dir=move_left(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        else:
        #left
            temp,temp_dir=move_left(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        #down
            temp,temp_dir=move_down(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        #right
            temp,temp_dir=move_right(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        
    elif zero_i == 2:
        if zero_j == 0:
        #up 
            temp,temp_dir=move_up(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        #right
            temp,temp_dir=move_right(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        elif zero_j == 2:
        #left
            temp,temp_dir=move_left(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        #up
            temp,temp_dir=move_up(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        else:
            #left
            temp,temp_dir=move_left(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())

                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)                
                 
            #right
            temp,temp_dir=move_right(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())

                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)


                q.put(tempdata)
                 
            #up
            temp,temp_dir=move_up(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())

                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)


                q.put(tempdata)
                 
    if zero_j == 0:
        if zero_i == 0:
            #down
            temp,temp_dir=move_down(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
                #right
            temp,temp_dir=move_right(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        elif zero_i == 2:
            #up
            temp,temp_dir=move_up(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            #right
            temp,temp_dir=move_right(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        else:
            #up
            temp,temp_dir=move_up(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            #down
            temp,temp_dir=move_down(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            #right
            temp,temp_dir=move_right(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
    elif zero_j == 2:
        if zero_i == 0:
            #down
            temp,temp_dir=move_down(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)
                 
                q.put(tempdata)
                 
            #left
            temp,temp_dir=move_left(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)
                 
                q.put(tempdata)
                 
        elif zero_i == 2:
            #up
            temp,temp_dir=move_up(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            #left
            temp,temp_dir=move_left(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
        else:
            #up
            temp,temp_dir=move_up(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            #down
            temp,temp_dir=move_down(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
            #left
            temp,temp_dir=move_left(data,zero_i,zero_j)
            state=to_string(temp)
            try:
                discovered_states[state]
                if dfs==True:
                    if data.get_steps() not in discovered_states[state]:
                        discovered_states[state].append(data.get_steps())
                        tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                        temp=copy.deepcopy(data.get_previous_states())
                        temp.append(temp_dir)
                        tempdata.set_previous_states(temp)

                        q.put(tempdata)
                         
            except:
                if dfs == True:
                    discovered_states[state]=[]
                    discovered_states[state].append(data.get_steps())
                else:
                    discovered_states[state]=0
                tempdata=chain(temp,data.get_steps()+1,data.get_init_state())
                temp=copy.deepcopy(data.get_previous_states())
                temp.append(temp_dir)
                tempdata.set_previous_states(temp)

                q.put(tempdata)
                 
    

    del temp

#Iterative_deepening_DFS() implementation. takes 2 2d lists 3x3 as input
#one is initial state and another is goal state
def Iterative_deepening_DFS(init_state,goal):
    t1=time.time()
    
    current_data=chain(init_state,0,init_state)
    
    #initialize frontier as LIFO queue (stack)
    frontier = LifoQueue()
    
    
    keep = Queue()
    keep.put(current_data)
    #initialize dictionary to save states
    discovered_states={}
    state=to_string(init_state)
    discovered_states[state]=0 
    
    
    #the main loop that defines the 'depth'
    for i in range(0,1000):
        
        while not keep.empty():
            temp=keep.get()
            frontier.put(temp)
        
                
        while not frontier.empty():
            current_data=frontier.get()
            if current_data.get_state()==goal:
            
                t2=time.time()
#                print("-----------------------------------------------------")
#                print("FOUND!")
#                print("Algorithm: IDDFS")
#                print(current_data.get_state()[:1])
#                print(current_data.get_state()[1:2])
#                print(current_data.get_state()[2:3])
#                print('----From----')
#                print(init_state[:1])
#                print(init_state[1:2])
#                print(init_state[2:3])
#                print("Path:",current_data.get_previous_states())
#                print("Steps taken:",current_data.get_steps())
#                print("Time:",t2-t1)
#                print("-----------------------------------------------------")
                return current_data
            
            if current_data.get_steps() > i:
                keep.put(current_data)
            elif current_data.get_steps() <= i:
                actions(current_data,discovered_states,frontier,False)


#implementation of function "breadthFirstSearch", takes 2 2d lists 3x3 as input
#one is initial state and another is goal state
def breadthFirstSearch(init_state,goal):
    t1=time.time()
    
    #initialize dictionary of discovered_states, add initial state right away
    discovered_states={}
    state=to_string(init_state)
    discovered_states[state]=0
    
    #initialize current_data as chain() object
    current_data=chain(init_state,0,init_state)
    
    #initialize queue
    frontier = Queue()
    frontier.put(current_data)
    
    while not frontier.empty():
        
        #take item from frontier and start searching with actions() function
        current_data=frontier.get()        
        
        #goal check
        if current_data.get_state()==goal:
            t2=time.time()
#            print("-----------------------------------------------------")
#            print("FOUND!")
#            print("Algorithm: BFS")
#            print(current_data.get_state()[:1])
#            print(current_data.get_state()[1:2])
#            print(current_data.get_state()[2:3])
#            print('----From----')
#            print(init_state[:1])
#            print(init_state[1:2])
#            print(init_state[2:3])
#            print("Path:",current_data.get_previous_states())
#            print("Steps taken:",current_data.get_steps())
#            print("Time:",t2-t1)
#            print("-----------------------------------------------------")
            return current_data

        actions(current_data,discovered_states,frontier,False)        

#Helper functions for print_results(result)
def move_up_list(data,zero_i,zero_j):
    temp_data = copy.deepcopy(data)
    temp=temp_data[zero_i-1][zero_j]
    temp_data[zero_i-1][zero_j]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data

def move_left_list(data,zero_i,zero_j):
    temp_data = copy.deepcopy(data)
    temp=temp_data[zero_i][zero_j-1]
    temp_data[zero_i][zero_j-1]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data

def move_right_list(data,zero_i,zero_j):
    temp_data = copy.deepcopy(data)
    temp=temp_data[zero_i][zero_j+1]
    temp_data[zero_i][zero_j+1]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data

def move_down_list(data,zero_i,zero_j):
    temp_data = copy.deepcopy(data)
    temp=temp_data[zero_i+1][zero_j]
    temp_data[zero_i+1][zero_j]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data


# In[6]:


#implementation of function "print_results(result)"
#Prints individual result as a sequence of states from initial to goal
#take chain() class objects as input
def print_results(result):
    solution=[]
    solution = copy.deepcopy(result.get_previous_states())
    temp_state=result.get_init_state()
    
    print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
    print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
    print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])
        
    for k in solution:
        print('to')
        
        for i in range(3):
            if '0' in temp_state[i]:
                zero_i=i
                for j in range(3):
                    if temp_state[i][j]=='0':
                        zero_j=j
                    
        if k == 'U':
            temp_state=move_up_list(temp_state,zero_i,zero_j)
            print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
            print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
            print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])
        elif k =="D":
            temp_state=move_down_list(temp_state,zero_i,zero_j)
            print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
            print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
            print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])
        elif k=='R':
            temp_state=move_right_list(temp_state,zero_i,zero_j)
            print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
            print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
            print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])
        elif k=='L':
            temp_state=move_left_list(temp_state,zero_i,zero_j)
            print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
            print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
            print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])

#Final print_result() function
#Loads the file, takes first example from the file
#launches BFS and prints its results with help of print_results(result) function defined above
def print_result():
    
    #load file, store its contents in states[] list

    f= open("Input8PuzzleCases.txt", "r")
    states=[]
    for i in range(0,100):
        temp=[]
        temp = f.readline().strip('\n')
        temp=temp.split(', ')
        states.append(temp)
    f.close()
    del temp
    
    
    #load first example from the file into sample[] list
    sample=[]

    sample.append(states[0][0:3])
    sample.append(states[0][3:6])
    sample.append(states[0][6:9])
    
    #construct goal state (0,1,2,3,4,5,6,7,8)
    goal_state=[]
    for i in range(0,9,3):
        goal_state.append([str(i),str(i+1),str(i+2)])
    
    print("Solution of the first Scenario:")
    print('BFS:')
    print_results(breadthFirstSearch(sample,goal_state))
    print('IDDFS:')
    print_results(Iterative_deepening_DFS(sample,goal_state))
    print('Recorded averages for 100 cases on my machine:')
    print('            Average_Steps    Average_Time')
    print('IDS            22.33             7.0 s')
    print('BFS            22.33             7.4 s')
    print('Solving 100 cases for your machine...')
    
    times_bfs=[]
    steps_bfs=[]
    times_iddfs=[]
    steps_iddfs=[]
    for i in range(len(states)):        
        sample=[]
        sample.append(states[i][0:3])
        sample.append(states[i][3:6])
        sample.append(states[i][6:9])
        
        t1=time.time()
        solution=breadthFirstSearch(sample,goal_state)
        t2=time.time()
        t2=t2-t1
        times_bfs.append(float(t2))
        steps_bfs.append(solution.get_steps())
        print(i+1,"done in",solution.get_steps(),'steps and',format(t2,'.2f'),'s (BFS)')
        
        t1=time.time()
        solution=Iterative_deepening_DFS(sample,goal_state)
        t3=time.time()
        t3=t3-t1
        times_iddfs.append(float(t2))
        steps_iddfs.append(solution.get_steps())
        print(i+1,"done in",solution.get_steps(),'steps and',format(t3,'.2f'),'s (IDS)\n')
    
    avg_time_bfs=sum(times_bfs)/len(times_bfs)
    avg_steps_bfs=sum(steps_bfs)/len(steps_bfs)
    avg_time_iddfs=sum(times_iddfs)/len(times_iddfs)
    avg_steps_iddfs=sum(steps_iddfs)/len(steps_iddfs)
    print('            Average_Steps    Average_Time')
    print('IDS           ',avg_steps_iddfs,'           ',format(avg_time_iddfs,'.2f'),'s')
    print('BFS           ',avg_steps_bfs,'           ',format(avg_time_bfs,'.2f'),'s')


print_result()



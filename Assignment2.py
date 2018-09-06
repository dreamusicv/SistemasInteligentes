from search import *
#from utils import FIFOQueue
import time


class CleanUp(Problem):
    
    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        
        
        self.initial = initial
        self.N = len(self.initial) 
        if goal==None:
            self.goal = self.__get_default_goal()
        else:
            self.goal = goal
        
        
        self.action_list = self.__get_actions()
        
    def __get_actions(self):
        """ Create a list of possible clic locations """
        action_list = []
        for i in range(0, self.N):
            for j in range(0, self.N):
                action_list.append((i, j))
        return tuple(action_list)
                
    def __get_default_goal(self):
        """ Create a default NxN size goal state """
        goal = []
        for i in range(0, self.N):
            row = []
            for j in range(0, self.N):
                row.append(0)
            goal.append(tuple(row))
        return tuple(goal)
            
    def get_surroundings(self, action):
        """ Returns a list of the surrounding postions """
        pos_list = []
        if (action[1]-1)>=0:
            pos_list.append((action[0], action[1]-1))
        if (action[1]+1)<self.N:
            pos_list.append((action[0], action[1]+1))
        if (action[0]-1)>=0:
            pos_list.append((action[0]-1, action[1]))
        if (action[0]+1)<self.N:
            pos_list.append((action[0]+1, action[1]))
        return pos_list
        
    def get_s_zeros(self, state, action):
        z = 0
        for pos in self.get_surroundings(action):
            if(state[pos[0]][pos[1]]==0):
                z+=1
        return z
    
    def get_s_ones(self, state, action):
        o = 0
        for pos in self.get_surroundings(action):
            if(state[pos[0]][pos[1]]==1):
                o+=1
        return o
        
    def get_zeros(self, state):
        z=0
        for pos in self.action_list:
            if(state[pos[0]][pos[1]]==0):
                z+=1
        return z
    
    def get_ones(self, state):
        o=0
        for pos in self.action_list:
            if(state[pos[0]][pos[1]]==1):
                o+=1
        return o
                
        
    def h(self, node):
        # hval = 0
        # for action in self.action_list:
        #     s_ones=self.get_s_ones(node.state, action)
        #     if(s_ones>0):
        #         hval += (4-s_ones)/(4*self.get_ones(node.state))
        raise NotImplementedError
    
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        return self.action_list
        
    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        state2 = []
        for row in state:
            r2 = []
            for elem in row:
                r2.append(elem)
            state2.append(r2)
            
        for pos in self.get_surroundings(action):
            if state2[pos[0]][pos[1]] == 1:
                state2[pos[0]][pos[1]] = 0
            else:
                state2[pos[0]][pos[1]] = 1
        state3 = []
        for row in state2:
            state3.append(tuple(row))
            
        return tuple(state3)
        
    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        return state == self.goal
        
class CleanUpH1(CleanUp):
    def __init__(self, initial, goal=None):
        super().__init__(initial)
        
    def h(self, node):
        hval = 0
        for action in self.action_list:
            s_ones=self.get_s_ones(node.state, action)
            if(s_ones>0):
                hval += (4-s_ones)/(4*self.get_ones(node.state))
        
        return hval
        
class CleanUpH2(CleanUp):
    def __init__(self, initial, goal=None):
        super().__init__(initial)
        
    def h(self, node):
        hval = 0
        for action in self.action_list:
            s_ones=self.get_s_ones(node.state, action)
            if(s_ones>0):
                hval += (4-s_ones)/(4*self.get_ones(node.state))
        
        return hval

def s_print(state):
    """ Print the state as a matrix. """
    for row in state:
        print(row)
    print()

state = ((0, 1, 0, 1),
         (1, 0, 0, 0),
         (0, 1, 0, 1),
         (0, 0, 0, 0))
         
state = ((1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1),
         (1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0),
         (1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1),
         (0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0),
         (0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0),
         (0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0),
         (0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0),
         (1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0),
         (1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0),
         (1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0),
         (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        )
         
#c = CleanUp(state)
start_time = time.time()
c = CleanUpH1(state)

# s_print(c.initial)
# s_print(c.result(state, (1,0)))
# print("Breadth First Tree Search")
# n1 = breadth_first_tree_search(c)
# for node in n1.path():
#     s_print(node.state)
# print()
#     
print("A* Search")
n2 = astar_search(c)
for node in n2.path():
    s_print(node.state)
print()

print("--- %s seconds ---" % (time.time() - start_time))
# f.append(Node(c.initial))
# n=f.pop()
# f.extend(n.expand(c))
# n=f.pop()

#c.result(n.state, (0,0))
#n.child_node(c, (0,0))

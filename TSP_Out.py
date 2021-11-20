import numpy as np

class SA:
    def __init__(self,t,cooling_rate,iter_no,arr):
        self.t = t
        self.cooling_rate = cooling_rate
        self.iter_no = iter_no
        self.x = len(arr)
        self.arr= arr
        self.route = np.random.permutation(range(self.x))
        

    
    def optimize(self):
        old_route= np.copy(self.route)
        old_dist = self.total_distance(old_route)
        
        T = self.t
        
        self.distances = [old_dist]
        self.temperatures = [T]
        
        for i in range(self.iter_no):
            new_route = self.new_route()
            new_dist = self.total_distance(new_route)
            
            if new_dist < old_dist:
                old_route = new_route
                old_dist = new_dist
                
            else:
                if np.random.random() < np.exp(-(new_dist - old_dist) / T):
                    old_route = new_route
                    old_dist = new_dist
                
                
            T = T * self.cooling_rate
            
            self.distances.append(old_dist)
            self.temperatures.append(T)
            
        return old_route, old_dist, self.distances, self.temperatures
            
            
    
    def total_distance(self,route):
        dist = 0

        for i in range(len(route)-1):
            dist += self.arr[(route[i],route[i+1])]
        return dist
    
    def new_route(self):
        i1 , i2 = np.random.choice(self.x,2)
        new_route = self.route.copy()
        new_route[i2], new_route[i1] = new_route[i1], new_route[i2]  
        return new_route
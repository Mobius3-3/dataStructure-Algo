import heapq

"""
REFERENCE: https://en.wikipedia.org/wiki/A*_search_algorithm
"""

def Euclidean_distance(intersect1, intersect2):
    """
    Euclidean Distance between two intersections
    """
    return abs(intersect2[0] - intersect1[0]) + abs(intersect2[1] - intersect1[1]) 

def reconstruct_path(came_from, current, start):
    """
    Traversing backwards to find the optimal path
    """
    total_path = []
    
    while current != start:
        total_path.append(current)
        current = came_from[current]
       
    total_path.append(start)
    total_path.reverse()
    return total_path


def shortest_path(M, start, goal):
    """
    Finding the shortest path using A* Algorithm using Priority Queue
    """
    open_set = [] # Initializing the Priority Queue to add/remove/search the intersection with lowest g_score with O(1)
    came_from = {} # To keep track of previous intersection while reaching from start to current intersection i
    g_score = {}  # To keep track of cost of the shortest path from start to current intersection i
    
    came_from[start] = None # For the start intersection, there won't be any previous intersection. Hence, set as None
    g_score[start] = 0
    heapq.heappush(open_set, (0, start)) # adding the start intersection to the Priority Queue
    visited_set = set()
    
    
    while len(open_set) > 0:
        current = heapq.heappop(open_set)[1]  # Fetching the intersect with lowest cost (g_score) from the Priority Queue
        
        if current in visited_set:
            continue
        else:
            if current == goal:
                return reconstruct_path(came_from, current, start)


            for neighbor in M.roads[current]:
                # f(i) = g(i) + h(i) for intersect i
                tentative_g_score = g_score[current] + Euclidean_distance(M.intersections[current], M.intersections[neighbor])

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score

                    if neighbor not in visited_set:
                        heapq.heappush(open_set, (tentative_g_score, neighbor)) 
                    
    return 
            
            
            
            
        
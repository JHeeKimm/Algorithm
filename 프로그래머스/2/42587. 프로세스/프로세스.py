from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0
    
    while queue:
        current = queue.popleft()
        
        next = False
        
        for q in queue:
            if q[1] > current[1]:
                next = True
                break
                
        if next:
            queue.append(current)
        else:
            count += 1
            
            if current[0] == location:
                return count
from heapq import heappush, heappop   # Import priority queue functions (push = add, pop = remove smallest)

goal = ((1,2,3),                     # Goal state row 1 (final board we want to reach)
        (4,5,6),                     # Goal state row 2
        (7,8,0))                     # Goal state row 3, 0 = empty tile

def h(state):                        # Heuristic function = calculates "how far we are from goal"
    d = 0                            # Distance counter starts at 0
    for i in range(3):               # Loop over rows (0,1,2)
        for j in range(3):           # Loop over columns (0,1,2)
            v = state[i][j]          # Current tile value at row i, col j
            if v != 0:               # Ignore empty tile
                x, y = divmod(v-1, 3) # Get goal position of tile v (x=row, y=col)
                d += abs(x-i) + abs(y-j) # Add Manhattan distance from current → goal position
    return d                          # Return total distance score

def moves(state):                     # Generate all possible next board positions
    for i in range(3):                # Loop rows
        for j in range(3):            # Loop cols
            if state[i][j] == 0:      # Find empty tile position
                x, y = i, j           # Store empty tile coordinates
    res = []                          # List to store new possible states
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]: # Possible directions: up, down, left, right
        nx, ny = x+dx, y+dy           # New position after moving empty tile
        if 0 <= nx < 3 and 0 <= ny < 3: # Check move is inside board
            s = [list(r) for r in state] # Convert tuples → lists so we can modify
            s[x][y], s[nx][ny] = s[nx][ny], s[x][y] # Swap empty tile with neighbor
            res.append(tuple(tuple(r) for r in s)) # Convert back to tuple and store
    return res                         # Return all valid next states

def astar(start):                      # A* search function to find shortest path
    pq = []                           # Create empty priority queue
    heappush(pq, (h(start), 0, start, [start])) # Push start state with f=h, g=0, and path list
    vis = set()                       # Set to track visited states

    while pq:                         # Run until queue is empty
        f, g, cur, path = heappop(pq) # Pop state with smallest f score
        if cur == goal:               # If current state is goal, stop
            return path                # Return path to goal
        if cur in vis:                # If already visited, skip
            continue                  # Go to next loop
        vis.add(cur)                  # Mark current state as visited
        for nxt in moves(cur):        # For each possible move from current state
            heappush(pq, (g+1+h(nxt), g+1, nxt, path+[nxt])) # Push new state with updated scores

start = ((8,6,7),                      # Start board row 1 (scrambled puzzle)
         (2,5,4),                      # row 2
         (3,0,1))                      # row 3

sol = astar(start)                     # Run A* search and store solution path

if sol is not None:                    # If solution exists
    print("Total steps:", len(sol) - 1) # Print number of moves taken (exclude start state)
    for step in sol:                   # Print each board in path
        for row in step:               # Print each row
            print(row)                 # Output row
        print()                        # Blank line after each board
else:                                  # If no solution
    print("No solution found")         # Print failure message
import typing


def main(tomato_grid: typing.List[typing.List[int]]):
    # START WRITING CODE HERE
    #find all rotten tomatoes to start with and append to a queue
    #check if all values are 0 and return 0 right away
    check_0 = True 
    queue = []
    tomato_count = 0
    
    r,c = len(tomato_grid),len(tomato_grid[0])
    for i in range(r):
        for j in range(c) :
            if tomato_grid[i][j] != 0 :
                check_0 = False
            if tomato_grid[i][j] == -1 :
                queue.append((i,j))
            elif tomato_grid[i][j] == 1 :
                tomato_count += 1

    if check_0 == True :
        return 0
    
    
    #start from the rotten tomato to propogate rotting process
    #check the neighbors of every rotten tomato and simulate rotting BFS with minutes count 
    dirs = [(-1,0),(0,-1),(0,1),(1,0)]
    minutes = -1
    while(queue):
        # for every level of rotting tomatoes
        minutes += 1
        
        for i in range(len(queue)): 
            r_c,c_c = queue.pop(0)
            for d in dirs :
                r_check,c_check = r_c+d[0], c_c+d[1]
                if 0 <= r_check < r and 0 <= c_check < c :
                    #check if there is tomato
                    if tomato_grid[r_check][c_check] == 1 :
                        tomato_grid[r_check][c_check] = -1
                        tomato_count -= 1
                        queue.append((r_check,c_check))
        
    return -1 if tomato_count else minutes

if __name__ == "__main__":
    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [1, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]
    assert (main(tomato_grid) == 2), "Tomatoes will be rotten in 2 days"
    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [0, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]
    assert (main(tomato_grid) == -1), "All tomatoes cannot be rotten"

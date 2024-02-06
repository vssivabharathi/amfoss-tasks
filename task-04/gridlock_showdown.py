
def main():
   
    num_test_cases = int(input().strip())

    
    for _ in range(num_test_cases):

        grid = []

  
        for _ in range(3):
            row = input().strip()
            grid.append(row)
# strip cmd is ude to rm the extra write space from the user
        
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != '.':
                print(grid[i][0]) 
                break
        else:
           
            for i in range(3):
                if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != '.':
                    print(grid[0][i]) 
                    break
            else:
              
                if (grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '.') or \
                   (grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '.'):
                    print(grid[1][1])  
                else:
                    print("DRAW") 


if __name__ == "__main__":
    main()

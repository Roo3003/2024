class Grid():
    def __init__(self, grid):
        '''
        Converts the grid format from immutable strings to a matrix - makes it much easier to work with
        '''
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self.grid = [[' ']*self.num_cols for _ in range(self.num_rows)]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = grid[row][col]

    def print_grid(self):
        '''
        Prints map to output (with nicer formatting than a list of strings)
        '''
        out_str = ''
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                out_str += self.grid[row][col]
            out_str += '\n'
        print(out_str)

    def replace_tile(self, row, col, new_val):
        '''
        Replaces tile at given row/col to new_val
        '''
        self.grid[row][col] = new_val
    
    def get_tile(self, row, col):
        '''
        Returns tile at row/col
        '''
        return self.grid[row][col]

    def count_tiles(self, val):
        '''
        Counts the number of tiles in the grid that have the character given by val and returns that value
        '''
        count = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] == val:
                    count += 1
        return count


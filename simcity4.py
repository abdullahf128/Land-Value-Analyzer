"""
CMPUT 174 Lab 7 'Simcity4' Program
Prints Given Land Values in Grid form and Then Calculates Unknown Land Values as well as Average and Max Land Value in a City
Author: Abdullah Faisal
When: November 2, 2022
"""

# import statement
import copy


# reads a list of land values from a file and returns an array of values
def create_grid(filename: str) -> list[list[int]]:
    
    with open(filename, 'r') as file:
        land_values = file.readlines()
    counter = 0
    land_values_array = []  # empty list for full array values
    row_values = []  # empty list for appending small lists into the array
    for value in land_values:
        separate_values = value.find( '/n' )  # separates land values
        if counter > 1:
            row_values.append(int(value[0:separate_values]))
            if len(row_values) == row_length:
                land_values_array.append(row_values)
                row_values = []                
        elif counter == 1:
            row_length = int(value[0:separate_values])
        counter += 1
    return land_values_array


# organizes and displays values in a grid form
def display_grid(grid: list[list[int]]) -> None:
    
    row_length = len(grid[0])
    for a_list in grid:
        for value in a_list:
            print(f"{value:8}", end=" ")  # creates consistent spacing between grid values and keeps them aligned
        print('\n', end="")  # moves next row of land values to be printed on the next line


# finds and returns a list of a certain land value's neighbors
def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    
    rows = len(grid)
    cols = len(grid[0])
    neighbours = []
   
    for row_num in range(row-1, row+2):  # row-1, row, row+1
        for col_num in range(col-1, col+2):  # col-1, col, col+1
            if row_num == row and col_num == col:
                continue  # skip inputted location
            if row_num < 0 or row_num >= rows or col_num < 0 or col_num >= cols:
                continue  # skip location if it falls outside of the grid
            neighbours.append(grid[row_num][col_num])
    return neighbours


# replaces empty/missing values with the average values of it's neighbors and returns a new array of values
def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    
    new_grid = copy.deepcopy(grid)
    row_count = 0
    for row in new_grid:
        col_count = 0
        for value in row:
            if value == 0:
                neighbors = find_neighbor_values(new_grid, row_count, col_count)  # calls find_neighbor_values function to find values of neighbors
                avg_land_val = round(sum(neighbors) / len(neighbors)) 
                new_grid[row_count][col_count] = avg_land_val  # replaces missing value with calculated value
            col_count += 1
        row_count += 1
    return new_grid
    

# finds and returns the highest land value in the array
def find_max(grid: list[list[int]]) -> int:
    
    max_nums_list = []
    for value_list in grid:
        max_nums_list.append(max(value_list))  # appends highest values in each list within the array to max_nums_list
    max_num = max(max_nums_list)
    return max_num


# calculates and returns total average land value in array
def find_average(grid: list[list[int]]) -> int:
    
    total_value = 0
    for row in grid:
        total_value += sum(row)
    num_of_values = len(grid) * len(grid[0])  # number of rows times number of columns = total number of values
    avg_value = round(total_value / num_of_values)
    return avg_value


# calls all functions in order to print/fill in land values matrix and calculate average/highest values in the city
def main() -> None:
    
    grid = create_grid("data_1.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")

main()

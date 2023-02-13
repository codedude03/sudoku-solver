#Grids 1-4 are 2x2
grid1 = [
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[0, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 2, 3, 4],
		[2, 1, 4, 3],
		[3, 4, 2, 1],
		[4, 3, 1, 2]]

grid4 = [
		[1, 3, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

#Grids 4-7 are 3x3
grid5 = [
		[1, 2, 3, 4, 5, 6, 7, 8, 9,],
		[2, 3, 4, 5, 6, 7, 8, 9, 1,],
		[3, 4, 5, 6, 7, 8, 9, 1, 2,],
		[4, 5, 6, 7, 8, 9, 1, 2, 3,],
		[5, 6, 7, 8, 9, 1, 2, 3, 4,],
		[6, 7, 8, 9, 1, 2, 3, 4, 5,],
		[7, 8, 9, 1, 2, 3, 4, 5, 6,],
		[8, 9, 1, 2, 3, 4, 5, 6, 7,],
		[9, 1, 2, 3, 4, 5, 6, 7, 8,]]

grid6 = [
		[6, 1, 7, 8, 4, 2, 5, 3, 9,],
		[7, 4, 5, 3, 6, 9, 1, 8, 2,],
		[8, 3, 2, 1, 7, 5, 4, 6, 9,],
		[1, 5, 8, 6, 9, 7, 3, 2, 4,],
		[9, 6, 4, 2, 3, 1, 8, 7, 5,],
		[2, 7, 3, 5, 8, 4, 6, 9, 1,],
		[4, 8, 7, 9, 5, 6, 2, 1, 3,],
		[3, 9, 1, 4, 2, 8, 7, 5, 6,],
		[5, 2, 6, 7, 1, 3, 9, 4, 8,]]

grid7 = [
		[6, 1, 9, 8, 4, 2, 5, 3, 7,],
		[7, 4, 5, 3, 6, 9, 1, 8, 2,],
		[8, 3, 2, 1, 7, 5, 4, 6, 9,],
		[1, 5, 8, 6, 9, 7, 3, 2, 4,],
		[9, 6, 4, 2, 3, 1, 8, 7, 5,],
		[2, 7, 3, 5, 8, 4, 6, 9, 1,],
		[4, 8, 7, 9, 5, 6, 2, 1, 3,],
		[3, 9, 1, 4, 2, 8, 7, 5, 6,],
		[5, 2, 6, 7, 1, 3, 9, 4, 8,]]

#grids 8-10 are 2x3
grid8 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grid9 = [
		[1, 2, 6, 5, 4, 3],
		[5, 3, 4, 6, 2, 1],
		[6, 1, 3, 4, 5, 2],
		[2, 5, 5, 3, 1, 6],
		[4, 6, 1, 2, 3, 5],
		[3, 5, 2, 1, 6, 4]]

grid10 = [
		[1, 2, 6, 5, 4, 3],
		[5, 3, 4, 6, 2, 1],
		[6, 1, 3, 4, 5, 2],
		[2, 4, 5, 3, 1, 6],
		[4, 6, 1, 2, 3, 5],
		[3, 5, 2, 1, 6, 4]]


grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), 
		(grid5, 3, 3), (grid6, 3, 3), (grid7, 3, 3),
		(grid8, 2, 3), (grid9, 2, 3), (grid10, 2, 3)]

expected_outputs = [False, False, False, True, False, False, True, False, False, True]

'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''
        
#To complete the first assignment, please write the code for the following function
def check_solution(grid_input):
    '''
    This function is used to check whether a sudoku board has been correctly solved

    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''

    def verif_list(vals_list):
        '''
        check all digits in length of given list are within given list (example in list length 6 should contain 1-6)
        '''
        for i in range(len(vals_list)):
            if (i+1) not in vals_list:
    #            print('returned False')
                return False
    #    print('returned True')
        return True

    def verif_rows(grid_input):
        '''
        iterate through the inner 1d lists pass to check 1-n within list
        '''
        for row in grid_input:
            if not verif_list(row):
                return False
        return True

    def verif_columns(grid_input):
        '''
        iterate amount of times of height of 2d list, and iterate for number of columns, taking each number from same position in each row to pass in list
        '''
        for column_num in range(len(grid_input[0])):
            column_list = []
            for row in grid_input:
                column_list.append(row[column_num])
            if not verif_list(column_list):
                return False
        return True

    def verif_grid(grid_input):
        '''
        iterate through the grids and within each grid pass all the digits as a list to list checker
        '''
        for grid_row in range(0,len(grid_input[0]),grid_input[2]):
            for grid_column in range(0,len(grid_input[0][0]),grid_input[1]):
                temp_grid_list = []
                for block_row in range(grid_input[1]):
                    for block_column in range(grid_input[2]):
                        temp_grid_list.append(grid_input[0][grid_column + block_row][grid_row + block_column])
                if not verif_list(temp_grid_list):
                    return False
        return True

    #run each of the checkers
    if not verif_rows(grid_input[0]):
        return False
    if not verif_columns(grid_input[0]):
        return False
    if not verif_grid(grid_input):
        return False
    return True


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():
    '''
    This function will call the check_solution function on each of the provided grids, 
    comparing the answer to the expected output. Each correct output is given 10 'points
    '''

    points = 0

    print("Running test script for coursework 1")
    print("====================================")
	
    #Loop through the grids and expected outputs together
    for (i, (grid, output)) in enumerate(zip(grids, expected_outputs)):

	#Compare output to expected output
        print("Checking grid: %d" % (i+1))
        checker_output = check_solution(grid)

        if checker_output == expected_outputs[i]:
            #Output is correct - yay!
            print("grid %d correct" % (i+1))
            points = points + 5
        else:
	    #Output is incorrect - print both output and expected output.
            print("grid %d incorrect" % (i+1))
            print("Output was: %s, but expected: %s" % (checker_output, expected_outputs[i]))

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    main()

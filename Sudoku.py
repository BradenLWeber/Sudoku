''' Solves a sudoku board using human methods
To test any board in the code, edit the name of it 'board' '''

board =					[[0, 0, 0, 7, 0, 0, 0, 0, 0], 
						[1, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 4, 3, 0, 2, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 6], 
						[0, 0, 0, 5, 0, 9, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 4, 1, 8], 
						[0, 0, 0, 0, 8, 1, 0, 0, 0], 
						[0, 0, 2, 0, 0, 0, 0, 5, 0], 
						[0, 4, 0, 0, 0, 0, 3, 0, 0]]
boardtest =				[[0, 1, 0, 0, 0, 0, 0, 0, 0], 
						[0, 2, 0, 0, 5, 0, 0, 8, 0], 
						[0, 3, 4, 0, 0, 0, 0, 7, 0], 
						[0, 0, 6, 0, 0, 0, 0, 2, 0], 
						[0, 0, 7, 0, 0, 0, 0, 1, 0], 
						[0, 0, 8, 0, 0, 0, 0, 0, 0], 
						[0, 7, 2, 1, 0, 0, 5, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 0, 0, 0, 0, 0, 6]]
boardeasy =  			[[0, 3, 0, 0, 1, 0, 0, 6, 0], 
						[7, 5, 0, 0, 3, 0, 0, 4, 8], 
						[0, 0, 6, 9, 0, 4, 3, 0, 0], 
						[0, 0, 3, 0, 0, 0, 8, 0, 0], 
						[9, 1, 2, 0, 0, 0, 6, 0, 4], 
						[0, 0, 4, 0, 0, 0, 0, 0, 0], 
						[0, 0, 0, 6, 7, 5, 2, 0, 0], 
						[6, 8, 0, 0, 9, 0, 0, 1, 5], 
						[0, 9, 0, 0, 4, 0, 0, 3, 0]]
boardimpossible= 		[[8, 0, 0, 0, 0, 0, 0, 0, 0], 
						[0, 0, 3, 6, 0, 0, 0, 0, 0], 
						[0, 7, 0, 0, 9, 0, 2, 0, 0], 
						[0, 5, 0, 0, 0, 7, 0, 0, 0], 
						[0, 0, 0, 0, 4, 5, 7, 0, 0], 
						[0, 0, 0, 1, 0, 0, 0, 3, 0], 
						[0, 0, 1, 0, 0, 0, 0, 6, 8], 
						[0, 0, 8, 5, 0, 0, 0, 1, 0], 
						[0, 9, 0, 0, 0, 0, 4, 0, 0]]
						
possible = [ [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ], [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ], [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ], [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ], [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ], [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ], [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ], [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ], [ [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9] ] ]

def actual_to_possible():
	'''Checks all board values, and if they are non-zero, deletes all possibilities except the actual
	This is only useful for the beginning when numbers have been entered in manually'''
	for row in range(9):
		for column in range(9):
			if board[row][column] != 0 and len(possible[row][column]) != 1:
				for i in range(9):
					if i == board[row][column]:
						continue
					try:
						possible[row][column].remove(i)
					except:
						pass

def possible_to_actual():
	'''Checks all the possible values, and if there are any that have been whittled down to one, they are added to the board'''
	for row in range(9):
		for number in range(9):
			if board[row][number] == 0 and len(possible[row][number]) == 1:
				board[row][number] = possible[row][number][0]
				
def show_board():
	'''Shows the sudoku board'''
	for row in range(9):
		print()
		if row in [3, 6]:
			print()
		for column in range(9):
			print(board[row][column], end = ' ')
			if column in [2, 5]:
				print(end=' ')
		
def check_row_column_quadrant():
	'''Goes through every number and makes sure it is taken 
	off the possibilities for each other spot in its column, row, and quadrant'''
	
	#This will run through every spot
	for row in range(9):
		for column in range(9):
			if board[row][column] != 0:
				# row2 will run through every row again now to delete from the possibilities each number in the corresponding columns
				for row2 in range(9):
					if row2 != row:
						try:
							possible[row2][column].remove(board[row][column])
						except:
							pass
				# column2 will run through every column again now to delete from the possibilities each number in the corresponding rows
				for column2 in range(9):
					if column2 != column:
						try:
							possible[row][column2].remove(board[row][column])
						except:
							pass
				# Now we take each number and delete it from the possibilities of each spot in the quadrant
				for row2 in range((row // 3) * 3, (row // 3) * 3 + 3):
					for column2 in range((column // 3) * 3, (column // 3) * 3 + 3):
						if row2 == row and column2 == column:
							continue
						try:
							possible[row2][column2].remove(board[row][column])
						except:
							continue
							
def only_possible():
	'''This runs through and sees if there is only one possible spot 
	for a number in a particular row, column, or quadrant'''

	# This runs through each row and checks if any of the numbers can only go in one spot in that row
	for row in range(9):
		for i in range(1, 10):
			# i_count is counting how many times a number i appears in the possibilities in that row
			i_count = 0
			for column in range(9):
				if i in possible[row][column]:
					i_count += 1
			# If the number only appeared once in the possibilities, it must go in that one spot
			if i_count == 1:
				for column in range(9):
					if i in possible[row][column]:
						board[row][column] = i
						possible[row][column] = [i]

	# Runs through each column and checks if any of the numbers can only go in one spot in that column
	for column in range(9):
		for i in range(1, 10):
			# i_count is counting how many times a number i appears in the possibilities in that column
			i_count = 0
			for row in range(9):
				if i in possible[row][column]:
					i_count += 1
			# If the number only appeared once in the possibilities, it must go in that one spot
			if i_count == 1:
				for row in range(9):
					if i in possible[row][column]:
						board[row][column] = i
						possible[row][column] = [i]

	# Runs through each quadrant and checks if any of the numbers can only go in one spot in that quadrant
	for rows in [range(3), range(3, 6), range(6, 9)]:
		for columns in [range(3), range(3, 6), range(6, 9)]:
			for i in range(1, 10):
				# i_count is counting how many times a number i appears in the possibilities in this quadrant
				i_count = 0
				for row in rows:
					for column in columns:
						if i in possible[row][column]:
							i_count += 1
				# If i appears only once, it must go in that one spot
				if i_count == 1:
					for row in rows:
						for column in columns:
							if i in possible[row][column]:
								board[row][column] = i
								possible[row][column] = [i]
								
def only_possible_line():
	'''Looks in each quadrant for numbers that can only possibly be in a certain column or row
	If so, deletes said number from every other box in the column or row
	'''
	
	for rows in [range(3), range(3, 6), range(6, 9)]:
		for columns in [range(3), range(3, 6), range(6, 9)]:
			for i in range(1, 10):
				# i_count is counting how many times a number i appears in each possibilities of each row
				i_count_1 = 0
				i_count_2 = 0
				i_count_3 = 0
				# Now count the i's'
				for row in rows:
					if i in possible[row][columns[0]]:
						i_count_1 += 1
					if i in possible[row][columns[1]]:
						i_count_2 += 1
					if i in possible[row][columns[2]]:
						i_count_3 += 1
				# Make list of i_counts and figure out if there is only one row possible
				i_counts = [i_count_1, i_count_2, i_count_3]
				if max(i_counts) == 1:
					continue
				if i_counts.count(0) == 2:
					# index of i determines which row to use in rows
					ro = i_counts.index(max(i_counts))
				# Now take that i out of every possibility in that row except the ones in the quadrant
				for column in range(9):
					if column not in columns:
						try:
							possible[row[ro]][column].remove(i)
						except:
							pass
							
				# i_count is counting how many times a number i appears in each possibilities of each column
				i_count_1 = 0
				i_count_2 = 0
				i_count_3 = 0
				# Now to count the i's'
				for column in columns:
					if i in possible[rows[0]][column]:
						i_count_1 += 1
					if i in possible[rows[1]][column]:
						i_count_2 += 1
					if i in possible[rows[2]][column]:
						i_count_3 += 1
				# Make list of i_counts and figure out if there is only one column possible
				i_counts = [i_count_1, i_count_2, i_count_3]
				if max(i_counts) == 1:
					continue
				if i_counts.count(0) == 2:
					col = i_counts.index(max(counts))
				# now take i out of the possiblities in that column except ones in the quadrant
				for row in range(9):
					if row not in rows:
						try:
							possible[row][columns[col]].remove(i)
						except:
							pass
					
def check_twins_and_triplets():
	'''Checks each quadrant, row, and column for a pair of numbers that have only two
	possibilities that are in the same two spots'''
	
	# Start by checking every row
	for row in range(9):
		# This stores the numbers that occur exactly twice in the possibilities
		twins = []
		triplets = []
		for i in range(1, 10):
			# i_count is counting how many times a number i appears in the possibilities in that row
			i_count = 0
			for column in range(9):
				if i in possible[row][column]:
					i_count += 1
			if i_count == 2:
				twins.append(i)
			if i_count == 3:
				triplets.append(i)
		# If there are only two twins, checks to see if they are in the same locations
		if len(twins) > 1:
			twin_row_recursion(twins, row, pivot=len(twins) - 1)
		if len(triplets) > 2:
			triplet_row_recursion(triplets, row, len(triplets) - 1)
		
	# Now check every column
	for column in range(9):
		# This stores numbers that appear exactly twice in the possibilities
		twins = []
		triplets = []
		for i in range(1, 10):
			# i_count is counting how many times a number i appears in the possibilities in that column
			i_count = 0
			for row in range(9):
				if i in possible[row][column]:
					i_count += 1
			if i_count == 2:
				twins.append(i)
			if i_count == 3:
				triplets.append(i)
		# If there are only two twins, checks to see if locations are the same
		if len(twins) > 1:
			twin_column_recursion(twins, column, len(twins) - 1)
		if len(triplets) > 2:
			triplet_column_recursion(triplets, column, len(triplets) - 1)
		
	for rows in [range(3), range(3, 6), range(6, 9)]:
		for columns in [range(3), range(3, 6), range(6, 9)]:
			twins = []
			triplets = []
			for i in range(1, 10):
				# i_count is counting how many times a number i appears in the possibilities in this quadrant
				i_count = 0
				for row in rows:
					for column in columns:
						if i in possible[row][column]:
							i_count += 1
				if i_count == 2:
					twins.append(i)
				if i_count == 3:
					triplets.append(i)
			if len(twins) > 1:
				twin_quadrant_recursion(twins, rows, columns, len(twins) - 1)
			if len(triplets) > 2:
				triplet_quadrant_recursion(triplets, rows, columns, len(triplets) - 1)
								
def twin_row_recursion(twins, row, pivot):
	''' This checks each combination of twins to see if any have the same location
	Input: list of twins, row number, and pivot point to start at
	Output: None
	'''

	# This checks every combination of the pivot with the twins before it
	for spot in range(pivot):
		check_twins = [twins[spot], twins[pivot]]
		twin_spots = []
		# Now finding the columns that each twin is in
		for twin in check_twins:
			for column in range(9):
				if twin in possible[row][column] and column not in twin_spots:
					twin_spots.append(column)
		# If they are in the same location, the possibilities are updated to include only them
		if len(twin_spots) == 2:
			for column in range(9):
				if check_twins[0] in possible[row][column]:
					possible[row][column] = [check_twins[0], check_twins[1]]
	# Once we've tried all the combinations, recursion stops'
	if pivot != 1:
		twin_row_recursion(twins, column, pivot - 1)

def twin_column_recursion(twins, column, pivot):
	'''This checks each combination of twins to see if any have the same location
	Input: list of twins, column number, and pivot point to start at'''

	# This checks every combination of the pivot with the twins before it
	for spot in range(pivot):
		check_twins = [twins[spot], twins[pivot]]
		twin_spots = []
		# Now finding the columns that each twin is in
		for twin in check_twins:
			for row in range(9):
				if twin in possible[row][column] and row not in twin_spots:
					twin_spots.append(row)
		# If they are in the same location, the possibilities are updated to include only them
		if len(twin_spots) == 2:
			for row in range(9):
				if check_twins[0] in possible[row][column]:
					possible[row][column] = [check_twins[0], check_twins[1]]
	# Once we've tried all the combinations, recursion stops'
	if pivot != 1:
		twin_column_recursion(twins, column, pivot - 1)

def twin_quadrant_recursion(twins, rows, columns, pivot):
	'''This checks each combination of twins to see if any have the same location
	Input: list of twins, rows in quadrant, columns in quadrant, and pivot to start at
	Output: None
	'''
	
	# This checks every combination of the pivot with the twins before it
	for spot in range(pivot):
		check_twins = [twins[spot], twins[pivot]]
		twin_spots = []
		# This is storing the locations of the two twins
		for twin in check_twins:
			for row in rows:
				for column in columns:
					if twin in possible[row][column] and [row, column] not in twin_spots:
						twin_spots.append([row, column])
		# If the locations are the same, the possibilities are updated to include only them
		if len(twin_spots) == 2:
			for row in rows:
				for column in columns:
					if check_twins[0] in possible[row][column]:
						possible[row][column] = [check_twins[0], check_twins[1]]
	if pivot != 1:
		twin_quadrant_recursion(twins, rows, columns, pivot - 1)

def triplet_row_recursion(triplets, row, pivot):
	''' This checks each combination of triplets to see if any have the same location
	and if so, makes those 3 numbers the only ones possible at that location
	Input: list of triplets, row number, and pivot point to start at
	Output: None
	'''

	# This checks every combination of the pivot with the triplets before it
	for spot1 in range(pivot):
		for spot2 in range(pivot - 1):
			if spot1 == spot2:
				continue
			check_triplets = [triplets[spot2], triplets[spot1], triplets[pivot]]
			triplet_spots = []
			# This is counted to ensure that if the first set of triplets changed the possibilities, it didn't knock out any of the other sets of triplets
			# So if this number is 9 by the end, that means all the triplet numbers are still there
			triplet_count = 0
			for triplet in check_triplets:
				for column in range(9):
					if triplet in possible[row][column]:
						triplet_count += 1
						if column not in triplet_spots:
							triplet_spots.append(column)
			# If they are in the same location, the possibilities are updated to include only them
			if len(triplet_spots) == 3 and triplet_count == 9:
				for column in range(9):
					if check_triplets[0] in possible[row][column]:
						possible[row][column] = [check_triplets[0], check_triplets[1], check_triplets[2]]
		# Once we've tried all the combinations, recursion stops'
		if pivot != 2:
			triplet_row_recursion(triplets, row, pivot - 1)
			
def triplet_column_recursion(triplets, column, pivot):
	'''This checks each combination of triplets to see if any have the same location
	and if so, makes those 3 numbers the only possibility at those locations
	Input: list of triplets, column number, and pivot point to start at
	Output: None
	'''

	# This checks every combination of the pivot with the triplets before it
	for spot1 in range(pivot):
		for spot2 in range(pivot - 1):
			if spot1 == spot2:
				continue
			check_triplets = [triplets[spot2], triplets[spot1], triplets[pivot]]
			triplet_spots = []
			# This is counted to ensure that if the first set of triplets changed the possibilities, it didn't knock out any of the other sets of triplets
			# So if this number is 9 by the end, that means all the triplet numbers are still there
			triplet_count = 0
			for triplet in check_triplets:
				for row in range(9):
					if triplet in possible[row][column]:
						triplet_count += 1
						if row not in triplet_spots:
							triplet_spots.append(column)
			# If they are in the same location, the possibilities are updated to include only them
			if len(triplet_spots) == 3 and triplet_count == 9:
				for row in range(9):
					if check_triplets[0] in possible[row][column]:
						possible[row][column] = [check_triplets[0], check_triplets[1], check_triplets[2]]
		# Once we've tried all the combinations, recursion stops'
		if pivot != 2:
			triplet_row_recursion(triplets, column, pivot - 1)

def triplet_quadrant_recursion(triplets, rows, columns, pivot):
	'''This checks each combination of triplets to see if any have the same location
	and if so, makes those 3 numbers the only possibility at those locations
	Input: list of triplets, column number, and pivot point to start at
	Output: None
	'''

	# This checks every combination of the pivot with the triplets before it
	for spot1 in range(pivot):
		for spot2 in range(pivot - 1):
			if spot1 == spot2:
				continue
			check_triplets = [triplets[spot2], triplets[spot1], triplets[pivot]]
			triplet_spots = []
			# This is counted to ensure that if the first set of triplets changed the possibilities, it didn't knock out any of the other sets of triplets
			# So if this number is 9 by the end, that means all the triplet numbers are still there
			triplet_count = 0
			for triplet in check_triplets:
				for row in rows:
					for column in columns:
						if triplet in possible[row][column]:
							triplet_count += 1
							if [row, column] not in triplet_spots:
								triplet_spots.append([row, column])
			# If they are in the same location, the possibilities are updated to include only them
			if len(triplet_spots) == 3 and triplet_count == 9:
				for row in rows:
					for column in columns:
						if check_triplets[0] in possible[row][column]:
							possible[row][column] = [check_triplets[0], check_triplets[1], check_triplets[2]]
		# Once we've tried all the combinations, recursion stops'
		if pivot != 2:
			triplet_quadrant_recursion(triplets, rows, columns, pivot - 1)

# ------------------------------- Main Code ---------------------------------------

actual_to_possible()

print('Original:')
show_board()
print('\n')

unsolvable = 0
while True:
	unsolvable += 1
	
	check_row_column_quadrant()
	only_possible()
	only_possible_line()
	possible_to_actual()
	
	check_twins_and_triplets()
	possible_to_actual()
	
	finished = 0
	for row in range(9):
		for column in range(9):
			if board[row][column] != 0:
				finished += 1
	
	if finished == 81 or unsolvable == 100:
		break

print("Final:")
show_board()
if unsolvable == 100:
	print()
	print('\nUnsolvable using these methods')
print()

		

				
# Last technique is the x-wing, still not implimented
		

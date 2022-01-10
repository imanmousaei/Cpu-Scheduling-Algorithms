def arrangeArrival(n, array):
	for i in range(0, n):
		for j in range(i, n-i-1):
			if array[1][j] > array[1][j+1]:
				for k in range(0, n):
					array[k][j], array[k][j+1] = array[k][j+1], array[k][j]


def CompletionTime(n, array):
	value = 0
	array[3][0] = array[1][0] + array[2][0]
	array[5][0] = array[3][0] - array[1][0]
	array[4][0] = array[5][0] - array[2][0]
	for i in range(1, n):
		temp = array[3][i-1]
		mini = array[2][i]
		for j in range(i, n):
			if temp >= array[1][j] and mini >= array[2][j]:
				mini = array[2][j]
				value = j
		array[3][value] = temp + array[2][value]
		array[5][value] = array[3][value] - array[1][value]
		array[4][value] = array[5][value] - array[2][value]
		for k in range(0, 6):
			array[k][value], array[k][i] = array[k][i], array[k][value]


def SJF_non_preemptive():
    # <fill-here>
    n = 4
    arrival  = [2, 0, 4, 5]
    burst = [3, 4, 2, 4]
    # </fill-here>

    arr = [[int(i) for i in range(1, n+1)], arrival, burst, [0]*n, [0]*n, [0]*n]
    arrangeArrival(n, arr)
    CompletionTime(n, arr)
    print("Process Arrival Burst Completion \tWaiting \tTurnaround ")
    waitingtime = 0
    turaroundtime = 0
    for i in range(0, n):
        print(arr[0][i], "\t\t", arr[1][i], "\t\t", arr[2][i],
        "\t\t", arr[3][i], "\t\t", arr[4][i], "\t\t\t", arr[5][i])
        waitingtime += arr[4][i]
        turaroundtime += arr[5][i]
    print("Average waiting time is ", (waitingtime/n))
    print("Average Turnaround Time is ", (turaroundtime/n))


# Python3 program to implement Shortest Remaining Time First
# Shortest Remaining Time First (SRTF)

# Function to find the waiting time
# for all processes
def findWaitingTime(processes, n, wt):
	rt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rt[i] = processes[i][1]
	complete = 0
	t = 0
	minm = 999999999
	short = 0
	check = False

	# Process until all processes gets
	# completed
	while (complete != n):
		
		# Find process with minimum remaining
		# time among the processes that
		# arrives till the current time`
		for j in range(n):
			if ((processes[j][2] <= t) and
				(rt[j] < minm) and rt[j] > 0):
				minm = rt[j]
				short = j
				check = True
		if (check == False):
			t += 1
			continue
			
		# Reduce remaining time by one
		rt[short] -= 1

		# Update minimum
		minm = rt[short]
		if (minm == 0):
			minm = 999999999

		# If a process gets completely
		# executed
		if (rt[short] == 0):

			# Increment complete
			complete += 1
			check = False

			# Find finish time of current
			# process
			fint = t + 1

			# Calculate waiting time
			wt[short] = (fint - proc[short][1] -
								proc[short][2])

			if (wt[short] < 0):
				wt[short] = 0
		
		# Increment time
		t += 1

# Function to calculate turn around time
def findTurnAroundTime(processes, n, wt, tat):
	
	# Calculating turnaround time
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]

# Function to calculate average waiting
# and turn-around times.
def findavgTime(processes, n):
	wt = [0] * n
	tat = [0] * n

	# Function to find waiting time
	# of all processes
	findWaitingTime(processes, n, wt)

	# Function to find turn around time
	# for all processes
	findTurnAroundTime(processes, n, wt, tat)

	# Display processes along with all details
	print("Processes Burst Time	 Waiting",
					"Time	 Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t",
				processes[i][1], "\t\t",
				wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = ", total_tat / n)
	
def SJF_preemptive():
    # <fill-here>
    n = 4
    # Process's : [id,burst,arrival]
    proc = [[1, 6, 1], [2, 8, 1],
            [3, 7, 2], [4, 3, 3]]
    # </fill-here>

    findavgTime(proc, n)


if __name__ =="__main__":
    # SJF_non_preemptive()
    SJF_preemptive()
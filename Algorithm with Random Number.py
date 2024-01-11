import random

# Define the size of the disk
disk_size = 200

# Function to simulate the SCAN disk scheduling algorithm
def scan(arr, head, direction):
    # Initialize variables
    temp1 = 0
    temp2 = 0
    seek_count = 0
    distance, cur_track = 0, 0
    max_seek = 0  # Track the maximum seek time
    max_seek_pair = (None, None)  # Track the request pair for max seek time
    left = []  # Tracks to the left of the head
    right = []  # Tracks to the right of the head
    seek_sequence = []  # Order of tracks that the head will seek

    # Add 0 to the left list and disk_size - 1 to the right list only if 0 is not in arr
    if 0 not in arr:
        left.append(0)
    if (disk_size - 1) not in arr:
        right.append(disk_size - 1)

    # Categorize requests based on their position relative to the head
    for i in range(len(arr)):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Sort the left and right lists
    left.sort()
    right.sort()
    
    # Process requests in both directions
    run = 2
    while run != 0:
        # Process requests to the left of the head
        if direction == "left":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
                temp1 = left[1]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                # Check and update max seek time and pair
                if distance > max_seek:
                    max_seek = distance
                    max_seek_pair = (head, cur_track)
                head = cur_track
            
            # Add additional distance when crossing 0
            if run > 1 and right:
                seek_count += 1  # Add 1 for crossing 0
                
            direction = "right"
        # Process requests to the right of the head
        elif direction == "right":
            for i in range(len(right)):
                cur_track = right[i]
                temp2 = right[0]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                # Check and update max seek time and pair
                if distance > max_seek:
                    max_seek = distance
                    max_seek_pair = (head, cur_track)
                head = cur_track
            direction = "left"
        run -= 1

    temp = abs(temp1 - 0) + abs(0 - temp2)
    if temp > max_seek:
        max_seek = temp
        max_seek_pair = (temp1, temp2)
        
    # Print the results
    print("\nTotal number of seek operations for SCAN scheduling algorithm=", seek_count)
    print("Seek Sequence is")
    for track in seek_sequence:
        print(track, end=", ")
    print("\n")
    
    # Return the total seek count, max seek time, and max seek pair
    return seek_count, max_seek, max_seek_pair



# Function to simulate the C-SCAN disk scheduling algorithm
def c_scan(arr, head):
    # Initialize variables
    temp1 = 0
    temp2 = 0
    seek_count = 0  # Total number of seek operations
    distance = 0  # Distance between head and track
    cur_track = 0  # Current track being accessed
    max_seek = 0  # Maximum seek time
    max_seek_pair = (None, None)  # Pair of requests with maximum seek time
    left = []  # List to store requests to the left of the head
    right = []  # List to store requests to the right of the head
    seek_sequence = []  # Sequence of seeks performed

    # Add 0 to the left list and disk_size - 1 to the right list only if 0 is not in arr
    if 0 not in arr:
        left.append(0)
    if (disk_size - 1) not in arr:
        right.append(disk_size - 1)

    # Categorize requests based on their position relative to the head
    for i in range(len(arr)):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Sort the left and right lists
    left.sort()
    right.sort()

    # First, service the requests on the right side of the head
    for i in range(len(right)):
        cur_track = right[i]
        if (disk_size - 1) not in arr:
            temp1 = right[i-1]
        else:
            temp1 = right[i]
            
        seek_sequence.append(cur_track)  # Append current track to seek sequence
        distance = abs(cur_track - head)  # Calculate absolute distance
        seek_count += distance  # Increase the total count

        # Check and update max seek time and pair
        if distance > max_seek:
            max_seek = distance
            max_seek_pair = (head, cur_track)

        head = cur_track  # Accessed track is now the new head

    # Once reached the right end, jump to the beginning
    head = 0
    seek_count += (disk_size - 1)  # Adding seek count for head returning from end to start

    # Now service the requests on the left side
    for i in range(len(left)):
        cur_track = left[i]
        temp2 = left[1]
        seek_sequence.append(cur_track)  # Append current track to seek sequence
        distance = abs(cur_track - head)  # Calculate absolute distance
        seek_count += distance  # Increase the total count

        # Check and update max seek time and pair
        if distance > max_seek:
            max_seek = distance
            max_seek_pair = (head, cur_track)

        head = cur_track  # Accessed track is now the new head

    temp = abs(temp1 - 199) + abs(199 - 0) + abs(0 - temp2)
    if temp > max_seek:
        max_seek = temp
        max_seek_pair = (temp1, temp2)
        
    # Print the results
    print("\nTotal number of seek operations CSCAN scheduling algorithm=", seek_count)
    print("Seek Sequence is")
    for track in seek_sequence:
        print(track, end=", ")
    print("\n")
    
    # Return the total seek count, max seek time, and max seek pair
    return seek_count, max_seek, max_seek_pair


# Function to simulate the C-LOOK disk scheduling algorithm
def c_look(arr, head):
    # Initialize variables for seek count, distance, and current track
    temp1 = 0
    temp2 = 0
    seek_count = 0
    distance = 0
    cur_track = 0
    max_seek = 0  # Variable to track the maximum seek time
    max_seek_pair = (None, None)  # To track the request pair for max seek time
    left = []  # List to hold requests to the left of the head
    right = []  # List to hold requests to the right of the head
    seek_sequence = []  # List to record the sequence of seeks

    # Divide requests into left and right lists based on their position relative to the head
    for i in range(len(arr)):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Sort the left and right lists to optimize the seek sequence
    left.sort()
    right.sort()

    # First, service the requests on the right side of the head
    for i in range(len(right)):
        cur_track = right[i]
        temp1 = right[i]
        
        # Append the current track to the seek sequence
        seek_sequence.append(cur_track)

        # Calculate the absolute distance from the current head position
        distance = abs(cur_track - head)

        # Add this distance to the total seek count
        seek_count += distance

        # Check and update the maximum seek time and the corresponding track pair
        if distance > max_seek:
            max_seek = distance
            max_seek_pair = (head, cur_track)

        # Update the head position to the current track
        head = cur_track

    # Jump to the leftmost request (if any) after servicing the right side
    if left:
        seek_count += abs(head - left[0])
        head = left[0]

    # Now service the requests on the left side
    for i in range(len(left)):
        cur_track = left[i]
        temp2 = left[0]

        # Append the current track to the seek sequence
        seek_sequence.append(cur_track)

        # Calculate the absolute distance from the current head position
        distance = abs(cur_track - head)

        # Add this distance to the total seek count
        seek_count += distance

        # Check and update the maximum seek time and the corresponding track pair
        if distance > max_seek:
            max_seek = distance
            max_seek_pair = (head, cur_track)

        # Update the head position to the current track
        head = cur_track
        
    temp = abs(temp1 - temp2)
    if temp > max_seek:
        max_seek = temp
        max_seek_pair = (temp1, temp2)

    # Print the total number of seek operations and the seek sequence
    print("\nTotal number of seek operations for CLOOK scheduling algorithm =", seek_count)
    print("Seek Sequence is")
    for track in seek_sequence:
        print(track, end=", ")
    print("\n")
    
    # Return the total seek count, the maximum seek time, and the track pair with the maximum seek time
    return seek_count, max_seek, max_seek_pair


## Function to generate a list of random disk requests
def generate_requests(count):
    return [random.randint(0, 199) for _ in range(count)]

# Main simulation loop
request_sizes = [10, 20, 50, 100]

for size in request_sizes:
    print(f"\nNumber of requests: {size}")
    
    direction = 'left'  # Initial direction for SCAN algorithm
    requests = generate_requests(size)  # Generate random requests
    
    # If want to have the same result as the report can uncomment the following lines
    # if(size==10):
    #     requests=[172, 8, 15, 126, 74, 20, 151, 114, 180, 154]
    # elif(size==20):
    #     requests=[146, 169, 73, 6, 75, 6, 56, 170, 45, 185, 10, 172, 34, 186, 126, 51, 80, 42, 174, 177]
    # elif(size==50):
    #     requests=[179, 189, 123, 50, 26, 92, 123, 189, 44, 117, 25, 74, 96, 122, 58, 166, 17, 175, 91, 99, 14, 149, 106, 51, 163, 192, 72, 102, 35, 40, 164, 74, 176, 116, 44, 192, 153, 179, 136, 146, 176, 38, 180, 72, 76, 152, 171, 120, 71, 26]
    # elif(size==100):
    #     requests=[40, 28, 4, 36, 119, 148, 122, 100, 133, 177, 103, 48, 14, 199, 158, 136, 32, 186, 173, 58, 79, 57, 65, 199, 147, 80, 173, 154, 53, 139, 95, 131, 16, 197, 51, 82, 20, 57, 134, 41, 147, 101, 106, 15, 118, 60, 80, 172, 60, 133, 182, 146, 135, 178, 43, 122, 151, 159, 67, 72, 13, 88, 165, 183, 136, 64, 118, 29, 86, 132, 168, 69, 112, 149, 136, 28, 160, 59, 47, 161, 38, 134, 128, 98, 57, 135, 122, 7, 67, 20, 190, 20, 199, 86, 100, 63, 177, 198, 41, 193]
    
    current_position = 50  # Current position of the disk head
    print("Random Requests:", requests)
    
    # Run each algorithm and print the results
    scan_seek_time, scan_max_seek, scan_max_pair = scan(requests, current_position, direction)
    c_scan_seek_time, c_scan_max_seek, c_scan_max_pair = c_scan(requests, current_position)
    c_look_seek_time, c_look_max_seek, c_look_max_pair = c_look(requests, current_position)

    print(f"Average Seek Time for SCAN: {scan_seek_time / size}")
    print(f"Worst-Case Seek Time for SCAN: {scan_max_seek} between tracks {scan_max_pair} \n")
    print(f"Average Seek Time for C-SCAN: {c_scan_seek_time / size}")
    print(f"Worst-Case Seek Time for C-SCAN: {c_scan_max_seek} between tracks {c_scan_max_pair} \n")
    print(f"Average Seek Time for C-LOOK: {c_look_seek_time / size}")
    print(f"Worst-Case Seek Time for C-LOOK: {c_look_max_seek} between tracks {c_look_max_pair} \n")
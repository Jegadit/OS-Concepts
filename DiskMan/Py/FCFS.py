def FCFS(head, sequence):
    seek_operations = 0
    for i in sequence:
        if i!= head:
            print("Moving header from ", head, " to", end=" ")
            if head >= i:
                difference = head - i
                seek_operations += difference
                head = i
            if head <= i:
                difference = i - head
                seek_operations += difference
                head = i
            print(i)

    return seek_operations


if __name__ == "__main__":
    Number_disk = int(input("Enter the number of disks:	"))
    if Number_disk > 0:
        head = int(input("Enter initial header position : 	"))
        while not head in range(Number_disk + 1):
            head = int(input("Please enter valid initial head position :"))
        sequence = []
        sequence = list(map(int, input("Enter the sequence : 	").split()))
        for i in sequence:
            if i < 0 or i > Number_disk:
                print("Sequence out of range")
                exit(0)

        seek_operations = FCFS(head, sequence)
        print("Total number of seek operations : ", seek_operations)


'''
Enter the number of disks:      200
Enter initial header position :         55
Enter the sequence :    93 176 42 148 27 14 180
         Moving header from  55  to 93
         Moving header from  93  to 176
         Moving header from  176  to 42
         Moving header from  42  to 148
         Moving header from  148  to 27
         Moving header from  27  to 14
         Moving header from  14  to 180
Total number of seek operations :  661
'''
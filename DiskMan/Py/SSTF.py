def SSTF(head, sequence):
    seek_sequence = []
    seek_operations = 0
    seek_sequence.append(head)
    for i in range(len(sequence)):
        near_num = sequence[
            min(range(len(sequence)), key=lambda i: abs(sequence[i] - head))
        ]
        if head >= near_num:
            difference = head - near_num
            seek_operations += difference
            head = near_num
        if head <= near_num:
            difference = near_num - head
            seek_operations += difference
            head = near_num
        sequence.remove(near_num)
        seek_sequence.append(near_num)
    print("Seek Sequence : 	", end=" ")
    for i in seek_sequence:
        if i == seek_sequence[len(seek_sequence) - 1]:
            print(i)
        else:
            print(i, " ==> ", end=" ")
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

        seek_operations = SSTF(head, sequence)
        print("Total number of seek operations : ", seek_operations)



'''
Enter the number of disks:      200
Enter initial header position:         50
Enter the sequence:    82 170 43 140 24 16 190
Seek Sequence:      50  ==>  43  ==>  24  ==>  16  ==>  82  ==>  140  ==>  170  ==>  190
Total number of seek operations:  208
'''
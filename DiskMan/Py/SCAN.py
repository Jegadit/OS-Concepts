def max_num(head, sequence):
    for i in sequence:
        if i > head:
            return i


def min_num(head, sequence):
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] < head:
            return sequence[i]


def SCAN(N, head, sequence):
    old_head = head
    seek_sequence = []
    seek_operations = 0
    seek_sequence.append(head)
    near_num = max_num(head, sequence)
    for i in range(len(sequence)):
        if near_num > head:
            difference = near_num - head
            seek_operations += difference
            head = near_num
            seek_sequence.append(head)
            near_num = max_num(head, sequence)
        elif near_num < head:
            difference = head - near_num
            seek_operations += difference
            head = near_num
            seek_sequence.append(head)
            near_num = min_num(head, sequence)
            if head == min(sequence):
                break
        if head == max(sequence):
            near_num = min_num(old_head, sequence)
            difference = (N - 1 - head) + (N - 1 - near_num)
            seek_operations += difference
            head = near_num
            seek_sequence.append(head)
            near_num = min_num(head, sequence)
    print("Seek Sequence : 	", end=" ")
    for i in seek_sequence:
        if i == min(seek_sequence):
            print(i)
        elif i == max(sequence):
            print(i, " ==> ", N - 1, " ==> ", end=" ")
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
        sequence.sort()
        if min(sequence) < 0 or max(sequence) > Number_disk:
            print("Sequence out of range")
            exit(0)

        seek_operations = SCAN(Number_disk, head, sequence)
        print("Total number of seek operations : ", seek_operations)



'''
Enter the number of disks:      200
Enter initial header position :         55
Enter the sequence :    93 176 42 148 27 14 180
Seek Sequence :          55  ==>  93  ==>  148  ==>  176  ==>  180  ==>  199  ==>  42  ==>  27  ==>  14
Total number of seek operations :  329
'''
class Disk:
    def __init__(self, numPlaters, numOfTracks, needlePosition, seetTime):
        self.numOfPlaters = int(numPlaters)
        self.numOfTracks = int(numOfTracks)
        self.needle = int(needlePosition)
        self.seekTime = int(seetTime)

    def schedule(self, queue):
        totalSeekTime = 0
        while queue:
            temp = queue.pop(0)

            totalSeekTime += (abs(self.needle - temp))*self.seekTime
            print("Track: {} ".format(temp))

            self.needle = temp
        
        print("\nTotal seek time = {} ns".format(totalSeekTime))

diskDetails = input()

det = diskDetails.split()

diskObj = Disk(det[0], det[1], det[2], det[3])

n = input()

queue = []

for i in range(int(n)):
    queue.append(int(input()))

diskObj.schedule(queue)
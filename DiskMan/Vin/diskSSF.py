class Disk:
    def __init__(self, numPlaters, numOfTracks, needlePosition, seetTime):
        self.numOfPlaters = int(numPlaters)
        self.numOfTracks = int(numOfTracks)
        self.needle = int(needlePosition)
        self.seekTime = int(seetTime)

    def schedule(self, queue):
        totalSeekTime = 0
        while queue:
            min = abs(self.needle - queue[0])
            pos = 0

            for i in range(1, len(queue)):
                if( abs(self.needle - queue[i]) < min ):
                    min = self.needle - queue[i]
                    pos = i
            
            totalSeekTime += (abs(self.needle - queue[pos]))*self.seekTime
            self.needle = queue[pos]

            print("Track: {}".format(queue[pos]))

            queue.pop(pos)
        
        print("\nTotal seek time = {} ns".format(totalSeekTime))

diskDetails = input()

det = diskDetails.split()

diskObj = Disk(det[0], det[1], det[2], det[3])

n = input()

queue = []

for i in range(int(n)):
    queue.append(int(input()))

diskObj.schedule(queue)
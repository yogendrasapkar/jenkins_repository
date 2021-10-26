import os
# path='/home/yogendra/python'
path ='/mnt/shared_from_host'

def checkWord(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        # print('file name: ' + fileName)
        file = open(fileName,"r")
        count =0
        for line in file:
            world = line.split(" ")
            count += len(world)
        file.close()
        print(fileName,"-->" ,count,"(words)")
        

if __name__ == '__main__':
    checkWord(path)





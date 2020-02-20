import operator


books = [] #index = book id, value = score
libraries = [] #
totaltime = 0 #holds total number of days

#signup should be none if there are no books in the process of signing up
#or libraries[x] if a library is signing up
#for every day that passes, libraries[x].time decreases by 1 until
#it's at 0
scanned = [] #array of libraries that have signed up


class Library:
    def __init__(self, _id, books, time, num):
        self.id = _id #int - library id
        self.books = books #array of ints
        self.time = time #int - time to sign up
        self.scanRate = num #int - num of books that can be scanned
        self.scanned = [] #array of ints: bookIds that have been scanned
        
    
def readData(fname):
    global totaltime
    global books
    #global libraries

    f=open(fname, "r")
    lines = f.readlines()
    f.close()
    
    #gets test parameters
    (bks, libs, days) = [int(val) for val in lines[0].split(' ')]
    totaltime += days
    for score in lines[1].split(' '):
        books.append(int(score))

    # gets values for each library and its books
    for i in range(2, len(lines), 2):
        (numBooks, signupTime, shipRate) = [int(val) for val in lines[i].split(' ')]
        bookIds = [int(id) for id in lines[i+1].split(' ')]
        libraries.append(Library(i-2, bookIds, signupTime, shipRate))


def printResult(fname):
    f= open(fname,"w")
    
    f.write(str(len(scanned)) + "\n")
    
    for i in range(len(scanned)):
        f.write(str(scanned[i].id) + " " + str(len(scanned[i].scanned)) + "\n")
        
        t = " ".join(str(book) for book in scanned[i].scanned)
        f.write(t + "\n")
    
    f.close()
    
def bookScanning(fin, fout):
    
    readData(fin)
    

    shipped = [False]*len(books)
    queue = sorted(libraries, key=operator.attrgetter('time', 'scanRate'), reverse=True)
    
    currentDay = 0
    # scanned.append(queue.pop())
    # currentDay += scanned[0].time
    setuplib = queue.pop()
    
    while currentDay < totaltime:
        if(setuplib.time > 0):
            setuplib.time-=1
        elif setuplib.time == 0:
            scanned.append(setuplib)
            if len(queue) > 0:
                setuplib = queue.pop()
            
            
        for library in scanned:
            sentBooks = 0
            while(sentBooks<library.scanRate and len(library.books)>0):
                currentBook = library.books.pop(0)
                if(not shipped[currentBook]):
                    shipped.append(currentBook)
                    library.scanned.append(currentBook)
                    sentBooks += 1
        
        currentDay += 1 

    printResult(fout)

bookScanning("b_read_on.txt", "out.txt")
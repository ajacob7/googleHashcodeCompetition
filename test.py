import operator

#signup should be none if there are no books in the process of signing up
#or libraries[x] if a library is signing up
#for every day that passes, libraries[x].time decreases by 1 until
#it's at 0
signedUp = [] #array of libraries that have signed up

books = [] #index = book id, value = score
libraries = [] #
totaltime = 0 #holds total number of days

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

    # f=open(fname, "r")
    # lines = f.readlines()
    with open(fname) as f_in:
        lines = list(line for line in (l.strip() for l in f_in) if line)
    f_in.close()
    
    # gets test parameters
    days = int(lines[0].split(' ')[2])
    totaltime += days
    for score in lines[1].split(' '):
        books.append(int(score))

    # # gets values for each library and its books
    for i in range(2, len(lines), 2):
        # print(i+1, "::", lines[i].split(' '))
        signupTime = int(lines[i].split(' ')[1])
        shipRate = int(lines[i].split(' ')[2])
        booksInLib = [int(id) for id in lines[i+1].split(' ')]
        libraries.append(Library(int((i/2)-1), booksInLib, signupTime, shipRate))


def printResult(fname):
    f= open(fname,"w")
    
    f.write(str(len(signedUp)) + "\n")
    
    for i in range(len(signedUp)):
        f.write(str(signedUp[i].id) + " " + str(len(signedUp[i].scanned)) + "\n")
        
        t = " ".join(str(book) for book in signedUp[i].scanned)
        f.write(t + "\n")
    
    f.close()
    
def bookScanning(fin, fout):
    readData(fin)

    shipped = [False]*len(books)
    queue = sorted(libraries, key=operator.attrgetter('time', 'scanRate'), reverse=True)
    
    currentDay = 0
    setuplib = queue.pop()
    
    while currentDay < totaltime:
        if(setuplib.time > 0):
            setuplib.time-=1
        elif setuplib.time == 0:
            signedUp.append(setuplib)
            if len(queue) > 0:
                setuplib = queue.pop()
            
            
        for library in signedUp:
            sentBooks = 0
            while(sentBooks<library.scanRate and len(library.books)>0):
                currentBook = library.books.pop(0)
                if(not shipped[currentBook]):
                    shipped.append(currentBook)
                    library.scanned.append(currentBook)
                    sentBooks += 1

        print("Total time:: ", totaltime, "Days Left:: ", totaltime - currentDay)
        currentDay += 1 
        

    printResult(fout)

inFiles = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "f_libraries_of_the_world.txt", "e_so_many_books.txt"]
outFiles = ["a_out.txt", "b_out.txt", "c_out.txt", "d_out.txt", "e_out.txt", "f_out.txt"]

#input should be the corresponding indexes of the desired input files
def runFiles(*files):
    for file in files:
        print("Current File:: " + inFiles[file])
        bookScanning("InData//" + inFiles[file], "OutData//" + outFiles[file])

runFiles(0,1,2,3,4,5)

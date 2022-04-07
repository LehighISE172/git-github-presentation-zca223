'''
Brief description:
Contains Tree class which draws a random tree using turtle graphics

Detailed description:
Classes contained:
Tree:
    attributes:
        turtle:        turtle object, more info can be found on official
                       Python documentation 
                       type: turtle.Turtle
        meanBranchLength:
                       mean branch Length in pixels
                       type: int
        drawMode:      changes draw mode, either RECURSIVE or NONRECURSIVE, if
                       it is RECURSIVE, draw_r() method is used, if
                       NONRECURSIVE, draw_nr() method is used.
                       type: string
        myWin:         turtle graphics screen
                       type: TurtleScreen
    methods:
        __init__(self, drawMode = RECURSIVE, meanBranchLength = 100,
                 randomSeed = 0):
                       sets drawMode, meanBranchLength, uses randomSeed as
                       seed input for random module creates turtle instance
        draw(self, meanBanchLen):
                       draws tree by calling either draw_r() or draw_nr()
                       method
        draw_r(self, meanBranchLength):
                       recursive function that draws random tree given mean
                       branch length
        draw_nr(self):
                       draws random tree using stack data structure 
'''

#importing the random and seed packages to adjust for randomness
from random import seed, randint

# from within our tree folder referencing data structure python codes to open Queue and Stack
from dataStructures.Queue import Queue
from dataStructures.Stack import Stack

__version__ = '1.0.0'
__author__ = 'Aykut Bulut, Ted Ralphs (ayb211@lehigh.edu,ted@lehigh.edu)'
__license__ = 'BSD'
__maintainer__ = 'Aykut Bulut'
__email__ = 'ayb211@lehigh.edu'
__title__ = 'Recursive Tree'

from turtle import *

#Global constants
EPS = 0.000000001
RECURSIVE = 'recursive'
NONRECURSIVE = 'nonrecursive'
#Global variables
counts = {}
#Random lengths of tree branches
randomVal = randint(80,100)


def counter(func):
    counts[func.__name__] = 0

    def wrapper(*arg):
        counts[func.__name__] += 1
        res = func(*arg)
        return res
    return wrapper


class Tree(object):
    '''
    Tree class which draws a random tree using turtle graphics.
    '''

    def __init__(self, drawMode=RECURSIVE, meanBranchLength=100,
                 randomSeed=0):
        '''
        Sets drawMode, meanBranchLength, uses randomSeed as seed input for
        random module creates turtle instance.
        Inputs:
            drawMode:
            meanBranchLength:
            randomSeed:
        Post: Sets drawMode and meanBranchLength. Calls seed(randomSeed)
        '''
        seed(randomSeed)
        self.turtle = Turtle()
        self.meanBranchLength = meanBranchLength
        self.drawMode = drawMode

    def draw(self, meanBranchLen=None):
        '''
        Draws tree by calling either draw_r() or draw_nr() method.
        Inputs:
            meanBanchLen:
        Post: myWin and turtle are initialized.
        '''
        if meanBranchLen == None:
            meanBranchLen = self.meanBranchLength
        self.myWin = self.turtle.getscreen()
        self.turtle.left(90)
        self.turtle.up()
        self.turtle.backward(300)
        self.turtle.down()
        self.turtle.pensize(20)
        self.turtle.speed(0)
        if self.drawMode == RECURSIVE:
            self.draw_r(meanBranchLen)
        elif self.drawMode == NONRECURSIVE:
            self.draw_nr(meanBranchLen)
        else:
            raise Exception("Unknown drawing mode")
        self.myWin.exitonclick()

    @counter
    def draw_r(self, branchLen):
        '''
        Recursive function that draws random tree given mean branch length.
        Post: turtle updated.
        '''

        # I have been working in the NONRECURSIVE for my changes left this to display original tree
        # Not using Recursive part for my changes to program
        if branchLen > 5:
            self.turtle.forward(branchLen)
            self.turtle.right(20)
            self.draw_r(branchLen-15)
            self.turtle.left(40)
            self.draw_r(branchLen-10)
            self.turtle.right(20)
            self.turtle.backward(branchLen)

    def draw_nr(self, branchLen):
        '''
        Draws random tree using stack data structure.
        Post: turtle is changed.
        '''

        '''
        The non-recursive implementation draws the same tree as the 
        recursive implementation because it goes through all values in the stack or 
        the queue, the same with the recursive implementation.
        It simply does it through a while loop.
        '''
        # choose either stack or Queue to comment out depending on which method you want to use
        # I like doing stack more so I changed it to produce a tree with random lengths better
        # s = Queue()
        s = Stack()
        x = 10 #initilializng a color changing variable
        while True:
            self.turtle.pendown()
            if branchLen > 5:
                if x >= 5:  # if x is below threshold the color is brown towards bottom branch
                    self.turtle.color('brown')
                elif x < 5:  # if x is above a certain theshold the color is green which draws the leaves
                    self.turtle.color('green')

                self.turtle.forward(branchLen)
                self.turtle.left(20)
                # decreasing branch length by random value pushing from either stack or queue
                s.push((branchLen-randint(8, 16),
                        self.turtle.position(),
                        self.turtle.heading(), x-1))
                self.turtle.right(40)
                # decreasing branch length by random value pushing from either stack or queue
                s.push((branchLen-randint(8, 16), 
                        self.turtle.position(),
                        self.turtle.heading(), x-1))
                self.turtle.left(20)
                self.turtle.backward(branchLen)
                #finally drawing ends when nothing left to iterate in the list
                if s.isEmpty():
                    break
            branchLen, p, h, x = s.pop()
            self.turtle.pensize(x)
            self.turtle.setheading(h)
            self.turtle.penup()
            self.turtle.goto(p)

            # tracking in console the length of branch as it changes
            print("Branch length = ", branchLen)

# choosing to work in nonrecursive
t = Tree(NONRECURSIVE)
t.draw(randomVal)
for k in counts:
    print(k, counts[k])
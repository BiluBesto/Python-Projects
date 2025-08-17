import curses
from curses import wrapper
import queue
import time
maze = [
    ['O',' ',' ',' ','#'],
    [' ','#',' ',' ',' '],
    ['#',' ','#',' ','#'],
    ['#',' ',' ',' ','#'],
    ['#','X','#',' ','#']
]
def dispmaze(maze,stdscr,path=[]):
    blue=curses.color_pair(2)
    red=curses.color_pair(1)
    for i,row in enumerate(maze):
        for j,col in enumerate(row):
            if(i,j) in path:
                stdscr.addch(i,j*2,'X',red)
            else:
                stdscr.addch(i,j*2,col,blue)

def findstart(maze,start):
    for i,row in enumerate(maze):
        for j,col in enumerate(row):
            if col==start:
                return i,j
    return None

def findpath(maze,stdscr):
    start='O'
    end='X'
    start_pos=findstart(maze,start)
    q=queue.Queue()
    q.put((start_pos,[start_pos]))
    visited = set()
    while not q.empty():
        current_pos ,path=q.get()
        row ,col=current_pos
        stdscr.clear()
        dispmaze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()
        if maze[row][col]==end:
            return path
        neighbours=uppath(maze,row,col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            r,c = neighbour
            if maze[r][c]=='#':
                continue
            newpath=path+[neighbour]
            q.put((neighbour,newpath))
            visited.add(neighbour)

def uppath(maze,row,col):
    ne=[]
    if row>0:
        ne.append((row-1,col))
    if row+1<len(maze):
        ne.append((row+1,col))
    if col>0:
        ne.append((row,col-1))
    if col+1<len(maze[0]):
        ne.append((row,col+1))
    return ne
def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    findpath(maze,stdscr)
    stdscr.getch()
wrapper(main)
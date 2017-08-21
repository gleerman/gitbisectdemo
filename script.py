#!/usr/bin/python

from random import randint
from subprocess import call


filename = "file.txt"

rightWord = "good"
wrongWord = "bad"
totalWrites = 300


def commit(nr):
    message = "Commit nr. " + str(nr)
    call(["git", "commit", "-a", "-m", message])
    

def doWrite(good):
    with open(filename, 'a') as file:
        if (good): 
            file.write(rightWord + "\n")
        else:
            file.write(wrongWord + "\n")


def main():
    # reset to clean state
    call(["git", "checkout", "feature"])
    call(["git", "reset", "--hard", "master"])
    open(filename, 'w').close
    
    # start committing
    wrongCommit = randint(0, totalWrites - 1)
    for i in range(0, totalWrites):
        doWrite(i != wrongCommit)
        commit(i)


if __name__ == "__main__":
    main()

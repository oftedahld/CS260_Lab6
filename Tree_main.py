#
#  main.cpp
#  getNext_search_tree
#
#  Created by Jim Bailey on 4/25/20.
#  Updated by Jim Bailey 5/6/21
#  Licensed under a Creative Commons Attribution 4.0 International License.
#
#  Transpiled to Python by Katie Strauss 5/6/21

from Tree import Tree

def main():

    # Basic lab requirements
    testInsertInOrder()
    testFind()
    testRemove()

    # Advanced lab requirements
    testFindLarger()
    testRemoveLarger()


# Basic lab requirements
def testInsertInOrder():
    fir = Tree()
    int_values=  [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 0, -2]

    print("\nTesting insertValue and inOrder traversal ")

        # build a nice noble fir that is balanced
    print(" Insert and display 17 even integers ")
    try:
        for value in int_values:
            fir.insertValue(value)
    
            # display the tree, should be even integers in order
        print(" InOrder expected -2 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30")
        try:
            print("  and it is " + fir.inOrder())
        except:
            print(" Failed test of inOrder traversal", end="\n\n")
    
        print(" PreOrder expected 16 8 4 2 0 -2 6 12 10 14 24 20 18 22 28 26 30")
        try:
            print("  and it is " + fir.preOrder())
        except:
            print(" Failed test of preOrder traversal", end="\n\n")
    
        print(" PostOrder expected -2 0 2 6 4 10 14 12 8 18 22 20 26 30 28 24 16")
        try:
            print("  and it is " + fir.postOrder())
        except:
            print(" Failed test of postOrder traversal", end="\n\n")
    except:
        print(" Failed test of insertValue")

    print("\nEnd test insertValue and displayTree\n")


def testFind():
    try:
        primes = [19, 11, 29, 5, 3, 7, 13, 17, 23, 31, 37]
        oak = Tree()

        print("Testing findValue ")

        print(" Add and display 11 primes ")
        for value in primes:
            oak.insertValue(value)

        print("  " + oak.inOrder())

        print(" Should find 5 and 23, not find 21 or 2: ")
        print("  Looking for 5 ", end="")
        if oak.findValue(5):
            print("found")
        else:
            print("not found")
        print("  Looking for 23 ", end="")
        if oak.findValue(23):
            print("found")
        else:
            print("not found")
        print("  Looking for 21 ", end="")
        if oak.findValue(21):
            print("found")
        else:
            print("not found")
        print("  Looking for 2 ", end="")
        if oak.findValue(2):
            print("found")
        else:
            print("not found")

        print("End of test findValue", end="\n\n")
    except:
        print(" Failed test of findValue", end="\n\n")


def testRemove():
    # test deleteValue
    try:
        odds = [15, 7, 23, 3, 11, 19, 27, 1, 5, 9, 13, 17, 21, 25, 29, -1]
        plum = Tree()

        print("Testing removeValue ")

        print(" Add and display 15 odd numbers plus -1")
        for value in odds:
            plum.insertValue(value)

        print("  " + plum.inOrder())

        print(" Now testing remove, 9 should be there and then gone ")
        print("  Looking for 9 ", end="")
        if plum.removeValue(9):
            print("found")
        else:
            print("not found")
        print("  Looking for 9 ", end="")
        if plum.findValue(9):
            print("found")
        else:
            print("not found")
            
        print(" Displaying tree after removing 9 ")
        print("  InOrder expected -1 1 3 5 7 9D 11 13 15 17 19 21 23 25 27 29")
        print("  and actually is  " + plum.inOrder())

        print("\n Now checking if branch was burned on delete.  Should still find children of 9.")
        print("  Looking for 11 ", end="")
        if plum.findValue(11):
            print("found")
        else:
            print("not found")
        print("  Looking for 7 ", end="") #changed search value from 7 to 9, doesn't make sense that it would state it's looking for 9 but instead look for 7
        if plum.findValue(7):
            print("found")
        else:
            print("not found")

        print(" Now seeing if adding 9 back works")
        plum.insertValue(9)
        print("  Looking for 9 ", end="")
        if plum.findValue(9):
            print("found")
        else:
            print("not found")
            
        print(" Displaying tree after adding 9 back ")
        print("  InOrder expected -1 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29")
        print("  and actually is  " + plum.inOrder())

        print("End of test removeValue", end="\n\n")
    except:
        print(" Failed test of removeValue", end="\n\n")


# Advanced lab requirements
def testFindLarger():
    try:
        nums = [30, 15, 45, 7, 23, 3, 10, 18, 24, 36, 52, 33, 40, 48, 64]
        apple = Tree()

        print("Testing findLarger ")

        print(" Add and display 15 integers ")
        for value in nums:
            apple.insertValue(value)

        print("  " + apple.inOrder())

        print(" Now testing findLarger ")
        print("  1 should return 3 and returns " + str(apple.findLarger(1)))
        print("  4 should return 7 and returns " + str(apple.findLarger(4)))
        print("  9 should return 10 and returns " + str(apple.findLarger(9)))
        print("  12 should return 15 and returns " + str(apple.findLarger(12)))
        print("  16 should return 18 and returns " + str(apple.findLarger(16)))
        print("  30 should return 30 and returns " + str(apple.findLarger(30)))
        print("  34 should return 36 and returns " + str(apple.findLarger(34)))
        print("  40 should return 40 and returns " + str(apple.findLarger(40)))
        print("  43 should return 45 and returns " + str(apple.findLarger(43)))
        print("  47 should return 48 and returns " + str(apple.findLarger(47)))
        print("  62 should return 64 and returns " + str(apple.findLarger(62)))
        print("  90 should return -1 and returns " + str(apple.findLarger(90)))

        print("End of test findLarger", end="\n\n")
    except:
        print(" Failed test of findLarger", end="\n\n")


def testRemoveLarger():
    try:
        vals = [15, 8, 24, 4, 11, 19, 30, 2, 7, 10, 13, 16, 22, 28, 34]
        pear = Tree()

        print("Testing removeLarger ")

        print(" Add and display 15 integers ")
        for value in vals:
            pear.insertValue(value)

        print("  " + pear.inOrder())

        print(" Now testing removeLarger ")
        print("  5 should return 7 and returns " + str(pear.removeLarger(5)))
        print("  7 should be gone and is ", end="")
        if pear.findValue(7):
            print("found")
        else:
            print("not found")

        print("  19 should return 19 and returns " + str(pear.removeLarger(19)))
        print("  19 should be gone and is ", end="")
        if pear.findValue(19):
            print("found")
        else:
            print("not found")

        print("\n Same as above values, but without 7 and 19")
        print("  " + pear.inOrder())

        # verifying tree traversal after delete
        # potentially burning a branch
        print("  11 should return 11 and returns " + str(pear.removeLarger(11)) + "\n")
        print("  11 should be gone and is ", end="")
        if pear.findValue(11):
            print("found")
        else:
            print("not found")

        print("  9 should return 10 and returns " + str(pear.removeLarger(9)) + "\n")
        print("  15 should still be present and is ", end="")
        if pear.findValue(15):
            print("found")
        else:
            print("not found")

        print("End of test removeLarger", end="\n\n")
    except:
        print(" Failed test of removeLarger", end="\n\n")


if __name__ == "__main__":
    main()

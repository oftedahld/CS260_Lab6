class TreeNode:
    def __init__(self, value=""):
        self.value = value
        self.left = None
        self.right = None
        self.present = True
    
    def __str__(self):
        """Created custom string operator to display nodes by their value and the value of their children"""
        leftValue = ""
        rightValue = ""
        if self.left != None:
            leftValue = str(self.left.getValue())
        if self.right != None:
            rightValue = str(self.right.getValue())
        outputString = "[L:" + leftValue + "|V:" + str(self.value) + "|R:" + rightValue + "]"
        return outputString

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setPresent(self, present):
        self.present = present

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getValue(self):
        return self.value  

    def getPresent(self):
        return self.present

class Tree:
    
    def __init__(self):
        self.root = None

    def insertValue(self, value):
        """add a new node containing value to the tree"""
        if self.root == None:
            temp = TreeNode(value)
            self.root = temp
            # print (f"Root set as {temp}") #TEMP FOR TESTING ONLY
            return
        self.recInsertValue(value, self.root)

    def recInsertValue(self, value, ptr):
        if value < ptr.getValue():
            if ptr.getLeft() == None: #When the left of the root is empty, space is open for new node
                temp = TreeNode(value)
                ptr.setLeft(temp)
                # print (f"{temp} added to set to left of {ptr}") #TEMP FOR TESTING ONLY
            else: #When left of root was not empty, need to 
                self.recInsertValue(value, ptr.getLeft())
        else:
            if ptr.getValue() == value and ptr.getPresent() == False: #If the righ child was not empty, but the value is the same and the current item was marked as deleted, unmark deletion
                ptr.setPresent(True)
            elif ptr.getRight() == None:
                temp = TreeNode(value)
                ptr.setRight(temp)
                # print (f"{temp} added to set to right of {ptr}") #TEMP FOR TESTING ONLY
            else:
                self.recInsertValue(value, ptr.getRight())

    def findValue(self, value):
        """return true if there is a node containing value, false otherwise"""
        ptr = self.root
        while ptr != None:
            checkValue = ptr.getValue()
            if checkValue == value and ptr.getPresent():
                return True
            if value < checkValue:
                ptr  = ptr.getLeft()
            else:
                ptr = ptr.getRight()
        return False

    def removeValue(self, value):
        """if there is a node in the tree containing value, remove it and return true. If there is not such a node, return false. You should mark it as removed, not actually remove the node."""
        ptr = self.root
        while ptr != None:
            checkValue = ptr.getValue()
            if checkValue == value and ptr.getPresent():
                ptr.setPresent(False)
                return True
            if value < checkValue:
                ptr = ptr.getLeft()
            else:
                ptr = ptr.getRight()
        return False
            

    def preOrder(self):
        """return a string containing a prefix listing of the tree’s contents. If a node was deleted, add a D to its value. This method must be coded recursively."""
        return self.recPreOrder(self.root)
    
    def recPreOrder(self, ptr):
        """Recursive function to perform pre-order traversal"""
        buffer = ""
        if ptr == None:
            return buffer
        if ptr.getPresent():
            buffer += (str(ptr.getValue()) + " ")
        else:
            buffer += (str(ptr.getValue()) + "D ")
        buffer += self.recPreOrder(ptr.getLeft())
        buffer += self.recPreOrder(ptr.getRight())
        return buffer

    def inOrder(self):
        """return a string containing an infix listing of the tree’s contents. If a node was deleted, add a D to its value. This method must be coded recursively."""
        return self.recInOrder(self.root)

    def recInOrder(self, ptr):
        """Recursive function to perform in-order traversal"""
        buffer = ""
        if ptr == None:
            return buffer
        buffer += self.recInOrder(ptr.getLeft())
        if ptr.getPresent():
            buffer += (str(ptr.getValue()) + " ")
        else:
            buffer += (str(ptr.getValue()) + "D ")
        buffer += self.recInOrder(ptr.getRight())
        return buffer

    def postOrder(self):
        """return a string containing a postfix listing of the tree’s contents. If a node was deleted, add a D to its value. This method must be coded recursively."""
        return self.recPostOrder(self.root)
    
    def recPostOrder(self, ptr):
        """Recursive function to perform post-order traversal"""
        buffer = ""
        if ptr == None:
            return buffer
        buffer += self.recPostOrder(ptr.getLeft())
        buffer += self.recPostOrder(ptr.getRight())
        if ptr.getPresent():
            buffer += (str(ptr.getValue()) + " ")
        else:
            buffer += (str(ptr.getValue()) + "D ")
        return buffer

    def findLarger(self, value):
        """– search for a node containing value and return value if such a node is found. If no such node is found, return the next larger value in the tree. If there are no larger values in the tree, return -1."""
        ptr = self.root
        return self.recFindLarger(value, ptr)
  
    # def recFindLarger(self, value, ptr):
    #     nodeValue = ptr.getValue()
    #     nodePresent = ptr.getPresent()
    #     if nodeValue == value and nodePresent:
    #         return value
    #     elif nodeValue > value:
    #         leftNode = ptr.getLeft()
    #         if leftNode == None:
    #             return nodeValue
    #         else:
    #             leftNodeValue = leftNode.getValue()
    #         if leftNodeValue == value:
    #             return value
    #         elif leftNodeValue < value:
    #             checkLeft = self.recFindLarger(value, leftNode)
    #             if checkLeft > -1:
    #                 return checkLeft
    #             else:
    #                 return nodeValue
    #         elif leftNodeValue > value:
    #             return self.recFindLarger(value, leftNode)
    #     elif nodeValue < value:
    #         rightNode = ptr.getRight()
    #         if rightNode == None:
    #             return -1
    #         else:
    #             rightNodeValue = rightNode.getValue()
    #         if rightNodeValue == value:
    #             return value
    #         else:
    #             return self.recFindLarger(value, rightNode)


    def recFindLarger(self, value, ptr):
        nodeValue = ptr.getValue()
        nodePresent = ptr.getPresent()
        if nodeValue == value and nodePresent:
            return value
        elif nodeValue > value:
            leftNode = ptr.getLeft()
            if leftNode == None:
                if nodePresent:
                    return nodeValue
                else:
                    return -1
            else:
                leftNodeValue = leftNode.getValue()
                leftNodePresent = leftNode.getPresent()
            if leftNodeValue == value and leftNodePresent:
                return value
            elif leftNodeValue < value:
                checkLeft = self.recFindLarger(value, leftNode)
                if checkLeft > -1:
                    return checkLeft
                else:
                    if nodePresent:
                        return nodeValue
                    else:
                        return -1
            elif leftNodeValue > value:
                return self.recFindLarger(value, leftNode)
        elif nodeValue < value:
            rightNode = ptr.getRight()
            if rightNode == None:
                return -1
            else:
                rightNodeValue = rightNode.getValue()
                rightNodePresent = rightNode.getPresent()
            if rightNodeValue == value and rightNodePresent:
                return value
            else:
                return self.recFindLarger(value, rightNode)



    
    def removeLarger(self, value):
        """similar to findLarger but removes the node before returning."""
        ptr = self.root
        return self.recRemoveLarger(value, ptr)
        
    def recRemoveLarger(self, value, ptr):
        nodeValue = ptr.getValue()
        nodePresent = ptr.getPresent()
        if nodeValue == value and nodePresent:
            ptr.setPresent(False)
            return value
        elif nodeValue > value:
            leftNode = ptr.getLeft()
            if leftNode == None:
                if nodePresent:
                    ptr.setPresent(False)
                    return nodeValue
                else:
                    return -1
            else:
                leftNodeValue = leftNode.getValue()
                leftNodePresent = leftNode.getPresent()
            if leftNodeValue == value and leftNodePresent:
                leftNode.setPresent(False)
                return value
            elif leftNodeValue < value:
                checkLeft = self.recRemoveLarger(value, leftNode)
                if checkLeft > -1:
                    return checkLeft
                else:
                    if nodePresent:
                        ptr.setPresent(False)
                        return nodeValue
                    else:
                        return -1
            elif leftNodeValue > value:
                return self.recRemoveLarger(value, leftNode)
        elif nodeValue < value:
            rightNode = ptr.getRight()
            if rightNode == None:
                return -1
            else:
                rightNodeValue = rightNode.getValue()
                rightNodePresent = rightNode.getPresent()
            if rightNodeValue == value and rightNodePresent:
                rightNode.setPresent(False)
                return value
            else:
                return self.recRemoveLarger(value, rightNode)
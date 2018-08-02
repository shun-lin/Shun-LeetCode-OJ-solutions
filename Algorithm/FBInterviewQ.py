# Given a Binary Tree, find if it's possible to cut the tree into two halfs of equal sums. Only cut one edge

# Questions:
# Is the binary tree BST or just binary tree?
# Are the binary tree storing int or floats?
# Are inputs valid BT or can it be null?
# can there be any negative numbers?
# for a given input, are there multiple possible valid cuts or just one?
# can we modify the original tree? Like adding an attribute to the node?

# input: BT, output: boolean

# example

#   1
#  2  3

# return true because we can put 1 - 3 to got 3 and 3

# naive idea: perform all possible cut and check if the halfs are the same
# runtime: n nodes, which means we have n - 1 edges, thus we will do n - 1 cuts, and without memo
# caluating sum of halfs will take n times so O(n^2), can improve

# better idea: perform a one down pass down the tree to find the sum of all subtrees at each node and store them
# then use a "binary search" style check to find the cut
# first pass will be O(n)
# second pass will be O(log n)
# thus the runtime is O(n)

# assumption
# TreeNode has the following attributes
# .left , .right, .val

def canBeCutInHalf(bt):

    # Null checking
    if (bt is None):
        return False

    # create a "running sum" binary tree where each node is the
    def createRunningSumTree(bt):

        # null checking and base case
        if (bt is None):
            return None

        # initialize the tree node to itself
        runningTree = TreeNode(bt.val)

        leftRunningTree = createRunningSumTree(bt.left)
        rightRunningTree = createRunningSumTree(bt.right)

        runningTree.left = leftRunningTree
        runningTree.right = rightRunningTree

        if (runningTree.left != null):
            runningTree.val += runningTree.left.val
        if (runningTree.right != null):
            runningTree.val += runningTree.right.val

        return runningTree

    runningSumTree = createRunningSumTree(bt)

    # get the current node we are looking at
    currentNode = bt
    currentRunningSumNode = runningSumTree

    headSum = 0
    solved = False

    while (not solved and currentNode not None):
        # will solve

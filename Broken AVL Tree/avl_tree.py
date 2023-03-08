"""
AVL Tree implementation

CISC320 Algorithms Spring 2023

1. Line 27: self.height: int = 3,  Height of one node is given three on a tree while it should be zero since the height of the tree node starts at zero. Thus, according to the height it should be one
2. Line 70: Had to return if there is nothing given, test on empty tree structure, if local_root is None:
            # Return all the values on the left
            yield from self._traverse_from_node(local_root.left)
            # Return this node's value
            yield local_root.value
            # Return all the values on the right
            yield from self._traverse_from_node(local_root.right), we should indicate if the tree structure is legit just the root, return because an empty tree structure returns nothing. I added an if else case if the tree has no node, return none otherwise,
            call the traverse from node functions (Preorder, postorder and in order)
3. Line 124: needs to indicate the balance when you are rotating,  # Case 3 - Right Left Rotation
                root.right = self._right_rotate(root.right). I've modified it to include
4. Line 173: Returns the min of the function, since _get_max_height_of_children returns the maximum height of children, I modified the min in the return statement to a max as it returns the max value instead of the minimum
5. Line 96:  root.right = self._insert_at(root.right, new) We want to insert the root at the left of the tree structure. I've changed it to update the roots left value to insert the root root.left = self._insert_at(root.left, new)
at the left node
6. Line 148-149: local_root.height = 1 + self._get_max_height_of_children(local_root), right_child.height = 1 + self._get_max_height_of_children(right_child), each node (other than the root has a height of one so we add the one to level). I've modified it to add one each time
7. Line 172-173: The last bug was updating the left child's right node became the local root in the right rotation function but updated the left childs right again to be the grand child which was
hella of confusing, thus throwing an maximum recursion depth. Once visualizing it out, the left childs right value should be the root and the left childs root should be the grand children. 
 left_child.right = local_root
        local_root.right = left_right_grandchild
"""


class TreeNode:
    """
    Simple class to hold the data for a Tree Node; has no methods, just the children, height, and node value.
    
    Leaf nodes (without children) have the value None for their `left` and `right` attributes.
    """

    def __init__(self, value):
        self.value = value
        self.left: TreeNode = None
        self.right: TreeNode = None
        #Bug found, if the tree does not have children its height should be one as the initial value of the "root" should be one
        #Height of one node is given three on a tree (line 27)
        self.height: int = 0

    def __str__(self):
        return f"<TreeNode({self.value})>"

    def tree(self):
        return f"{self.value}({self.left.tree() if self.left else '_'},{self.right.tree() if self.right else '_'})"


class AVLTree:
    """
    An implementation of an AVL Tree, supporting `insert` and `traverse`.
    
    The constructor consumes a list of comparable values to be inserted immediately.
    """

    def __init__(self, starting_values: list):
        # Root starts off as None
        self.root: TreeNode = None

        # Add in any starting values
        for starting_value in starting_values:
            self.insert(starting_value)

    def traverse(self) -> list:
        """
        Traverse the tree starting from the root node, in order.
        """
        # The `_traverse_from_node` function returns a generator,
        # so we need to convert that to a list.
        return list(self._traverse_from_node(self.root))

    def _traverse_from_node(self, local_root: TreeNode) -> list:
        """
        Traverse the tree starting from the given node, in order.
        
        If you don't know about `yield` statements, then be sure
        to google about them! They let you return a value from a
        function, but continue execution past that point. This
        effectively produces a list (or more accurately, a "generator"
        that can be turned into a list).
        """
        # If there is no root, then there's nothing to traverse
        if local_root is None:
            return
        else:
            yield from self._traverse_from_node(local_root.left)
            # Return this node's value
            yield local_root.value
            # Return all the values on the right
            yield from self._traverse_from_node(local_root.right)

    def insert(self, new) -> TreeNode:
        """
        Add the given `new` value at the root of the tree. Returns the root TreeNode.
        """
        # Uses a helper function, so that we provide a cleaner interface
        self.root = self._insert_at(self.root, new)
        return self.root

    def _insert_at(self, root: TreeNode, new) -> TreeNode:
        """
        Add the given `new` value, starting from the given `root`. Returns the given root.
        """
        # Step 1 - Perform normal Binary Search Tree insertion behavior
        if root is None:
            # This is a new leaf!
            return TreeNode(new)
        elif new < root.value:
            # Add to the left
            root.left = self._insert_at(root.left, new)
        else:
            # Add to the right
            root.right = self._insert_at(root.right, new)

        # Step 2 - Update the height of the given root node
        root.height = 1 + self._get_max_height_of_children(root)

        # Step 3 - Get the balance factor
        balance: int = self._get_balance(root)

        # Step 4 - If the node is unbalanced, then try out the 4 cases
        # Left
        if balance > 1:
            if self._get_balance(root.left) < 0:
                # Case 1 - Left Right Rotation
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)
            else:
                # Case 2 - Right Rotation
                return self._right_rotate(root)
        # Right
        if balance < -1:
            if self._get_balance(root.right) > 0:
                # Case 3 - Right Left Rotation
                root.right = self._right_rotate(root.right)
                #bug needs to indicate the balance when you are rotating
                return self._left_rotate(root)
            else:
                # Case 4 - Left Rotation
                return self._left_rotate(root)

        # Return the root
        return root

    def _left_rotate(self, local_root: TreeNode) -> TreeNode:
        """
        Swap the given root with its right child.
        """
        # Get right child and right-left grandchild
        right_child: TreeNode = local_root.right
        right_left_grandchild: TreeNode = right_child.left

        # Actual rotation
        right_child.left = local_root
        local_root.right = right_left_grandchild

        # Update heights
        local_root.height = 1 + self._get_max_height_of_children(local_root)
        right_child.height = 1 + self._get_max_height_of_children(right_child)

        # Return the new root
        return right_child

    def _right_rotate(self, local_root: TreeNode) -> TreeNode:
        """
        Swap the given root with its left child.
        """
        # Get left child and left-right grandchild
        left_child: TreeNode = local_root.left
        left_right_grandchild: TreeNode = left_child.right

        # Perform rotation 
        left_child.right = local_root
        local_root.left = left_right_grandchild

        # Update heights
        local_root.height = 1 + self._get_max_height_of_children(local_root)
        left_child.height = 1 + self._get_max_height_of_children(left_child)

        # Return the new root 
        return left_child

    def _get_max_height_of_children(self, local_root: TreeNode) -> int:
        """
        Calculate the maximum of the height of the left and right children.
        """
        left_height: int = self._get_height(local_root.left)
        right_height: int = self._get_height(local_root.right)
        return max(left_height, right_height)

    def _get_height(self, local_root: TreeNode) -> int:
        """
        Get the height of the given node; if no node is given, then return the height of the root.
        An empty tree has height 0.
        """
        # Handle empty node
        if local_root is None:
            return 0

        return local_root.height

    def _get_balance(self, local_root: TreeNode) -> int:
        """
        Get the balance factor between the left and right children - aka the difference
        between the two children's heights. A positive value means that the left child is taller.
        A negative value means that the right child is taller. A value of zero means that the left and
        right side are the same height, or the given root is None.
        """
        if local_root is None:
            return 0
        
        # Get the left and right heights
        left_height: int = self._get_height(local_root.left)
        right_height: int = self._get_height(local_root.right)
        # Find their difference
        return left_height - right_height


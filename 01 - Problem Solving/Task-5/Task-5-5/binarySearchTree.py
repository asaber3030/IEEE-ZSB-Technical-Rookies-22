class Node:
    def insert(self, val):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return

        current = self.root
        while current:
            if val < current.info:
                if current.left is None:
                    current.left = newNode
                    return

                current = current.left

            else:
                if current.right is None:
                    current.right = newNode
                    return

                current = current.right
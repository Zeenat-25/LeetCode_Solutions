class Solution:
    def longestConsecutive(self, root):
        if not root:
            return -1

        self.max_len = 0

        def dfs(node, parent_val, current_len):
            if not node:
                return

            if node.data == parent_val + 1:
                current_len += 1
            else:
                current_len = 1

            self.max_len = max(self.max_len, current_len)

            dfs(node.left, node.data, current_len)
            dfs(node.right, node.data, current_len)

        dfs(root, root.data - 1, 0)
       
        return self.max_len if self.max_len > 1 else -1

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for i in range(level_size):
                node = queue.pop(0)
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            result.append(level_sum / float(level_size))
        
        return result
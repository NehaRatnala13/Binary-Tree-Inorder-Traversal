# Binary-Tree-Inorder-Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values. An inorder traversal visits nodes in the following order: **Left Subtree -> Root -> Right Subtree**.
# LeetCode 94: Binary Tree Inorder Traversal

## Problem Description
Given the root of a binary tree, return the inorder traversal of its nodes' values. An inorder traversal visits nodes in the following order: **Left Subtree -> Root -> Right Subtree**.

## Solution Approach
This solution uses a recursive Depth-First Search (DFS) helper function nested inside the main function:
1. **Base Case:** If the current node is `None`, the function returns immediately.
2. **Left Traversal:** Recursively traverse the left subtree to process smaller values/leftmost positions first.
3. **Node Visit:** Append the current node's value to the result tracking array `res`.
4. **Right Traversal:** Recursively traverse the right subtree.

## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N)$ where $N$ is the total number of nodes in the tree, as every single node is visited exactly once.
* **Space Complexity:** $\mathcal{O}(N)$ in the worst-case scenario (a highly skewed tree) due to the implicit recursion stack frame allocation. For a balanced tree, the space complexity is $\mathcal{O}(\log N)$.

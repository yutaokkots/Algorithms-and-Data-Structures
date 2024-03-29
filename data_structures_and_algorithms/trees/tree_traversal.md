# Binary Tree Traversal

Be able to:
1. traversal in-order
2. traversal pre-order
3. traversal post-order


| In-order | Pre-order | Post-order |
| -------- | --------  | --------   |
| left branch -> current node -> right branch | current node -> left branch / right branch | child nodes -> current node |
| 'in-order' because the nodes are visited in ascending order |  'pre-order' because the current node is visited before its children | 'post-order' because the root node is visited after the children |


## In-order traversal

left branch -> current node -> right branch

Visit the left branch, then current node, then right branch
It is called 'in-order' because the nodes are visited in ascending order. 

```
>>> Java

void inOrderTraversal(TreeNode node){
    if (node != null){
        inOrderTraversal(node.left);
        visit(node);
        inOrderTraversal(node.right);
    }
}
```

```
>>> Python

def inOrderTraversal(node):
    if node != None:
        inOrderTraversal(node.left)
        visit(node)
        inOrderTraversal(node.right)
```

## Pre-order traversal

current node -> left branch / right branch

Visit the current node before vising the children
It is called 'pre-order' because the current node is visited before its children.

```
>>> Java

void preOrderTraversal(TreeNode node){
    if (node != null){
        visit(node);
        preOrderTraversal(node.left);
        preOrderTraversal(node.right);
    }
}
```

```
>>> Python

def preOrderTraversal(node):
    if node != None:
        visit(node)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
```

## Post-order traversal

child nodes -> current node
Visit the child nodes before visiting the current node
It is called 'post-order' because the root node is visited after the children. 
In a post-order traversal, the root is always visited last. 

```
>>> Java

void postOrderTraversal(TreeNode node){
    if (node != null){
        postOrderTraversal(node.left);
        postOrderTraversal(node.right);
        visit(node);
    }
}
```

```
>>> Python

def postOrderTraversal(node):
    if node != None:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        visit(node)
```

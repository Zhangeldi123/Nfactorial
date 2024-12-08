from typing import List, Any, Dict, Set, Generator

class StaticArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity

    def set(self, index: int, value: int) -> None:
        if 0 <= index < self.capacity:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def get(self, index: int) -> int:
        if 0 <= index < self.capacity:
            return self.array[index]
        else:
            raise IndexError("Index out of range")


class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value: int) -> None:
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        if 0 <= index < len(self.array):
            self.array.pop(index)
        else:
            raise IndexError("Index out of range")

    def get(self, index: int) -> int:
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of range")


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, position: int, value: int) -> None:
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, value: int) -> None:
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    def find(self, value: int) -> Node:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        return self.head is None

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        current = self.head
        while current and current.next:
            current = current.next
        return current

class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert(self, position: int, value: int) -> None:
        new_node = DoubleNode(value)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        if not new_node.next:
            self.tail = new_node

    def delete(self, value: int) -> None:
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def find(self, value: int) -> DoubleNode:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        return self.head is None

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        current = self.head
        self.head, self.tail = self.tail, self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

    def get_head(self) -> DoubleNode:
        return self.head

    def get_tail(self) -> DoubleNode:
        return self.tail

class Queue:
    def __init__(self):
        """
        Initialize an empty queue using a list.
        """
        self.queue = []

    def enqueue(self, value: int) -> None:
        """
        Add a value to the end of the queue.
        """
        self.queue.append(value)

    def dequeue(self) -> int:
        """
        Remove a value from the front of the queue and return it.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Peek at the value at the front of the queue without removing it.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0

class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """
        def _insert(node, value):
            if node is None:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """
        def _delete(node, value):
            if node is None:
                return None
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # Replace with inorder successor
                min_larger_node = self.minimum(node.right)
                node.value = min_larger_node.value
                node.right = _delete(node.right, min_larger_node.value)
            return node

        self.root = _delete(self.root, value)

    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """
        def _search(node, value):
            if node is None or node.value == value:
                return node
            if value < node.value:
                return _search(node.left, value)
            return _search(node.right, value)

        return _search(self.root, value)

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return result

    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self.root)

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """
        return self.root is None

    def height(self) -> int:
        """
        Returns the height of the tree.
        """

        def _height(node):
            if not node:
                return 0  # Correct base case for height
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)


    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the tree.
        """
        result = []

        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
        return result

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the tree.
        """
        result = []

        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)

        _postorder(self.root)
        return result

    def level_order_traversal(self) -> List[int]:
        """
        Perform a level order (breadth-first) traversal of the tree.
        """
        if not self.root:
            return []

        queue = Queue()
        queue.enqueue(self.root)
        result = []

        while not queue.is_empty():
            node = queue.dequeue()
            result.append(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return result

    def minimum(self, node=None) -> TreeNode:
        """
        Returns the node with the minimum value in the tree.
        """
        if node is None:
            node = self.root
        while node and node.left:
            node = node.left
        return node

    def maximum(self, node=None) -> TreeNode:
        """
        Returns the node with the maximum value in the tree.
        """
        if node is None:
            node = self.root
        while node and node.right:
            node = node.right
        return node

    def is_valid_bst(self) -> bool:
        """
        Check if the tree is a valid binary search tree.
        """
        def _is_valid(node, low, high):
            if not node:
                return True
            if not (low < node.value < high):
                return False
            return _is_valid(node.left, low, node.value) and _is_valid(node.right, node.value, high)

        return _is_valid(self.root, float('-inf'), float('inf'))

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

def shell_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

from typing import List

def merge_sort(lst: List[int]) -> List[int]:
    def merge(left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements from both halves
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)



def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


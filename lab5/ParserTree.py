from typing import List

from lab5.config import *


class Node:
    def __init__(self, elem):
        self.element = elem
        self.parent = None
        self.leftChild = None
        self.rightChild = None


class ParserTree:
    def __init__(self, grammar):
        self.head = None
        self.grammar = grammar

    def createTree(self, productionString: List[WorkElement]):
        if not productionString:
            return

        head = Node(productionString[0])
        self.head = head

        self.parseNode(head, productionString, 1)

        self.traverse_tree(head)

    def parseNode(self, node, productionString, index):
        production = self.grammar.productions[productionString[index - 1].value][
            productionString[index - 1].productionNumber - 1]

        newNode = Node(WorkElement(production[0]))
        node.leftChild = newNode
        node = node.leftChild

        if index < len(productionString) and node.element.value == productionString[index].value:
            node.element.production_nr = productionString[index].productionNumber
            index += 1
            self.parseNode(node, productionString, index)

        for i in range(1, len(production)):
            newNode = Node(WorkElement(production[i]))
            node.rightChild = newNode
            node = node.rightChild

            if index < len(productionString) and node.element.value == productionString[index].value:
                node.element.production_nr = productionString[index].productionNumber
                index += 1
                self.parseNode(node, productionString, index)

    def printNode(self, node: Node):
        queue = []
        print(node.element.value)

        if node.leftChild is not None:
            queue.append(node.leftChild)

        aux = node

        while aux.rightChild is not None:
            aux = aux.rightChild
            print(' ' + str(aux.element.value), end=" ")
            if aux.leftChild is not None:
                queue.append(aux)

        print()

        if node.leftChild is not None:
            print("Left child: " + node.leftChild.element.value)

        print()

        while queue:
            self.printNode(queue.pop(0))

    def traverseTree(self, root):
        if root is None:
            return

        while root:
            print(f"{str(root.element)} ", end="")
            if root.left_child:
                self.traverseTree(root.leftChild)
            root = root.rightChild

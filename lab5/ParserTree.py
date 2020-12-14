from typing import List

from lab5.config import *


class Node:
    def __init__(self, elem, pos=0):
        self.element = elem
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.position = pos

    def __str__(self):
        parent = self.parent.position if self.parent else None
        left_c = self.leftChild.position if self.leftChild else None
        right_s = self.rightChild.position if self.rightChild else None
        return f"Node: position {self.position} value: {str(self.element)} Parent {parent} leftChild: {left_c} rightChild {right_s}"


class ParserTree:
    def __init__(self, grammar):
        self.head = None
        self.table = {}
        self.values = []
        self.grammar = grammar
        self.currentPosition = 1
        self.currentIndex = 1

    def createTree(self, productionString: List[WorkElement]):
        if not productionString:
            return

        head = Node(productionString[0], 0)
        self.head = head
        self.values.append(str(head.element))
        self.table[0] = head

        self.parseNode(head, productionString)

        with open("parser.out", 'w') as f:
            self.printAll(f)

        self.printAll()

    def parseNode(self, node, productionString):
        parent = node
        nonTerminal = productionString[self.currentIndex - 1].value
        productionNumber = productionString[self.currentIndex - 1].productionNumber
        production = self.grammar.productions[nonTerminal][
            productionNumber - 1]

        newNode = Node(WorkElement(production[0]), self.currentPosition)
        node.leftChild = newNode
        newNode.parent = parent
        node = node.leftChild
        self.table[self.currentPosition] = newNode

        self.values.append(str(newNode.element))

        if self.currentIndex < len(productionString) and node.element.value == productionString[
            self.currentIndex].value:
            node.element.productionNumber = productionString[self.currentIndex].productionNumber
            self.currentIndex += 1
            self.currentPosition += 1
            self.parseNode(node, productionString)

        for i in range(1, len(production)):
            self.currentPosition += 1
            newNode = Node(WorkElement(production[i]), self.currentPosition)
            newNode.parent = parent
            self.table[self.currentPosition] = newNode
            node.rightChild = newNode
            node = node.rightChild
            self.values.append(str(newNode.element))

            if self.currentIndex < len(productionString) and node.element.value == productionString[
                self.currentIndex].value:
                node.element.productionNumber = productionString[self.currentIndex].productionNumber
                self.currentIndex += 1
                self.currentPosition += 1
                self.parseNode(node, productionString)

    def printAll(self, file=None):
        fathers = [-1 for _ in range(len(self.values))]
        leftChild = [-1 for _ in range(len(self.values))]
        rightChild = [-1 for _ in range(len(self.values))]
        toPrint = ""
        for node in self.table.values():
            if node.parent:
                fathers[node.position] = node.parent.position
            if node.leftChild:
                leftChild[node.position] = node.leftChild.position
            if node.rightChild:
                rightChild[node.position] = node.rightChild.position
            toPrint = ""

            if node.position == 0:
                toPrint += str(node.element)
            else:
                nodeCopy = node
                while nodeCopy.parent:
                    if nodeCopy.parent.rightChild:
                        toPrint = "|\t" + toPrint
                    else:
                        toPrint = "\t" + toPrint
                    nodeCopy = nodeCopy.parent

                if node.rightChild is None:
                    toPrint += "\\--"
                else:
                    toPrint += "|--"
                toPrint += str(node.element)

            if file is None:
                print(toPrint)
            else:
                file.write(toPrint + "\n")

        if file is None:
            print(
                f' \nValues: {self.values}\nFathers: {fathers}\nLeft children: {leftChild}\nRight siblings = {rightChild}')
        else:
            file.write(
                f' \nValues: {self.values}\nFathers: {fathers}\nLeft children: {leftChild}\nRight siblings = {rightChild}')

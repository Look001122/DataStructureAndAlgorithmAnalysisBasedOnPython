# @Time:2025/8/24 17:12
# @Author:卢科
# @Description:代码清单6-9 解析树构建器
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator

def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree('')
    pStack.push(eTree)
    currentTree=eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree=currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            parent=pStack.pop()
            currentTree=parent
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
        elif i ==')':
            currentTree=pStack.pop()
        else:
            raise ValueError('Unknown Operator:'+i)
    return eTree

def evaluate(parseTree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC=parseTree.getLeftChild()
    rightC=parseTree.getRightChild()

    if leftC and rightC:
        fn=opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

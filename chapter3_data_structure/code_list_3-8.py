# @Time:2025/7/13 9:52
# @Author:卢科
# @Description:代码清单3-8 用python实现后序表达式的计算

from pythonds.basic import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList=postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2=operandStack.pop()
            operand1=operandStack.pop()
            result=doMath(token,operand1,operand2)
            operandStack.push(result)

    return operandStack.pop()
def doMath(op,op1,op2):
    if op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "+":
        return op1+op2
    else:
        return op1-op2



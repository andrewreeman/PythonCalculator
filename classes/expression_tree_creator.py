from classes.parser.stack.interactor import ParserStackInteractor

class ExpressionTreeCreator:
    def __init__(self, interactor: ParserStackInteractor):        
        self._tree = None  
        self._stack_interactor: ParserStackInteractor = interactor
    
    def create_expression(self):                        
        self._tree = self._createNodeFromStack(0, self._tree)
        return self._tree
    
    def _createNodeFromStack(self, depth, tree=None, orphan=None):        
        logic = self._stack_interactor
        stack = self._stack_interactor.stack

        if depth == 0:
            # todo: if popping stack state just depends on an existence of a tree then just use that instead
            logic.query.setIsPoppingStack(False)
    
        if stack.isOperatorStackEmpty():
            if stack.isNumberStackEmpty():
                return tree
            else:
                rootNode = logic.popSingleNumberAddition(stack, tree)
                return self._createNodeFromStack(depth + 1, rootNode)
        elif orphan:            
            rootNode = logic.popOperatorAndJoinNodes(stack, tree, orphan)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.query.isNumberStackCountGreaterThanOperatorStackCount(stack):            
            logic.query.setIsPoppingStack(True)
            rootNode = logic.popRootNode(stack)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.query.areBothStacksSizeOfOneAndCurrentlyPoppingStack(stack):            
            rootNode = logic.popJoiningRootNodeToRightOperand(stack, tree)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.query.areBothStacksSizeOfOneAndCurrentlyNotPoppingStack(stack):            
            rootNode = logic.popJoiningRootNodeToLeftOperand(stack, tree)
            return self._createNodeFromStack(depth + 1, rootNode)

        elif logic.query.areBothStacksEqualSize(stack):            
            orphan = logic.popRootNode(stack)
            return self._createNodeFromStack(depth + 1, tree, orphan)
    
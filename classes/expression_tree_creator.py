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
        query = self._stack_interactor.query

        if query.areBothStacksEmpty():
            return tree

        rootNode = tree
        if depth == 0:
            self._start_popping_stack()                                
        
        if stack.isOperatorStackEmpty():
            rootNode = logic.popSingleNumberAddition(stack, tree)
        elif orphan:            
            rootNode = logic.popOperatorAndJoinNodes(stack, tree, orphan)            
        elif logic.query.isNumberStackCountGreaterThanOperatorStackCount():            
            logic.query.setIsPoppingStack(True)
            rootNode = logic.popRootNode(stack)            
        elif logic.query.areBothStacksSizeOfOneAndCurrentlyPoppingStack():            
            rootNode = logic.popJoiningRootNodeToRightOperand(stack, tree)            
        elif logic.query.areBothStacksSizeOfOneAndCurrentlyNotPoppingStack():            
            rootNode = logic.popJoiningRootNodeToLeftOperand(stack, tree)                        
        elif logic.query.areBothStacksEqualSize():            
            orphan = logic.popRootNode(stack)            
            
        return self._createNodeFromStack(depth + 1, rootNode, orphan)
    
    def _start_popping_stack(self):        
        self._stack_interactor.query.setIsPoppingStack(False)
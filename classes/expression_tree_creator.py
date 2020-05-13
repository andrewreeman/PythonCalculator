from classes.parser.stack.interactor import ParserStackInteractor

class ExpressionTreeCreator:
    def __init__(self, interactor: ParserStackInteractor):        
        self._tree = None  
        self._stack_interactor: ParserStackInteractor = interactor
    
    def create_expression(self):                        
        self._tree = self._createNodeFromStack(0, self._tree)
        return self._tree
    
    def _createNodeFromStack(self, depth, tree):                
        logic = self._stack_interactor        
        query = self._stack_interactor.query

        if query.areBothStacksEmpty():
            self._stop_popping_stack()            
            return tree

        rootNode = tree        
        
        if query.isOperatorStackEmpty():            
            rootNode = logic.popSingleNumber()    
        elif logic.query.isNumberStackCountGreaterThanOperatorStackCount():            
            self._start_popping_stack()            
            rootNode = logic.popRootNode()            
        elif logic.query.areBothStacksSizeOfOneAndCurrentlyPoppingStack():                        
            leftOperand = logic.popSingleNumber()
            rootNode = logic.popOperatorAndJoinNodes(leftOperand, tree)        
        elif logic.query.areBothStacksSizeOfOneAndCurrentlyNotPoppingStack():            
            rightOperandNode = logic.popSingleNumber()
            rootNode = logic.popOperatorAndJoinNodes(tree, rightOperandNode)
        else:
            rightOperand = logic.popRootNode()
            rootNode = logic.popOperatorAndJoinNodes(tree, rightOperand)
            
        return self._createNodeFromStack(depth + 1, rootNode)
    
    def _start_popping_stack(self):
        self._stack_interactor.query.setIsPoppingStack(True)

    def _stop_popping_stack(self):        
        self._stack_interactor.query.setIsPoppingStack(False)
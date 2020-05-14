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

        if query.are_both_stacks_empty():
            self._stop_popping_stack()            
            return tree

        rootNode = tree        
        
        if query.is_operator_stack_empty():            
            rootNode = logic.popSingleNumber()    
        elif query.is_expression_stack_higher_than_operator_stack():            
            self._start_popping_stack()            
            rootNode = logic.popRootNode()            
        elif query.are_both_stacks_size_of_one() and query.is_popping_stack():                        
            leftOperand = logic.popSingleNumber()
            rootNode = logic.popOperatorAndJoinNodes(leftOperand, tree)        
        elif query.are_both_stacks_size_of_one() and not query.is_popping_stack():                       
            rightOperandNode = logic.popSingleNumber()
            rootNode = logic.popOperatorAndJoinNodes(tree, rightOperandNode)
        else:
            rightOperand = logic.popRootNode()
            rootNode = logic.popOperatorAndJoinNodes(tree, rightOperand)
            
        return self._createNodeFromStack(depth + 1, rootNode)
    
    def _start_popping_stack(self):
        self._stack_interactor.query.set_is_popping_stack(True)

    def _stop_popping_stack(self):        
        self._stack_interactor.query.set_is_popping_stack(False)
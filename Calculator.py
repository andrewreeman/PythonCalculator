import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton

import ExpressionEvaluator

class Calculator(BaseWidget):

    def __init__(self):
        super(Calculator,self).__init__('Calculator')

        #Definition of the forms fields
        self._expression     = ControlText('', '0')        
        self._equalsButton        = ControlButton('Equals')

        #Define the button action
        self._equalsButton.value = self.__equalsClicked

    def __equalsClicked(self):
        """Button action event"""
	ExpressionEvaluator.evaluate(self._expression.value)


#Execute the application
if __name__ == "__main__":   pyforms.start_app( Calculator )

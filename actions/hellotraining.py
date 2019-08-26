import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, message,message2):
        print(message+message2)
        return(True,message+message2)

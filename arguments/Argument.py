from arguments.Comparison import Comparaison
from arguments.CoupleValue import CoupleValue

class Argument :
    """ Argument class .
    This class implements an argument used during the interaction .
    attr :
    decision :
    item :
    comparison_list :
    couple_values_list :
    """
    def __init__ ( self , boolean_decision , item ) :
        """ Creates a new Argument .
        """
        self . decision = boolean_decision
        self . item = item
        self . comparison_list = []
        self . couple_values_list = []
    #To be completed
    def add_premiss_comparison ( self , criterion_name_1 , criterion_name_2 ) :
        """ Adds a premiss comparison in the comparison list .
        """
    # To be completed
    def add_premiss_couple_values ( self , criterion_name , value ) :
        """ Add a premiss couple values in the couple values list .
        """
    # To be completed

from arguments.Comparison import Comparison
from arguments.CoupleValue import CoupleValue
from communication.preferences.Value import Value

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
        self.decision = boolean_decision
        self.item = item
        self.comparison_list = []
        self.couple_values_list = []
    #To be completed
    def add_premiss_comparison ( self , criterion_name_1 , criterion_name_2 ) :
        """ Adds a premiss comparison in the comparison list .
        """
        self.comparison_list.append ( Comparison ( criterion_name_1 , criterion_name_2 ) )
    # To be completed
    def add_premiss_couple_values ( self , criterion_name , value ) :
        """ Add a premiss couple values in the couple values list .
        """
        self.couple_values_list.append ( CoupleValue ( criterion_name , value ) )
    # To be completed
    def List_supporting_proposal ( self , item , preferences ):
        """ 
        Generate a list of premisses which can be used to support an item
        param item : Item - name of the item
        return : list of all premisses PRO an item ( sorted by order of importancebased on agent ’s preferences """
        supporting_proposals=[]
        criteria_names=preferences.get_criterion_name_list()
        for criterion in criteria_names:
            value=preferences.get_value(item,criterion)
            if value in [Value.VERY_GOOD,Value.GOOD]:
                supporting_proposals.append(criterion)
        return supporting_proposals
    
            # if preferences.get_value(item,criterion) > preferences.get_value(self.item,criterion):
            #     self.add_premiss_comparison(criterion,self.item)
            # else:
            #     self.add_premiss_comparison(self.item,criterion)

    def List_attacking_proposal ( self , item , preferences ) :
        opposing_proposals=[]
        criteria_names=preferences.get_criterion_name_list()
        for criterion in criteria_names:
            value=preferences.get_value(item,criterion)
            if value in [Value.BAD,Value.VERY_BAD]:
                opposing_proposals.append(criterion)
        return opposing_proposals
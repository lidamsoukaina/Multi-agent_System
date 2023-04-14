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
        criteria_names=preferences.get_criterion_name_list()
        for criterion in criteria_names:
            value=preferences.get_value(item,criterion)
            if value in [3,4]:
                self.add_premiss_couple_values(criterion,value)
        return self.couple_values_list
    
            # if preferences.get_value(item,criterion) > preferences.get_value(self.item,criterion):
            #     self.add_premiss_comparison(criterion,self.item)
            # else:
            #     self.add_premiss_comparison(self.item,criterion)

    def List_attacking_proposal ( self , item , preferences ) :

        criteria_names=preferences.get_criterion_name_list()
        for criterion in criteria_names: #{order by default}
            value=preferences.get_value(item,criterion)
            if value in [0,1]:
                self.add_premiss_couple_values(criterion,value)
        return self.couple_values_list

    def support_proposal ( self , item,preferences ) :
        """
        Used when the agent receives " ASK_WHY " after having proposed an item
        param item : str - name of the item which was proposed
        return : string - the strongest supportive argument
        """
        # To be completed
        if self.decision:
            List_supporting_proposal=self.List_supporting_proposal(item , preferences )
            if len(List_supporting_proposal)>0:
                return List_supporting_proposal[0]
            else:
                return None
        else:
            List_attacking_proposal=self.List_attacking_proposal (item , preferences )
            if len(List_attacking_proposal)>0:
                return List_attacking_proposal[0]
            else:
                return None
    def __str__(self) -> str:
        if self.decision:
            return self.item.__str__() + " <- " + self.couple_values_list[0].__str__()
        else:
            # TO DO: write response for attack
            if len(self.comparison_list):
                return '~ ' + self.item.__str__() + " <- " + self.couple_values_list[0].__str__() + " , " + self.comparison_list[0].__str__() 
            else:
                return '~ ' + self.item.__str__() + " <- " + self.couple_values_list[0].__str__()
from mesa import Model
from mesa.time import RandomActivation
import random

from communication.agent.CommunicatingAgent import CommunicatingAgent
from communication.message.MessageService import MessageService

from communication.preferences.CriterionName import CriterionName
from communication.preferences.CriterionValue import CriterionValue
from communication.preferences.Preferences import Preferences
from communication.preferences.Item import Item

class ArgumentAgent(CommunicatingAgent) :
    """ ArgumentAgent which inherit from CommunicatingAgent .
    """
    def __init__(self , unique_id , model , name , preferences) :
        super().__init__(unique_id, model, name)
        self.preference = preferences

    def step(self) :
        super().step()

    def get_preference(self):
        return self.preference
    
    def set_criteria(self, List_criteria):
        self.preference.get_criterion_name_list(List_criteria)

    def generate_preferences(self, List_items):
        List_criteria = self.preference.get_criterion_name_list()
        for i in List_items:
            for j in List_criteria:
                self.preference.add_criterion_value(CriterionValue(i,j,random.randint(0,5)))
                
class ArgumentModel(Model) :
    """ ArgumentModel which inherit from Model .
    """
    def __init__(self,N) :
        self.schedule = RandomActivation(self)
        self.__messages_service = MessageService(self.schedule)
        self.running = True
        # init list of items
        items = [Item("Diesel Engine", "A super cool diesel engine"), Item("Electric Engine", "A very quiet engine")]
        # init list of criteria
        criteria = [CriterionName.PRODUCTION_COST, CriterionName.ENVIRONMENT_IMPACT,
                                        CriterionName.CONSUMPTION, CriterionName.DURABILITY,
                                        CriterionName.NOISE]
        for i in range(N):
            init_pref = Preferences()
            random.shuffle(criteria)
            init_pref.set_criterion_name_list(criteria)
            a = ArgumentAgent(i,self, " agent_" + str(i), init_pref)
            # TO DO: maybe random sample items
            a.generate_preferences(items)
            self.schedule.add(a)
        # Communication by pair
        
    def step(self) :
        self.__messages_service.dispatch_messages()
        self.schedule.step()


if __name__ == "__main__":
    argument_model = ArgumentModel(2)
    # get the first agent  
    agent = argument_model.schedule.agents[0]
    # get the preference of the first agent
    pref = agent.get_preference()
    print(len(pref.get_criterion_value_list()))
    for value in pref.get_criterion_value_list():
        print(value.get_item(), value.get_criterion_name(), value.get_value())
    # get the second agent  
    agent = argument_model.schedule.agents[1]
    # get the preference of the first agent
    pref = agent.get_preference()
    print('agent 2')
    for value in pref.get_criterion_value_list():
        print(value.get_item(), value.get_criterion_name(), value.get_value())
    for i in range(10):
        argument_model.step()

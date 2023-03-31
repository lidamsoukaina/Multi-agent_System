from mesa import Model
from mesa.time import RandomActivation
import random

from communication.agent.CommunicatingAgent import CommunicatingAgent
from communication.message.MessageService import MessageService
from communication.message.MessagePerformative import MessagePerformative
from communication.message.Message import Message

from communication.preferences.CriterionName import CriterionName
from communication.preferences.CriterionValue import CriterionValue
from communication.preferences.Preferences import Preferences
from communication.preferences.Item import Item

from arguments.Argument import Argument


class ArgumentAgent(CommunicatingAgent) :
    """ ArgumentAgent which inherit from CommunicatingAgent .
    """
    def __init__(self , unique_id , model , name , preference , is_commited=False) :
        super().__init__(unique_id, model, name)
        self.preference = preference
        self.is_commited=is_commited
        self.commited_val=None

    def step(self) :
        super().step()
        # TO DO: add the argumentation process
        if self.is_commited==True:
            pass
        else:
            messages=self.get_new_messages()
            performatives=[msg.get_performative() for msg in messages]
            print('agent',self.get_name(),'messages',performatives)
            if len(messages)!=0:
            
                for msg in messages:
                    sender=msg.get_exp()
                    performative=msg.get_performative()
                    content=msg.get_content()
                    if performative==MessagePerformative.PROPOSE:
                        # get top 10% items according to the preference
                        is_top_10_item = self.preference.is_item_among_top_10_percent(content,self.model.items)
                        if is_top_10_item:
                            
                            message=Message(self.get_name(),sender,MessagePerformative.ACCEPT,content)
                            self.send_message(message)
                            print(message)
                        else:
                            message=Message(self.get_name(),sender,MessagePerformative.ASK_WHY,content)
                            self.send_message(message)
                            print(message)
                    if performative==MessagePerformative.ASK_WHY:
                        args=Argument(True,content)
                        prop=args.support_proposal(content,self.preference)
                        if prop!=None:
                            message=Message(self.get_name(),sender,MessagePerformative.ARGUE,prop)
                            self.send_message(message)
                            print(message)
                        else:
                            items_list=self.model.items.copy()
                            items_list.remove(content)
                            top_item = self.preference.most_preferred(items_list)
                            message=Message(self.get_name(),sender,MessagePerformative.PROPOSE,top_item)
                            self.send_message(message)
                            print(message)
                    if performative==MessagePerformative.ARGUE:
                        print('to be done')

                    if performative in [MessagePerformative.ACCEPT,MessagePerformative.COMMIT]:
                        message=Message(self.get_name(),sender,MessagePerformative.COMMIT,content)
                        self.commited_val=content
                        self.is_commited=True
                        self.send_message(message)
                        print(message)
            else:
                # get random agent
                agent_list = self.model.schedule.agents.copy()
                agent_list.remove(self)
                agent=random.choice(agent_list)
                # get the top item according to the preference
                top_item = self.preference.most_preferred(self.model.items)
                # print(self.get_name(),' top ',top_item)
                message=Message(self.get_name(),agent.get_name(),MessagePerformative.PROPOSE,top_item)
                self.send_message(message)
                print(message)

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
    def __init__(self,N,items,criteria) :
        self.schedule = RandomActivation(self)
        self.__messages_service = MessageService(self.schedule)
        self.running = True
        self.items = items
        self.criteria=criteria
        
        
        for i in range(N):
            init_pref = Preferences()
            random.shuffle(self.criteria)
            init_pref.set_criterion_name_list(self.criteria)
            a = ArgumentAgent(i,self, " agent_" + str(i), init_pref)
            # TO DO: maybe random sample items
            a.generate_preferences(self.items)
            self.schedule.add(a)
        # Communication by pair
        
    def step(self) :
        self.__messages_service.dispatch_messages()
        self.schedule.step()


if __name__ == "__main__":
    # init list of items

    items=[Item("Diesel Engine", "A super cool diesel engine"), Item("Electric Engine", "A very quiet engine"),
           Item("Hybrid Engine", "A very efficient engine"),Item("Petrol Engine", "A very cheap engine"),
           Item("Gas Engine", "A very powerful engine")]
    # init list of criteria
    criteria = [CriterionName.PRODUCTION_COST, CriterionName.ENVIRONMENT_IMPACT,
                                    CriterionName.CONSUMPTION, CriterionName.DURABILITY, CriterionName.NOISE]
    argument_model = ArgumentModel(2,items,criteria)
    # get the first agent  
    agent = argument_model.schedule.agents[0]
    # get the preference of the first agent
    pref = agent.get_preference()
                # print(len(pref.get_criterion_value_list()))
                # for value in pref.get_criterion_value_list():
                #     print(value.get_item(), value.get_criterion_name(), value.get_value())
    # get the second agent  
    agent = argument_model.schedule.agents[1]
    # get the preference of the first agent
    pref = agent.get_preference()
        # print('agent 2')
        # for value in pref.get_criterion_value_list():
        #     print(value.get_item(), value.get_criterion_name(), value.get_value())
    for i in range(10):
        print('__________________________________________________________________')
        print("step ",i)
        print('__________________________________________________________________')
        argument_model.step()

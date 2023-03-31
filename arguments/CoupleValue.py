


class CoupleValue :
    """ CoupleValue class .
    This class implements a couple value used in argument object .

    attr :
    criterion_name :
    value : """

    def __init__ ( self , criterion_name , value ):
        """ Creates a new couple value .
        """
        self.criterion_name = criterion_name
        self.value = value
    def __str__ ( self ):
        """ Returns couple value as a String .
        """
        return str(self.criterion_name) + " = " + str ( self.value )
    def get_criterion_name ( self ):
        """ Returns the criterion name .
        """
        return self.criterion_name

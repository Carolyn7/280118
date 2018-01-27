class Rewards():
    def __init__(self, name, card_type):
        self.__name = name
        self.__card_type = card_type

    def get_name(self):
        return self.__name
    def get_card_type(self):
        return self.__card_type

    def set_name(self, name):
        self.__name = name
    def set_card_type(self, card_type):
        self.__card_type = card_type

class deduct_pt():
    def __init__(self,point,exp_date,torf,card):
        self.__point = point
        self.__exp_date = exp_date
        self.__torf = torf
        self.__card = card
    def get_point(self):
        return self.__point
    def get_exp_date(self):
        return self.__exp_date
    def get_torf(self):
        return self.__torf
    def get_card(self):
        return self.__card

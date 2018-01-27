class User():
    def __init__(self, bank, card_name, details, expire_date):
        self.__bank = bank
        self.__card_name = card_name
        self.__details = details
        self.__expiry_date = expire_date


    def get_bank(self):
        return self.__bank
    def get_card_name(self):
        return self.__card_name
    def get_details(self):
        return self.__details
    def get_expire_date(self):
        return self.__expiry_date


    def set_bank(self, bank):
        self.__bank = bank
    def set_card_name(self, card_name):
        self.__card_name = card_name
    def set_details(self, details):
        self.__details = details
    def set_expire_date(self, expire_date):
        self.__expiry_date = expire_date

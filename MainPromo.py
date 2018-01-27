import PromoUser as P
def ProcessUser():
    userList = []
    xiaoyang = open("file/promotion.txt", "r")
    for i in xiaoyang:
        content = i.split("/")
        j = P.User(content[0], content[1], content[2], content[3])
        userList.append(j)
    return userList

def ActualUser(name):
    actual = open('file/account.txt', 'r')
    card_type = []
    for t in actual:
        name_list = t.split(',')
        if name == name_list[0] :
            card_type.append(name_list[2])
    return card_type




import rewards as R
import datetime

def ProcessRewards():
    rewardList = []
    reward_file = open("file/rewards.txt", "r")
    for rList in reward_file:
        listR = rList.split(",")
        a = R.Rewards(listR[0], listR[1])
        rewardList.append(a)

    return rewardList

def ProcessTransaction(name):
    t_file = open("file/transactionRewards.txt", "r")
    totalpoint = open("file/total.txt", "r")
    lines = totalpoint.readlines()
    totalpoint.close()
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    total = 0
    for i in lines :
        j = i.split(",")
        if name == j[0] :
            total = int(j[1][:-1])
            for trans in t_file:
                listT = trans.split(",")
                i = listT[1].split("-")
                date_now = datetime.datetime(int(date[6:]), int(date[3:5]), int(date[:2]))
                date_reward = datetime.datetime(int(i[2]),int(i[1]),int(i[0]))
                if listT[0] == name and date_reward < date_now:
                    total -= int(listT[2][:2])
                    d = open("file/total.txt", "w")
                    for line in lines:
                        if line != name +","+ str(j[1][:-1])+"\n" :
                            d.write(line)
                    d.close()
                    add = open("file/total.txt", "a")
                    add.write(name+","+str(total)+"\n")
                    add.close()
    return total

def ProcessDate(name):
    d_file = open("file/transactionRewards.txt", "r")
    dateList = []
    date_n = datetime.datetime.now().strftime("%d-%m-%Y")
    for date in d_file:
        listD = date.split(",")
        if name == listD[0]:
            i = listD[1].split("-")
            date_now = datetime.datetime(int(date_n[6:]), int(date_n[3:5]), int(date_n[:2]))
            date_reward = datetime.datetime(int(i[2]), int(i[1]), int(i[0]))
            if date_reward < date_now :
                a = R.deduct_pt(listD[2][:2], listD[1], "True", listD[3][:-1])
                dateList.append(a)
            else :
                a = R.deduct_pt(listD[2][:2],listD[1],"False", listD[3][:-1])
                dateList.append(a)
    return dateList




def get_point(name):
    gfile=open("file/total.txt","r")
    for g in gfile :
        pt = g.split(',')
        if name == pt[0] :
            return str(pt[1][:-1])



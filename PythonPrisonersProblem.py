# veritasium 100 prisoners problem calculator
import random


def gen_rand_box_to_slip(lim):
    sliplist = [ a for a in range(1, lim + 1)]
    random.shuffle(sliplist)
    pdict = {}
    for number in range(1, lim + 1):
        pdict[number] = sliplist.pop(0)
    return pdict



def try_forpris_no(iter,no,pdict):
    checking = no
    tryno = 1
    while tryno < 51:
        result = pdict[checking]
        print(f"universe {iter} prisoner {no} checked box no {checking} and found slip no {result}")
        if result == no:
            print(f"universe {iter} prisoner {no} has found their slip!")
            return True
        else:
            checking = result
            tryno += 1
    return False

def ite(iterno,pricount):
    pdict = gen_rand_box_to_slip(pricount)
    for prisonerno in range(1,pricount+1):
        tried = try_forpris_no(iterno,prisonerno,pdict)
        if tried == False:
            return False
    return True

def main(pricount):
    success = 0
    for i in range(1,500):
        wha = ite(i,pricount)
        if wha == True:
            success += 1
        print(f"SUCCESS RATE IS = {success/i*100}% percent")
        # should be around 31%

main(100)
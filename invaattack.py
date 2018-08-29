from Linephu.linepy import *
from Linephu.akad.ttypes import *

client = LINE()

oepoll = OEPoll(client)

whitelist = ["u52afe1d4ea5332242efacfeb9190d2a3"]

def RECEIVE_MESSAGE(op):

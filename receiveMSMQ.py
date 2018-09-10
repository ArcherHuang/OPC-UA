#  pip install pypiwin32

import win32com.client
import os

def get_from_msmq():
    qinfo = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    qinfo.FormatName = "direct=os:"+computer_name+"\\PRIVATE$\\myQueue"
    queue = qinfo.Open(1,0)   # Open a ref to queue to read(1)
    msg = queue.Receive()
    print "Label:",msg.Label
    print "Body :",msg.Body
    queue.Close()
    # return msg.Label, msg.Body
    return msg.Body

# label, Body = get_from_msmq()
# print("label:" + label + " Body:" + Body)

#Body = get_from_msmq()
#print("Body:" + Body)
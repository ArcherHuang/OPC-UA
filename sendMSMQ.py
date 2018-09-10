import win32com.client
import os

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\KaruthQueue"
queue=qinfo.Open(2,0)   # Open a ref to queue
msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
msg.Label="TestMsg"
msg.Body = "The quick brown fox jumps over the lazy dog"
msg.Send(queue)

queue.Close()
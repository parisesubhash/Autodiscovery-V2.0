import subprocess
import sys

blist=[str(sys.argv[1]),'%cpu','%mem']
var='ps -p %s -o %s,%s,cmd' %(blist[0],blist[1],blist[2])
proc = subprocess.Popen(var, stdout=subprocess.PIPE,shell=True)
output = proc.stdout.read()
alist=output.split(' ',5)
dict={'PID':sys.argv[1],'CPU':alist[3],'RAM':alist[4],'Process':alist[5]}

print dict
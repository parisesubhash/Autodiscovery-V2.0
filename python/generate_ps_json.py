import subprocess
import sys
import re


def json_data(pid):

	blist=[pid,'%cpu','%mem']
	var='ps -p %s -o %s,%s,cmd' %(blist[0],blist[1],blist[2])
	proc = subprocess.Popen(var, stdout=subprocess.PIPE,shell=True)
	output = proc.stdout.read()
	output=re.sub(' +',' ',output)
	output=re.sub('\n','',output)
	alist=output.split(' ',5)
	dict={'PID':sys.argv[1],'CPU':alist[3],'RAM':alist[4],'Process':alist[5]}
	print dict

json_data(str(sys.argv[1]))

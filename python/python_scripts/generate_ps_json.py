#!/usr/bin/python

import subprocess
import sys
import re


def pid_json(pid):
	blist=[pid,'%cpu','%mem']
	var='ps -p %s -o %s,%s,cmd' %(blist[0],blist[1],blist[2])
	proc = subprocess.Popen(var, stdout=subprocess.PIPE,shell=True)
	output = proc.stdout.read()
	output=re.sub(' +',' ',output)
	output=re.sub('\n','',output)
	alist=output.split(' ',5)
	global dict1
	dict1={'PID':pid,'CPU':alist[3],'RAM':alist[4],'Process':alist[5]}
	return dict1


def ps_rollin():
	ps='ps -ef'
	psoc= subprocess.Popen(ps, stdout=subprocess.PIPE,shell=True)
	output=psoc.stdout.read()
	output=re.sub(' +',' ',output)
	#output=re.sub('\n',' \n ',output)
	alist=output.split('\n')
	length=len(alist)
	del alist[length-1]
	del alist[0]	
	pid_data={'data':[]}	
	count=0
	for list in alist:
		li_output=list.split(' ',7)
		li_json={'User-Id':li_output[0],'PID':li_output[1],'Parent_PID':li_output[2],'STARTUP_TIME':li_output[4],'PROCESS':li_output[7]}
		pid_json(li_output[1])
		li_json.update(dict1)
		pid_data['data'].append(li_json)
	print len(pid_data['data'])
	ram=0.0
	for d in pid_data['data']:
		tmp=d['RAM']
		ram=ram+float(tmp)
	print ram



	#print alist

#pid_json(str(sys.argv[1]))
ps_rollin()

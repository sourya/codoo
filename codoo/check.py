from flask import session
from subprocess import call

def check_answer(prob_code):
	script = "python ../code/%s%s.py < ../input/%s > ../outfile/%s%s" %(session['username'], prob_code, prob_code, session['username'], prob_code)
	call(script, shell=True)

	output = open('../output/%s' %(prob_code), 'r').readlines()
	outfile = open('../outfile/%s%s' %(session['username'], prob_code), 'r').readlines()

	if len(output) != len(outfile):
		return "Wrong answer"

	i = 0
	while i < len(output):
		if output[i] != outfile[i]:
			return "Wrong answer at test case number %d" % (i+1)
		i += 1
	
	if i >= len(output):
		return "Correct Answer"

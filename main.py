from combinator import makeCouples
from mail import sendMails

with open('./data/mails','r') as f:
	stakeholders=[[y.strip() for y in x.split('-',1)] for x in f.readlines()]
	couples=makeCouples(stakeholders)
	with open('./data/savedsent','w') as of:
		of.write('-'.join([str(x) for x in couples]))
	sendMails(couples)

	pass
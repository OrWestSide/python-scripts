# Python API assignement for Encode
import requests
import json
import time
import sys
import argparse
import re

# Parse cmd arguments
parser = argparse.ArgumentParser(description = 'Python Assignment for Encode Group')

parser.add_argument('--since',nargs = '*', help = 'Enter the since date/time in YYYY-mm-dd hh:mm:ss format')
parser.add_argument('--until',nargs = '*', help = 'Enter the until date/time in YYYY-mm-dd hh:mm:ss format')
parser.add_argument('--output-format', help = 'Output format is tabular, json or html')

opts = parser.parse_args()
if (opts.since == None or opts.until == None or opts.output_format == None):
	print('\t Usage:')
	print('\t stats --since \'YYYY-mm-dd hh:mm:ss\' --until \'YYYY-mm-dd hh:mm:ss\' --output-format format_out')
	sys.exit()

formats = ['tabular', 'json', 'html']
if (opts.output_format not in formats):
	print('\t Output format must be tabular, json or html')
	sys.exit()

# Get epoch time from date/time formats
fromdate = opts.since[0][1:] + ' ' + opts.since[1][:-1]
todate = opts.until[0][1:] + ' ' + opts.until[1][:-1]
pattern = '%Y-%m-%d %H:%M:%S'
try:
	start_epoch = int(time.mktime(time.strptime(fromdate, pattern)))
except ValueError:
	print('Date/time has to be entered in YYYY-mm-dd hh:mm:ss format')
	print('Exiting...')
	sys.exit()
try:
	end_epoch = int(time.mktime(time.strptime(todate, pattern)))
except ValueError:
	print('Date/time has to be entered in YYYY-mm-dd hh:mm:ss format')
	print('Exiting...')
	sys.exit()

if (end_epoch < start_epoch):
	print('\n \t \"since\" date/time must be before \"until\" date/time!!')
	print('\t Exiting...')
	exit()

# Create the url about answers and request it
url1 = 'https://api.stackexchange.com/2.2/answers?fromdate=' + str(start_epoch) + '&todate=' + str(end_epoch) + '&order'
url2 = '=desc&sort=activity&filter=default&site=stackoverflow&key=6OCrTot*LgO0ncaJToxYcQ(('
url = url1 + url2
resp_obj = requests.get(url)
ans_data = resp_obj.json()

ans_accepted = 0
ans_scores = 0
highest_score_answers = {}
counter = 0
for users in ans_data['items']:
	if (users['is_accepted'] == True):
		ans_accepted = ans_accepted + 1
		ans_scores = ans_scores + users['score']

		# Keeping track of the answers with the highest score
		if (counter < 10):
			highest_score_answers[users['answer_id']] = users['score']
			counter = counter + 1
		else:
			if (min(highest_score_answers.values()) < users['score']):
				min_key = min(highest_score_answers, key = highest_score_answers.get)
				del highest_score_answers[min_key]
				highest_score_answers[users['answer_id']] = users['score']
		
# Create the url about questions and request it
url1 = 'https://api.stackexchange.com/2.2/questions?fromdate=' + str(start_epoch) + '&todate=' + str(end_epoch) + '&order'
url2 = '=desc&sort=activity&filter=default&site=stackoverflow&key=6OCrTot*LgO0ncaJToxYcQ(('
url = url1 + url2
resp_obj = requests.get(url)
ques_data = resp_obj.json()

total_answers = 0
questions = 0
for users in ques_data['items']:
	total_answers = total_answers + users['answer_count']
	questions = questions + 1

# Create the url about comments and request it
highest_score_answers_comms = {}
for key in highest_score_answers.keys():
	s_url = 'https://api.stackexchange.com/2.2/answers/' + str(key) + '/comments?'
	m_url = 'fromdate' + str(start_epoch) + '&todate=' + str(end_epoch)
	e_url = '&order=desc&filter=default&site=stackoverflow&key=6OCrTot*LgO0ncaJToxYcQ(('

	url = s_url + m_url + e_url

	resp_obj = requests.get(url)
	comm_data = resp_obj.json()
	highest_score_answers_comms[key] = len(comm_data['items'])

# Print output depending on format
if (opts.output_format == 'tabular'):
	max_len = 60
	print('\n')
	print('\t Total Accepted answers:            ' + str(ans_accepted))
	print('\t Average score of accepted answers: %.1f' %(ans_scores/ans_accepted))
	print('\t Average answers per question:      %.1f' %(total_answers/questions))
	print('\t Top ten answers comment count:')
	for i,j in highest_score_answers_comms.items():
		print('\t\t' + str(i) + ': ' + str(j))
	sys.exit()
elif (opts.output_format == 'json'):
	json_dict = {}
	json_dict['total_accepted_answers'] = ans_accepted
	json_dict['accepted_answers_average_score'] = ans_scores/ans_accepted
	json_dict['average_answers_per_question'] = total_answers/questions
	json_dict['top_ten_answers_comment_count'] = highest_score_answers_comms
	print(json.dumps(json_dict, indent = 4, separators = (',', ': ')))
	sys.exit()
elif (opts.output_format == 'html'):
	print('\t <html>')
	print('\t \t <head>')
	print('\t \t \t <title>Encoding API Assignment</title>')
	print('\t \t </head>')
	print('\t \t <body>')
	print('\t \t \t Total accepted answers: ' + str(ans_accepted) + ' <br>')
	print('\t \t \t Average score of accepted answers: ' + ' %.1f'  %(ans_scores/ans_accepted) + '<br>')
	print('\t \t \t Average answers per question: ' + '%.1f' %(total_answers/questions) + '<br>')
	print('\t \t \t Top ten answers comment count: ' + '<br>')
	for i,j in highest_score_answers_comms.items():
		print('\t \t \t &emsp; '+ str(i) + ': ' + str(j) + '<br>')
	print('\t \t </body>')
	print('\t </html>')
	sys.exit()
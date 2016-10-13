from nltk.tokenize import word_tokenize
import re
import string
from nltk.corpus import stopwords


print("What file do you want to read?")
incoming_reports = open(str(input()),'r').readlines()
print("And where do you want to write to?")
outgoing_reports = str(input()+ '.txt')
outgoing_reports_append = outgoing_reports[:-4] + '_no_punct.txt'
outgoing_reports_no_stops = outgoing_reports[:-4] + '_no_stops.txt'


tokenized_reports = [word_tokenize(report) for report in incoming_reports]

with open(outgoing_reports,'w') as outfile:
    for lines in tokenized_reports:
        outfile.writelines("%s\n" % lines)
        
regex = re.compile('[%s]' % re.escape(string.punctuation))

tokenized_reports_no_punctuation = []

for review in tokenized_reports:
    
    new_review = []
    for token in review:
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
            
    tokenized_reports_no_punctuation.append(new_review)
    

with open(outgoing_reports_append,'w') as outfile:
    for lines in tokenized_reports_no_punctuation:
        outfile.writelines("%s\n" % lines)

tokenized_reports_no_stopwords = []

for report in tokenized_reports_no_punctuation:
    new_term_vector = []
    for word in report:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    tokenized_reports_no_stopwords.append(new_term_vector)
    
with open(outgoing_reports_no_stops,'w') as outfile:
    for lines in tokenized_reports_no_stopwords:
        outfile.writelines("%s\n" % lines)
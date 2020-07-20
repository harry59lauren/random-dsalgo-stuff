import csv
import ics
import pprint


with open('cyber600-syllabus.csv') as csvfile:
	events = []
	reader = csv.DictReader(csvfile)
	for row in reader:
		event = {
			'week': int(row['Week'] or events[-1]['week']),
			'event' : row['Event'],
			'date' : row['Date']
		}
		events.append(event)


c = ics.Calendar()

for e in events:
	evt = ics.Event()



pprint.pprint(events)
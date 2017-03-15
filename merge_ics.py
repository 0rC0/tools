#!/usr/bin/python3
import sys
from icalendar import Calendar
from os.path import isfile

def add_to_calendar(file_name, calendar):
    if isfile(file_name):
        with open(file_name, 'rb' ) as f:
            cal_from_file = Calendar.from_ical(f.read())
        for component in cal_from_file.walk('VEVENT'):
            if not component in calendar.walk('VEVENT'):
                calendar.add_component(component)
    else:
        raise Exception('not found{0}'.format(file_name))
    print(' {0} added'.format(file_name))    


def write_calendar(calendar):
    
    #if out.ics exists change filename with out[number].txt
    filename = 'out.ics'
    new_file_name = isfile(filename)
    i = 1
    while new_file_name:
        filename = 'out' + str(i) + '.ics'
        i += 1
        new_file_name = isfile(filename)
        
    with open(filename, 'wb') as f:
        f.write(calendar.to_ical())
    
    
def merge_ics(file_list):

    for i in file_list:
        try:
            calendar
        except:
            with open(i, 'rb' ) as f:
                calendar = Calendar.from_ical(f.read())
            print('{0} is added'.format(i))
        else:
            add_to_calendar(i, calendar)
    write_calendar(calendar)
    
    
def main(args):
    
    file_list = []
    for f in args:
        file_list.append(f)
    
    merge_ics(file_list)
    
if __name__ == '__main__':
    main(sys.argv[1:])

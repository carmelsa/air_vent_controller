import datetime

start = datetime.time(0, 0, 0)
end = datetime.time(0, 0, 0)
current = datetime.time(0, 0, 0)


def close_or_open(situation):
    global start
    global end
    global current
    if situation == 'open':
        print('0')
    elif situation == 'close':
        print('0')
    else:
        print('1', 'The inserted situation is not accepted')
    start = datetime.time(21, 0, 0)
    end = datetime.time(9, 0, 0)
    current = datetime.datetime.now().time()
    if close_or_open(start, end, current) == True:
        situation = 'open'
    start = datetime.time(12, 0, 0)
    end = datetime.time(16, 0, 0)
    current = datetime.datetime.now().time()
    if close_or_open(start, end, current) == True:
        situation = 'close'


close_or_open('open')

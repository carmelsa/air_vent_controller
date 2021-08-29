import datetime


def open_or_close(vent_status):
    is_input_valid(vent_status)
    wanted_status = get_wanted_vent_status()
    get_wanted_vent_status()
    if vent_status == wanted_status:
        print('you dont need to change the status')
    else:
        print('you need to change the status')


def is_input_valid(situation):
    if situation == 'open':
        valid = 0
        return valid
    elif situation == 'close':
        valid = 0
        return valid
    else:
        print('The inserted situation is not accepted')
        valid = 1



def get_wanted_vent_status():
    current = datetime.datetime.now().time()
    start = datetime.time(12, 0, 0)
    end = datetime.time(15, 0, 0)
    time = start <= current <= end
    if time == True:
        wanted_status = 'close'
        return wanted_status
    else:
        wanted_status = 'open'
        return wanted_status


def main():
    open_or_close('fgcxggfd')


if __name__ == '__main__':
    main()

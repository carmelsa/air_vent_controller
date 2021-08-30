temperature = [16, 17, 18, 19, 20]


def valid_check(temperature):
    for i in temperature:
        if i > 40:
            print('The temperature entered is not valid')
            exit()
        if i < 16:
            print('The temperature entered is not valid')
            exit()


def get_avg_temp(temperature):
    return sum(temperature) / len(temperature)


def get_min_temp(temperature):
    temperature.sort()
    return temperature[0]


def get_max_temp(temperature):
    temperature.sort()
    return temperature[-1]


get_avg_temp(temperature)
get_min_temp(temperature)
get_max_temp(temperature)

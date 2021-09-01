list_temperatures = []
highest_temperature = 40
lowest_temperature = 16


def get_all():
    get_avg_temp(list_temperatures)
    get_min_temp(list_temperatures)
    get_max_temp(list_temperatures)


def valid_check(temperatures):
    for i in temperatures:
        if i > highest_temperature:
            print('The temperature entered is not valid')
            exit()
        if i < lowest_temperature:
            print('The temperature entered is not valid')
            exit()


def get_avg_temp(temperatures):
    return sum(temperatures) / len(temperatures)


def get_min_temp(temperatures):
    temperatures.sort()
    return temperatures[0]


def get_max_temp(temperatures):
    temperatures.sort()
    return temperatures[-1]


def main():
    get_all()


if __name__ == '__main__':
    main()

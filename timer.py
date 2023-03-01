import math
import random
import sys
import time


def main():
    """
        main function is Just for testing code.
        be potion please.
        wrote by NightFox | Powered by python | Beta Version v0.001
    """
    # one line security
    # sys.exit() if not input('Enter Your Registration key: ') in ['secure', 'sex', '69', 'kiss', 'love'] else None


class Theme:
    """This class is going to save and organise attributes that we need in GUI"""

    def __init__(self):
        self.colors = {'pink': '#e2979c', 'red': '#e7305b', 'green': '#9bdeac', 'yellow': '#f7f5dd', 'blue': '#2555af'}
        self.font = ['Courier']
        self.argument = sys.argv[1] if len(sys.argv) > 1 else None


class Timer:
    """Convert different types of time to standard format hh:mm:ss or only seconds to make calculating easier."""

    def __init__(self):
        self.seconds = 0  # time in seconds
        self.datetime = [0, 0, 0]  # time in hh/mm/ss standard format
        self.hour = self.minute = self.second = 0
        self.update_time()

    def __repr__(self):
        return self.present()  # return str

    def __str__(self):
        return self.present()  # return str

    def __int__(self):
        return self.seconds  # return int as seconds

    def get_time(self, hour=0, minute=0, second=0) -> None:
        """Convert nonsense times like "101 second" to standard hh/mm/ss"""
        h = self.hour_to_second(hour)
        m = self.minute_to_second(minute)
        s = h + m + second
        self.seconds = s
        self.update_time()

    def update_time(self):
        self.datetime = self.second_to_time(self.seconds)
        self.hour, self.minute, self.second = self.datetime  # split time to for easy access and freeze original data

    def present(self, datetime=None) -> str:
        """ Presentation in standard format -> HH:mm:ss """
        # update the time first
        self.update_time()
        if not datetime:
            return f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}'
        else:
            return f'{str(datetime[0]).zfill(2)}:{str(datetime[1]).zfill(2)}:{str(datetime[2]).zfill(2)}'

    @staticmethod
    def minute_to_second(minute: int) -> int:
        if minute > 0 and isinstance(minute, int):
            return minute * 60
        else:
            return 0

    @staticmethod
    def hour_to_second(hour: int) -> int:
        if hour > 0 and isinstance(hour, int):
            return hour * 60 * 60
        else:
            return 0

    @staticmethod
    def second_to_time(second: int) -> list:
        s = m = h = int()
        if second >= 60:
            m = second // 60
            s = second % 60
        else:
            s = second
        if m >= 60:
            h = m // 60
            m = m % 60
        return [h, m, s]

    @staticmethod
    def hour_to_date(hour: int) -> list:
        """It's a feature"""
        # if Hours > 24 -> yy/mm/dd
        pass

    @staticmethod
    def delay(secs=1) -> None:
        """simple (1 second) interrupt function for Timer count-down"""
        time.sleep(1)

    def counter(self) -> None:
        # update the time first
        self.update_time()
        f = second = self.seconds  # count-down time as seconds | f=frozen_time
        datetime = self.second_to_time  # shorthand for second_to_time | [h,m,s]
        present = self.present  # shorthand for present | [h,m,s] -> hh:mm:ss
        print(f'Count-Down for {f}second|{present(datetime(f))} is starting:\n')  # start notification alert
        for i in range(self.seconds):
            second -= 1  # one second count-down
            self.delay()
            print(f'\r{present(datetime(second))}', end='')

    def count_down(self):
        # update the time first
        self.update_time()
        datetime = self.second_to_time  # shorthand for second_to_time | [h,m,s]
        present = self.present  # shorthand for present | [h,m,s] -> hh:mm:ss
        # count_down action one-by-one
        self.seconds -= 1
        return present(datetime(self.seconds))  # datetime(self.seconds) -> [h,m,s]


if __name__ == '__main__':
    main()

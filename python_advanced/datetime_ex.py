from datetime import datetime, date, time

def get_datetime():
    now = datetime.now()
    print(now)

    print(datetime(1999, 12, 31))

    # 요일
    print(now.weekday())

    # date
    print(now.date())
    # time
    print(now.time())


def timedelta_ex():
    current = datetime.now()
    past = datetime(2012, 9, 24)
    print(current > past)
    diff = current - past
    print(diff, type(diff))  # timedelta


def format_date():
    current = datetime.now()
    print(current)
    print(current.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

    mystr = "2045년 12월 23일 15시 43분 42초"
    parsed_date = datetime.strptime(mystr, "%Y년 %m월 %d일 %H시 %M분 %S초")
    print(repr(parsed_date))


if __name__ == '__main__':
    # get_datetime()
    # timedelta_ex()
    format_date()
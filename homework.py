import datetime as dt


class Record:
    FORMAT_DATE = '%d.%m.%Y'

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            moment = dt.datetime.strptime(date, Record.FORMAT_DATE)
            day = moment.date()
            self.date = day


class Calculator:
    day_now = dt.date.today()

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        amount = (sum(i.amount for i in self.records
                      if i.date == dt.date.today()))
        return amount

    def get_week_stats(self):
        date_ago = Calculator.day_now - dt.timedelta(days=7)
        amount = (sum(i.amount for i in self.records if i.date >= date_ago
                      and i.date <= dt.date.today()))
        return amount

    def calс_rest(self):
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        rest = self.calс_rest()
        if rest > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с '
                    f'общей калорийностью не более {rest} кКал')
        return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 80.0
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        currencies = {'eur': (CashCalculator.EURO_RATE, 'Euro'),
                      'usd': (CashCalculator.USD_RATE, 'USD'),
                      'rub': (CashCalculator.RUB_RATE, 'руб')
                      }
        rest = self.calс_rest()
        if rest == 0:
            return 'Денег нет, держись'
        curren_rate, curren = currencies[currency]
        rest = rest / curren_rate
        if rest < 0:
            rest_abs = abs(rest)
            return ('Денег нет, держись: твой долг - '
                    f'{rest_abs:.2f} {curren}')
        return f'На сегодня осталось {rest:.2f} {curren}'

import datetime as dt


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            moment = dt.datetime.strptime(date, '%d.%m.%Y')
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
        amount_all = 0
        for i in self.records:
            if i.date == Calculator.day_now:   
                amount_all += i.amount        
        return amount_all
        
    def get_week_stats(self):
        amount_all = 0
        date_ago = Calculator.day_now - dt.timedelta(days=7)     
        for i in self.records:
            if i.date >= date_ago and i.date <= Calculator.day_now : 
                amount_all += i.amount
        return amount_all 


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):     
        rest = self.limit - self.get_today_stats()        
        if rest > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с '
                    f'общей калорийностью не более {rest} кКал')
        else:
            return f'Хватит есть!'    
    

class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 80.0

    def get_today_cash_remained(self, currency):     
        curren = 'руб'
        rest = self.limit - self.get_today_stats()          
        if rest != 0:
            if currency == 'eur':
                rest = rest / CashCalculator.EURO_RATE
                curren = 'Euro'
            elif currency == 'usd':
                rest = rest / CashCalculator.USD_RATE
                curren = 'USD'
            if rest > 0:
                return f'На сегодня осталось {rest:.2f} {curren}'
            else:
                rest_abs = abs(rest)
                return (f'Денег нет, держись: твой долг - '
                        f'{rest_abs:.2f} {curren}')
        else:
            return f'Денег нет, держись'
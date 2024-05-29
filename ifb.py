import math
from babel.numbers import format_decimal
from copy import copy
def currencify(x):
    return format_decimal(x, locale="en_US")

def floor_to_nearest_50000(num):
    return math.floor(num / 50000) * 50000

class IFB_Feb2024:
    PAYMENT_DATES = ["19-Aug-2024", "17-Feb-2025", "18-Aug-2025", 
                     "16-Feb-2026", "17-Aug-2026", "15-Feb-2027", 
                     "16-Aug-2027", "14-Feb-2028", "14-Aug-2028", 
                     "12-Feb-2029", "13-Aug-2029", "11-Feb-2030", 
                     "12-Aug-2030", "10-Feb-2031", "11-Aug-2031",
                     "09-Feb-2032", "09-Aug-2032"]
    def __init__(self, face_value):
        self.face_value = float(face_value.replace(",", ""))
        self.create_bond_top_ups()
        self.interest_rate = 0.184607/2
        self.redemption_date = "09-Aug-2032"
        self.first_armotization = {"date": "15-Feb-2027", "proportion": 0.2}
        self.second_armotization = {"date": "11-Feb-2030", "proportion": 0.3}
        self.interests = []
        self.amortization = []
        self.get_all_results()
        self.bond_earnings()

    
    def create_bond_top_ups(self):
        self.face_value = floor_to_nearest_50000(self.face_value)
        self.original_face_value = copy(self.face_value)
    
    def get_all_results(self):
        for date in IFB_Feb2024.PAYMENT_DATES:
            self.calculate_interest(date)
            if date == self.first_armotization["date"]:
                if self.face_value <= 1_000_000:
                    self.redeem(date)
                    break
                else:
                    self.amortization.append({"date": date, "amortized": self.first_armotization["proportion"] * self.face_value})
                    self.face_value *= (1-self.first_armotization["proportion"])
            else:
                if date == self.second_armotization["date"]:
                    self.amortization.append({"date": date, "amortized": self.second_armotization["proportion"] * self.face_value})
                    self.face_value *= (1-self.second_armotization["proportion"])
            if date == IFB_Feb2024.PAYMENT_DATES[-1]:
                self.redeem(date)
            

    def calculate_interest(self, date):
        self.interests.append({"date": date, "outstanding principal": self.face_value , "interest": self.face_value * self.interest_rate})

    def redeem(self,date):
        interest = self.face_value * self.interest_rate
        for adict in self.interests:
            if date == adict["date"]:
                adict["interest"] = interest
                adict["final redemption"] = self.face_value + interest

    def bond_earnings(self):
        total_earnings = 0
        self.total_amortization= sum([i["amortized"] for i in self.amortization])
        for payment in self.interests:
            total_earnings += payment["interest"]
        self.all_earnings = {"total earnings": total_earnings, 
                             "total gross payback": self.original_face_value+total_earnings+self.total_amortization}
    
if __name__ == "__main__":
    fv = 3800_000
    inst = IFB_Feb2024(fv)
    [print(i) for i in inst.interests]
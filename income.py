from babel.numbers import format_decimal
def currencify(x):
    return format_decimal(x, locale="en_US")

class IFB_Feb2024:
    PAYMENT_DATES = ["19-Aug-2024", "17-Feb-2025", "18-Aug-2025", 
                     "16-Feb-2026", "17-Aug-2026", "15-Feb-2027", 
                     "16-Aug-2027", "14-Feb-2028", "14-Aug-2028", 
                     "12-Feb-2029", "13-Aug-2029", "11-Feb-2030", 
                     "12-Aug-2030", "10-Feb-2031", "11-Aug-2031",
                     "9-Feb-2032", "9-Aug-2032"]
    def __init__(self, face_value):
        self.face_value = float(face_value.replace(",", ""))
        self.interest_rate = 0.184607
        self.redemption_date = "09-Aug-2032"
        self.first_armotization = {"date": "15-Feb-2027", "proportion": 0.2}
        self.second_armotization = {"date": "11-Feb-2030", "proportion": 0.3}
    
    def calculate_interest_payments(self):
        interest_list = []
        sumup_interest = 0
        amortization_payouts = 0

        for date in IFB_Feb2024.PAYMENT_DATES:
            interest = self.interest_rate * self.face_value/2
            sumup_interest += interest
            if date == self.first_armotization["date"]:
                if self.face_value <= 1_000_000:
                    interest_list.append({"date": date, 
                                          "interest": f'{currencify(interest)}', 
                                          "outstanding principal": f'{currencify(0)}', 
                                          "amortization_payout": f'{0}',
                                          "final redemption": f'{currencify(self.face_value+interest)}'})
                    break
                else:
                    pr1 = self.first_armotization["proportion"]
                    amortization_payout = pr1*self.face_value
                    amortization_payouts += amortization_payout
                    interest_list.append({"date": date, "outstanding principal": f'{currencify(self.face_value)}', 
                                          "interest": f'{currencify(interest)}', 
                                          "outstanding principal": f'{currencify(self.face_value)}',
                                          "amortization_payout": f'{currencify(amortization_payout)}',
                                          "total payout": f'{currencify(amortization_payout + interest)}'})

                    self.face_value = (1-pr1) * self.face_value
            elif date == self.second_armotization["date"]:
                pr2 = self.second_armotization["proportion"]
                amortization_payout = pr2*self.face_value
                amortization_payouts += amortization_payout
                interest_list.append({"date": date, "outstanding principal": f'{currencify(self.face_value)}', 
                                      "interest": f'{currencify(interest)}', 
                                      "outstanding principal": f'{currencify(self.face_value)}',
                                      "amortization payout": f'{currencify(amortization_payout)}',
                                      "total payout": f'{currencify(amortization_payout + interest)}'})
                self.face_value = (1-pr2) * self.face_value
            else:
                if date != IFB_Feb2024.PAYMENT_DATES[-1]:
                    interest_list.append({"date": date, "outstanding principal": f'{currencify(self.face_value)}', "interest": f'{currencify(interest)}'})
                else:
                    total_payout = self.face_value + sumup_interest + amortization_payouts
                    interest_list.append({"date": date,
                                          "interest":  f'{currencify(interest)}',
                                          "outstanding principal": f'{currencify(self.face_value)}', 
                                          "total interest payments": f'{currencify(sumup_interest)}',
                                          "final redemption": f'{currencify(self.face_value+interest)}',
                                          "total amortization payout": f'{currencify(amortization_payouts)}',
                                          "total amount paid back since investment": f'{currencify(total_payout)}'})
        
        return interest_list
                


if __name__ == "__main__":
    fv = 900_000
    ifb = IFB_Feb2024(fv)
    interests = ifb.calculate_interest_payments()
    for i in interests:
        print(i)
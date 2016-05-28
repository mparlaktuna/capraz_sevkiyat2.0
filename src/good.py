class Good():
    def __init__(self):
        self.good_amount = 0
        self.good_index = 0
        self.income_truck = 0

    def remove_good(self, amount):
        if amount >= self.good_amount:
            removed_amount = self.good_amount
            self.good_amount = 0
            return [removed_amount, self.income_truck]
        else:
            self.good_amount -= amount
            return [amount, self.income_truck]


from src.good import Good


class GoodList():
    def __init__(self, good_name):
        self.total_amount = 0
        self.good_index = good_name
        self.good_list = []

    def add_good(self, amount, income_truck):
        new_good = Good()
        new_good.good_amount = amount
        new_good.good_index = self.good_index
        new_good.income_truck = income_truck
        self.good_list.append(new_good)
        self.calculate_total()

    def calculate_total(self):
        total = 0
        for good in self.good_list:
            total += good.good_amount
        self.total_amount = total
        return self.total_amount

    def check_enough(self, amount):
        self.calculate_total()
        if self.total_amount >= amount:
            return True
        else:
            return False

    def remove_good(self, amount):
        removed_amount = 0
        remove_list = []
        if self.check_enough(amount):
            while amount != 0:
                for good in self.good_list:
                    remove_item = good.remove_good(amount)
                    amount -= remove_item[0]
                    removed_amount += remove_item[0]
                    remove_list.append(remove_item)

            self.remove_zeros()
            self.calculate_total()
            return remove_list
        else:
            print("Not Enough Good")
            return False

    def remove_zeros(self):
        zero_list = []
        for i, good in enumerate(self.good_list):
            if good.good_amount == 0:
                zero_list.append(i)
        for i in (sorted(zero_list, reverse=True)):
            del self.good_list[i]


    def print_goods(self):
        for good in self.good_list:
            print("Good Name:", good.good_index, "Goood Amount: ", good.good_amount)

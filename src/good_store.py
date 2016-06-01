from src.good_list import GoodList


class GoodStore():
    def __init__(self):
        self.good_dictionary = {}
        self.good_amounts = {}

    def add_good_type(self, good_name):
        new_good_list = GoodList(good_name)
        self.good_dictionary[good_name] = new_good_list
        self.good_amounts[good_name] = 0

    def add_good(self, amount, name, truck_name):
        if name in self.good_dictionary.keys():
            self.good_dictionary[name].add_good(amount, truck_name)
        else:
            self.add_good_type(name)
            self.good_dictionary[name].add_good(amount, truck_name)
        self.calculate_total()

    def calculate_total(self):
        for good_name, good_list in self.good_dictionary.items():
            self.good_amounts[good_name] = good_list.calculate_total()
        return sum(self.good_amounts.values())

    def check_enough(self, good_dict):
        enough = False
        for good_name, good_amount in good_dict.items():
            if good_name in self.good_amounts.keys():
                if self.good_amounts[good_name] >= good_amount:
                    enough = True
                else:
                    enough = False
                    return enough
            else:
                enough = False
                return enough
        return enough

    def remove_good(self, good_dict):
        remove_dict = {}
        if self.check_enough(good_dict):
            for good_name, good_amount in good_dict.items():
                remove_list = GoodList(good_name)
                removed_items = self.good_dictionary[good_name].remove_good(good_amount)
                for items in removed_items:
                    remove_list.add_good(items[0], items[1])
                remove_dict[good_name] = remove_list
        else:
            print("Not Enough Good")
        self.calculate_total()
        return remove_dict

    def add_good_dict(self, good_dict):
        for good_name, good_list in good_dict.items():
            for good in good_list.good_list:
                self.add_good(good.good_amount, good_name, good.income_truck)

    def reset_goods(self):
        for good_name, good_list in self.good_dictionary.items():
            self.good_dictionary[good_name] = GoodList(good_name)
            self.good_amounts[good_name] = 0

    def print_goods(self):
        t = ''
        for good_name, good_list in self.good_dictionary.items():
            t += "Good Name:{0}\n".format(good_name)
            t += good_list.print_goods()
        return t


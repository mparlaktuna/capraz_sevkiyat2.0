from src.good_store import GoodStore

good_store = GoodStore()
good_store.add_good_type(0)
good_store.add_good_type(1)
good_store.add_good_type(3)

print(good_store.good_amounts)
print(good_store.good_dictionary)

good_store.add_good(50, 0, 'inbound0')
good_store.add_good(50, 0, 'inbound1')

print(good_store.good_amounts)
print(good_store.good_dictionary)

good_store.add_good(200, 2, 'inbound0')
good_store.add_good(200, 1, 'inbound0')
print(good_store.good_amounts)
print(good_store.good_dictionary)

remove_dict = {0: 100, 1: 200, 2:100}
removed = good_store.remove_good(remove_dict)
print(removed)
print(good_store.good_amounts)
print(good_store.good_dictionary)
for good_list in removed.values():
    good_list.print_goods()

good_store.add_good_dict(removed)
print(good_store.good_amounts)
print(good_store.good_dictionary)

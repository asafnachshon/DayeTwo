import unittest
from Inventory import *
from random import *

items_upper = ["T-SHIRT", "SHIRT", "JEANS", "TROUSERS", "HOODIES", "SHOES",
               "SOCKS", "HAT", "TIE", "SWEATSHIRTS"]
items_lower = ['t-shirt', 'shirt', 'jeans', 'trousers', 'hoodies', 'shoes',
               'socks', 'hat', 'tie', 'sweatshirts']
items_cap = ['T-shirt', 'Shirt', 'Jeans', 'Trousers', 'Hoodies', 'Shoes',
             'Socks', 'Hat', 'Tie', 'Sweatshirts']
number_of_items = len(items_upper)
item_num = randint(0,number_of_items-1)

store_name = "Clothes 4 ALL"

current_week = datetime.datetime.now().isocalendar()[1]
current_year = datetime.datetime.now().year
weeks = list(range(1,53))
years = [y for y in range(2013,current_year)]


class TestIvnentory(unittest.TestCase):
    
    def setUp(self):
        self.Store = Inventory(store_name)
        for year in years:
            for week in weeks:
                for item in items_upper:
                    self.Store.item_count(item, randint(1,100), week, year)
        for week in list(range(1,current_week+1)):
            for item in items_upper:
                self.Store.item_count(item, randint(1,100), week, current_year)

    def test_StoreName(self):
        print("Store Name:  " + store_name+"\nStore's name case sensitive test")
        self.assertEqual(self.Store.store, store_name)
        self.assertNotEqual(self.Store.store, store_name.upper())
        self.assertNotEqual(self.Store.store, store_name.lower())

    def test_itemCount(self):
        print("\nItems input are not case sensitive")
        print("Items are added only in capitalize form regardless of their input")
        print("Each item has its own inventory history, represented by 'Item' class")
        print("'Item' class consist of Name and a dictionary")
        print("The dictionary Keys are years, and the values are count per week")
        item_num = randint(0,number_of_items-1)
        self.assertNotIn(items_upper[item_num], list(self.Store.inventory.keys()))
        item_num = randint(0,number_of_items-1)
        self.assertNotIn(items_upper[item_num], list(self.Store.inventory.keys()))
        item_num = randint(0,number_of_items-1)
        self.assertNotIn(items_lower[item_num], list(self.Store.inventory.keys()))
        item_num = randint(0,number_of_items-1)
        self.assertNotIn(items_lower[item_num], list(self.Store.inventory.keys()))
        item_num = randint(0,number_of_items-1)
        self.assertIn(items_upper[item_num].capitalize(), list(self.Store.inventory.keys()))
        item_num = randint(0,number_of_items-1)
        self.assertIn(items_upper[item_num].capitalize(), list(self.Store.inventory.keys()))
        item_num = randint(0,number_of_items-1)
        self.assertIn(items_lower[item_num].capitalize(), list(self.Store.inventory.keys()))
        item_num = randint(0,number_of_items-1)
        self.assertIn(items_lower[item_num].capitalize(), list(self.Store.inventory.keys()))
        item_num = randint(0,number_of_items-1)
        print("\nEach year can contain a list of up to 52 integers")
        print("Each integer represents the count for that week")
        print("'None' value will appear when no count has been made that week")
        rand_item = items_cap[randint(0,number_of_items-1)]
        years_indx = randint(0,len(years)-1)
        self.assertLessEqual(len(self.Store.inventory[rand_item].inventory[years[years_indx]]), 52)
        rand_item = items_cap[randint(0,number_of_items-1)]
        years_indx = randint(0,len(years)-1)
        self.assertLessEqual(len(self.Store.inventory[rand_item].inventory[years[years_indx]]), 52)
        rand_item = items_cap[randint(0,number_of_items-1)]
        years_indx = randint(0,len(years)-1)
        self.assertLessEqual(len(self.Store.inventory[rand_item].inventory[years[years_indx]]), 52)

    def test_week_X(self):
        print("\n'Week_X' Retrieves the inventory count for week #X of a particular year")
        print("'this_week' retrieves the inventory count for the currnet week")
        print("'week-before' retrieves the inventory count for the week befor the input week")
        self.assertDictEqual(self.Store.this_week(),self.Store.week_X(current_week,current_year))
        years_indx = randint(1,len(years)-1)
        weeks_indx = randint(1,len(weeks)-2)
        self.assertDictEqual(self.Store.week_X(weeks[weeks_indx],years[years_indx]),\
                                      self.Store.week_before(weeks[weeks_indx+1],years[years_indx]))
        years_indx = randint(1,len(years)-1)
        weeks_indx = randint(1,len(weeks)-2)
        self.assertDictEqual(self.Store.week_X(weeks[weeks_indx],years[years_indx]),\
                                      self.Store.week_before(weeks[weeks_indx+1],years[years_indx]))
        years_indx = randint(1,len(years)-1)
        weeks_indx = randint(1,len(weeks)-2)
        self.assertDictEqual(self.Store.week_X(weeks[weeks_indx],years[years_indx]),\
                                      self.Store.week_before(weeks[weeks_indx+1],years[years_indx]))
        years_indx = randint(1,len(years)-1)
        weeks_indx = randint(1,len(weeks)-2)
        self.assertDictEqual(self.Store.week_X(weeks[weeks_indx],years[years_indx]),\
                                      self.Store.week_before(weeks[weeks_indx+1],years[years_indx]))

    def test_show_inventory(self):
        print("\n'show_inventory' returns a dictionary with items as keys")
        print("Every item has a list as value")
        print("The list consists of three values:")
        print("1- The chosen week count")
        print("2- The week before count")
        print("3- The difference between them")
        week = weeks[randint(1,len(weeks)-1)]
        year = years[randint(1,len(years)-1)]
        print("\nInventory for week #" + str(week) + " in " + str(year) + ":")
        print(self.Store.show_inventory(week, year))
        week = weeks[randint(1,len(weeks)-1)]
        year = years[randint(1,len(years)-1)]
        print("\nInventory for week #" + str(week) + " in " + str(year) + ":")
        print(self.Store.show_inventory(week, year))
        week = weeks[randint(1,len(weeks)-1)]
        year = years[randint(1,len(years)-1)]
        print("\nInventory for week #" + str(week) + " in " + str(year) + ":")
        print(self.Store.show_inventory(week, year))
        week = weeks[randint(1,len(weeks)-1)]
        year = years[randint(1,len(years)-1)]
        print("\nInventory for week #" + str(week) + " in " + str(year) + ":")
        print(self.Store.show_inventory(week, year))
        week = weeks[randint(1,len(weeks)-1)]
        year = years[randint(1,len(years)-1)]
        print("\nInventory for week #" + str(week) + " in " + str(year) + ":")
        print(self.Store.show_inventory(week, year))
        
            
        
        
if __name__== '__main__':
    unittest.main()

import datetime
from datetime import date

class Item():

    def __init__(self, name):
        self.item = name
        self.inventory = dict() #Keys are years
                                #Values are lists of up to 52 integers (count per week)

    def __repr__(self):
        return str(self.item)

    def quantity_update(self, quantity, week, year):
        #Updates the item's inventory count for a given week and year
        if year not in self.inventory:
            self.inventory[year] = [0] * week
            #Create a new inventory count for a new year
            #The inventory count will be up to the given week
        if week > len(self.inventory[year]):
            difference = week - len(self.inventory[year])#The number of weeks between the given week and the last week on the list
            self.inventory[year] += [0] * difference #Extension of the list
        self.inventory[year][week-1] = quantity #Updating the item quantity for the given week

    def inventory_by_year(self, year):
        #Returns the item's inventory count for a specific year
        if year in self.inventory:
        #Check to see if there is an inventory count that year
            return self.inventory[year] #A list of up to 52 values, one for each week
        else:
            return None

    def inventory_by_week(self, week, year):
        #Returns the item's inventory count for a specific week and year
        year_inventory = self.inventory_by_year(year)
        if year_inventory == None or len(year_inventory) < week:
        #Check to see if there is an inventory count that week
            return None
        else:
            return self.inventory_by_year(year)[week-1]

class Inventory():

    def __init__(self, store_name):
        assert isinstance(store_name, str)
        self.store = store_name
        self.inventory = dict() #Keys are the items names
                                #Values are 'Item' class

    def __repr__(self):
        return str(self.store)

    def add_item(self, item):
        assert isinstance(item, str) #Most be string
        item = item.capitalize()
        self.inventory[item] = Item(item) #Creating a new item inventory

    def item_count(self, item, count,\
                   week = datetime.datetime.now().isocalendar()[1],\
                   year = datetime.datetime.now().year):
        #The default values for the week and year are the current ones
        assert isinstance(count, int) and\
               week in list(range(1,53)) and\
               isinstance(year, int)
        #Count most be an integer
        #Week must be between 1 and 52
        #Year most be an integer
        item = item.capitalize()
        if item not in self.inventory:
            self.add_item(item) #Add item to inventory list if missing
        self.inventory[item].quantity_update(count, week, year) #Update item quantity for the given week and year

    def week_X(self, week, year):
        assert week in list(range(1,53)) and\
               isinstance(year, int)
        #Week must be between 1 and 52 and
        #Year most be an integer
        items = list(self.inventory.keys()) #All items listed in the inventory
        week_X_inventory = dict()
        for item in items:
            week_X_inventory[item] = self.inventory[item].inventory_by_week(week, year)
            #Create a dictionary of items and their amount for the selected week 
        return week_X_inventory

    def this_week(self):
        #Create a dictionary of items and their amount for the corrent week
        return self.week_X(datetime.datetime.now().isocalendar()[1],\
                           datetime.datetime.now().year)

    def week_before(self,\
                    week = datetime.datetime.now().isocalendar()[1],\
                    year = datetime.datetime.now().year):
        #Create a dictionary of items and their amount for week befor the selected week
        #Returns last week's values by defult
        if week == 1:
            return self.week_X(52, datetime.datetime.now().year - 1)
            #The week before it is 52 of the previous year
        return self.week_X(week-1, year)
            
    def show_inventory(self, week = None, year = None):
        #Returns the list of items of the selected week with this week
        #amount, the amount of the week before, and the difference between them
        if week == None:
            current = self.this_week()
            before = self.week_before()
        else:
            if year == None:
                year = datetime.datetime.now().year
            current = self.week_X(week, year)
            before = self.week_before(week, year)
        items = current.keys()
        table = dict()
        for item in items:
            table[item] = [current[item]]
            if item in before:
                table[item] += [before[item]]
                if None not in table[item]:
                    table[item] += [current[item] - before[item]]
                else:
                    table[item] += [None]
            else:
                table[item] += [None, None]
        return table


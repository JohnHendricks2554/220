"""
Name: John Hendricks
sales_person.py

Problem: Encapsulate data for a sales person creating class

Authenticity: I certify that the code below is entirely my own and no one else's
"""

class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return list(self.sales)

    def met_quota(self, quota):
        if sum(self.sales) > quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other > self:
            return -1
        if other < self:
            return 1
        if other == self:
            return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, sum(self.sales))

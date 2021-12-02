"""
Name: John Hendricks
sales_force.py

Problem: Encapsulate data for a sales person using classes

Authenticity: I certify that the code below is entirely mine and no on else's
"""
from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, filename):
        infile = open(filename, "r")
        for line in infile:
            self.sales_people.append(line)

    def quota_report(self, quota):
        x = True
        y = False
        for line in self.sales_people:
            if sum(self.sales_people[2]) >= quota:
                self.sales_people.append(x)
            else:
                self.sales_people.append(y)

        return self.sales_people

    #def top_seller(self):

    def individual_sales(self, employee_id):
        if employee_id == SalesPerson.get_id(employee_id):
            return SalesPerson
        else:
            return None


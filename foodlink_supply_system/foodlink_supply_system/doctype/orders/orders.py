# # Copyright (c) 2023, rsvasanth and contributors
# # For license information, please see license.txt

# # import frappe
# from frappe.model.document import Document

# class Orders(Document):
# 	pass

import frappe
from datetime import datetime, timedelta
from frappe.utils import add_to_date , today
from frappe.model.document import Document

day = today()
dt = datetime.strptime(day, '%Y-%m-%d')
st = dt - timedelta(days=dt.weekday())
start = add_to_date(st, days=7, as_string=True)
end = add_to_date(start, days=5, as_string=True)

class Orders(Document):
	def validate(self):
		self.order_starting_date = start
		self.order_ending_date = end
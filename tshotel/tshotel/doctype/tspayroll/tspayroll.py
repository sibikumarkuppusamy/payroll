# Copyright (c) 2021, sibi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class tspayroll(Document):
	def validate(self):
		r={"software developer":10000,"HR":20000,"manager":15000}
		self.ts_salary=r[self.ts_role]
		

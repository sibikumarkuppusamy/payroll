# Copyright (c) 2013, sibi and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from erpnext.accounts.utils import get_balance_on
def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data
def get_columns(filters):
	columns = [
		{
			"label": _("Name"),
			"fieldtype": "Data",
			"fieldname": "ts_emp_name",
			"width": 100
		},
		{
			"label": _("No Of Days"),
			"fieldtype": "Int",
			"fieldname": "tsno_of_days",
			"width": 100
		},
		{
			"label": _("salary"),
			"fieldtype": "Float",
			"fieldname": "ts_salary",
			"options": "ts_salary",
			"width": 100
		}
	]

	return columns
def get_conditions(filters):
	conditions = {}

	if filters.tsno_of_days:
		conditions["tsno_of_days"] = filters.tsno_of_days
	

	return conditions
def get_data(filters):

	data = []
	conditions = get_conditions(filters)
	print(conditions)
	accounts = frappe.db.get_all("tspayroll", fields=["ts_emp_name", "tsno_of_days", "ts_salary"], filters=conditions,order_by='ts_emp_name')
	for d in accounts:
		row = {"ts_emp_name": d.ts_emp_name, "tsno_of_days": d.tsno_of_days,"ts_salary":d.ts_salary}

		data.append(row)


	return data

import frappe
@frappe.whitelist(allow_guest=True)
def si():
    name=frappe.get_all("employee_details")
    return name

#/home/thirvusoft/frappe-bench/apps/tshotel/tshotel/api.py
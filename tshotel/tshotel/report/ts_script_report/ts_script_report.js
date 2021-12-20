// Copyright (c) 2016, sibi and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Ts Script Report"] = {
	"filters": [
		{
			fieldname:"tsno_of_days",
			label: __("No of days"),
			fieldtype: "Int",
			mandatory: true,
			default: frappe.defaults.get_user_default("20")
		},

	]
};

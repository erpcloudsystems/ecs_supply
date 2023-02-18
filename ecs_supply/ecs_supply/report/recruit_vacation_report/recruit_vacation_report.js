// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Recruit Vacation Report"] = {
	"filters": [
	    {
			fieldname: "date",
			label: __("تاريخ العودة من الاجازة"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
		},
        {
			fieldname: "recruit",
			label: __("رقم المجند"),
			fieldtype: "Link",
			options: "Employee",
		},
        {
			fieldname: "overnight",
			label: __("نوع الاجازة"),
			fieldtype: "Select",
			options: ["","مبيت","اجازة دورية"],
			reqd: 1,
		},


	]
};
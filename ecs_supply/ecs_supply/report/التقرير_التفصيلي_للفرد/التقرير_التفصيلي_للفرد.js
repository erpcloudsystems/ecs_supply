// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["التقرير التفصيلي للفرد"] = {
	"filters": [
	    // {
		// 	fieldname: "from_date",
		// 	label: __("من تاريخ"),
		// 	fieldtype: "Date",
		// 	// default: frappe.datetime.add_months(frappe.datetime.get_today(), -12),
		// },
		// {
		// 	fieldname:"to_date",
		// 	label: __("إلى تاريخ"),
		// 	fieldtype: "Date",
		// 	// default: frappe.datetime.get_today(),
		// },
        {
			fieldname: "policemen",
			label: __("أسم الفرد"),
			fieldtype: "Link",
			options: "Envestigation Employee",
		},
		// {
		// 	fieldname: "policemen_rank",
		// 	label: __("الرتبة"),
		// 	fieldtype: "Link",
		// 	options: "Policemen Rank",
		// },
		// {
		// 	fieldname: "punishment_type",
		// 	label: __("نوع العقوبة"),
		// 	fieldtype: "Link",
		// 	options: "Punishment Type",
		// },

	]
};
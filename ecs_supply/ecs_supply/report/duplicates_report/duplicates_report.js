// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Duplicates Report"] = {
	"filters": [
	
        {
			fieldname: "entities",
			label: __("جهة العمل"),
			fieldtype: "Link",
			options: "Entities",
		},
        {
			fieldname: "filter_value",
			label: __("طريقة العرض"),
			fieldtype: "Select",
			options: [
				{ "value": "personal_name", "label": __("عرض الاسماء المكرره") },
				{ "value": "id_number", "label": __("عرض ارقام الشرطه المكرره") },

			],
			default:"personal_name",
		},
        {
			fieldname: "fiscal_year",
			label: __("السنة المالية"),
			fieldtype: "Link",
			options: "Fiscal Year",
			default: "2023-2024",
		},

	]
};
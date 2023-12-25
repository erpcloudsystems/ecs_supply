// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير الكشف الجنائي 2"] = {
	"filters": [
        {
			fieldname: "the_recruits",
			label: __("أسم المتحري عنه"),
			fieldtype: "Link",
			options:"The Recruits"
		},
		{
			fieldname: "filter",
			fieldtype: "Select",
			options:["","احكام مجندين","احكام الاقارب","معلومات مجندين","معلومات الاقارب"]
		},
		
	]
};
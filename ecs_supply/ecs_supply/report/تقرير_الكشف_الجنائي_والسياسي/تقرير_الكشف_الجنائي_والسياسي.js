// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt


frappe.query_reports["تقرير الكشف الجنائي والسياسي"] = {
	"filters": [
        {
			fieldname: "recruit",
			label: __("أسم المتحري عنه"),
			fieldtype: "Link",
			options:"Envestigation Employee"
		},
		{
			fieldname: "filter",
			fieldtype: "Select",
			options:["","احكام افراد","احكام الاقارب","معلومات افراد","معلومات الاقارب"]
		},
		
	]
};
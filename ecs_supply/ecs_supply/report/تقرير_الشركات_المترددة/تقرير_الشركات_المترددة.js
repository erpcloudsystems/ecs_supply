// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير الشركات المترددة"] = {
	"filters": [
        {
			fieldname: "name",
			label: __("الأسم"),
			fieldtype: "Data"
		},
		{
			fieldname: "company_name",
			label: __("أسم الشركة"),
			fieldtype: "Data"
		}
	]
};

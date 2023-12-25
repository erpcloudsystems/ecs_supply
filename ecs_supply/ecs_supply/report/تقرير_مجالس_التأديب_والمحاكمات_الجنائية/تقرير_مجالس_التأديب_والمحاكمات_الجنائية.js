// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير مجالس التأديب والمحاكمات الجنائية"] = {
	"filters": [
        {
			fieldname: "policemen",
			label: __("أسم الفرد"),
			fieldtype: "Link",
			options: "Envestigation Employee",
		}
	]
};
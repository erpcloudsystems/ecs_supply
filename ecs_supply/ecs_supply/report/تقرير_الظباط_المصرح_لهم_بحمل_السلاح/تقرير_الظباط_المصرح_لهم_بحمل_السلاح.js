// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير الظباط المصرح لهم بحمل السلاح"] = {
	"filters": [
		{
			fieldname: "recruit",
			label: __("أسم المتحري عنه"),
			fieldtype: "Link",
			options: "Officers Affairs"
		},
		{
			fieldname: "gun_reason",
			label: __("تصريح حمل السلاح"),
			fieldtype: "Select",
			options: ['','غير مصرح إحترازي', 'غير مصرح عضوي' ,'غير مصرح نفسي','مصرح']
		},
	]
};

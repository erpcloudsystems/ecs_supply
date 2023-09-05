// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Print Analysis for Entities"] = {
	"filters": [
		{
			fieldname: "title",
			label: __("فئة التعريف"),
			fieldtype: "Select",
			options: [
					"أفراد",
					"مساعدين",
					"ضباط"],
			default:"ضباط"
		},
	    {
			fieldname: "from_date",
			label: __("من تاريخ"),
			fieldtype: "Date",
			// default: frappe.datetime.add_months(frappe.datetime.get_today(), -12),
		},
		{
			fieldname:"to_date",
			label: __("إلى تاريخ"),
			fieldtype: "Date",
			// default: frappe.datetime.get_today(),
		},
        {
			fieldname: "entities",
			label: __("جهة العمل"),
			fieldtype: "Link",
			options: "Entities",
		},
        {
			fieldname: "reason_for_entitlement",
			label: __("سبب الاستحقاق"),
			fieldtype: "Link",
			options: "Reason for Entitlement",
		},
        {
			fieldname: "fiscal_year",
			label: __("السنة المالية"),
			fieldtype: "Link",
			options: "Fiscal Year",
			default: frappe.defaults.get_user_default("fiscal_year"),
		},

	]
};
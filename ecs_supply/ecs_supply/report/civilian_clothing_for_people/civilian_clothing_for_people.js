// Copyright (c) 2024, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["Civilian Clothing For people"] = {
	"filters": [
		{
			fieldname: "officer_name",
			label: __("اسم الفرد"),
			fieldtype: "Data",
		},
		{
			fieldname: "id_number",
			label: __("رقم الأقدمية"),
			fieldtype: "Data",
		},
		{
			fieldname: "name",
			label: __("رقم الكوبون"),
			fieldtype: "Data",
		},
		{
			fieldname: "entities",
			label: __("الجهة"),
			fieldtype: "Link",
			options: "Clothing Entity",
		},
		{
			fieldname: "rank",
			label: __("الرتبة"),
			fieldtype: "Link",
			options: "police rank",
		},
        {
			fieldname: "fiscal_year",
			label: __("السنة المالية"),
			fieldtype: "Link",
			options: "Fiscal Year"

		},
		{
			fieldname: "listed_unlisted",
			label: __("مدرج / غير مدرج"),
			fieldtype: "Select",
			options: ["","مدرج","غير مدرج"],
		},
		{
			fieldname: "reason_for_entitlement",
			label: __("سبب الإستحقاق"),
			fieldtype: "Link",
			options: "Reason for Entitlement",
		},
		{
			fieldname: "assigned_work",
			label: __("العمل المسند"),
			fieldtype: "Link",
			options: "Job Code",
		},
        {
			fieldname: "job",
			label: __("نوع الوظيفة"),
			fieldtype: "Select",
			options: ["","مباحث","نظام"],
		},
		{
			fieldname: "print",
			label: __("حالة الطباعة"),
			fieldtype: "Select",
			options: ["","تم الطباعه","لم يتم الطباعه"],
		},
		{
			fieldname: "clear_filters",
			label: __("حذف الفلاتر"),
			fieldtype: "Check",
			on_change: function(){
				frappe.query_report.set_filter_value('officer_name', '');
				frappe.query_report.set_filter_value('id_number', '');
				frappe.query_report.set_filter_value('name', '');
				frappe.query_report.set_filter_value('entities', '');
				frappe.query_report.set_filter_value('rank', '');
				frappe.query_report.set_filter_value('listed_unlisted', '');
				frappe.query_report.set_filter_value('reason_for_entitlement', '');
				frappe.query_report.set_filter_value('assigned_work', '');
				frappe.query_report.set_filter_value('job', '');
				frappe.query_report.set_filter_value('print', '');
				frappe.query_report.set_filter_value('clear_filters', 0);
				frappe.query_report.refresh();
			}
		},
	]
};
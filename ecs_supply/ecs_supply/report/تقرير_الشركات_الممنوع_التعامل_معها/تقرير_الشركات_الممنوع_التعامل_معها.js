// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.query_reports["تقرير الشركات الممنوع التعامل معها"] = {
	"filters": [
        {
			fieldname: "year",
			label: __("السنة المالية"),
			fieldtype: "Link",
			options: "Fiscal Year",
		},
		{
			fieldname: "the_company_name",
			label: __("أسم الشركة"),
			fieldtype: "Data"
		},
		{
			fieldname: "the_owner_of_the_company",
			label: __("مالك الشركة"),
			fieldtype: "Data"
		},
	]
};

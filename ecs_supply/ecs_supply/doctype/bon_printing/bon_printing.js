// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on("Bon Printing", {
    refresh: function(frm, cdt, cdn) {
        if (frm.doc.docstatus == 1) {
            frm.add_custom_button(__("تكرار"), function() {
                var child = locals[cdt][cdn];
                frappe.route_options = {
                    "entity": frm.doc.entity,
                    "title": frm.doc.title,
                    "reason_for_entitlement": frm.doc.reason_for_entitlement,
                    "fiscal_year": frm.doc.fiscal_year,
                    "print_count": frm.doc.print_count,
                };
            frappe.new_doc("Bon Printing");
            },);
        }
    }
});

frappe.ui.form.on('Bon Printing', {
	refresh:function(frm){
        // frm.set_df_property("officers_deserves_exchange_report", "cannot_delete_rows", true);
        frm.set_df_property("bon_printing_civilians", "cannot_add_rows", true);
		if (frm.doc.printed) {

			frm.set_df_property("officers_deserves_exchange_report", "hidden", true);
		} else {
			frm.set_df_property("officers_deserves_exchange_report", "hidden", false);

		}
		frm.refresh_field("officers_deserves_exchange_report")
	
    },
	search: function(frm) {
		frappe.call({
			doc: frm.doc,
			method: "get_entity_data",
			freeze:1,
			callback: function(r) {
				frm.refresh_fields();
				frm.refresh();
				
			}
		});
	},
});


frappe.ui.form.on("Bon Printing", "print_bons", function(frm){
	var myWin = window.open('/printview?doctype=Bon%20Printing&name='+ frm.doc.name +'&trigger_print=1&format=Bons%20Print&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=ar');
});
frappe.ui.form.on("Bon Printing", "print_analysis_entity", function(frm){
	let fromDate = frm.doc.from_date == undefined ? "": frm.doc.from_date 
	let toDate = frm.doc.to_date == undefined ? "": frm.doc.to_date 
	var myWin = window.open('/app/query-report/Print%20Analysis%20for%20Entities?title=' + frm.doc.title +'&from_date='+ fromDate +'&to_date='+ toDate  +'&entities='+ frm.doc.entity +'&reason_for_entitlement='+ frm.doc.reason_for_entitlement +'&fiscal_year='+frm.doc.fiscal_year);
});

frappe.ui.form.on("Bon Printing", "officers_deserves_exchange_report", function(frm){
	var myWin = window.open('/app/query-report/Valid%20Officers%20and%20Civilians%20to%20Exchange?title=' + frm.doc.title +'&entities='+ frm.doc.entity +'&reason_for_entitlement='+ frm.doc.reason_for_entitlement +'&fiscal_year='+frm.doc.fiscal_year);
	frappe.db.set_value("Bon Printing", frm.doc.name, "printed", 1)
	frm.refresh()
});
frappe.ui.form.on("Bon Printing", "total_daily_print_count", function(frm){
	let fromDate = frm.doc.from_date == undefined ? "": frm.doc.from_date 
	let toDate = frm.doc.to_date == undefined ? "": frm.doc.to_date 
	var myWin = window.open('/app/query-report/Printed%20Bons%20for%20Period%20of%20Time?from_date=' + fromDate +'&to_date='+ toDate  +'&fiscal_year='+frm.doc.fiscal_year +'&entities='+ frm.doc.entity +'&reason_for_entitlement='+ frm.doc.reason_for_entitlement );
});
frappe.ui.form.on("Bon Printing", "daily_print_report", function(frm){
	let fromDate = frm.doc.from_date == undefined ? "": frm.doc.from_date 
	let toDate = frm.doc.to_date == undefined ? "": frm.doc.to_date 
	var myWin = window.open('/app/query-report/Printed%20Bons%20for%20Period%20of%20Time?from_date=' + fromDate +'&to_date='+ toDate  +'&fiscal_year='+frm.doc.fiscal_year +'&entities='+ frm.doc.entity +'&reason_for_entitlement='+ frm.doc.reason_for_entitlement );
});
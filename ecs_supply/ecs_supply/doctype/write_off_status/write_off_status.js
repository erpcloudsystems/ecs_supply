// Copyright (c) 2022, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Write_off Status', {
 onload(frm) {
        if (frappe.user.has_role("Policemen")){
            frm.set_df_property("national_security_for_employee","cannot_delete_rows", 0);
        }else {
            frm.set_df_property("national_security_for_employee","cannot_delete_rows", 1);
        }
	},
});

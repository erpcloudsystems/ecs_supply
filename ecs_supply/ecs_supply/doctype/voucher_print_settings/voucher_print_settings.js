// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Voucher Print Settings', {
    refresh:function(frm){
        frm.set_df_property("bon_settings", "cannot_delete_rows", true);
        frm.set_df_property("bon_settings", "cannot_add_rows", true);
		frm.set_df_property("footer_settings", "cannot_delete_rows", true);
        frm.set_df_property("footer_settings", "cannot_add_rows", true);
    }
});

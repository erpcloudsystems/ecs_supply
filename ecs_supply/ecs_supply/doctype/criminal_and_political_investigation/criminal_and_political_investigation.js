// Copyright (c) 2023, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on("Criminal And Political Investigation", {
	recruit(frm) {
        if (frm.doc.recruit) {
            frappe.call({
                method: 'history_investigation',
                doc:frm.doc,
                freeze: true,
                callback: (r) => {
                    console.log(r)
                    if(r.message){
                        r.message.forEach((row, idx, array)=>{
                            let investigation_history = frm.add_child("investigation_history");
                            investigation_history.recruit = row.recruit;
                            investigation_history.employment_type = row.employment_type;
                            investigation_history.send_investigation_number2 = row.send_investigation_number2;
                            investigation_history.political_investigation_date = row.political_investigation_date;
                            investigation_history.investigation_entry_number2 = row.investigation_entry_number2;
                            investigation_history.receipt_the_result_of_political_investigation_date = row.receipt_the_result_of_political_investigation_date;
                            investigation_history.political_investigation_result = row.political_investigation_result;
                            investigation_history.result_notes = row.result_notes;
                            investigation_history.send_investigation_number = row.send_investigation_number;
                            investigation_history.criminal_investigation_date = row.criminal_investigation_date;
                            investigation_history.investigation_entry_number = row.investigation_entry_number;
                            investigation_history.receipt_the_result_of_criminal_investigation_date = row.receipt_the_result_of_criminal_investigation_date;
                            investigation_history.custom_criminal_investigation_result3 = row.custom_criminal_investigation_result3;
                            investigation_history.result_of_the_investions = row.result_of_the_investions;
                            investigation_history.criminal_investigation_result = row.criminal_investigation_result;
                            investigation_history.result_of_the_investions_of_his_relatives = row.result_of_the_investions_of_his_relatives;
                            investigation_history.investigation_history = row.investigation_history;

                            cur_frm.refresh_field("investigation_history");
                        })
                    }
                },
            
            })
        }
       
	},
    onload(frm) {
        if (frappe.user.has_role("Policemen")){
            frm.set_df_property("national_security_for_employee","cannot_delete_rows", 0);
        }else {
            frm.set_df_property("national_security_for_employee","cannot_delete_rows", 1);
        }
	},
});

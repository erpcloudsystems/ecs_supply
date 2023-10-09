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


frappe.ui.form.on('Voucher Print Settings', {
	refresh: async function(frm) {
		if(!frm.doc.__islocal) {
            console.log(frm.fields_dict)
			$(frm.fields_dict.html_wcyq.wrapper).empty()

			var template = `<div style="position: relative;">\
                    <div id="cheque_preview" style="width: 210.00mm; \
                        height:297.00mm;\
                        background-repeat: no-repeat;\
                        background-image: url('{{ scan_image }}') ;\
                        background-size: cover;
                        position: relative;
                        color: darkblue;
                        font-weight: bold;
                        ">\
                        \
                        <span style="right: 0; margin: {{ bon_settings[0]['vertical'] + voucher1_space }}mm {{ bon_settings[0]['horizontal'] }}mm 0 0; 
                            position: absolute;">  {{ bon_settings[0]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[1]['vertical'] + voucher1_space }}mm {{ bon_settings[1]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[1]['example'].split("-")[2] }} &nbsp; {{ bon_settings[1]['example'].split("-")[1] }} &nbsp; {{ bon_settings[1]['example'].split("-")[0] }}</span>\
                        <span style="right: 0; margin: {{ bon_settings[2]['vertical'] + voucher1_space }}mm {{ bon_settings[2]['horizontal'] }}mm 0 0; 
                        position: absolute;">  
                        {% if print_name_with_rank %}
                        {{ bon_settings[2]['example'] }}/ {{ footer_settings[0]['example'] }}
                        {% else %}
                        {{ bon_settings[2]['example'] }}
                        {% endif %}
                         </span>
                        <span style="right: 0; margin: {{ bon_settings[3]['vertical'] + voucher1_space }}mm {{ bon_settings[3]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[3]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[4]['vertical'] + voucher1_space }}mm {{ bon_settings[4]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[4]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[5]['vertical'] + voucher1_space }}mm {{ bon_settings[5]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[5]['example'].split("-")[2] }} &nbsp; {{ bon_settings[5]['example'].split("-")[1] }} &nbsp; {{ bon_settings[5]['example'].split("-")[0] }}</span>\


                        <span style="right: 0; margin: {{ bon_settings[0]['vertical'] + voucher2_space }}mm {{ bon_settings[0]['horizontal'] }}mm 0 0; 
                            position: absolute;">  {{ bon_settings[0]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[1]['vertical'] + voucher2_space }}mm {{ bon_settings[1]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[1]['example'].split("-")[2] }} &nbsp; {{ bon_settings[1]['example'].split("-")[1] }} &nbsp; {{ bon_settings[1]['example'].split("-")[0] }}</span>\
                        <span style="right: 0; margin: {{ bon_settings[2]['vertical'] + voucher2_space }}mm {{ bon_settings[2]['horizontal'] }}mm 0 0; 
                        position: absolute;">
                        {% if print_name_with_rank %}
                        {{ bon_settings[2]['example'] }}/ {{ footer_settings[0]['example'] }}
                        {% else %}
                        {{ bon_settings[2]['example'] }}
                        {% endif %}
                        </span>\
                        <span style="right: 0; margin: {{ bon_settings[3]['vertical'] + voucher2_space }}mm {{ bon_settings[3]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[3]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[4]['vertical'] + voucher2_space }}mm {{ bon_settings[4]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[4]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[5]['vertical'] + voucher2_space }}mm {{ bon_settings[5]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[5]['example'].split("-")[2] }} &nbsp; {{ bon_settings[5]['example'].split("-")[1] }} &nbsp; {{ bon_settings[5]['example'].split("-")[0] }}</span>\


                        <span style="right: 0; margin: {{ bon_settings[0]['vertical'] + voucher3_space }}mm {{ bon_settings[0]['horizontal'] }}mm 0 0; 
                            position: absolute;">  {{ bon_settings[0]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[1]['vertical'] + voucher3_space }}mm {{ bon_settings[1]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[1]['example'].split("-")[2] }} &nbsp; {{ bon_settings[1]['example'].split("-")[1] }} &nbsp; {{ bon_settings[1]['example'].split("-")[0] }}</span>\
                        <span style="right: 0; margin: {{ bon_settings[2]['vertical'] + voucher3_space }}mm {{ bon_settings[2]['horizontal'] }}mm 0 0; 
                        position: absolute;">
                        {% if print_name_with_rank %}
                        {{ bon_settings[2]['example'] }}/ {{ footer_settings[0]['example'] }}
                        {% else %}
                        {{ bon_settings[2]['example'] }}
                        {% endif %}
                        </span>\
                        <span style="right: 0; margin: {{ bon_settings[3]['vertical'] + voucher3_space }}mm {{ bon_settings[3]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[3]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[4]['vertical'] + voucher3_space }}mm {{ bon_settings[4]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[4]['example'] }} </span>\
                        <span style="right: 0; margin: {{ bon_settings[5]['vertical'] + voucher3_space }}mm {{ bon_settings[5]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ bon_settings[5]['example'].split("-")[2] }} &nbsp; {{ bon_settings[5]['example'].split("-")[1] }} &nbsp; {{ bon_settings[5]['example'].split("-")[0] }}</span>\


                        <span style="right: 0; margin: {{ footer_settings[0]['vertical'] + voucher_footer_space }}mm {{ footer_settings[0]['horizontal'] }}mm 0 0; 
                            position: absolute;">  {{ footer_settings[0]['example'] }} </span>\
                        <span style="right: 0; margin: {{ footer_settings[1]['vertical'] + voucher_footer_space }}mm {{ footer_settings[1]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ footer_settings[1]['example'] }} </span>\
                        <span style="right: 0; margin: {{ footer_settings[2]['vertical'] + voucher_footer_space }}mm {{ footer_settings[2]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ footer_settings[2]['example'] }} </span>\
                        <span style="right: 0; margin: {{ footer_settings[3]['vertical'] + voucher_footer_space }}mm {{ footer_settings[3]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ footer_settings[3]['example'] }} </span>\
                        <span style="right: 0; margin: {{ footer_settings[4]['vertical'] + voucher_footer_space }}mm {{ footer_settings[4]['horizontal'] }}mm 0 0; 
                        position: absolute;">  {{ footer_settings[4]['example'].split("-")[2] }} &nbsp; {{ footer_settings[4]['example'].split("-")[1] }} &nbsp; {{ footer_settings[4]['example'].split("-")[0] }}</span>\
    
                    </div>\
			</div>
            `;

			await $(frappe.render(template, frm.doc)).appendTo(frm.fields_dict.html_wcyq.wrapper)
            if (frm.doc.scan_image) {
                $(frm.fields_dict.html_wcyq.wrapper).find("#cheque_preview").css('background-image','url(' + frm.doc.scan_image + ')');
            }
		}
	}
});


frappe.ui.form.on('Voucher Print Settings', {
	scan_image: function(frm) {
        console.log(frm.doc.scan_image)
        if (frm.doc.scan_image) {
            console.log(frm.doc.scan_image)
            $(frm.fields_dict.html_wcyq.wrapper).find("#cheque_preview").css('background-image','url(' + frm.doc.scan_image + ')');
            frm.refresh()
        }
		
	}
});


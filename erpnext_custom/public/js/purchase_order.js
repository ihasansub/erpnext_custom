frappe.ui.form.on("Purchase Order", {
	setup: function(frm) {

		alert("test");
		frm.set_query("supplier_2", function() {
			return {
				filters: {
					'supplier_type': 'Company',

				}
			}
		});
	},
});

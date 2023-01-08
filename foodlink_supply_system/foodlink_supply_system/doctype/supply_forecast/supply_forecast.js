frappe.ui.form.on('Supply Forecast', {
	refresh: function(frm) {

		let first_day_of_the_week = moment().startOf('isoWeek').add(1, 'week');

		frm.set_value('supply_stating_date', first_day_of_the_week.format('YYYY-MM-DD'));
		frm.set_value('supply_ending_date', frappe.datetime.add_days(first_day_of_the_week, 5));
		console.log(first_day_of_the_week);
	}
});

import frappe

@frappe.whitelist()
def get_supply_balance():
    return frappe.db.sql (""" 
    select f.produce_name,
coalesce(f.monday_supply,0) as monday_supply,coalesce(o.monday_order,0)as monday_order,coalesce(sum( f.monday_supply - o.monday_order),0 )as mon_avl_qty,
coalesce(f.tuesday_supply,0) as tuesday_supply,coalesce(o.tuesday_order,0)as tuesday_order,coalesce(sum( f.tuesday_supply - o.tuesday_order),0 )as tue_avl_qty,
coalesce(f.wednesday_supply,0) as wednesday_supply,coalesce(o.wednesday_order,0)as wednesday_order,coalesce(sum( f.wednesday_supply - o.wednesday_order),0 )as wed_avl_qty,
coalesce(f.thursday_supply,0) as thursday_supply,coalesce(o.thursday_order,0)as thursday_order,coalesce(sum( f.thursday_supply - o.thursday_order),0 )as thu_avl_qty,
coalesce(f.friday_supply,0) as friday_supply,coalesce(o.friday_order,0)as friday_order,coalesce(sum( f.friday_supply - o.friday_order),0 )as fri_avl_qty,
coalesce(f.saturday_supply,0) as saturday_supply,coalesce(o.saturday_order,0)as saturday_order,coalesce(sum( f.saturday_supply - o.saturday_order),0 )as sat_avl_qty,
sum(f.monday_supply + f.tuesday_supply + f.wednesday_supply + f.thursday_supply + f.friday_supply + f.saturday_supply) as total_supply
FROM `tabForecast Items Table` as f
LEFT JOIN `tabOrder Items Table` as o
ON f.produce_name = o.produce_name group by f.produce_name,o.produce_name;
   
    
    """)

import frappe

@frappe.whitelist(allow_guest=True)
def get_supply():
    supply = frappe.db.sql("""  
        select produce_name,
        sum(monday_supply) as monday_sup,
        sum(tuesday_supply) as tuesday_sup,
        sum(wednesday_supply) as wednesday_sup,
        sum(thursday_supply) as thursday_sup,
        sum(friday_supply) as friday_sup,
        sum(saturday_supply) as saturday_sup  
        from `tabForecast Items Table` group by produce_name;
     """,as_dict = True)
    
    demand = frappe.db.sql(""" 
        select produce_name,
        sum(monday_order) as monday_ord,
        sum(tuesday_order) as tuesday_ord,
        sum(wednesday_order) as wednesday_ord,
        sum(thursday_order) as thursday_ord,
        sum(friday_order ) as friday_ord,
        sum(saturday_order) as saturday_ord
        from  `tabOrder Items Table` group by produce_name;
    """,as_dict = True)
    new_list=[]

    for d in supply:
        new_list.append({'produce_name':d['produce_name'],'monday_balance':d['monday_sup'],'tuesday_balance':d['tuesday_sup'],'wednesday_balance':d['wednesday_sup'],'thursday_balance':d['thursday_sup'],'friday_balance':d['friday_sup'],'saturday_balance':d['saturday_sup']})

    update_list = []
    for s in new_list:
        found = False
        for i in demand:
            if s['produce_name'] == i['produce_name']:
                update_list.append({
                    'produce_name':s['produce_name'],
                    'monday_balance':s['monday_balance']-i['monday_ord'],
                    'tuesday_balance':s['tuesday_balance']-i['tuesday_ord'],
                    'wednesday_balance':s['wednesday_balance']-i['wednesday_ord'],
                    'thursday_balance':s['thursday_balance']-i['thursday_ord'],
                    'friday_balance':s['friday_balance']-i['friday_ord'],
                    'saturday_balance':s['saturday_balance']-i['saturday_ord'],
                    
                })
                found = True
                break  # added this line
        if not found:
            update_list.append(s)
    return update_list



@frappe.whitelist(allow_guest=True)
def get_supply_balance():
    return frappe.db.sql (""" 
select f.produce_name,
coalesce(f.monday_supply,0.0) as monday_supply,coalesce(o.monday_order,0.0)as monday_order,coalesce(sum( (f.monday_supply - coalesce(o.monday_order,0.0) )),0.0 )as mon_avl_qty,
coalesce(f.tuesday_supply,0) as tuesday_supply,coalesce(o.tuesday_order,0)as tuesday_order,coalesce(sum( f.tuesday_supply - coalesce(o.tuesday_order,0)),0 )as tue_avl_qty,
coalesce(f.wednesday_supply,0) as wednesday_supply,coalesce(o.wednesday_order,0)as wednesday_order,coalesce(sum( f.wednesday_supply - coalesce(o.wednesday_order,0)),0 )as wed_avl_qty,
coalesce(f.thursday_supply,0) as thursday_supply,coalesce(o.thursday_order,0)as thursday_order,coalesce(sum( f.thursday_supply - coalesce( o.thursday_order,0)),0 )as thu_avl_qty,
coalesce(f.friday_supply,0) as friday_supply,coalesce(o.friday_order,0)as friday_order,coalesce(sum( f.friday_supply - coalesce(o.friday_order,0)),0 )as fri_avl_qty,
coalesce(f.saturday_supply,0) as saturday_supply,coalesce(o.saturday_order,0)as saturday_order,coalesce(sum( f.saturday_supply - coalesce(o.saturday_order,0)),0 )as sat_avl_qty,
sum(f.monday_supply + f.tuesday_supply + f.wednesday_supply + f.thursday_supply + f.friday_supply + f.saturday_supply) as total_supply
FROM `tabForecast Items Table` as f
LEFT JOIN `tabOrder Items Table` as o
ON f.produce_name = o.produce_name group by f.produce_name,o.produce_name;
    
    """,as_dict = True)

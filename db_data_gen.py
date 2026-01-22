import names
import random as rnd

def invoice_gen(gen_range: int):
    

    for i in range(gen_range): 
        cName = names.get_full_name(gender = any)

        total_amount = rnd.randint(1, 1000)

        year =  "2026"
        month = "01"
        day = rnd.randint(1, 20)

        if (day < 10):
            day = "0" + str(day)
        else:
            day = str(day)

        date = year + "-" + month + "-" + day
        print(f"INSERT INTO admin_invoices (customer_name, total_amount, created_at) VALUES ('{cName}', {total_amount}, '{date}');")



def invoice_detail_gen(gen_range: int):
    for i in range(gen_range):
        print(f"INSERT INTO admin_invoice_details (invoice_id, product_id, quantity, unit_price) VALUES ({rnd.randint(10, 100)}, {rnd.randint(2, 6)}, {rnd.randint(1, 100)}, {rnd.randint(1, 100)});")


invoice_gen(10)
invoice_detail_gen(10)
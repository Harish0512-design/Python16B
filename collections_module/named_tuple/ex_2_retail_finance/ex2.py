from collections import namedtuple

Sale = namedtuple('Sale', ['invoice_id', 'date', 'store', 'amount'])

sales = [
    Sale(1001, "2025-10-19", "StoreA", 5000),
    Sale(1002, "2025-10-20", "StoreB", 7000),
    Sale(1003, "2025-10-19", "StoreA", 5000),
    Sale(1004, "2025-10-20", "StoreB", 6000),
    Sale(1005, "2025-10-19", "StoreA", 4000),
    Sale(1006, "2025-10-20", "StoreB", 1000),
    Sale(1007, "2025-10-19", "StoreA", 2000),
    Sale(1008, "2025-10-20", "StoreB", 4000),
    Sale(1009, "2025-10-19", "StoreA", 9000),
    Sale(1010, "2025-10-20", "StoreB", 1000),
    Sale(1011, "2025-10-19", "StoreA", 1000),
    Sale(1012, "2025-10-20", "StoreB", 2000),
]

# Calculate total sales
total = sum(s.amount for s in sales)
print("Total Sales:", total)

# Calculate total sales by store
distinct_stores = []
for sale in sales:
    if sale.store not in distinct_stores:
        distinct_stores.append(sale.store)

total_sales_by_store = {}
for store in distinct_stores:
    total_sales_by_store[store] = sum(s.amount for s in sales if s.store==store)
        
print(total_sales_by_store)

# Which store has highest sales?
highest_sales_store = dict(sorted(total_sales_by_store.items(), key=lambda item: item[1]))
print(f"Highest Sales Store: {list(highest_sales_store.items())[-1]}")
from tabulate import tabulate

dicz={"ITEM0001":{"BREED":"PERSIAN","AGE":"7","PRICE":"15000"},"ITEM0002":{"BREED":"AEGEAN","AGE":"3","PRICE":"20000"}}
category=["SrNum","BREED","AGE","PRICE"]
for key,val in dicz.items():
    print(tabulate([val], headers=[key], tablefmt='orgtbl'))
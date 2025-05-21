from report import Report
from person import Builder
from person import Supplier
from person import Client
from material import RawMaterials
from material import FinishingMaterials
import mysql.connector as my_conn

my_db = my_conn.connect(host="localhost", port=3306, user="root", password="sadainahmad12345", database="materials_management")

print("connection established....")
cur = my_db.cursor()

rep = Report()

print("""
        ********************************************************
        ********************************************************
        *****                                              *****
        *****           MADE BY : SADAIN AHMAD             *****
        *****                                              *****
        ********************************************************
        ********************************************************

""")

while True:
    choice = int(input("1: Press 1 to add/remove/update/display suppliers\n2: Press 2 to add/remove/update/display builders\n3: Press 3 to add/remove/update/display orders\n4: Press 4 to add/remove/update/display client\n5: Press any key to exit: "))

    if choice == 1: # add supplier
        select = int(input("1: Press 1 to add supplier\n2: Press 2 to remove Supplier\n3: Press 3 to update Supplier\n4: Press 4 to display all Suppliers: "))
        if select == 1:
            cid = input("Enter supplier ID: ")
            name = input("Enter the name of supplier: ")
            address = input(f"Enter the address of {name}: ")
            contact_no = input(f"Enter the contact number of {name}: ")
            email = input(f"Enter the email of {name}: ")
            factory_address = input(f"Enter the factory address of {name}: ")
            rep.add_supplier(my_db, Supplier(cid, name, address, contact_no, email, factory_address))

        elif select == 2: # remove supplier
            cid = input("Enter supplier ID to remove: ")
            rep.remove_supplier(my_db, cid)

        elif select == 3:  # update supplier
            old_cid = input("Enter supplier old ID: ")
            print("\tInsert Updated Data")
            cid = input("Enter supplier ID: ")
            name = input("Enter the name of supplier: ")
            address = input(f"Enter the address of {name}: ")
            contact_no = input(f"Enter the contact number of {name}: ")
            email = input(f"Enter the email of {name}: ")
            factory_address = input(f"Enter the factory address of {name}: ")
            rep.update_supplier(my_db, old_cid, Supplier(cid, name, address, contact_no, email, factory_address))

        elif select == 4: # display all suppliers
            rep.display_suppliers(cur)

    # builders
    elif choice == 2:
        select = int(input("1: Press 1 to add Builder\n2: press 2 to remove Builder\n3: Press 3 to update Builder\n4: Press 4 to display all Builders: "))
        
        if select == 1: # add builder
            cid = input("Enter builder ID: ")
            name = input("Enter the name of builder: ")
            address = input(f"Enter the address of {name}: ")
            contact_no = input(f"Enter the contact number of {name}: ")
            email = input(f"Enter the email of {name}: ")
            construction_site = input("Enter construction site: ")
            rep.add_builder(my_db, Builder(cid, name, address, contact_no, email, construction_site))

        elif select == 2: # remove Builder
            cid = input("Enter Builder ID to remove: ")
            rep.remove_builder(my_db, cid)
        
        elif select == 3: # update builder
            old_cid = input("Enter builder old ID: ")
            print("\tInsert Updated Data")
            cid = input("Enter builder ID: ")
            name = input("Enter the name of builder: ")
            address = input(f"Enter the address of {name}: ")
            contact_no = input(f"Enter the contact number of {name}: ")
            email = input(f"Enter the email of {name}: ")
            construction_site = input("Enter construction site: ")
            rep.update_builder(my_db, old_cid, Builder(cid, name, address, contact_no, email, construction_site))

        elif select == 4: # Display all builder info
            rep.display_builders(cur)

    # Orders/client
    elif choice == 3:
        select = int(input("1: Press 1 to add an order\n2: press 2 to remove an order\n3: Press 3 to update an order\n4: Press 4 to display the whole report of the orders: "))
        
        if select == 1:
            # add order
            cid = input("Enter client ID: ")
            name = input("Enter material name that you wanna order: ")
            quantity = float(input(f"Enter Quantity of {name}: "))
            unit_price = float(input(f"Enter unit Price of {name}: "))
            category = int(input("1: Press 1 to update Raw Material\n2: Press 2 to update Finishing Mateial: "))
            
            if category==1:
                rep.add_material(my_db, RawMaterials(cid, name, quantity, unit_price))
            elif category == 2:
                rep.add_material(my_db, FinishingMaterials(cid, name, quantity, unit_price))
            else:
                print("Invalid Input......")

        elif select == 2:
            # remove order
            cid = input("Enter client ID: ")
            name = input("Enter material name that you wanna remove: ")
            rep.remove_material(my_db, cid, name)
        
        elif select == 3:
            # update order
            cid = input("Enter client ID: ")
            name = input("Enter material name that you wanna update: ")
            quantity = float(input(f"Enter Quantity of {name}: "))
            unit_price = float(input(f"Enter unit Price of {name}: "))
            if category == 1:
                rep.update_material(my_db, cid, name, RawMaterials(cid, name, quantity, unit_price))
            elif category == 2:
                rep.update_material(my_db, cid, name, FinishingMaterials(cid, name, quantity, unit_price))
            else:
                print("Invalid Input....")

        elif select == 4:
            # display orders
            cid = input("Enter client ID: ")
            rep.display_report(cur, cid)

    # cruds on client
    elif choice == 4: 
        select = int(input("1: Press 1 to add client\n2: press 2 to remove client\n3: Press 3 to update client\n4: Press 4 to display all client: "))

        if select == 1: # add client
            cid = input("Enter client ID: ")
            name = input("Enter the name of client: ")
            address = input(f"Enter the address of {name}: ")
            contact_no = input(f"Enter the contact number of {name}: ")
            email = input(f"Enter the email of {name}: ")

            rep.display_suppliers(cur)
            supplier_id = input("Select Supplier id to order materials(enter 0 when supplier not available): ")
            rep.display_builders(cur)
            builder_id = input("Select builder id to hire him(enter 0 when builder not available): ")

            rep.add_client(my_db,Client(cid, name, address, contact_no, supplier_id, builder_id, email))        

        elif select == 2: # remove client
            cid = input("Enter Client id that you wanna remove: ")
            rep.remove_client(my_db, cid)

        elif select == 3: # update client
            old_cid = input("Enter Client old ID: ")
            print("\tInsert updated Info")
            cid = input("Enter client ID: ")
            name = input("Enter the name of client: ")
            address = input(f"Enter the address of {name}: ")
            contact_no = input(f"Enter the contact number of {name}: ")
            email = input(f"Enter the email of {name}: ")

            print("\tSuppliers")
            rep.display_suppliers(cur)
            supplier_id = input("Select Supplier id to order materials(enter 0 when supplier not available): ")
            rep.display_builders(cur)
            builder_id = input("Select builder id to hire him(enter 0 when builder not available): ")
            rep.update_client(my_db, old_cid, Client(cid, name, address, contact_no, supplier_id, builder_id, email))
        elif select == 4: # display all clients
            rep.display_clients(cur)
    
    else: # exit
        break
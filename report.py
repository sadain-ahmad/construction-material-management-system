class Report:

    # Add a new material to the list
    def add_material(self, my_db, material):
        cur = my_db.cursor()
        try:
            insertion = "INSERT INTO orders(cid, name, quantity, unit_price, total_price, category) VALUES(%s, %s, %s, %s, %s, %s)"
            
            data = (material.get_cid(), material.get_name(), material.get_quantity(), material.get_unit_price(), material.total_cost(), material.get_category())

            cur.execute(insertion, data)
            my_db.commit()
            print("order added")

        except Exception as e:
            print(e)
    
    # remove an existing material
    def remove_material(self, my_db, cid, name):
        cur = my_db.cursor()
        cur.execute("SELECT * FROM orders WHERE cid=%s", (cid,))
        if cur.fetchall():
            try:
                deletion = "DELETE FROM orders WHERE cid=%s AND name=%s"
                data = (cid, name)
                cur.execute(deletion, data)
                my_db.commit()
                print("order deleted")
            except Exception as e:
                print(e)
        else:
            print(f"No order found for {cid} id")

###########################################################################3
        # for i,item in enumerate(self.__material_list):
        #     if item.get_name().lower() == name.lower():
        #         del self.__material_list[i]
        # else:
        #     print("Sorry! Material not found")

    # Update an existing material
    def update_material(self, my_db, cid, name, material):
        cur = my_db.cursor()
        cur.execute("SELECT * FROM orders WHERE cid=%s", (material.get_cid(),))
        if cur.fetchall():
            try:
                updation = "UPDATE orders SET quantity=%s, unit_price=%s, total_price=%s WHERE cid=%s AND name=%s"
                data = (material.get_quantity(), material.get_unit_price(), material.total_cost(), cid, name)
                cur.execute(updation, data)
                my_db.commit()
                print("order updated")
            except Exception as e:
                print(e)
        else:
            print(f"No order found for {cid} id")

##########################################################################
        # for i,item in enumerate(self.__material_list):
        #     if item.get_name().lower() == material.get_name().lower():
        #         self.__material_list[i] = material
        # else:
        #     print("Sorry! Material Not Found\nIf you wanna add material (try add method)")
        
        
    # Display the while report of materials
    def display_report(self, cur, cid):

        cur.execute("SELECT * FROM orders WHERE cid=%s", (cid,))
        if cur.fetchall():
            try:
                print("\n\tReport:")
                print("\n\tClient Details:")
                cur.execute("SELECT cid,name,contact_no FROM client WHERE cid=%s", (cid,))
                info = cur.fetchone()
                print("\nClient ID: ",info[0], end="")
                print("\tClient Name: ",info[1], end="")
                print("\tContact Number: ",info[2])
                
                retrieval = "SELECT name,quantity,unit_price,total_price,category FROM orders WHERE cid=%s"
                data = (cid,)
                cur.execute(retrieval, data)
                print("\n\tMaterials:")
                for i,item in enumerate(cur.fetchall()):
                    print(f"{i+1}", end="")
                    print("\tName | Quantity | UnitPrice | TotalPrice | Category")
                    print("\t",item)
                
                cur.execute("SELECT SUM(total_price) FROM orders")
                print(f"\nTotal Expense: {cur.fetchall()[0][0]}")
            except Exception as e:
                print(e)
        else:
            print("order not found")


##########################################################################################
        # print("Customer",customer)
        # self.__total_expenses = 0
        # for i,item in self.__material_list:
        #     print(f"Material No. {i+1}")
        #     print(item)
        #     self.__total_expenses += item.total_cost() # calculate total cost of the materials
        
        # print(f"Total Expenses: {self.__total_expenses}")
    
    
    # store supplier info
    def add_supplier(self, my_db, sup):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM supplier")
        for i in cur.fetchall():
            if sup.get_cid() == i[0]:
                raise ValueError("This id have been registered!")
        else:
            try:
                insertion = "INSERT INTO supplier(cid,name,address,contact_no,email,factory_address) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (sup.get_cid(), sup.get_name(), sup.get_address(), sup.get_contact_number(), sup.get_email(), sup.get_factory_address())

                cur.execute(insertion, data)
                my_db.commit()
                print("Info saved successfully....")

            except Exception as e:
                print(e)
        
    # remove supplier
    def remove_supplier(self, my_db, cid):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM supplier")
        if cur.fetchall():
            try:
                deletion = "DELETE FROM supplier WHERE cid=%s"
                data = (cid,)
                cur.execute(deletion, data)
                my_db.commit()
                print("Supplier Removed")
            except Exception as e:
                print(e)
        else:
            print("Supplier not found")

    # update supplier
    def update_supplier(self, my_db, old_cid, sup):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM supplier")
        if cur.fetchall():
            try:
                updation = "UPDATE supplier SET cid=%s, name=%s, address=%s, contact_no=%s, email=%s, factory_address=%s WHERE cid=%s"
                data = (sup.get_cid(), sup.get_name(), sup.get_address(), sup.get_contact_number(), sup.get_email(), sup.get_factory_address(), old_cid)
                cur.execute(updation, data)
                my_db.commit()
                print("Supplier Info Updated...")
            except Exception as e:
                print(e)

    # display all supplier
    def display_suppliers(self, cur):
        try:
            retrieval = "SELECT * FROM supplier"
            cur.execute(retrieval)
            print("\n\tSuppliers")
            for i,sup in enumerate(cur.fetchall()):
                print(f"\n{i+1}", end="")
                print("\tCid | Name | Address | Contact number | Email | Factory Address")
                print("\t",sup)
            
        except Exception as e:
            print(e)

    # add builder
    def add_builder(self, my_db, builder):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM builder")
        for i in cur.fetchall():
            if builder.get_cid() == i[0]:
                raise ValueError("This id have been registered!")
        else:
            try:
                insertion = "INSERT INTO builder(cid,name,address,contact_no,email,construction_site) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (builder.get_cid(), builder.get_name(), builder.get_address(), builder.get_contact_number(), builder.get_email(), builder.get_construction_site())

                cur.execute(insertion, data)
                my_db.commit()
                print("Info saved successfully....")

            except Exception as e:
                print(e)

    # remove builder
    def remove_builder(self, my_db, cid):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM builder")
        if cur.fetchall():
            try:
                deletion = "DELETE FROM builder WHERE cid=%s"
                data = (cid,)
                cur.execute(deletion, data)
                my_db.commit()
                print("Builder Removed")
            except Exception as e:
                print(e)
        else:
            print("Builder not found")

    # update Builder
    def update_builder(self, my_db, old_cid, builder):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM builder")
        if cur.fetchall():
            try:
                updation = "UPDATE builder SET cid=%s, name=%s, address=%s, contact_no=%s, email=%s, construction_site=%s WHERE cid=%s"
                data = (builder.get_cid(), builder.get_name(), builder.get_address(), builder.get_contact_number(), builder.get_email(), builder.get_construction_site(), old_cid)
                cur.execute(updation, data)
                my_db.commit()
                print("Builder Info Updated...")
            except Exception as e:
                print(e)

    # display all Builders
    def display_builders(self, cur):
        try:
            retrieval = "SELECT * FROM builder"
            cur.execute(retrieval)
            print("\n\tBuilders")
            for i,builder in enumerate(cur.fetchall()):
                print(f"\n{i+1}", end="")
                print("\tCid | Name | Address | Contact number | Email | Construction site")
                print("\t",builder)
            
        except Exception as e:
            print(e)

    # add client
    def add_client(self, my_db, client):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM client")
        for i in cur.fetchall():
            if client.get_cid() == i[0]:
                raise ValueError("This id have been registered!")
        else:
            try:
                insertion = "INSERT INTO client(cid,name,address,contact_no,email,supplier_id,builder_id) VALUES (%s, %s, %s, %s, %s, %s,%s)"
                data = (client.get_cid(), client.get_name(), client.get_address(), client.get_contact_number(), client.get_email(), client.get_supplier_id(), client.get_builder_id())

                cur.execute(insertion, data)
                my_db.commit()
                print("Info saved successfully....")

            except Exception as e:
                print(e)

    # remove client 
    def remove_client(self, my_db, cid):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM client")
        if cur.fetchall():
            try:
                deletion = "DELETE FROM client WHERE cid=%s"
                data = (cid,)
                cur.execute(deletion, data)
                my_db.commit()
                print("Client Removed")
            except Exception as e:
                print(e)
        else:
            print("Client not found")

    # update client
    def update_client(self, my_db, old_cid, client):
        cur = my_db.cursor()
        cur.execute("SELECT cid FROM client")
        if cur.fetchall():
            try:
                updation = "UPDATE client SET cid=%s, name=%s, address=%s, contact_no=%s, email=%s, supplier_id=%s, builder_id=%s WHERE cid=%s"
                data = (client.get_cid(), client.get_name(), client.get_address(), client.get_contact_number(), client.get_email(), client.get_supplier_id(), client.get_builder_id(), old_cid)
                cur.execute(updation, data)
                my_db.commit()
                print("client Info Updated...")
            except Exception as e:
                print(e)
                
    # display client
    def display_clients(self, cur):
        try:
            retrieval = "SELECT * FROM client"
            cur.execute(retrieval)
            print("\n\tClients")
            for i,client in enumerate(cur.fetchall()):
                print(f"\n{i+1}", end="")
                print("\tCid | Name | Address | Contact number | Email | Supplier ID | Builder ID")
                print("\t",client)
            
        except Exception as e:
            print(e)
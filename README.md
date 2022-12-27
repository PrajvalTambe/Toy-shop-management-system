# Toy-shop-management-system

1  Use MySQL Database

2  Create mydb Database 

3  Create following table in Database

Table: bill

Columns:

      customer_id     int(11) PK 
      
      customer_name   varchar(45) 
  
      mobile_no       varchar(45) 
      
      product_name    varchar(45) 
      
      date            varchar(45) 
      
      price           int(11) 
      
      quantity        int(11) 
   
      total           int(11)
   
   
Table: add_supplier

Columns:

        supplier_id     int(11) PK 
        
        supplier_name   varchar(45) 
        
        mobile_no       varchar(45) 
        
        adhar_no        varchar(45) 
        
        address         varchar(45)
       
Table: add_stock

Columns:

        product_id      int(11) PK 
        
        product_name    varchar(45) 
        
        current_stock   int(10) 
        
        new_stock       int(10)       
        
        
Table: add_product

Columns:

      product_id        int(11) PK 
      
      product_name      varchar(45) 
      
      supplier_name     varchar(45) 
      
      stock_add_date    varchar(45) 
      
      p_price           int(5) 
      
      s_price           int(5) 
      
      added_stock       int(10)        
        
        
   
Open Login.py file and run

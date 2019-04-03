import sys
import os


#python ./src/purchase_analytics.py ./input/order_products.csv ./input/products.csv ./output/report.csv

orders_file = sys.argv[1]
products_file = sys.argv[2]
outputfile = sys.argv[3]

product_department_dict = {}

def makePDRelation():
    print(products_file)
    with open(products_file) as infile:
        lineIndex = 0
        for line in infile:
            
             # skip the first title line 
            if lineIndex != 0:
                info = line.split(",")
                #print("line = ", line)
                product_department_dict[info[0].strip()] = int(info[len(info) - 1].strip())
                    
            lineIndex = 1

print("start making relations of orders and products")

makePDRelation()            

print("done with making relations of orders and products, size=", len(product_department_dict))

# In[55]:


# define a dict with type list as elements
result = {}
department = "UNKNOWN"

print("start parsing orders orders_file: ", orders_file)

with open(orders_file) as infile:
    #print(orders_file)
    lineIndex = 0
    for line in infile:
        #print(line)
        if lineIndex != 0: # skip the first title line 
            info = line.split(",")
            product_id = info[1].strip()
            reordered = info[3].strip()
            
            if product_id in product_department_dict:
                department = product_department_dict[product_id]
            
            detail = [department, 1, 0] # [order_num, first_order_num]
            
            # first order indicator
            if reordered == "0":
                detail = [department, 1, 1]
                
            if department in result:
                detail = [department, result[department][1] + detail[1], result[department][2] + detail[2]]
            
            result[department] = detail

            if lineIndex%1000 == 0:
                print("cursor in line " + str(lineIndex))
    
    
        lineIndex = lineIndex + 1

    print("total lines of " + str(lineIndex))


values = result.values()
sortedValues = sorted(values)

with open(outputfile, 'w') as outfile:
    outfile.write("department_id,number_of_orders,number_of_first_orders,percentage\r\n")
    for v in sortedValues:
        line = str(v[0]) + "," + str(v[1]) + "," + str(v[2]) + "," + str("%0.2f" % (v[2]/v[1]) + "\r\n")
        #print(line)
                                                                         
        outfile.write(line)
        

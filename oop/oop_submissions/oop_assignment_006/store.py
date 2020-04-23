from operators import gt,lt,ge,le
class Item:
    def __init__(self,price,name,category):
        self.name=name
        self.price=price
        self.category=category
        if self.price<=0:
            raise ValueError("Invalid value for price, got {}".format(self.price))
    def __str__(self):
        return self.name+"@"+str(self.price)+"-"+self.category

class Query:
    def __init__(self,field,operation,value):
        k=["EQ","IN","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
        self.field=field
        self.operation=operation
        self.value=value
        if self.operation not in k:
            raise ValueError("Invalid value for operation, got {}".format(self.operation))
    def __str__(self):
        return self.field+" "+self.operation+" "+str(self.value)    

class Store:
    def __init__(self):
        self.items=[]
    
    def count(self):
        return len(self.items)
    
    def __str__(self):
        if len(self.items)>0:
            return "\n".join(map(str,self.items))
        else:
            return "No items"
    
    def add_item(self,item_obj):
        self.items.append(item_obj)
    
    def filter(self,*args):
        compare_operations={"GTE":ge,"LTE":le,"LT":lt,"GT":gt}
        results=Store()
        for query_obj in args:
            if query_obj.operation == "IN" or query_obj.operation == "EQ":
                if not isinstance(query_obj.value,list):
                    query_obj.value=[query_obj.value]
                [results.add_item(item) for value in query_obj.value for item in self.items if value in item.__dict__.values()]
        
            elif (query_obj.operation == "GT" or query_obj.operation == "GTE" or query_obj.operation == "LT" or query_obj.operation == "LTE"):     
                [results.add_item(item) for item in self.items if compare_operations[query_obj.operation](item.price,query_obj.value)]
        
     
        
            elif query_obj.operation == "STARTS_WITH" or query_obj.operation == "ENDS_WITH" or query_obj.operation == "CONTAINS":     
                for item in self.items:
                    if (query_obj.field in item.__dict__.keys() and query_obj.value in str(item.__dict__[query_obj.field])):
                            results.add_item(item)   
                        
            return results                

    def exclude(self,*args):
        excluded_items=Store()
        for query_obj in args:
            included_items=self.filter(query_obj)
            [excluded_items.add_item(i) for i in self.items if i not in included_items.items and i not in excluded_items.items]        
            return excluded_items     
        
    def __add__(self,exclude):
        items_added=Store()
        for i in self.items:
            items_added.add_item(i)
        for i in exclude.items:
            items_added.add_item(i)
        return items_added    




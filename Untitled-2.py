user_list = ['俞家安','史子龙','李涛']
date_list = 1
date_head = "1月"
while date_list < 30:
    for i in user_list:
        
        print(date_head,date_list,"日","\t",end="")
        print(i)
        date_list = date_list + 1
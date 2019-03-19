def Sort_two(List_a,List_b):##此函数表示将List_b按照List_a顺序排序
    if List_a !=[] and List_b != []:
        Index_number = []
        Listb_sort = []
        # 定义一个中间索引列表以及初始化结果的列表
        A_sort = sorted(List_a,reverse = True)
        ##将A排序
        for index_a in range(len(A_sort)):
            Index_number.append(List_a.index(A_sort[index_a]))
        ##将A排序后的列表对应原列表的索引找出来
        for index_b in Index_number:
            Listb_sort.append(List_b[index_b])
        #按照索引值从需要排序的列表中取出元素，行成一个与a排序后对应的列表
        return A_sort,Listb_sort
    ### 实现两个列表元素对的同步排序
    else: 
        return List_a,List_b
    
#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:Airubby 
@file: pagination.py 
@time: 2018/05/05 
"""
from django.utils.safestring import mark_safe
class Page:
    def __init__(self,current_page,data_count,per_page_count=10,pager_num=7):
        self.current_page=current_page
        self.data_count=data_count
        self.per_page_count=per_page_count
        self.pager_num=pager_num
    @property
    def start(self):
        return (self.current_page-1)*self.per_page_count

    @property
    def end(self):
        return self.current_page*self.per_page_count

    @property
    def total_count(self):
        v,y=divmod(self.data_count,self.per_page_count)
        if y:
            v+=1
        return v
    def page_str(self,base_url):

        page_list = []

        # start_index=current_page-5
        # end_index=current_page+6  #区间含头部含尾
        if self.total_count < self.pager_num:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.current_page <= (self.pager_num + 1) / 2:
                start_index = 1
                end_index = self.pager_num + 1
            else:
                start_index = self.current_page - (self.pager_num - 1) / 2
                end_index = self.current_page + (self.pager_num + 1) / 2
                if (self.current_page + (self.pager_num - 1) / 2) > self.total_count:
                    start_index = self.total_count - self.pager_num + 1
                    end_index = self.total_count + 1
        if self.current_page == 1:
            prev = '<a class="page" href="javascript:;">上一页</a>'
        else:
            prev = '<a class="page" href="%s?p=%s">上一页</a>' % (base_url,self.current_page - 1)

        page_list.append(prev)
        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = '<a class="page active" href="%s?p=%s">%s</a>' % (base_url,i, i)
            else:
                temp = '<a class="page" href="%s?p=%s">%s</a>' % (base_url,i, i)
            page_list.append(temp)
        if self.current_page == self.total_count:
            next = '<a class="page" href="javascript:;">下一页</a>'
        else:
            next = '<a class="page" href="%s?p=%s">上一页</a>' % (base_url,self.current_page + 1)
        page_list.append(next)

        jump = """
            <input type='text' /><a onclick='jumpTo(this,"%s?p=");' id='go'>GO</a>
            <script>
                function jumpTo(_this,base){
                    var val=_this.previousSibling.value;
                    location.href=base+val;
                }
            </script>
        """ %(base_url,)
        page_list.append(jump)
        page_str = mark_safe("".join(page_list))  # 设置html，js代码信任，不然会以字符串显示
        return page_str














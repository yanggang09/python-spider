# -*- coding: utf8 -*-
from Tkinter import*
import Tkinter as tk
from  tkMessageBox import askquestion
from  tkMessageBox import showerror
from  tkFileDialog import asksaveasfilename
from  tkFileDialog import askopenfile
class Denlu():
    def __init__(self,root):
        '''Init Form'''
        self.root = root
        self.frameTop()
        self.frameBottom()
    def frameTop(self):
        """Creat To Frame"""
        self.top_label = tk.Label(self.root,text='电影下载',fg = 'red',bg='white',font=('Tempus Sans ITC',20),justify='left')
        self.top_label.grid(row=0,column=0,padx=20,pady=3)
    def frameBottom(self):
        """Create Bottom Frame"""
        self.bottom = tk.LabelFrame(self.root)
        self.bottom.grid(row=1,column=0,padx=20,pady=3)
        # self.bottom_cbtn_int_0 = IntVar()
        # self.bottom_cbtn_0 = tk.Checkbutton(self.bottom,variable=self.bottom_cbtn_int_0,text='记住密码',font=('Tempus Sans ITC',10))
        # self.bottom_cbtn_0.grid(row=2,column=1,padx=20,pady=3,sticky='w')
        # self.bottom_btn_0 = tk.Button(self.bottom,text='登陆',relief=RIDGE,bd=4,width=10\
        #                                   ,font=('Tempus Sans ITC',12),command=self.print_nima)#你可以添加其他的函数等
        # self.bottom_btn_0.grid(row=3,column=1,padx=20,pady=3)
        self.bottom_entry_var_0 = StringVar()
        self.bottom_entry_0 = tk.Entry(self.bottom,textvariable=self.bottom_entry_var_0)
        self.bottom_entry_0.grid(row=0,column=0,padx=20,pady=3)
        self.bottom_btn_0 = tk.Button(self.bottom,text='确认',relief=RIDGE,bd=4,width=10,font=('Tempus Sans ITC',12),command=self.print_nima)
        self.bottom_btn_0.grid(row=0, column=1, padx=20, pady=3)
        # self.bottom_entry_var_1 = StringVar()

    def print_nima(self):
        """btn callback"""

        self.bottom_entry_1 = tk.Label(self.bottom, text=self.test01())
        self.bottom_entry_1.grid(row=1, column=0, padx=20, pady=20)
        #print self.bottom_entry_var_0.get()

    def test01(self):
        # text="这是一个测试"
        data={'0':'测试1','1':'测试2','3':'测试3'}
        entry01 = self.bottom_entry_var_0.get()
        if entry01 in data.keys():
            return data[entry01]
        else:
            text = "输入错误"
            return text





def fun_fuck():
    if __name__ == '__main__':
        """main loop"""
        root2 = tk.Tk()
        root2.title('FUCK')
        Denlu(root2)
        root2.mainloop()
class Zouqi():
    def __init__(self,root):
        """Init Form"""
        self.root = root
        self.frameTop()
    def frameTop(self):
        """top frame"""
        btn_toplevel = tk.Button(self.root,text='开始',command=self.toplevel_click)
        btn_toplevel.grid(row=0,column=0,padx=40,pady=30,sticky='wesn')
    def toplevel_click(self):
        """toplevel click"""
        func_list = ['Day','Week','Month','Year']
        self.frm_toplevel = tk.Toplevel(self.root)
        self.frm_toplevel.title('选择您要观看的变化')
        for (count,func_name) in enumerate(func_list):
            btn = tk.Button(self.frm_toplevel,width=25,text=func_name)
            btn.grid(row=count//2,column=2*(count%2),padx=5,pady=5)
            btn.bind('<Button-1>',self.hhhh)#我整个hhh函数当例子。
    def hhhh(self,event):
        fff = event.widget['text']
        if fff == 'Month':
            #写下你想执行的内容或者PY程序，这里我简单的以一打开文件的程序替代下你想要的PY程序。
            openfile = askopenfile(filetypes=(('所有文件','*.'),('All files','*.*')))
            #。。。。。。。。。。。。。。。。
        if fff == 'Week':
            #写下你想执行的内容或者PY程序。
            #这里我简单的以是否保存(是，出现保存窗口，否出现错误提示框）程序替代下你想要的PY程序。
            if askquestion('保存','是否保存',parent=self.frm_toplevel) == 'yes':
                saveasfile = asksaveasfilename()
            else:
                try:showerror('error!','show error!',parent=self.frm_toplevel)
                except:pass
        if fff == 'Day':
            #我们创建一登陆界面，当然你也可以写你自己的PY！
            fun_fuck()
        try:self.frm_toplevel.destroy()
        except:pass

if __name__ == '__main__':
    '''main loop '''
    root = tk.Tk()
    root.title('2018最新电影下载器')
    root.geometry("400x200")
    Denlu(root)
    root.mainloop()
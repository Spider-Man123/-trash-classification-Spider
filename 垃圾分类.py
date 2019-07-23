from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
def fenlei():
    m=link.get()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    url = 'https://lajifenleiapp.com/'
    browser.get(url)
    input = browser.find_element_by_xpath('//*[@id="inputv"]')
    input.send_keys(m)
    button = browser.find_element_by_xpath('//*[@id="form"]/div/span')
    button.click()
    result = browser.find_element_by_xpath('/html/body/div/div[3]/div/h1')  # 结果
    jieshao = browser.find_element_by_xpath('/html/body/div/div[5]/div[1]')  # 垃圾介绍
    jieshaos = browser.find_element_by_xpath('/html/body/div/div[5]/div[2]')
    yao=browser .find_element_by_xpath('/html/body/div/div[7]/ul/li')#要求
    with open('laji.text','a',encoding= 'utf-8')as fp:
        fp.write("结果："+'\n'+result.text+'\n')
        fp.write("介绍："+'\n'+jieshao.text+'\n')
        fp.write(jieshaos.text+'\n')
        fp.write("投放要求："+'\n'+yao.text+'\n')
    browser.close()
    window.destroy()
    root = tk.Tk()
    root.title('spider-man.垃圾分类')
    root.geometry('500x200')
    text = tk.Text(bg='yellow',height=10,font=('黑体',15))
    text.pack()
    filename = 'laji.text'
    with open(filename,encoding= 'utf-8') as f:
        for each_line in f:
            text.insert(tk.INSERT, each_line)
    root.mainloop()
    file1 = open('laji.text', 'w+')
    file1.truncate()
window=tk.Tk()
window.title('spider-man.垃圾分类')
window.geometry ('500x300')
canvas=tk.Canvas(window,bg='blue',height=135,width=190)
image_file=tk.PhotoImage (file='1.png')
canvas .create_image(0,0,anchor='nw',image=image_file)
canvas .pack()
l=tk.Label (window,text='请输入垃圾名称',bg='yellow',font=('Calibri',25),width=30,height=2)
l.pack()
link= tk.Entry(window,width=20)
link.pack()
b=tk.Button (window,text='查询',bg='orange',font=('Calibri',25),width=10,height=1,command=fenlei)
b.pack()
window.mainloop()

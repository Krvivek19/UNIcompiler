def VideoUrl():
    downloadbartextlabel.configure(text="")
    downloadlabelresult.configure(text="")
    downloadsizelabelresult.configure(text="")
    downloadtimeleft.configure(text="")
    getdetail=threading.Thread(target=getvideo)
    getdetail.start()
    
def getvideo():
    global streams
    ListBox.delete(0,END)
    url=urltext.get()
    data = pafy.new(url)
    streams = data.allstreams
    index=0
    for i in streams:
        du='{:0.1f}'.format(i.get_filesize()//(1024*1024))
        datas=str(index) + '.'.ljust(3,' ')+str(i.quality).ljust(12,' ')+ str(i.extension).ljust(10,' ')+ str(i.mediatype) + ' ' + du.rjust(10,' ') + "MB"
        ListBox.insert(END,datas) 
        index += 1
def SelectCursor(evt):
    global downloadindex
    listboxdata= ListBox.get(ListBox.curselection())
    print(listboxdata)
    downloadstream=listboxdata[:3]
    downloadindex=int(''.join(x for x in downloadstream if x.isdigit()))
    
def DownloadVideo():
    getdata=threading.Thread(target=downloadvdata)
    getdata.start()
    
def downloadvdata():
    global downloadindex
    fgr= filedialog.askdirectory()
    downloadbartextlabel.configure(text="Your video is Downloading....")
    
    def mycallback(total, recvd, ratio, rate, eta):
        global total12
        total12 = float('{:.5}'.format(total/(1024*1024)))
        downloadprogress.configure(maximum=total12)
        recieved1 = '{:.5} mb'.format(recvd / (1024 * 1024))
        eta1 = '{:.2f} sec'.format(eta)
        downloadsizelabelresult.configure(text=total12)
        downloadlabelresult.configure(text=recieved1)
        downloadtimeleft.configure(text=eta1)
        downloadprogress['value'] = recvd/(1024*1024)
    
    streams[downloadindex].download(filepath=fgr,quiet=True,callback=mycallback)
    downloadbartextlabel.configure(text="Downloaded")
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
import threading
import pafy

root=Tk()
root.title('YOUTUBE')
root.geometry('650x700')
root.configure(bg='green')
root.attributes()
root.resizable(False,False)

downloadindex = 0
total12 = 0
streams = ""
#scrollbar
scrollbar=Scrollbar(root)
scrollbar.place(x=305,y=200,height=195,width=20)
urltext=StringVar()
UrlEntry= Entry(root,textvariable=urltext, font=('arial',20,'italic bold'),width=21)
UrlEntry.place(x=20,y=150)
#labels
introlabel= Label(root,text='Youtube Downloader',width=20,relief='ridge',bd=4,font=('Bernard',24,'bold'),fg='red')
introlabel.place(x=110,y=20)
ListBox= Listbox(root,yscrollcommand=scrollbar.set,width=31,height=10,font=('arial',12,'italic bold'),relief='ridge',bd=2,highlightcolor='red',highlightbackground='orange',highlightthickness=2)
ListBox.place(x=20,y=200)
ListBox.bind("<<ListboxSelect>>",SelectCursor)

downloadtime= Label(root,text='Time Left :',font=('arial',15,'italic bold'),bg=' blue',fg='red')
downloadtime.place(x=325,y=300)
downloadtimeleft= Label(root,text=' ',font=('arial',15,'italic bold'),bg=' blue',fg='red')
downloadtimeleft.place(x=475,y=300)
downloadbartextlabel= Label(root,text='Press Download Button To Start',width=26,font=('arial',10,'italic bold'),fg='red',bg='sky blue')
downloadbartextlabel.place(x=295,y=415)
dowlnloadprogresslabel=Label(root,text='',width=26,font=('arial',13,'italic bold'),fg='red',bg='blue',relief='raised')
dowlnloadprogresslabel.place(x=20,y=405)
downloadprogress=Progressbar(dowlnloadprogresslabel,orient= HORIZONTAL,value=0,length=100)
downloadprogress.grid(row=0,column=0,ipadx=85,ipady=3)
ClickButton=Button(root,text='Submit Url',font=('Arial',10,'italic bold'),bg='grey',fg='white',activebackground='olivedrab1',width=10,bd=8,command=VideoUrl)
ClickButton.place(x=400,y=150)
DownloadButton= Button(root,text='Download',font=('Arial',10,'italic bold'),bg='red',fg='white',activebackground='olivedrab1',width=10,bd=8,command=DownloadVideo)
DownloadButton.place(x=400,y=370)
root.mainloop()

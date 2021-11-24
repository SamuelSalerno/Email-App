import smtplib, ssl, getpass, datetime as dt, time
from datetime import date
import re
import email
import tkinter 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from tkinter import *
from tkinter import messagebox, filedialog
from email.message import EmailMessage
from email import encoders

#creation of gui
userInterface = Tk()
userInterface.title("Email App")
userInterface.geometry('1100x750')
userInterface.configure(bg='#262626')

# creation of variabl;e
sender_email = StringVar()
receiver_email = StringVar()
subject_email = StringVar()
message_email = StringVar()
password_email = StringVar()
cc_email = StringVar()
bcc_email = StringVar()
month_set = StringVar()
day_set = StringVar()
year_set = StringVar()
hour_set = StringVar()
minute_set = StringVar()
second_set = StringVar()
today = date.today()
time1 = dt.datetime.now()
month = today.month
day =  today.day
year = today.year
hour = time1.hour
minute = time1.minute+1
second = 0
bool = 0
attachments = []
port = 587  
smtp_server = "smtp.gmail.com"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Labels
receiver_label = Label(userInterface, text='To:', fg='#cccccc',bg='#262626', font=('Calibri',14))
receiver_label.grid(row=0, column=0, padx=5,pady=10)

cc_label = Label(userInterface, text='Cc:', fg='#cccccc',bg='#262626', font=('Calibri',14))
cc_label.grid(row=1, column=0, padx=5,pady=10)

bcc_label = Label(userInterface, text='Bcc:', fg='#cccccc',bg='#262626', font=('Calibri',14))
bcc_label.grid(row=2, column=0, padx=5,pady=10)

sender_label = Label(userInterface, text='From:', fg='#cccccc',bg='#262626', font=('Calibri',14))
sender_label.grid(row=3, column=0, padx=5,pady=10)

subject_label = Label(userInterface, text='Subject:', fg='#cccccc',bg='#262626', font=('Calibri',14))
subject_label.grid(row=4, column=0, padx=5,pady=10)

message_label = Label(userInterface, text='Message:', fg='#cccccc',bg='#262626', font=('Calibri',14))
message_label.grid(row=5, column=0, padx=5,pady=10)


# Text Inputs 
receiver_input = Entry(userInterface,textvariable = receiver_email, fg='#cccccc',bg='#404040',insertbackground = '#cccccc', width='40', font=('Calibri',14))
receiver_input.place(x=90, y=10,width=910)

cc_input = Entry(userInterface,textvariable = cc_email,fg='#cccccc',bg='#404040',insertbackground = '#cccccc', width='40', font=('Calibri',14))
cc_input.place(x=90, y=60,width=910)

bcc_input = Entry(userInterface,textvariable = bcc_email, fg='#cccccc',bg='#404040',insertbackground = '#cccccc', width='40', font=('Calibri',14))
bcc_input.place(x=90, y=110,width=910)

sender_input = Entry(userInterface, textvariable = sender_email, fg='#cccccc',bg='#404040',insertbackground = '#cccccc', width='40', font=('Calibri',14))
sender_input.place(x=90, y=160,width=910)
 
subject_input = Entry(userInterface, textvariable = subject_email, fg='#cccccc',bg='#404040',insertbackground = '#cccccc', width='40', font=('Calibri',14))
subject_input.place(x=90, y=210,width=910)

message_input = Text(userInterface, fg='#cccccc',bg='#404040', insertbackground = '#cccccc',font=('Calibri',14))
message_input.place(x=50, y=300, width=1000, height=365)

# attachment func
def attach_file():
  filename = filedialog.askopenfilename(initialdir='C:/', title='Select a file')
  attachments.append(filename)
  attach_num.config(fg='#7289da', bg='#262626',text='Attached ' + str(len(attachments)) + ' files')

# clearing attachment func
def clear_file():
  attachments.clear()
  attach_num.config(fg='#7289da',bg='#262626', text='Attached ' + str(len(attachments)) + ' files')


#validating email 
def check(email):
 
    if(re.fullmatch(regex, email)):
        return

    elif(email != ""):
        messagebox.showinfo("Invalid Email", f"Please enter a valid email! {email} is not a valid email")

def schedule():
            global month, day, year, hour,minute,second,bool
            month = int(month_set.get())
            day= int(day_set.get())
            year = int(year_set.get())
            hour = int(hour_set.get())
            minute = int(minute_set.get())
            second = int(second_set.get())
            bool = 1
            # set your sending time in PST(or whatever time it is on ur pc)
            
                                    #year, month, day, hour, minute, second
            
       
def timedSend():
    time_interface = Toplevel(userInterface)
    time_interface.title("Scheduled Email Window")
    time_interface.geometry('600x400')
    time_interface.configure(bg='#262626')

    month_label = Label(time_interface, text='Month:', fg='#cccccc', bg='#262626',font=('Calibri',14))
    month_label.grid(row=0, column=0, padx=5,pady=10)
    month_inputted = Entry(time_interface, textvariable = month_set, fg='#cccccc',bg='#404040', width='40', font=('Calibri',14))
    month_inputted.grid(row=0, column=1)

    day_label = Label(time_interface, text='Day:', fg='#cccccc',  bg='#262626',font=('Calibri',14))
    day_label.grid(row=1, column=0, padx=5,pady=10)
    day_input = Entry(time_interface,textvariable = day_set, fg='#cccccc',bg='#404040', width='40', font=('Calibri',14))
    day_input.grid(row=1, column=1)

    year_label = Label(time_interface, text='Year:', fg='#cccccc',  bg='#262626',font=('Calibri',14))
    year_label.grid(row=2, column=0, padx=5,pady=10)
    year_input = Entry(time_interface,textvariable = year_set, fg='#cccccc',bg='#404040', width='40', font=('Calibri',14))
    year_input.grid(row=2, column=1)

    hour_label = Label(time_interface, text='Hour:', fg='#cccccc',  bg='#262626',font=('Calibri',14))
    hour_label.grid(row=3, column=0, padx=5,pady=10)
    hour_input = Entry(time_interface,textvariable = hour_set, fg='#cccccc',bg='#404040', width='40', font=('Calibri',14))
    hour_input.grid(row=3, column=1)

    minute_label = Label(time_interface, text='Minute:', fg='#cccccc',  bg='#262626',font=('Calibri',14))
    minute_label.grid(row=4, column=0, padx=5,pady=10)
    minute_input = Entry(time_interface,textvariable = minute_set, fg='#cccccc',bg='#404040', width='40', font=('Calibri',14))
    minute_input.grid(row=4, column=1)


    second_label = Label(time_interface, text='Seconds:', fg='#cccccc',  bg='#262626',font=('Calibri',14))
    second_label.grid(row=5, column=0, padx=5,pady=10)
    second_input = Entry(time_interface,textvariable = second_set, fg='#cccccc',bg='#404040', width='40', font=('Calibri',14))
    second_input.grid(row=5, column=1)
    


    okay_btn = Button(time_interface, command = schedule, text='Schedule', fg='#cccccc', bg='#404040',font=('Calibri', 14), pady=10)
    okay_btn.place(x=475, y=350, width=100, height=40)

    def cancel():
        global bool
        time_interface.destroy()
        bool = 0
    cancel_btn = Button(time_interface, command = cancel, text='Cancel', fg='#cccccc', bg='#404040',font=('Calibri', 14), pady=10)
    cancel_btn.place(x=25, y=350, width=100, height=40)

    




# when send button is hit 
def send():
  
  
  check(sender_email.get())
  check(receiver_email.get())
  check(cc_email.get())
  check(bcc_email.get())

  psswrd_interface = Toplevel(userInterface)
  psswrd_interface.title("Password Window")
  psswrd_interface.geometry('650x200')
  psswrd_interface.configure(bg='#262626')

 
  email_label = Label(psswrd_interface, text='Email:', fg='#cccccc', bg='#262626',font=('Calibri',14))
  email_label.grid(row=0, column=0, padx=5,pady=10)
  email_inputted = Label(psswrd_interface, text = sender_email.get(), fg='#cccccc',bg='#404040', width='40', font=('Calibri',14))
  email_inputted.grid(row=0, column=1)
  password_label = Label(psswrd_interface, text='Password', fg='#cccccc',  bg='#262626',font=('Calibri',14))
  password_label.grid(row=1, column=0, padx=5,pady=10)
  password_input = Entry(psswrd_interface,textvariable = password_email, fg='#cccccc',bg='#404040', width='40', font=('Calibri',14), show="*")
  password_input.grid(row=1, column=1)

  # Define Sign In Command
  def signIn():
    
    password = password_email.get()
    message = MIMEMultipart("alternative")
    message["Subject"] = subject_email.get()
    message["From"] = sender_email.get()
    message["To"] = receiver_email.get()
    message["Cc"] = cc_email.get()
    text = message_input.get("1.0",END)

    receiver = str(receiver_email.get()).split()
    cc = str(cc_email.get()).split(', ')
    bcc = str(bcc_email.get()).split(', ')

    receiver.extend(cc)
    receiver.extend(bcc)

    part1 = MIMEText(text, "plain")
    message.attach(part1)

    psswrd_interface.destroy()

    for data in attachments:
      filename = data
      filetype = filename.split('.')
      filedir = filetype[0]
      filetype = filetype[1]
      with open(filename, "rb") as attachment:
        part = MIMEApplication(attachment.read(),_subtype=filetype)
      part.add_header('Content-Disposition', "attachment; filename= %s" % filename.split("/")[-1])
      message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
      server.starttls(context=context)
      server.login(sender_email.get(), password)
      if bool == 1:
          send_time = dt.datetime(year,month,day,hour,minute,second) 
          time.sleep(send_time.timestamp() - time.time())
            
      server.sendmail(sender_email.get(), receiver, message.as_string())
      messagebox.showinfo("Email Successful", "Email Sent!")
      server.quit()

 
  signin_btn = Button(psswrd_interface, command = signIn, text='Sign In', fg='#cccccc', bg='#404040',font=('Calibri', 14), pady=10)
  signin_btn.grid(row = 2, column = 1, padx = 5, pady = 10)


send_btn = Button(userInterface, command = send, text='Send', fg='#cccccc',bg='#404040', font=('Calibri', 14), pady=10)
send_btn.place(x=950, y=690, width=100, height=40)

schedule_btn = Button(userInterface, command = timedSend, text='Schedule Email ', fg='#cccccc',bg='#404040', font=('Calibri', 14), pady=10)
schedule_btn.place(x=780 , y=690, width=150, height=40)


attach_btn = Button(userInterface, command=attach_file, text="Attach File",  fg='#cccccc',bg='#404040', font=('Calibri', 14), pady = 10)
attach_btn.place(x=170, y=690, width=100, height=40)

clear_attach_btn = Button(userInterface, command=clear_file, text="Clear File",  fg='#cccccc',bg='#404040', font=('Calibri', 14), pady = 10)
clear_attach_btn.place(x=50, y=690, width=100, height=40)

attach_num = Label(userInterface, text="", font = ('Calibri', 14))
attach_num.place(x = 280, y = 695)

userInterface.mainloop()
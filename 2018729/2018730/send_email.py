#_*_ coding:utf-8 _*_
'''文本邮件发送
Usage:
    send_email <from_addr> <password> <to_addr> <smtp_server> <text> <Subject>
    send_email <from_addr> <password> <to_addr> <smtp_server> <text>

Options:
    -h --help       显示帮助菜单
    <To>            收件人
    <From>          发件人
    <Subject>       主题

Example:

'''
from docopt import docopt
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

class send_email():
    def __init__(self,data):
        #取出各项数据
        self.from_addr = data['<from_addr>']
        self.password = data['<password>']
        self.to_addr = data['<to_addr>']
        self.smtp_server = data['<smtp_server>']
        #self.From_who = data['<From>']
        #self.To_who = data['<To>']
        self.subject = data['<Subject>']
        self.Text = data['<text>']

    def _format_addr(self,s):
        name,addr = parseaddr(s)
        return formataddr((Header(name,'utf-8').encode(),addr))

    def send(self):
        msg = MIMEText(self.Text,'plain','utf-8')
        try:
            msg['From'] = self.from_addr
            msg['To'] = self.to_addr
            msg['Subject'] = Header(self.subject,'utf-8').encode()
        except:
            print('没有详细收发和主题~')

        server = smtplib.SMTP(self.smtp_server,25) #开区邮件服务端口25，商务邮件端口为587
        server.set_debuglevel(1)#打印debug
        server.login(self.from_addr,self.password)
        server.sendmail(self.from_addr,self.to_addr,msg.as_string())
        server.quit()

if __name__ == '__main__':
    arguement = docopt(__doc__)
    sender = send_email(arguement)
    sender.send()
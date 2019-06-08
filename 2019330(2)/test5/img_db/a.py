from  MyQR import myqr
import os
# myqr.run(words='nihaoma?',
#          picture=os.path.abspath('../')+'/media/img/1.gif',
#          colorized=True,
#          save_name='1.gif',
#          save_dir='../media/imgs'
#         )
# print(os.path.abspath('../media/imgs'))

myqr.run(
    words='nihaoma?',
    picture= '../media/img/1.gif',  #必须加上../
    colorized=True,
    save_name='1.gif',
    save_dir='../media/imgs',
)

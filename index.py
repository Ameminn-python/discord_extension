import sys
import io
import cgi
import discordbot
form = cgi.FieldStorage()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


user_id = form.getfirst('user_id')
text_content = form.getfirst('text_cnt')
result =  to_send(user_id,text_content)
if result == 'error':
    print('Content-type: text/html; charset=UTF-8')
    print('')
    print('送信に失敗しました')
else:
    print('Content-type: text/html; charset=UTF-8')
    print('') 
    print(user_id)
    print(text_content)
    print('送信に成功しました')



                             


# with open
with open('example.txt','w') as f:
    f.write('hello file')

with open('example.txt','r') as f:
    data = f.read()
    # print(data)

with open('C:\\Users\\user\\Desktop\\discord_bot\\noodle\\1.jpg','rb') as f:
    data = f.read()
    # print(data)

#BytesIO
from io import BytesIO

# f = BytesIO()
# f.write(b'hello bytesio')
# f.seek(0)
# print(f.read())

f = BytesIO(b'hello bytesio')
data_f = f.read()
# print(data_f)

#PIL
from PIL import Image
import base64

photo = Image.open('C:\\Users\\user\\Desktop\\discord_bot\\noodle\\1.jpg')
# print(photo)

b = BytesIO()
photo.save(b,format = 'JPEG')

# print(b.getvalue())
# print(type(b.getvalue()))
# print(base64.b64encode(b.getvalue()).decode())
# print(type(base64.b64encode(b.getvalue()).decode()))
# print(base64.b64encode(b.getvalue()))
# print(type(base64.b64encode(b.getvalue())))
# print(b.getvalue().decode())
# print(type(b.getvalue().decode()))

# b.seek(0)
# print(b.read())


    

#reference：https://docs.python.org/zh-tw/3.13/library/functions.html#open

#reference for BytesIO：https://docs.python.org/zh-tw/3.13/library/io.html#io.BytesIO

#reference for with open：https://docs.python.org/zh-tw/3.13/library/functions.html#open

#reference for Image.save()：https://pillow.readthedocs.io/en/stable/reference/Image.html

#reference for magic number：https://en.wikipedia.org/wiki/List_of_file_signatures#:~:text=A%20file%20signature%20is%20data%20used%20to%20identify,are%20not%20intended%20to%20be%20read%20as%20text.
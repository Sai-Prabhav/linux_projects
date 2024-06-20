# import pyperclip
# spam = pyperclip.paste()
# print(spam,"is in your clipboard")
# x=""
# for i in spam:
#     x+=f"||{i}||"
# pyperclip.copy(x)
# print(x)

# import pyperclip
# pyperclip.copy('The text to be copied to the clipboard.')
# spam = pyperclip.paste()

import pyperclip
pyperclip.copy("".join([f"||{i}||" for i in pyperclip.paste()]))

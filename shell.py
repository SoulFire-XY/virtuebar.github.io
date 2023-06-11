import run_i as VirtueBar
import os
os.system('cls')
from pprint import pprint
print('==========================================')
print('        VirtueBar Shell V1.0.1            ')
print('      Release Version: 01/04/2023         ')
print('==========================================')
while True:
    text = input('ON>> ')
    if text == 'VB_exit': 
        exit()
    elif text == '' or text == ' ': 
        pass
    else:
        result, error = VirtueBar.run('<stdin.filename>', text)

        if error: pprint(error.as_string())
        elif result:
            if len(result.elements) == 1:
                if result.elements[0] != str("null"):
                    if str(repr(result.elements[0])) != "null": pprint(result.elements[0])
            else:
                for i in result.elements:
                    if str(repr(result)) != "null": pprint(result)

import run_i as VirtueBar
import os

#os.system('cls')
print('==========================================')
print('        VirtueBar Shell V1.0.0            ')
print('      Release Version: 17/12/2022         ')
print('==========================================')
while True:
    text = input('ON>> ')
    if text == 'VB_exit': 
        exit()
    elif text == '' or text == ' ': 
        pass
    else:
        result, error = VirtueBar.run('<stdin.filename>', text)

        if error: print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                if result.elements[0] != str("null"):
                    if repr(result.elements[0]) != "null": print(repr(result.elements[0]))
            else:
                for i in result.elements:
                    if repr(result) != "null": print(repr(result))

import run_i as VirtueBar
import os
import sys
os.system('cls')

if len(sys.argv) > 1:
    path = sys.argv[1]
    file = path
    ext = file[-4:]
    if path == '' or path == ' ': 
        raise RuntimeError('No filename was specified')
    elif ext != 'virb':
        raise RuntimeError('Invalid file extension was given')
    else:          
        ospath = os.path.abspath(file)
        fullpath = ospath.replace("\\", "/")
        command = f'RUN("{fullpath}")'
        #print(command)
        result, error = VirtueBar.run(f'{file}', command)
        if error: print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                if result.elements[0] != str("null"):
                    if repr(result.elements[0]) != "null": print(repr(result.elements[0]))
            else:
                for i in result.elements:
                    if repr(result) != "null": print(repr(result))
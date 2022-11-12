import run_i as VirtueBar

while True:
    text = input('ON>> ')
    if text != 'VB_exit':
        result, error = VirtueBar.run('<stdin.filename>',text)

        if error: print(error.as_string())
        else: print(result)
    else: exit()
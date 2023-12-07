def do_stuff(num=0):
    try:
        if num:
            return int(num)*2
        else:
            return 'Please enter number'
    except ValueError as err:
        return err
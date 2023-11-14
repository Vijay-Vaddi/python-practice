user1 = {
    'name': 'Kenobi',
    'occupation': 'Jedi',
    'valid': True
}

def authentication(func):
    def test_auth(*args, **kwargs):
        if args[0]['valid']:
            func(*args,**kwargs)
        else:
            print('Can not send message')
    return test_auth


@authentication
def message_jedi_council(user):
    print('May the force be with you')

message_jedi_council(user1)
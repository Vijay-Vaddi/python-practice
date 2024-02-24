''' Using a dict let's you translate the key into a callable. 
The key doesn't need to be hardcoded though, as in your example.
# Usually, this is a form of caller dispatch,
where you use the value of a variable to connect to a function. 
Say a network process sends you command codes, a dispatch mapping 
lets you translate the command codes easily into executable code:'''

def do_ping(self, arg):
    return 'Pong, {0}!'.format(arg)

def do_ls(self, arg):
    return '\n'.join()

dispatch = {
    'ping': do_ping,
    'ls': do_ls,
}

def process_network_command(command, arg):
    # send(dispatch[command](arg))
    dispatch[command](arg)

process_network_command('ping', arg=15 )
'''Note that what function we call now depends entirely on what the value is of command. 
The key doesn't have to match either; it doesn't even have to be a string, 
you could use anything that can be used as a key, and fits your specific application.
# Using a dispatch method is safer than other techniques, such as eval(), 
as it limits the commands allowable to what you defined beforehand. No attacker is going to sneak a ls)";
DROP TABLE Students; -- injection past a dispatch table, for example.'''
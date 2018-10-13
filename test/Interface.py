import cmd

class Interface(cmd.Cmd):
    prompt = 'Command:'

    def do_foo(_self, args):
        print(args)


interface = Interface()
interface.cmdloop()

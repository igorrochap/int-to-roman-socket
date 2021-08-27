class Command():
    def __init__(self):
        self.allowed_commands = ['roman', 'int', 'out']

    def verify_command(self, user_command):
        if user_command in self.allowed_commands:
            return True
        else:
            return False
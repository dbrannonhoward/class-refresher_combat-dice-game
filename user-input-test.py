# Playing with the input function
import null


class HandleUserInput:
    def __init__(self):
        self.user_input = "Empty until defined."

    def get_user_input(self, user_prompt: str):
        self.user_input = input(user_prompt)

    def print_user_input(self):
        print(self.user_input)


HandleUserInput.get_user_input(null, "Test prompt\n")
HandleUserInput.print_user_input(null)

# end

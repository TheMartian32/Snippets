
# * Usually I use this to repeat a script

# * First part of what you want to happen
repeat = ''
while True:
    # * Asks to repeat the script.
    repeat = input(
        '\nWould you like to repeat the script? (Y/N): ').lower()
    if repeat[0] == 'y':
        # * what you want to repeat here
        continue
    if repeat[0] == 'n':
        break


# * Usually I use the ask_for method when I need the input to repeat if the wrong data type is given or the wrong answer is given.
# * Also used in conjunction with the repeat snippet.
class UI_Inputs():

    """
    A class responsible for the inputs in the UI and basically anything that requires
    either the UI or inputs.
    """

    def ask_for(self, prompt, error_msg=None, _type=None):
        """ While the desired prompt is not given, it repeats the prompt. """
        while True:
            inp = input(prompt).strip()
            if not inp:
                if error_msg:
                    print(error_msg)
                continue

            if _type:
                try:
                    inp = _type(inp)
                except ValueError:
                    if error_msg:
                        print(error_msg)
                    continue
            return inp

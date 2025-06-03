from rich import print

def get_valid_int_input(prompt, valid_options):
    while True:
        try:
            print(prompt, end='')
            x = int(input())
            if x not in valid_options:
                print(f"Пожалуйста, введите {', '.join(str(opt) for opt in valid_options)}")
                continue
            return x
        except ValueError:
            print("Пожалуйста, введите число")
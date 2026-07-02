__all__ = ['print_arg']

def print_arg(*args):
    print(type(args)) # tuple()
    list_elements = list(args)
    list_str_elements = []
    for arg in list_elements:
        if isinstance(arg, str):
            list_str_elements.append(arg)
        print(arg)
    return list_str_elements





def print_kwargs(**kwargs):
    print(type(kwargs)) # dict() # Kye : value
    print(kwargs)



def print_args_kwars(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)



if __name__ == '__main__':
    print_kwargs(name="Bob", age=12, list_values=[1, 23, 5434, 54, 356], dict_values={1: 2})
    print(print_arg())

    print_args_kwars(1, 23, 5345, 346, 45, 6756, 7, ['asdasd'])

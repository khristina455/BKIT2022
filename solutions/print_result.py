def print_result(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        if type(res) == list:
            for el in res:
                print(el)
        elif type(res) == dict:
            for el in res.keys():
                print(f"{el} = {res[el]}")
        else:
            print(res)
        return res
    return wrapper


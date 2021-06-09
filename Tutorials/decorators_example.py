def new_decorator(func):
    def warp_func():
        print('I run before the exec func')

        func()

        print("Code here after exec func()")

    return warp_func

@new_decorator
def func_needs_decorator():
    print("Please decorate me!!")

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
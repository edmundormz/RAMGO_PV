import ipdb


def table_things(**kwargs):
    apple_type = kwargs.get('apple')
    cabbage_type = kwargs.get('cabbage')
    ipdb.set_trace()

    # for name, value in kwargs.items():
    #    print('{0} = {1}'.format(name, value))


table_things(apple="fruit", cabbage="vegetable")

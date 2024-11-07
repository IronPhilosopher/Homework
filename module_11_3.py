import inspect

def introspection_info(obj):
    dict = {'Type': type(obj)}
    meth = []
    atr = []
    for i in dir(obj):
        if i[0] == '_' and i[1] == '_':
            meth.append(i)
        else:
            atr.append(i)
    dict.update({'Attributes': atr, 'Methods': meth})
    if inspect.getmodule(obj) == None:
        dict.update({'Module': '__main__'})
    else:
        dict.update({'Module': inspect.getmodule(obj)})
    return dict

number_info = introspection_info(42)
print(number_info)
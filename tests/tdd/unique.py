class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.it = iter(items)
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else :
            self.ignore_case = False
        self.d = {}

    def __next__(self):
        el = next(self.it)
        if self.ignore_case == True:
            el_change = el.lower().strip()
        else:
            el_change = str(el).strip()
        while el_change in self.d.keys():
            el = next(self.it)
            if self.ignore_case == True:
                el_change = el.lower().strip()
            else:
                el_change = str(el).strip()
            
        self.d[el_change] = 1
        return el


    def __iter__(self):
        return self




from collections.abc import Iterator,Iterable


class Company(object):
    def __init__(self,employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

    """自定义迭代器"""

    def __iter__(self):

        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]


class MyIterator(Iterator):
    def __init__(self,employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        #返回迭代值逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1

        return word








if __name__ == '__main__':
    company = Company(['TOMMY', 'BOB', 'TRUMP'])
    #myiter = iter(company)
    """判断是否存在__iter__方法"""
    for item in company:
        print(item)


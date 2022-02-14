# Author: Emily Su
# Last Revised: February 2022

from collections import defaultdict
from goody import type_as_str
import prompt


class Bag:
    '''The Bag class constructs a bag object. 
    A bag object is similar to a set object, but it can store multiple copies of an item.
    Bag object is stored in a dictionary; the key (any data type) is an item, the value (int) is the number of copies of the item.'''
    def __init__(self, iterable=[]):
        '''Parameter:
        iterable (iter): an iterable of values
        
        Attribute:
        iterable (dict): key (data type) representing the item in the bag, value (int) the number of copies of that item in the bag'''
        bag_obj = defaultdict(int)
        
        for item in iterable:
            bag_obj[item] += 1
            
        self.iterable = bag_obj


    def __repr__(self) -> str:
        '''Returns a printable representational string of a bag.
        String format example: Bag(['a','c','b','b','d','d','d'])'''
        item_list = []
        
        for k in self.iterable.keys():
            if self.iterable[k] == 1:
                item_list += k
            else:
                for __ in range(self.iterable[k]):
                    item_list += k
        
        return 'Bag(' + str(item_list) + ')'


    def __str__(self) -> str:
        '''Returns a more compact representational string of a bag.
        String format example: Bag(a[1],c[1],b[2],d[3])'''
        item_set = set()
        
        for k in self.iterable.keys():
            compact_item = str(k) + '[' + str(self.iterable[k]) + ']'
            item_set.add(compact_item)
        
        str_to_return = ', '.join(item_set)
        
        return 'Bag(' + str_to_return + ')'
        
    
    def __len__(self) -> int:
        '''Returns total_values (int): the total number of values in the bag.'''
        total_values = 0
        
        for v in self.iterable.values():
            total_values += v
        
        return total_values
    
    
    def unique(self) -> int:
        '''Returns unique_values (int): the number of unique values in the bag.'''
        unique_values = 0
        
        for __ in self.iterable.keys():
            unique_values += 1
        
        return unique_values
    
    
    def __contains__(self, item) -> bool:
        '''Check whether the bag contains the given argument.
        Parameter: 
        item (any data type): item to be checked if it exists in the bag
        
        Return:
        True: bag contains the item
        False: bag does not contain the item'''
        if item in self.iterable.keys():
            return True
        else:
            return False
    
    
    def count(self, item) -> int:
        '''Returns the number of copies (int) of given argument in the bag.
        Parameter:
        item (any data type): item to be counted'''
        if self.__contains__(item):
            return self.iterable[item]
        else:
            return 0
    
    
    def add(self, item):
        '''Adds the given argument to the bag if it does not already exist. 
        If the argument is already a key in the bag, its count is incremented by 1.
        
        Parameter:
        item (any data type): item to be added to the bag'''
        self.iterable[item] += 1
            
    
    def __add__(self, right):
        '''Returns a new bag object which is the union of the bag and the given argument.
        If the given argument is not a Bag object, raises TypeError.
        
        Parameter:
        right (Bag object): bag object to added with self'''
        if type(right) is not Bag:
            raise TypeError('Bag.__add__: unsupported operand type(s) for +: ' + type_as_str(right) + ' and bag')
        
        else:
            union_items = []
            for self_item in self.__repr__().strip('Bag()[]').split(','):
                union_items.append(self_item.strip("' "))
            for right_item in right.__repr__().strip('Bag()[]').split(','):
                union_items.append(right_item.strip("' "))
            
            return Bag(union_items)
    
    
    def remove(self, item):
        '''Modifies the bag to remove the given argument from the bag.
        If the given argument exists in the bag, the count is decremented by 1. If the item count is 0, the key (item) is removed from the Bag object.
        If the given argument does not exist in the bag, raises ValueError.
        
        Parameter:
        item (any data type): item to be removed from bag'''
        if self.iterable.__contains__(item) is False:
            raise ValueError('B.remove: value (' + str(item) +') could not be removed')
        
        else:
            self.iterable[item] -= 1

            if self.iterable[item] == 0:
                self.iterable.pop(item)
    
    
    def __eq__(self, right) -> bool:
        '''Checks whether one Bag operand is equal or not equal to the given argument.
        Parameter:
        right (Bag object): Bag operand to be compared against self
        
        Return:
        True: the two Bag operands contain the same values the same number of times
        False: the other operand is not a Bag object, or they do not contain the same values the same number of times''' 
        if type(right) is Bag:
            self_item_list = []
            right_item_list = []
            
            for self_item in self.__repr__().strip('Bag()[]').split(','):
                self_item_list.append(self_item.strip("' "))
            for right_item in right.__repr__().strip('Bag()[]').split(','):
                right_item_list.append(right_item.strip("' "))
            if sorted(self_item_list) == sorted(right_item_list):
                return True
        
        return False
        
            
    def __iter__(self):
        '''Returns a generator object on which next can be called to produce every value in the bag.'''
        def gen(bag_obj):
            for k, v in bag_obj.items():
                if v > 1:
                    for __ in range(v):
                        yield k
                else:
                    yield k
        
        
        bag_copy = {}
        for k, v in self.iterable.items():
            bag_copy[k] = v
        
        return gen(bag_copy)
   
    
if __name__ == '__main__':
    #Simple tests
    b = Bag(['d','a','b','d','c','b','d'])
    print('b = ' + str(b))
    print('b = ' + repr(b))
    
    b2 = Bag(['a','a','b','x','d'])
    print('b2 = ' + str(b2))
    print('b2 = ' + repr(b2))
    
    print('\nadd, remove, in, count')
    b.add('a')
    print("add 'a' to b: " + str(b))
    b2.remove('a')
    print("remove 'a' from b2: " + str(b2))
    print("'a' in b: " + str('a' in b))
    print("'x' in b: " + str('x' in b))
    print("count of 'd' in b: " + str(b.count('d')))
    
    print('\nlen, unique')
    print('length of b: ' + str(len(b)))
    print('# of unique items in b: ' + str(b.unique()))
    print('length of b2: ' + str(len(b2)))
    print('# of unique items in b2: ' + str(b2.unique()))
    
    
    print('\nb+b2, b==b2, b!=b2')
    print('b + b2: ' + str(b + b2))
    print('b == b2: ' + str(b == b2))
    print('b != b2: ' + str(b != b2))
    
    print('\niterator')
    print('i for i in sorted(b): ' + str([i for i in sorted(b)]))
    
    # print()
    # import driver
    # driver.default_file_name = 'bscp21W22.txt'
    # # driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
    # # driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
    # # driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    # driver.driver()

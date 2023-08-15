# 20) Write any example for map, filter, and reduce methods?
from functools import reduce


def performing_map(lst):
    """ this function adds 'ed' to all the elements in the lst """
    # converting map object into list and returning that list
    return list(map(lambda x: str(x) + 'ed', lst))


def performing_filter(tup):
    """
    this function takes a tuple as input and filters the names to categorize male, female and returns a dictionary
    """
    return {"male": list(filter(lambda x: x.find('Mr.') > -1, tup)),
            "female": list(filter(lambda x: x.find('Mrs.') > -1, tup))
            }


def performing_reduce(student_dict):
    """
     this function takes a dictionary of student with their marks and calculate each students average, sum, percentage
    """
    result_dict = {}
    for key, value in student_dict.items():
        total = reduce(lambda x, y: x + y, value)
        result_dict[key] = {'total marks': total,
                            'average': round(total / 6, 2),
                            'percentage': round((total / 600) * 100, 2)
                            }
    return result_dict


res = performing_map(['check', 'click', 'pick'])
print(res)

res1 = performing_filter(('Mr. Anuj', 'Mr. Kumar', 'Mrs. Kumari'))
print(res1)

st_dict = {
    'John': [65, 77, 84, 55, 89, 90],
    'James': [61, 70, 83, 59, 49, 92],
    'Tim': [63, 79, 84, 85, 79, 91],
}
res3 = performing_reduce(st_dict)
print(res3)

#
# Module for not_test functions
# Auxiliary functions
#
def is_unique(array):
    """
    Predicate. Check that all items in array(list) are unique
    :param array:
    :return boolean:
    """

    if len(array) == len(set(array)):
        return True
    return False

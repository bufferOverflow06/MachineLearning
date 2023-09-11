# Sequential order 
def assignNumericValue(target_column):
    item_dict = {}
    items = target_column.unique()
    for i,item in enumerate(items):
        if item not in item_dict:
            item_dict[item] = i
    return item_dict

# Natural order
def assignNumericValue(target_column):
    item_dict = {}
    items = list(target_column.unique())
    # Sort in alphabetical order
    items.sort()
    # For reverse order 
    # rev = sorted(columns,reverse=True)
    for i,item in enumerate(items):
        if item not in item_dict:
            item_dict[item] = i
    return item_dict
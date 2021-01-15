def TreeConstructor(strArr):
    # instantiate dicts
    parents = {}
    children = {}

    for pair in strArr:
        # separate and parse the integers
        child, parent = pair.split(',')

        child = child[1:]
        parent = parent[:-1]

        # if the parent integer was encountered before, append to list
        # otherwise create the list of the child
        if parent in parents:
            parents[parent].append(int(child))
        else:
            parents[parent] = [int(child)]

        # if the children integer was encountered before, append to list
        # otherwise create the list of the parent
        if child in children:
            children[child].append(int(parent))
        else:
            children[child] = [int(parent)]

    # parents should have no more than 2 children
    for key in parents.keys():
        if len(parents[key]) > 2:
            return 'false';

    # children should have no more than 1 parent
    for key in children.keys():
        if len(children[key]) > 1:
            return 'false';

    return 'true'


# keep this function call here
print
TreeConstructor(raw_input())
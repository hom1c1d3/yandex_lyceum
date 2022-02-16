def simple_map(transformation, values):
    for i in values:
        yield transformation(i)

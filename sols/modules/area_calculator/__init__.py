
def calc_area(type, dims):
    if type == 'square':
        return dims['side']**2
    elif type == 'rectangle':
        return dims['width']*dims['length']
    elif type == 'triangle':
        return dims['base']*dims['height']/2
    else:
        return None

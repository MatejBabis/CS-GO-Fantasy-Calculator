def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color


def highlight_event_winner(s):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == s.max()
    return ['background-color: gold' if v else '' for v in is_max]


def bold(s):
    '''
    Make the output bold
    '''
    return 'font-weight: bold'

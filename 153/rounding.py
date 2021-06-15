def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    return [round(num) for num in transactions]


round_up_or_down(transactions=list)

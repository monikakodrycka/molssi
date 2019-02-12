"""
string_util.py

Misc. string processing functions
"""


def title_case(sentence):
    """
    Convert a string to title case.

    Title case means that the first character of every word is capitalized
    and all the rest are lowercase.

    Parameters
    ----------
    sentence: string
        String to be converted to title case

    Return
    ------
    titled_sentence: string
        Sentence in a title case

    Examples
    --------
    >>> title_case('THiS iS a sTrInG tO be COnverTeD.')
        'This Is A String To Be Converted.'
    """

    if not isinstance(sentence, str):
        raise TypeError("Input sentence must be type str")

    if len(sentence) == 0:
        raise ValueError("Input sentence cannot be empty")

    return sentence.title()

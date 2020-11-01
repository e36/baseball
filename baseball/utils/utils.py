def convert_enum_list_to_delimited_string(enumlist, delimiter=','):
    """
    Converts a list of enums into a delimited string using the enum values
    E.g., [PlayerActionEnum.FLYBALL, PlayerActionEnum.HOMERUN, PlayerActionEnum.WALK] = 'FLYBALL,HOMERUN,WALK'
    :param enumlist:
    :param delimiter:
    :return:
    """

    return delimiter.join([listitem.value for listitem in enumlist])

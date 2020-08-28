from enum import Enum


class PlayerActionEnum(Enum):

    HOMERUN = 'homerun'
    SINGLE = 'single'
    DOUBLE = 'double'
    TRIPLE = 'triple'

    FLYBALLA = 'flyball'
    FLYBALLB = 'flyball'
    FLYBALLC = 'flyball'
    FLYBALLX = 'flyball'

    GROUNDBALLA = 'groundball'
    GROUNDBALLB = 'groundball'
    GROUNDBALLC = 'groundball'
    GROUNDBALLX = 'groundball'

    LINEOUT = 'lineout'
    WALK = 'walk'
    STRIKEOUT = 'strikeout'
    CATCHER_CARD = 'catchercard'

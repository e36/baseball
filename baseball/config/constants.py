from typing import Dict
from baseball.enums.PlayerPositionEnum import PlayerPositionEnum
"""
Stores game constants
"""

FIELD_POSITIONS: Dict[int, str] = {
    1: 'Pitcher',
    2: 'Catcher',
    3: 'First base',
    4: 'Second base',
    5: 'Third base',
    6: 'Shortstop',
    7: 'Left field',
    8: 'Center field',
    9: 'Right field',
    10: 'Designated hitter'
}

FIELD_POSITIONS_ABBREVIATED: Dict[int, str] = {
    1: 'P',
    2: 'C',
    3: '1B',
    4: '2B',
    5: '3B',
    6: 'SS',
    7: 'LF',
    8: 'CF',
    9: 'RF',
    10: 'DH'
}

FIELD_POSITIONS_PLAYERPOSITIONENUM: Dict[str, PlayerPositionEnum] = {
    'P': PlayerPositionEnum.Pitcher,
    'C': PlayerPositionEnum.Catcher,
    '1B': PlayerPositionEnum.FirstBase,
    '2B': PlayerPositionEnum.SecondBase,
    '3B': PlayerPositionEnum.ThirdBase,
    'SS': PlayerPositionEnum.ShortStop,
    'LF': PlayerPositionEnum.LeftField,
    'CF': PlayerPositionEnum.CenterField,
    'RF': PlayerPositionEnum.RightField,
    'DH': PlayerPositionEnum.DesignatedHitter
}


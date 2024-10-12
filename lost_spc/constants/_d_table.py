from dataclasses import dataclass

from numpy import floating
from typing import Union


@dataclass
class D:
    d2: Union[float, floating]
    d3: Union[float, floating]


_D_TABLE = {
    2: D(d2=0.7, d3=0.9),
}

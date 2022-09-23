
from a2.tabular import *


from a2.dates import *


from a2.a2 import *


#### Typing ######################################################################################
## https://www.pythonsheets.com/notes/python-typing.html
### from a2 import (  )
from typing import List, Optional, Tuple, Union, Dict, Any
Dict_none = Union[dict, None]
List_none = Union[list, None]
Int_none  = Union[None,int]
Path_type = Union[str, bytes, os.PathLike]

try:
    import numpy.typing
    npArrayLike = numpy.typing.ArrayLike
except ImportError:
    npArrayLike = Any

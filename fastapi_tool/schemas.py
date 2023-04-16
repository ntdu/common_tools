from pydantic import BaseModel
from typing import Dict, Any, Optional, ForwardRef, List, Union
from enum import Enum
import uuid

class DownloadSchema(BaseModel):
    url: str
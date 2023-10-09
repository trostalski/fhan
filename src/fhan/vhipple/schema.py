from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Dataset:
    id: int
    name: str
    description: Optional[str] = None
    dashboard_col_nums: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

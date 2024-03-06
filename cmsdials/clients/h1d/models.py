from typing import List, Optional

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field

from ...utils.base_model import OBaseModel


class LumisectionHistogram1D(BaseModel):
    id: int
    ls_number: int
    run_number: int
    date: AwareDatetime
    title: str = Field(..., max_length=220)
    entries: int
    data: list[float]
    x_min: float
    x_max: float
    x_bin: int
    source_data_file: int
    lumisection: int


class PaginatedLumisectionHistogram1DList(BaseModel):
    count: int | None
    next: AnyUrl | None
    previous: AnyUrl | None
    results: List[LumisectionHistogram1D] | None


class LumisectionHistogram1DFilters(OBaseModel):
    ls_number: Optional[int] = None
    lumisection_id: Optional[int] = None
    max_ls_number: Optional[int] = None
    max_run_number: Optional[int] = None
    min_entries: Optional[int] = None
    min_ls_number: Optional[int] = None
    min_run_number: Optional[int] = None
    page: Optional[str] = None
    run_number: Optional[int] = None
    title: Optional[str] = None
    title_contains: Optional[str] = None

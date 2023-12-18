from typing import Optional
from datetime import datetime, UTC

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base

class Tier(Base):
    __tablename__ = "tier"

    id: Mapped[int] = mapped_column(
        "id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False
    )
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default_factory=lambda:  datetime.now(UTC).replace(tzinfo=None)
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(default=None)

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        commanders_captains = [
            member
            for member in self.crew
            if member.rank in (Rank.commander, Rank.captain)
        ]
        if not commanders_captains:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = [
                m for m in self.crew if m.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                )

        inactive = [m for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        crew = [
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=42,
                specialization="Mission Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=10,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=5,
            ),
        ]
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15, 8, 0, 0),
            duration_days=900,
            crew=crew,
            budget_millions=2500.0,
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"  - {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )
    except ValidationError as e:
        print("Unexpected validation error:", e)

    print()
    print("=" * 40)
    print("Expected validation error:")

    try:
        crew_no_commander = [
            CrewMember(
                member_id="C004",
                name="Bob Lee",
                rank=Rank.officer,
                age=30,
                specialization="Piloting",
                years_experience=3,
            ),
        ]
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Doomed Voyage",
            destination="Pluto",
            launch_date=datetime(2024, 7, 1, 8, 0, 0),
            duration_days=100,
            crew=crew_no_commander,
            budget_millions=500.0,
        )
    except ValidationError as e:
        error_msg = str(e.errors()[0]["msg"])
        prefix = "Value error, "
        if error_msg.startswith(prefix):
            error_msg = error_msg[len(prefix):]
        print(error_msg)


if __name__ == "__main__":
    main()

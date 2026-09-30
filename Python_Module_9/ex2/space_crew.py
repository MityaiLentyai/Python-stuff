try:
    from enum import Enum
    from sys import exit
    from pydantic import BaseModel, Field, model_validator
    from pydantic import ValidationError
    from datetime import datetime
except ModuleNotFoundError as e:
    print(e)
    print("Perhaps you need to use virtual environment")
    exit(1)


class Rank(Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True

    @model_validator(mode='after')
    def crew_validator(self) -> "CrewMember":
        if not self.is_active:
            raise ValueError(
                "All crew members must be active")

        return self


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> "SpaceMission":
        for crew_member in self.crew:
            if crew_member.rank == Rank.commander \
                    or crew_member.rank == Rank.captain:
                break
            else:
                raise ValueError(
                    "Mission must have at least one Commander or Captain")
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with M")

        if self.duration_days > 365:
            experienced_crew = sum(
                member.years_experience >= 5 for member in self.crew)
            if experienced_crew / len(self.crew) < 0.5:
                raise ValueError(
                    "Missions longer than 365 days require at least "
                    "50% of crew to have 5+ years of experience"
                )
        return self

    def show(self) -> None:
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(valid_mission_crew)}")
        print("Crew members:")
        for crew_member in self.crew:
            print(
                f"- {crew_member.name} ({crew_member.rank.value}"
                f" - {crew_member.specialization})")


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    sarah_c = CrewMember(member_id="000", name="Sarah Connor",
                         rank=Rank.commander,
                         age=35, specialization="Mission Command",
                         years_experience=15, is_active=True)
    john_c = CrewMember(member_id="001", name="John Smith",
                        rank=Rank.lieutenant,
                        age=25, specialization="Navigation",
                        years_experience=5, is_active=True)
    alice_j = CrewMember(member_id="002", name="Alice Johnson",
                         rank=Rank.officer,
                         age=24, specialization="Engineering",
                         years_experience=5, is_active=True)
    valid_mission_crew = [sarah_c, john_c, alice_j]
    valid_mission = SpaceMission(mission_id="M2024_MARS",
                                 mission_name="Mars Colony Establishment",
                                 destination="Mars",
                                 duration_days=900,
                                 budget_millions=2500.0,
                                 launch_date=datetime(2077, 1, 1),
                                 crew=valid_mission_crew)
    print("Valid mission created:")
    valid_mission.show()
    print()
    print("=========================================")
    print("Expected validation error:")
    try:
        bang_cock = CrewMember(member_id="000", name="Bang COKCK",
                               rank=Rank.cadet,
                               age=69, specialization="Big Bang Theory",
                               years_experience=42, is_active=True)
        juicy_pussy = CrewMember(member_id="000", name="Juicy Pussy",
                                 rank=Rank.cadet,
                                 age=18,
                                 specialization="Juiciest of them all!",
                                 years_experience=6, is_active=True)
        invalid_mission_crew = [bang_cock, juicy_pussy]

        invalid_mission = SpaceMission(mission_id="M_VIDEOS",
                                       mission_name="Rated M for Mature",
                                       destination="Maximum Orgasm",
                                       duration_days=222,
                                       budget_millions=420.0,
                                       launch_date=datetime(6969, 1, 1),
                                       crew=invalid_mission_crew)
        invalid_mission.show()
    except ValidationError as e:
        print(f"{e.errors()[0]['msg'].replace('Value error, ', '')}")

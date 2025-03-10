import datetime
from app.errors import (VaccineError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError
                        )


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError(VaccineError)
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(VaccineError)
        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError
        else:
            return (f"Welcome to {self.name}")

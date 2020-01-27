REGEX_PATTERN = (
    r"^\d\s{3}(?P<TEAM>.+?)(?=\s{3})\s{3}"
    r"(?P<USER>\w+)\s{3}(?P<ROLE>-?\d+) \/ "
    r"(?P<BOOST>-?\d+)\s{3}(?P<POINTS>-?\d+)\s{3}(?P<TEAMPOINTS>-?\d+)\s{3}(?P<TOTAL>-?\d+)"
)

HEADERS = ["TEAM", "USER", "ROLE", "BOOST", "POINTS", "TEAMPOINTS", "TOTAL", "WAID"]

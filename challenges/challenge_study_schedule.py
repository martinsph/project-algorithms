def study_schedule(permanence_period, target_time):
    # testa se é nulo.
    if target_time is None:
        return None

    online_students = 0

    for login, logout in permanence_period:
        # testa se as entradas são inválidas.
        if not (
            isinstance(login, int)
            and isinstance(logout, int)
        ):
            return None

        # add plus one every time target_time value is between range
        if login <= target_time <= logout:
            online_students += 1

    return online_students

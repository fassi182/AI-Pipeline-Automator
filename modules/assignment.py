def assign_tasks(requirements):

    assignments = []

    for requirement in requirements:

        requirement = requirement.lower()

        if "database" in requirement:
            assignments.append("Database")

        elif "email" in requirement:
            assignments.append("Backend")

        elif "payment" in requirement:
            assignments.append("Backend")

        else:
            assignments.append("Backend")

    return assignments
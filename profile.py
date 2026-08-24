

def get_profile():
    return {
        "name": "Гришанов Михаил Алексеевич",
        "group": "РПО-2",
        "role": "student",
        "skills": ["Ниту"]
    }


def print_profile():
    profile = get_profile()
    print(f"Студент: {profile['name']}")
    print(f"Группа: {profile['group']}")
    print("Навыки:", ", ".join(profile["skills"]))
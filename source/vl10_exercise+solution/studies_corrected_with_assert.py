def erstelle_student(vorname, name, alter, matrikelnummer, studiengang):
    assert isinstance(vorname, str) and len(vorname) > 0, "Vorname muss ein nicht-leerer String sein"
    assert isinstance(name, str) and len(name) > 0, "Name muss ein nicht-leerer String sein"
    assert isinstance(alter, (int, str)), "Alter muss int oder str sein"
    assert isinstance(matrikelnummer, int), "Matrikelnummer muss int sein"
    assert isinstance(studiengang, str), "Studiengang muss String sein"
    
    return {
        "vorname": vorname,
        "name": name,
        "alter": alter,
        "matrikelnummer": matrikelnummer,
        "studiengang": studiengang
    }

def ist_minderjaehrig(student):
    # hier könnte man auch noch ein assert einfügen, 
    # dann ist der code allerdings im jetzigen Zustand nicht lauffähig --> langweilig
    #assert "alter" in student, "Feld 'alter' fehlt im student-Dictionary"
    try:
        alter = student.get("alter", None)
        return int(alter) < 18
    except (TypeError, ValueError):
        print(f"Ungültiger oder fehlender Alterseintrag bei: {student.get('vorname', 'Unbekannt')}")
        return False

def fuege_zu_studiengang_liste_hinzu(student, et_liste, inf_liste):
    assert isinstance(student, dict), "student muss ein Dictionary sein"
    assert isinstance(et_liste, list) and isinstance(inf_liste, list), "et_list und inf_list müssen Listen sein"
    
    gang = student.get("studiengang")
    vorname = student.get('vorname')
    if gang == "EI":
        et_liste.append(student)
    elif gang == "INF":
        inf_liste.append(student)
    else:
        print(f'Studiengang von {vorname} nicht bekannt – wird übergangen')

def drucke_liste(liste, titel):
    print(f"\nStudierende in {titel}:")
    for s in liste:
        assert "vorname" in s and "name" in s, "Studentendaten unvollständig"
        print(f"- {s['vorname']} {s['name']}")

def main():
    # Liste aller Studierenden
    students = [
        erstelle_student("Steph", "Curry", 21, 12345, "EI"),
        {"vorname": "Lukas", "name": "Zimmer", "matrikelnummer": 12349, "studiengang": "INF"},  # kein Alter
        erstelle_student("Lea", "Schüller", "17", 12348, "EI"),
        erstelle_student("Lionel", "Vitinha", 20, 12347, "BWL"),
        erstelle_student("Vito", "AlPacino", "17", 12348, "INF"),
        erstelle_student("Paolo", "Maldini", 45, 12347, "ET")        
    ]

    assert isinstance(students, list), "students muss eine Liste sein"
    for s in students:
        assert isinstance(s, dict), "Jedes Element in students muss ein Dictionary sein"

    et_list = []
    inf_list = []

    for student in students:
        fuege_zu_studiengang_liste_hinzu(student, et_list, inf_list)

        if ist_minderjaehrig(student):
            assert "vorname" in student, "Student ohne Vornamen in Minderjährigenprüfung"
            print(f"{student['vorname']} ist minderjährig.")

    drucke_liste(et_list, "ET")
    drucke_liste(inf_list, "INF")

if __name__ == "__main__":
    main()
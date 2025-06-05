
def erstelle_studentin(vorname, name, alter, matrikelnummer, studiengang):
    return {
        "vorname": vorname,
        "name": name,
        "alter": alter,
        "matrikelnummer": matrikelnummer,
        "studiengang": studiengang
    }

def ist_minderjaehrig(student):
    alter = student.get("alter", None)
    return alter < 18
    
def fuege_zu_studiengang_liste_hinzu(student, et_liste, inf_liste):
    gang = student.get("studiengang")
    if gang == "EI":
        et_liste.append(student)
    elif gang == "INF":
        inf_liste.append(student)
    
    
def drucke_liste(liste, titel):
    print(f"\n Studierende in {titel}:")
    for s in liste:
        print(f"- {s['vorname']} {s['name']}")

def main():
    # Liste aller Studierenden
    students = [
        erstelle_studentin("Caitlin", "Clark", 21, 12345, "EI"),
        {"vorname": "Lukas", "name": "Zimmer", "matrikelnummer": 12349, "studiengang": "INF"},  # kein Alter
        erstelle_studentin("Lea", "Schüller", "17", 12348, "EI"),
        erstelle_studentin("Lionel", "Vitinha", 20, 12347, "BWL"),
        erstelle_studentin("Vito", "AlPacino", "17", 12348, "INF"),
        erstelle_studentin("Paolo", "Maldini", 45, 12347, "ET")        
    ]

    et_list = []
    inf_list = []
    
    for student in students:
        fuege_zu_studiengang_liste_hinzu(student, et_list, inf_list)
        
        if ist_minderjaehrig(student):
            print(f"{student['vorname']} ist minderjährig.")

    drucke_liste(et_list, "ET")
    drucke_liste(inf_list, "INF")
    

if __name__ == "__main__":
    # Code to run when the script is executed directly
    main()
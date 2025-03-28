#!/usr/bin/env python
# coding: utf-8

# # Einführung in Python – Übungen

# ## jupyter formatierung

# In[ ]:


'''
# H1 (Größte Überschrift)
## H2
### H3
#### H4

**Fetter Text**  
*Kursiver Text*  
`Inline-Code`

Unsortierte Liste:
- Punkt 1
- Punkt 2
Sortierte Liste:
1. Erster Punkt
2. Zweiter Punkt


Tabelle
| Spalte 1 | Spalte 2 |
|----------|----------|
| Wert 1   | Wert 2   |
6. Zeilenumbrüche
Zeile 1  
Zeile 2  (mit zwei Leerzeichen am Ende)
'''


# ## Jupyter Shortcuts
# **Moduswechsel**
# - Esc : Wechsel in den Befehlsmodus  
# - Enter : Wechsel in den Editiermodus
#     
# **Zellennavigation & Bearbeitung**  
# - A : Neue Zelle oberhalb einfügen (Befehlsmodus)  
# - B : Neue Zelle unterhalb einfügen (Befehlsmodus)  
# - D, D (zweimal D drücken) : Zelle löschen (Befehlsmodus)  
# - Shift + Enter : Zelle ausführen und zur nächsten springen
# - Ctrl + Enter : Zelle ausführen, aber im selben Feld bleiben
# - Alt + Enter : Zelle ausführen und neue darunter erstellen
#  
# **Zellentypen ändern**
# - M : Zelle in Markdown umwandeln (für Text & Formatierung)
# - Y : Zelle in Code umwandeln
# - Zellen verschieben
# - Shift + Up/Down : Mehrere Zellen markieren
# - Esc + Up/Down : Zwischen Zellen wechseln
# - Shift + M : Markierte Zellen zusammenführen
# - Ctrl + S : Speichern
# - H : Shortcut-Hilfe anzeigen

# # Basic Navigation Commands in der Kommandozeile
# **navigation**
# - cd path\to\directory        # Change Directory
# - dir                         # List contents of the current directory
# - cd ..                       # Move up one directory level
# - cd \                        # Move to the root directory
# 
# **File Management Commands**
# - copy source_file destination_file  # Copy files
# - move source_file destination_file  # Move files
# - del filename                       # Delete files
# - ren old_filename new_filename      # Rename files
# 
# **Directory Management Commands**
# - mkdir new_directory                # Create a new directory
# - rmdir directory_name               # Remove an empty directory
# - rmdir /s directory_name            # Remove a directory and all its contents
# 
# **Other Useful Commands**
# - cls                         # Clear the Command Prompt screen
# - echo message                # Display messages or turn command echoing on or off
# - type filename               # Display the contents of a text file
# - help                        # Display a list of available commands and their descriptions
# 
# **Run a program**
# - navigate to the program (cd...)
# - program.exe
# 

# ### Git + Gitlab/Github
# 
# Verwaltung von Repos, Sharing von Code, Versionsverwaltung Code
# 
# - Installation git über Gui
# - repository erstellen -> github
# - repository initial lokal kopieren (clon) -> 
#     - zum Ordner navigieren, in dem das Repo erstellt werden soll
#     - git clone URL (URL bekommt man von github)
# - Änderungen hinzufügen: git add . (alle Änderungen im Ordner)
# - Änderungen sichern
#     - git commit -m "Beschreibung"
# - Änderungen auf Github hochladen -> push
#     - git push origin [branchname]
# - Änderungen von Github herunterladen/synchronisieren
#     - pull
# 
# 

# **Aufgabe git**
# - Erstellen Sie ein Repository
# - Clonen Sie das Repository in einen lokalen Ordner
# - Ändern Sie lokal etwas
# - Committen und pushen Sie die lokalen Änderungen auf github (bzw. System Ihrer Wahl)

# ##Pandas
# Tool zur Datenanalyse und -Manipulation
# 
# **Series**: 1-dimensionales Array mit Label (wie eine Excelspalte)
# 
# **DataFrame**: 
# - 2-dimensionale Datenstruktur, ähnlich einer Exceltabelle
# - Spalten sind einzelne Series (DataFrame mit einer spalte ist tatsächlich automatisch eine Series)
# - index wird automatisch assigned, kann aber verändert werden
# - df.columns -> liefert Spaltennamen
# - df.rename(columns='alterName1':'neuerName1','alterName2','neuerName2') -> Umbenennung von Spaltennamen
# - len(df) -> liefert Länge eines DataFrames, sprich number of rows
# - df.shape([1]) -> liefert Spaltenanzahl
# - df.info() -> basic Infos
# - df.describe() -> liefert einfache statische Kennwerte für einen DataFrame df
# 
# **Slicing eines DataFrames**
# - mit df['spalte'] wird auf eine einzelne Spalte zugegriffen
# - mit df

# In[ ]:


# Aufgabe: Erstellen Sie eine Series aus einer Liste und printen Sie


# **Aufgabe: Erstellen Sie verschiedene DFs**
# 
# - DataFrames können aus dictionaries, lists of dictionaries, list of lists, numpyArrays erzeugt werden
# - erstellen S/ie auf Basis der gezeigten Möglichkeinen einen DataFrame und benennen Sie die Spalten des Dataframe. Anschließend printen Sie den DF

# In[ ]:


# dict -> keys sind Spaltennamen, Values sind Spaltenwerte
# Tabelle mit Personen mit Alter und Wohnort


# In[ ]:


# list of dicts


# In[ ]:


# list of lists -> [ [],[],]



# In[ ]:


# from numpy array -> numpy array ist schneller als z.B. list -> numpy core in C
# dt=np.array([[],[]])


# In[ ]:


# from another df -> teil eines DF zu neuem DF machen



# **Slicing eines DataFrames mit loc und iloc**
# - mit df['spalte'] wird auf eine einzelne Spalte zugegriffen
# - mit loc bzw. iloc wird genauer auf einzelne Elemente oder eine Range von Elementen zugegriffen
# 
# **loc-based indexing**
# - nutzt label, sprich Zeilen- oder Spaltennamen
# - df.loc['a'] -> wenn nur 1 index gegeben, wird auf zeile (=index) zugegriffen
# - df.loc[1,'name'] -> es wird auf Zeile + Spalte zugegriffen
# - df.loc[:,'name'] -> range, aber in dem Fall alle Zeilen
# - df.loc[0:2,'name'] -> auf die Zeilen 0, 1,2 und die Spalte *name* wird zugegriffen 
# 
# **iloc-based indexing**
# - nutzt integer-Position zur Auswahl von Daten (wie beim Zugriff auf Java-Array, listenelement...)
# - df.iloc[1] -> wählt 2. Zeile
# - df.iloc[[1,3]] -> wählt 2. und 4. Zeile
# - df.iloc[:,1] -> wählt alle Zeilen der 2. Spalte
# - df.iloc[0:2,2] -> wählt 1. u 2. Zeile der 3. spalte

# **Aufgabe - loc**
# - Greifen Sie auf eine Zeile zu
# - Greifen Sie auf eine spalte zu 
# - Greifen Sie auf das element in der ersten Spalte in einer spezifischen Spalte zu
# 

# In[ ]:


# slicing mit loc



# **Aufgabe - iloc**
# - Greifen Sie auf eine Zeile zu
# - Greifen Sie auf eine spalte zu 
# - Greifen Sie auf das element in der ersten Spalte in einer spezifischen Spalte zu

# In[ ]:


# iloc


# In[ ]:





# **Erstellen von dataFrames aus csv**
# - mit pd.read_csv bzw. pd.read_excel werden Daten aus Textdateien geparsed (anstatt diese line by line zu parsen)
# - über sep, encoding und decimals wird hierbei festgelegt, wie mit der Textdatei umgegangen wird
# -------------------
# 
# **Aufgabe - lesen und schreiben von csv**
# 
# Lesen Sie die csvs "load_data.csv" & "ninja_pv.csv" ein und printen Sie jeweils die ersten drei Zeilen

# In[ ]:


# Auslesen von Daten aus einer csv
import pandas as pd
import os


# **Schreiben von Textdateien**
# - mit pd.to_csv() bzw. pd.to_excel können auch Dateien erstellt werden
#     - df.to_csv(path, sep=",",header=True,index=True, decimal=".") (enthält noch mehr Optionen)
#     - df.to_excel(excel_writer, *, sheet_name='Sheet1', columns=None, header=True, index=True, startrow=0, startcol=0, engine=None) (enthält noch mehr Optionen)
# - Gleiches gilt für das Schreiben in Datenbanken oder json-Files--> to_sql()
#     - df.to_sql(name, con, schema=None, if_exists={'fail','replace','append'}, index=True, index_label=None)
#     - pd.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None)
#     - Bsp.:df=pd.read_sql('SELECT * FROM testDB, conn)
# 
# -----
# **Aufgabe - Schreiben von csvs**
# Schreiben Sie die erzeugten Dateien in Excel und csv-Format

# In[ ]:





# In[ ]:


import sqlite3
import pandas as pd
import os
os.getcwd()



# ### Pandas - Analyse einer PV-Zeitreihe
# 
# - importieren Sie die Zeitreihe load_data.csv (moodle) mit der panda function read_csv()
# - achten Sie auf den Separator (z.B. semicolon, comma)
# - die Zeitreihe zeigt die Stromnachfrage einer Familie
# - löschen Sie alle Spalten bis auf hour_of_the_year und P_el raus
# - merge/join die Zeitreihe mit der Excel yearly_structure_2019.xlsx (Schlüssel für join ist die spalte "hour_of_the_year")
# - schauen Sie sich die Daten an
# - laden Sie eine Zeitreihe für eine PV-Anlage von der Seite https://www.renewables.ninja/ herunter, wählen Sie einen Ort Ihrer Wahl (alle anderen Parameter können beliebig verändert werden)
#     - import in python über read_csv()
#     - fügen Sie die Spalte hour_of_the_year aus dem dataframe yearly_structure_2019 hinzu (Länge sollte identich sein)
#     - mergen Sie den dataFrame ninja_pv mit load_data
#     - Erstellen Sie dieselbe Auswertung für die PV-Daten wie bereits oben für die Lastdaten
# 
# - Machen Sie eine statistische Auswertung der Daten in der Spalte total: 
#     - Was ist das Maximum und Minimum, was ist der Durchschnitt?
#     - was ist das Minimum/Maximum/Avg pro Woche?
#     - Was ist der Durchschnitt über das Jahr für jede Stunde des Tages?
# - erstellen Sie einen einfachen Plot deiner Wahl mit matplotlib
# 

# In[ ]:


# Auslesen von Daten aus einer csv
import pandas as pd
import os



# In[ ]:


#einlesen aus excel


# Zusammenführen von dataFrames über joins
# 
# dt=pd.merge(dt1,dt2,left_on, right_on) -> mit welchem gemeinsamen Schlüssel wird ein join durchgeführt?

# In[ ]:





# **Aufgabe - Gruppieren und einfache statistische Berechnungen durchführen, anschließend in eine Excel schreiben und einen einfachen Plot erstellen**
# - groupby bedeutet: es wird nach einer Kategorie bzw. Spalte gruppiert, alle Zeilen, bei denen der Wert in der Spalte gleich ist (z.B. jede 1. Stunde des Tages) werden zusammengenommen
# - mit agg() können dann direkt Rechenoperationen ausgeführt werden
# - dt1=dt2.groupby(['Spalte xy']).agg({'Spalte z':['min','mean','max','std','sum']}) 
# 
# Anschließend können die Daten geplottet werden
# - einfacher Plot geht bereits in pandas: Spalte.plot() (hierbei wird die Spalte nach Y und der Index nach x geplottet)
# 

# In[ ]:


# groupby -> Es wird nach der Stunde des Tages gruppiert
# agg -> es werden bestimmte Spalten aggregiert, hier die Spalte P_el, für die verschiedene Operationen ausgeführt werden
# anschließend muss man den DF-index bearbeiten -> von 2-line zu oneline


# **Aufgabe - individualisierter Plot - Ergebniszeitreihen plotten**
# 
# beim Plot mit pyplot werden die verwendeten Zeitreihen (P_el_mean (Stromverbrauch) und pv_mean (PV-Erzeugung)) nacheinander in einen Plot geladen und aufeinander gesetzt
# Anschließend werden Achsen beschriftet etc.
# - fig,ax=plt.subplots()
# - df.plot(y="",ax=ax,label='label1') -> der plot wird auf die Achsen des subplots gezeichnet
# - ax.set_xlabel('') bzw. ax.set_ylabel('') definieren Achsenbeschriftungen
# - ax.set_title('') für den Plottitel
# - plt.savefig('name',format='')
# - plt.show() -> sucht nach aktiven Figurenobjekten und öffnet ein Fenster, in dem diese angezeigt werden

# In[ ]:


import matplotlib.pyplot as plt
fig,ax=plt.subplots()


# ## Ende

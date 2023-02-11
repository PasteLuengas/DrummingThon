import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load sound files
Kick = pygame.mixer.Sound("Kick.wav")
Snare = pygame.mixer.Sound("Snare.wav")
Ride1 = pygame.mixer.Sound("Ride1.wav")
Ride1 = pygame.mixer.Sound("Ride2.wav")
HiHat = pygame.mixer.Sound("HiHat.wav")
Tom = pygame.mixer.Sound("Tom.wav")

# Define the pattern as arrays for each instrument
kick_pattern = [0, 0, 0, 0]
Snare_pattern = [0, 0, 0, 0]
Ride1_pattern = [0, 0, 0, 0]
Ride2_pattern = [0, 0, 0, 0]
HiHat_pattern = [0, 0, 0, 0]
Tom_pattern = [0, 0, 0, 0]

playing = False

# Define the tempo (in BPM)
tempo = 120

# Calculate the time for each step (in milliseconds)
step_time = 60000 / tempo

# Define la funcion para play
def play(self, ping=None):
    global playing

    if not playing:
        playing = True
    else:
        playing = False

    while playing:
        for i in range(len(kick_pattern)):
            try:    
                if kick_pattern[i] == 1:
                    Kick.play()
            except:
                pass

            try:
                if Snare_pattern[i] == 1:
                    Snare.play()
            except:
                pass
            
            try:
                if Ride1_pattern[i] == 1:
                    Snare.play()
            except:
                pass
            try:
                if Ride2_pattern[i] == 1:
                    Snare.play()
            except:
                pass
            try:
                if HiHat_pattern[i] == 1:
                    HiHat.play()
            except:
                pass
            try:
                if Tom_pattern[i] == 1:
                    Tom.play()
            except:
                pass
            pygame.time.wait(int(step_time))
            
            if playing == False:
                break
#    pygame.time.wait(int(step_time * len(kick_pattern)))


lineNumbers = 4

# ------------------- Bienvenidos al infierno -------------------------------#

import flet as ft

def main(page: ft.Page):
    global step_time

    def changeBPM(self):
        global tempo
        tempo = int(bpm_number.value)
        print(str(tempo))
        step_time = 60000 / tempo

    def remove_line(self):
        
        #DrumTable.rows.pop()
        #page.update()
        #for row in DrumTable.rows:
        #    row.cells.pop()
        #    page.update()

        #    """
        #    for cell in row.cells:
        #        print(cell)
        #        
        #        page.update()
        #       #row.cells.pop()
        #        #page.update()
        #    """
        DrumTable.columns.pop()

        DrumTable.rows[0].cells.pop()
        kick_pattern.pop()

        DrumTable.rows[1].cells.pop()
        Snare_pattern.pop()

        DrumTable.rows[2].cells.pop()
        Ride1_pattern.pop()

        DrumTable.rows[3].cells.pop()
        Ride2_pattern.pop()

        DrumTable.rows[4].cells.pop()
        HiHat_pattern.pop()

        DrumTable.rows[5].cells.pop()
        Ride1_pattern.pop()

        page.update()


    bpm_number = ft.TextField(value=tempo, text_align=ft.TextAlign.RIGHT, width=100, on_change=changeBPM)

    def checkbox_changed(pattern, val, e):
        #var[val] = str(int(e.value))
        #print(str(var))
        #checkbox = e.sender
        #print(str(checkbox.value))
        pattern[val] = int(e)
        print(pattern)

    #----- Aqui se pone la table 
    DrumTable = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Kick")),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(kick_pattern, 0, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(kick_pattern, 1, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(kick_pattern, 2, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(kick_pattern, 3, e.control.value))),

                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Snare")),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Snare_pattern, 0, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Snare_pattern, 1, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Snare_pattern, 2, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Snare_pattern, 3, e.control.value))),

                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Ride 1")),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Ride1_pattern, 0, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Ride1_pattern, 1, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Ride1_pattern, 2, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Ride1_pattern, 3, e.control.value))),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Ride 2")),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Ride2_pattern, 0, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Ride2_pattern, 1, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Ride2_pattern, 2, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Ride2_pattern, 3, e.control.value))),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("HiHat")),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(HiHat_pattern, 0, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(HiHat_pattern, 1, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(HiHat_pattern, 2, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(HiHat_pattern, 3, e.control.value))),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Tom")),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Tom_pattern, 0, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Tom_pattern, 1, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Tom_pattern, 2, e.control.value))),
                        ft.DataCell(ft.Checkbox(value=False, on_change=lambda e: checkbox_changed(Tom_pattern, 3, e.control.value))),
                    ],
                ),
            ],
        )


    page.add(

        DrumTable,

        # Contador de BPM
       ft.Row(
            [
                ft.Text("BPM", style=ft.TextThemeStyle.LABEL_LARGE),
                bpm_number
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        # TABLA INFERNAL


        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=remove_line),
                #ft.IconButton(ft.icons.ADD, on_click=add_line),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ), 

        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=play, bgcolor=ft.colors.BLUE_300),

        



    )


ft.app(target=main)



#-------------------- gracias por su estadia en el infierno ------------------#

# Play the pattern


# Wait for the pattern to finish playing

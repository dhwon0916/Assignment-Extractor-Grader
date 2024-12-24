#Microsoft Teams Assignment Extractor by @dhwon0916
import pip
try:
    import PySimpleGUI as sg
except:
    pip.main(["install", "--user", "PySimpleGUI"])
    import PySimpleGUI as sg
import os
import shutil
import PySimpleGUI as sg
import tkinter as tk
while True:
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.withdraw()
    sg.theme('LightGreen')
    mainlayout = [
        [sg.Text('      Teams Extractor      ', font=('Arial', 30), justification='center', expand_x=True, pad=(None, 10))],
        [sg.Frame('', [[sg.Text('Import:', font=('Arial', 10, 'bold'))], [sg.Text('', expand_x=True, background_color='White', border_width=3, key='texta'), sg.Button('  SET  ', font=('Arial', 10, 'bold'), key='buttona')],
                    [sg.Frame('', [[]], border_width=0)], [sg.Text('Assignment:', font=('Arial', 10, 'bold'))], [sg.Text('', expand_x=True, background_color='White', border_width=3, key='textb'), sg.Button('  SET  ', font=('Arial', 10, 'bold'), key='buttonb')],
                    [sg.Frame('', [[]], border_width=0)], [sg.Text('Export:', font=('Arial', 10, 'bold'))], [sg.Text('', expand_x=True, background_color='White', border_width=3, key='textc'), sg.Button('  SET  ', font=('Arial', 10, 'bold'), key='buttonc')],
                    [sg.Checkbox('Export to individual folder', font=('Arial', 9), key='check', default=False)],
                    [sg.Frame('', [[]], border_width=0)], [sg.Frame('', [[]], expand_x=True, border_width=0), sg.Button('Extract', font=('Arial', 15, 'bold'), expand_x=True, pad=(10, 10)), sg.Frame('', [[]], expand_x=True, border_width=0)]
                    ], expand_x=True, expand_y=True, pad=(10, 10), border_width=0)]
    ]
    window = sg.Window('Teams Extractor', mainlayout)
    importpath = ''
    assignmentname = ''
    exportpath = ''
    version = 0
    folderdir = ''
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            quit()
        elif event == 'buttona':
            importpath = sg.popup_get_folder('Import Folder', no_window=True, keep_on_top=True, font=('Arial', 10, 'bold'))
            window['texta'].update(importpath)
        elif event == 'buttonb':
            assignmentname = sg.popup_get_folder('Assignment Folder', no_window=True, keep_on_top=True, font=('Arial', 10, 'bold'))
            assignmentname = assignmentname.split('/')[-1]
            window['textb'].update(assignmentname)
        elif event == 'buttonc':
            exportpath = sg.popup_get_folder('Export Folder', no_window=True, keep_on_top=True, font=('Arial', 10, 'bold'))
            window['textc'].update(exportpath)
        elif event == 'Extract':
            if importpath == '' or assignmentname == '' or exportpath == '':
                sg.popup_timed('Please fill in all the fields', font=('Arial', 10, 'bold'), auto_close_duration=1.5)
            else:
                exportpath = os.path.join(exportpath, assignmentname)
                if os.path.exists(exportpath):
                    if os.path.exists(exportpath + ' (1)'):
                        counter = 1
                        while os.path.exists(exportpath + ' (' + str(counter) + ')'):
                            counter += 1
                        exportpath = exportpath + ' (' + str(counter) + ')'
                    else:
                        exportpath = exportpath + ' (1)'
                else:
                    pass
                os.mkdir(exportpath)
                if window['check'].get() == True:
                    studentnames = os.listdir(importpath)
                    for i in studentnames:
                        subexportpath = os.path.join(exportpath, i)
                        os.mkdir(subexportpath)
                        for ii in os.listdir(os.path.join(importpath, i)):
                            if ii == assignmentname:
                                version = 0
                                for iii in os.listdir(os.path.join(importpath, i, ii)):
                                    if os.path.isdir(os.path.join(importpath, i, ii, iii)):
                                        if version < int(iii[-1]):
                                            version = int(iii[-1])
                                            versionfolder = iii
                                    else:
                                        shutil.copy(os.path.join(importpath, i, ii, iii), subexportpath)
                                if version != 0:
                                    for iiii in os.listdir(os.path.join(importpath, i, ii, versionfolder)):
                                        shutil.copy(os.path.join(importpath, i, ii, versionfolder, iiii), subexportpath)
                else:
                    studentnames = os.listdir(importpath)
                    for i in studentnames:
                        for ii in os.listdir(os.path.join(importpath, i)):
                            if ii == assignmentname:
                                version = 0
                                for iii in os.listdir(os.path.join(importpath, i, ii)):
                                    if os.path.isdir(os.path.join(importpath, i, ii, iii)):
                                        if version < int(iii[-1]):
                                            version = int(iii[-1])
                                            versionfolder = iii
                                    else:
                                        filetype = os.path.splitext(os.path.join(importpath, i, ii, iii))[1]
                                        filename = iii + " - " + i
                                        filepath = os.path.join(exportpath, filename + filetype)

                                        shutil.copy(os.path.join(importpath, i, ii, iii), filepath)
                                if version != 0:
                                    for iiii in os.listdir(os.path.join(importpath, i, ii, versionfolder)):
                                        filetype = os.path.splitext(os.path.join(importpath, i, ii, versionfolder, iiii))[1]
                                        filename = iiii + " - " + i
                                        filepath = os.path.join(exportpath, filename + filetype)
                                        if os.path.exists(filepath):
                                            if os.path.exists(os.path.join(exportpath, filename + ' (1)' + filetype)):
                                                counter = 1
                                                while os.path.exists(os.path.join(exportpath, filename + ' (' + str(counter) + ')' + filetype)):
                                                    counter += 1
                                                filepath = os.path.join(exportpath, filename + ' (' + str(counter) + ')' + filetype)
                                            else:
                                                filepath = os.path.join(exportpath, filename + ' (1)' + filetype)
                                        else:
                                            filepath = os.path.join(exportpath, filename + filetype)
                                        shutil.copy(os.path.join(importpath, i, ii, versionfolder, iiii), filepath)
                sg.popup('Extraction Complete!', font=('Arial', 10, 'bold'))
                window.close()
                break
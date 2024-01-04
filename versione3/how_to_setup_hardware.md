# SETUP NEW HARDWARE

## STEP1 ( Configurazione librerie )

1. scrivere "python3" nella powershell e scaricare python dallo store
2. pip3 install -r requirements.txt       ( scarichi le librerie )
3. pip install --upgrade pillow  


## STEP2 ( Setting Visual Studio Code )

1. Eseguire uno screenshot avendo l'app vodafone aperta in fullscreen usando **/Tools/screen_help.py** (scelta=1)

2. Una volta che si ha il fullScreen dell'app aperta, lo si sposta nel desktop.

3. Una volta spostata nel desktop. Si avvia il programma **/Tools/screen_help.py** (scelta=2) e si apre l'immagine precedentemente fatta
in fullscreen.

4. Ora cambiando i parametri di **set_grill (x,y) e square_side**, generare l'immagine **output.png**

5. Aiutandoti con paint analizza l'immagine **output.png** e dovresti fare in modo di avere un puntino nello stesso punto per ogni item.

6. Dare in input a **Package/analyseBot.py** l'immagine **output.png** che ci sembra quella settata con la migliore griglia.



## STEP3 ( Setting Bluestacks )

1. Vai in impostazioni e togli CTRL+M sui **shortcut**
2. Importa le Macro
3. Cambia le 3 Macro finali ( Alt+5  , Alt+6 , Alt+7)


## STEP-Extra

### Nel caso si volesse usare un ambiente virtuale ecco come settarlo

1. pip3 install virtualenv
2. python3 -m venv __/path/to/new/virtual/environment__
3. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
4. .\Scripts\activate       ( attivazione ambiente virtuale)
5. pip3 install -r requirements.txt     (scarichi le librerie)
6. pip3 freeze > requirements.txt  ( nel caso vuoi salvare le librerie )
7. .\Script\deactivate   ( disattivazione ambiente virtuale)



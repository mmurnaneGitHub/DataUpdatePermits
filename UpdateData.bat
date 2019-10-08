:: *****************************************************************************
:: UpdateData.bat  1/28/2019 
:: Summary: Tacoma Permits Data Update
::
:: Description: Update json data used for the Tacoma Permits App 
::    		@ https://wspdsmap.cityoftacoma.org/website/PDS/Permits
::   
:: Scheduled Task: Every day @ 8:30 am (CivicData updated @ 8:16 am)
::
:: Path: \\Geobase-win\CED\GADS\R2018\R110\UpdateData\UpdateData.bat
:: *****************************************************************************

:: Set log directory for process verification file
    SET LogDir=\\Geobase-win\CED\GADS\R2018\R110\UpdateData\log\LandUse

:: Set variable %theDate% to today's date (YYYYMMDD)
    for /f "tokens=2,3,4 delims=/ " %%a in ('date/t') do set theDate=%%c%%a%%b

:: Record starting time
    time /T > %LogDir%%theDate%.log

Echo Archiving current data ... >> %LogDir%%theDate%.log
    COPY \\wsitd01\c$\GADS\website\PDS\Permits\data\Permits.json \\wsitd01\c$\GADS\website\PDS\Permits\data\_archive\Permits_%theDate%.json

Echo Downloading data ... >> %LogDir%%theDate%.log
 ::Send standard output (1) & errors (2) to log file
    C:\Python27\ArcGISx6410.4\python.exe \\Geobase-win\CED\GADS\R2018\R110\UpdateData\Data_Download.py 1>>%LogDir%%theDate%.log 2>&1

:: Record ending time
    time /T >> %LogDir%%theDate%.log

Echo  See Tacoma Permits for latest data - https://wspdsmap.cityoftacoma.org/website/PDS/Permits >> %LogDir%%theDate%.log

::Send Email with log file content
cscript \\geobase-win\ced\GADS\R2018\R110\UpdateData\Send_Email.vbs %LogDir%%theDate%.log

::For manual testing -
::pause
 

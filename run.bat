@echo off

if "%1"=="" goto BLANK

cd lib

call python install.py %1

cd ..

goto DONE

:BLANK
    echo "Missing Parameter!"
    echo "usage:"
    echo "  $run.bat <Skyrim_Directory>"
    echo "NOTE: <Skyrim_Directory> must be a path to the root directory of your Skyrim installation."
    
:DONE
@echo on
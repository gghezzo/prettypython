# This is the packager for the Race Game 
# From http://pythonprogramming.net/converting-pygame-executable-cx_freeze/?completed=/pygame-button-function-events/
# Typer: Ginny C Ghezzo 
# What I learned: This seems stupid to me. I just want an .exe 
import cx_Freeze 
executables = [cx_Freeze.Executable("MyGame.py")]
cx_Freeze.setup(
	name="A bit Racey", 
	options={"build_exe": {"packages":["pygame"], "include_files":["racecar.png"]}}, 
	executables = executables
	)



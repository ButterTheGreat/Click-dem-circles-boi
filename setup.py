import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="Click dem circles boi",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["circle.png","background.png"]}},
    executables = executables

    )

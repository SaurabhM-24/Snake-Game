import cx_Freeze

executables = [cx_Freeze.Executable('snake game.py')]

cx_Freeze.setup(
    name = 'Snake Game',
    options = {'build_exe':{'packages':['pygame'],'include_files':['apple.png','snakehead.png']}},
    description = 'Snake Game Practice',
    executables = executables
    )

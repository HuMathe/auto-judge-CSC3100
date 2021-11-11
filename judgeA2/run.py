import os
import platform

is_win = 'windows' in platform.system().lower()
if is_win:
	cmd.append['python']
else:
	cmd.append['python3']
cmd.append[stop_watch]
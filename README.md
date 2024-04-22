* Namecaller

Example python package to showcase installing pyhton cli packages directly from a git repo
* Prerisequites:
    * Python for windows 3.10 or higher
    * Windows Powershell

* Install or update from windows powershell)
```
PS> py -m pip install git+https://github.com/coderwessel/clishit.git
```
* installs the namecall2 cli tool
```
PS> namecall2 --name wessel
 _   _        _  _                                             _  _  _  _
| | | |  ___ | || |  ___      __      __  ___  ___  ___   ___ | || || || |
| |_| | / _ \| || | / _ \     \ \ /\ / / / _ \/ __|/ __| / _ \| || || || |
|  _  ||  __/| || || (_) | _   \ V  V / |  __/\__ \\__ \|  __/| ||_||_||_|
|_| |_| \___||_||_| \___/ ( )   \_/\_/   \___||___/|___/ \___||_|(_)(_)(_)
```
* Usage
```
namecall2 --help
Usage: namecall2 [OPTIONS]

Options:
  --name TEXT  The person to greet.
  --help       Show this message and exit.
```

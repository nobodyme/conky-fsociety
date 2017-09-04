<div align="center">

# Conky-fsociety

[Conky](https://wiki.archlinux.org/index.php/conky)(a light weight system monitoring tool) for desktop

<img src="https://github.com/nobodyme/conky-fsociety/blob/reddit-addition/screenshot-desktop.png">

Tested on cinnamon

</div>

### Install

  - First install conky following the reference guide below or from the [link here](https://www.shellhacks.com/install-configure-conky-linux-mint-ubuntu-debian/) and check if the default conky works for you.
  - Then clone the repository: `git clone https://github.com/nobodyme/conky-fsociety.git`
  - cd into the directory: `cd conky-fsociety`
  - Run the install script with: `./install.sh`.This should place the necessary files under `~/.conky/conky-fsociety/`
  
### Run
	
To run the conky: `conky -c ~/.conky/conky-fsociety/fsocietyrc`

Note: Although your conky will persist even if you close the terminal, it wouldn't be present on reboot, see [how to set up conky to run at startup](https://www.shellhacks.com/install-configure-conky-linux-mint-ubuntu-debian/) at the end of that page.

### Remove 

To remove the conky from desktop: `pkill conky`
  
### Uninstall

 - cd into the repository, if you're not
 - Run the uninstall script: `./uninstall.sh`.This should remove the `~/.conky/` directory.

### Other references
[Conky-Wiki-github](https://github.com/brndnmtthws/conky/wiki)

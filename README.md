# conky-fsociety
<div align="center">

[Conky](https://wiki.archlinux.org/index.php/conky)(a light weight system monitoring tool) for desktop

<img src="https://github.com/nobodyme/conky-fsociety/blob/master/screenshot-desktop.png">

</div>

### Install and run

  - First install conky following the reference guide below or from the [link here](https://www.shellhacks.com/install-configure-conky-linux-mint-ubuntu-debian/) and check if the default conky works for you.
  - Then clone the repository: `https://github.com/nobodyme/conky-fsociety.git`
  - cd into the directory: `cd conky-fsociety`
  - Run the install script with: `./install.sh`.This should place the necessary files under `~/.conky/conky-fsociety/` and run the conky.
  - Now although your conky will persist even if you close the terminal, it wouldn't be present on reboot, see [how to set up conky to run at startup](https://www.shellhacks.com/install-configure-conky-linux-mint-ubuntu-debian/) at the end of that page.
  
### Uninstallation

 - cd into the repository, if you're not
 - Run the uninstall script: `./uninstall.sh`.This should remove the `~/.conky/` directory.

### References
[Conky-Wiki](https://github.com/brndnmtthws/conky)

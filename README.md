# All about OSCP
*All the files listed below, and mentioned in any checklists are within this repo*

----

#### Custom checklists

- Linux privilege escalation
- Windows privilege escalation
- Windows post exploitation
- Windows 32 bit stack buffer overflow

#### Windows 32 bit stack buffer overflow

*Example scripts that are highly and easily customizable*

- Skeleton script
- Fuzzer
- Overflow EIP
- Sending unique pattern
- Sending bad characters
- Full script

#### Windows post exploitation
- Credential gathering
  - Compiled Mimikatz32.exe
  - Compiled Mimikatz64.exe
- Privilege escalation
  - Sherlock.ps1
  - Powerup.ps1
  - Priv checker (.exe/.py)
  - Compiled nc/nc64
  - [Compiled Windows kernel exploits](https://github.com/SecWiki/windows-kernel-exploits) < not my files, but link to repo with all compiled windows kernel exploits
- Cheatsheets
1. http://www.handgrep.se/repository/cheatsheets/postexploitation/WindowsPost-Exploitation.pdf
2. https://www.fuzzysecurity.com/tutorials/16.html
3. http://www.exumbraops.com/penetration-testing-102-windows-privilege-escalation-cheatsheet
4. https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md
5. https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/
  

#### Linux post exploitation
- Information gathering
  - Linenum.sh
  - linuxprivchecker.py
  - unix-priv-checker.sh
- Credential gathering
  - credential harvester

#### Stupid one liners that saved me some time

- Automate LinEnum.sh: download > chmod > run > output to file

```
wget https://raw.githubusercontent.com/Arken2/Everything-OSCP/master/Linux%20Post%20exploitation/LinEnum.sh ; chmod +x LinEnum.sh ; ./LinEnum.sh > LinEnum-Output.txt
```

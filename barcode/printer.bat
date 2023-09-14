sc stop spooler
sc start spooler
sc stop sysmain
sc config sysmain start= disabled
sc stop wuauserv
sc config wuauserv start= disabled
wmic pagefileset delete
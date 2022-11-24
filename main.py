import os
import time
import colorama
from colorama import Fore as fg

terminalOn = True

terminalLock = False

historyLock = False

historyList = []

#sysVars[0] are names
#sysVars[1] are values
sysVars = [[],[]]
#for fetching variables do sysVars.index(var you want to fetch) 

myFile = None

name = None

CYAN = fg.LIGHTCYAN_EX
WHITE = fg.LIGHTWHITE_EX
GREEN = fg.LIGHTGREEN_EX
RED = fg.RED
YELLOW = fg.LIGHTYELLOW_EX

def startUp():
  print("       __    _   _____   __   ___    __    ___")
  print("  / / |__|  /_\    |    /    /   \  |  \  |  ")
  print(" / /  |\   |   |   |   |    |     | |   | |-- ")
  print("/ /   | \  |   |   |    \__  \___/  |__/  |___   ")
  print("By: Rat")
  time.sleep(2)
  os.system('clear')

def name():
  global name
  name = input(WHITE + "<system:> \"what is your name?\": ")
  
startUp()
name()

def command():
  global name
  cmd = input(WHITE + "<"+ name +":> ")
  if cmd[0:5] == "echo ":
    echo(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:5] == "clear":
    clear(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:4] == "help":
    help(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:7] == "history":
    history(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:6] == "rename":
    rename(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:3] == "var":
    var(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:3] == "set":
    set(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:5] == "echov":
    echov(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:4] == "lock":
    lock(cmd)
    writeToHistory(cmd)
    return
  if cmd[0:7] == "request":
    request(cmd)
    writeToHistory(cmd)
    return
  else:
    print(RED + cmd + " is not a recognized command")

def echo(a):
  print(GREEN + a[5:])

def var(a):
  equPos = a.find('=')
  beforeEqu = equPos - 1
  afterEqu = equPos + 2
  sysVars[0].append(a[4:beforeEqu])
  sysVars[1].append(a[afterEqu:])
  print(GREEN + "Variable Declared")
  return

def set(a):
  equPos = a.find('=')
  beforeEqu = equPos - 1
  afterEqu = equPos + 2 
  c = sysVars[0].index(a[4:beforeEqu])
  sysVars[1][c] = a[afterEqu:]
  print(GREEN + "Variable Has Been Set")

def math(a):
  equPos = a.find('=')
  beforeEqu = equPos - 1
  afterEqu = equPos + 1 
  c = sysVars[0].index(a[3:beforeEqu])
  sysVars[1][c] = a[afterEqu:]

def echov(a):
  if a[6:] == "varNames":
    print(GREEN, sysVars[0])
    return
  if a[6:] == "varVals":
    print(GREEN, sysVars[1])
    return 
  else:
    try:
      c = sysVars[0].index(a[6:])
    except ValueError:
      print(RED + a[6:] + " does not exist")
      return
    else:
      print(GREEN + sysVars[1][c])

def help(a):
  if a[5:10] == "echo ":
    print(GREEN+"Echo Syntax:")
    print(GREEN+"  echo *msg*")
    return
  if a[5:10] == "echov":
    print(GREEN+"Echov Syntax:")
    print(GREEN+"  echov *varName*")
    return
  if a[5:10] == "clear":
    print(GREEN+"Clear Syntax:")
    print(GREEN+"  clear *all, history, or terminal*")
    return
  if a[5:9] == "help":
    print(GREEN+"haha very funny")
    return
  if a[5:9] == "lock":
    print(GREEN+"Lock Syntax:")
    print(GREEN+"  lock *history, terminal, or all*")
    return
  if a[5:12] == "history":
    print(GREEN+"History Syntax:")
    print(GREEN+"  history")
    return
  if a[5:8] == "var":
    print(GREEN+"Var Syntax:")
    print(GREEN+"  var *name* = *value*")
    return
  if a[5:8] == "set":
    print(GREEN+"Set Syntax:")
    print(GREEN+"  set *varname* = *value*")
    return
  if a[5:11] == "rename":
    print(GREEN+"Rename Syntax:")
    print(GREEN+"  raname *name*")
    return
  if a[5:6] == "":
    print(GREEN+"Echo Syntax:")
    print(GREEN+"  echo *msg*")
    print()
    print(GREEN+"Echov Syntax:")
    print(GREEN+"  echov *varName*")
    print()
    print(GREEN+"Clear Syntax:")
    print(GREEN+"  clear *all, history, or terminal*")
    print()
    print(GREEN+"Lock Syntax:")
    print(GREEN+"  lock *history, terminal, or all*")
    print()
    print(GREEN+"History Syntax:")
    print(GREEN+"  history")
    print()
    print(GREEN+"Var Syntax:")
    print(GREEN+"  var *name* = *value*")
    print()
    print(GREEN+"Set Syntax:")
    print(GREEN+"  set *varname* = *value*")
    print()
    print(GREEN+"Rename Syntax:")
    print(GREEN+"  raname *name*")
    return
    #all help below
  if a[5:8] == "all":
    print(GREEN+"Echo Syntax:")
    print(GREEN+"  echo *msg*")
    print()
    print(GREEN+"Echov Syntax:")
    print(GREEN+"  echov *varName*")
    print()
    print(GREEN+"Clear Syntax:")
    print(GREEN+"  clear *all, history, or terminal*")
    print()
    print(GREEN+"Lock Syntax:")
    print(GREEN+"  lock *history, terminal, or all*")
    print()
    print(GREEN+"History Syntax:")
    print(GREEN+"  history")
    print()
    print(GREEN+"Var Syntax:")
    print(GREEN+"  var *name* = *value*")
    print()
    print(GREEN+"Set Syntax:")
    print(GREEN+"  set *varname* = *value*")
    print()
    print(GREEN+"Rename Syntax:")
    print(GREEN+"  raname *name*")
    return
    return
  else:
    print(RED + "incorrect syntax")
    return

def clear(a):
  if a[6:] == "terminal":
    if terminalLock == False:
      print(YELLOW+"clearing terminal")
      time.sleep(2)
      os.system('clear')
    else:
      print(RED + "terminal lock is on")
  if a[6:] == "all":
    if terminalLock == False:
      if historyLock == False:
        print(YELLOW+"clearing terminal...")
        print(YELLOW+"clearing history...")
        time.sleep(2)
        os.system('clear')
        historyList.clear()
      else:
        print(RED + "history lock is on")
    else:
      print(RED + "terminal lock is on")
  if a[6:] == "history":
    if historyLock == False:
      print(YELLOW+"clearing history...")
      time.sleep(2)
      historyList.clear()
    else:
      print(RED + "history lock is on")
  if a[6:] == "":
    if terminalLock == False:
      print(YELLOW+"clearing terminal...")
      print(YELLOW+"clearing history...")
      os.system('clear')
    else:
      print(RED + "terminal lock is on")

def lock(a):
  global terminalLock
  global historyLock
  if a[5:8] == "all":
    terminalLock = True
    historyLock = True
  if a[5:12] == "history":
    historyLock = True
  if a[5:13] == "terminal":
    terminalLock = True
  if a[5:5] == "":
    historyLock = True
    terminalLock = True
  
def history(a):
  global historyList
  print(GREEN, end="")
  print(historyList)

def writeToHistory(a):
  global historyList
  historyList.append(a)

def rename(a):
  global name
  name = a[7:]

def request(a):
  if a[8:] == "admin":
    username = input(YELLOW + "Username: ")
    password = input(YELLOW + "Password: ")
    if username == "Rat":
      if password == "i8ur_drywall":
        print(GREEN + "Congrats You Solved The Easiest Puzzle I Have For You!")
        return
      else:
        print(RED + "Nope sry")
    else:
      print(RED + "Nope sry")
  else:
    print(RED + "incorrect syntax")
  
while terminalOn == True:
  command()


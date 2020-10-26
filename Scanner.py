"""
  While (not(eof)) do
      detect(token);
      if token is reserved word OR operator OR separator
          then genPIF(token, 0)
          else
          if token is identifier OR constant
              then index = pos(token, ST);
                  genPIF(token, index)
             else message “Lexical error”
          endif
      endif
  end while
"""
from ST import HashTable

class Scanner:
    def __init__(self):
        self.st = HashTable()
        self.f = ""

    def open_file(self, file):
        self.f = open(file, "r")

    def scan(self):
        ok = 1
        while ok == 1:
            line = self.f.readline()
            if not line:
                ok = 0
            else:
                split = line.split(" ")

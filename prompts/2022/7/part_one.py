class elf_dir():
  def __init__(self):
    self.contents = {}
  
  def add_file(self, name, size):
    if name[0] == '/':
      name = name[1:]
    if '/' in name:
      self.contents[name.split('/')[0]].add_file('/'.join(name.split('/')[1:]), size)
    else:  
      self.contents[name] = elf_file(size)

  def add_dir(self, name):
    if name[0] == '/':
      name = name[1:]
    if '/' in name:
      self.contents[name.split('/')[0]].add_dir('/'.join(name.split('/')[1:]))
    else:
      self.contents[name] = elf_dir()

  def size(self):
    return sum([v.size() for k,v in self.contents.items()])

  def show(self, tab_num = 0):
    for k, v in self.contents.items():
      print('\t'*tab_num, k, v.size())
      if isinstance(v, elf_dir):
        v.show(tab_num = tab_num + 1)
    
  def total_little_dirs(self):
    total = 0
    for k, v in self.contents.items():
      if isinstance(v, elf_dir):
        if v.size() <= 100000:
          total += v.size()
        total += v.total_little_dirs()
    return total

  def barely_over(self, target):
    best = None
    for k, v in self.contents.items():
      if isinstance(v, elf_dir):
        if v.size() >= target:
          if best is None or v.size() < best:
            best = v.size()
        if v.barely_over(target) is not None:
          return min(best, v.barely_over(target))
    return best

class elf_file():
  def __init__(self, size):
    self.b = size

  def size(self):
    return self.b

  # def show(self):
  #   str(self.size)

import sys
with open(sys.argv[1]) as f:
  lines = [l.strip() for l in f.readlines()]
  
# Create a data structure to store the directory structure
root = elf_dir()
working_dir = '/'
i = 0
while i < len(lines):
  print(i)
  if lines[i][0] == '$':
    if lines[i][2] == 'c': #cd command
      new_path = lines[i].split(' ')[2]
      if new_path == '/':
        print('goto root')
        working_dir = ''
      elif new_path == '..':
        print('before', working_dir)
        working_dir =  '/'.join(working_dir.split('/')[:-1])
        print('after',working_dir)
      else:
        working_dir = '/'.join([working_dir, new_path])
      i += 1
    if lines[i][2] == 'l': #ls command
      i += 1
      while i < len(lines) and lines[i][0] != '$':
        tokens = lines[i].split(' ')
        if tokens[0] == 'dir':
          new_dir = '/'.join([working_dir,tokens[1]])
          print('adding dir', new_dir)
          root.add_dir(new_dir)
        else:
          new_file = ('/'.join([working_dir,tokens[1]]), int(tokens[0]))
          print('adding new file', new_file)
          root.add_file(new_file[0], new_file[1])
          
        i += 1


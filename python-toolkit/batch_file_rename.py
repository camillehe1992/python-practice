# batch_file_remane.py

import argparse
import os

def batch_rename(work_dir, old_ext, new_ext):
  """
  This will batch rename a group of files in a given directory,
  once you pass the current and new extensions
  """
  for filename in os.listdir(work_dir):
    # Get the file extension
    split_file = os.path.splitext(filename)
    root_name, file_ext = split_file
    # Check the file extensions, if old_ext = file_ext
    if old_ext == file_ext:
      new_file = root_name + new_ext
      # Write the files
      os.rename(
        os.path.join(work_dir, filename),
        os.path.join(work_dir, new_file)
      )

    print("rename is done!")
    print(os.listdir(work_dir))

def get_parser():
  """
  Initize parser object for command-line inputs
  """
  parser = argparse.ArgumentParser(description='change extension of files in a working directory')
  parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the dirctory where to change extension')
  parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
  parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
  return parser

def main():
  """
  This will be called if the script is directly invoked
  """
  # add command line argument
  parser = get_parser()
  args = vars(parser.parse_args())
  print("args: ", args)

  work_dir = args['work_dir'][0]
  old_ext = args['old_ext'][0]
  if old_ext and old_ext[0] != '.':
    old_ext = '.' + old_ext
  new_ext = args['new_ext'][0]
  if new_ext and new_ext[0] != '.':
    new_ext = '.' + new_ext

  batch_rename(work_dir, old_ext, new_ext)

if __name__ == "__main__":
    main()

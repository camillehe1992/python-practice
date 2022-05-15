# create_dir_if_not_there.py

import argparse
import os

def create_dir(relative_dir):
  """
  Checks to see if a directory exists,
  if not then create it
  """
  try:
    if not os.path.exists(relative_dir):
      os.makedirs(relative_dir)
    else:
      print("The directory already exists")
  except Exception as e:
    print(e)

def get_parser():
  """
  Initize parser object for command-line inputs
  """
  parser = argparse.ArgumentParser(description='change extension of files in a working directory')
  parser.add_argument('relative_dir', metavar='RELATIVE_DIR', type=str, nargs=1, help='the relative dirctory')
  return parser

def main():
  # add command line argument
  parser = get_parser()
  args = vars(parser.parse_args())
  relative_dir = args['relative_dir'][0]
  
  create_dir(relative_dir)

if __name__ == "__main__":
    main()
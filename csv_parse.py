#!/usr/bin/env python3
import pandas as pd
import argparse

def main(args):
  df = pd.read_csv(args.csv_file)
  #df = pd.read_csv(args.csv_file, engine='python')
  columns = args.column_names.split(",")
  df1 = df[columns]
  print(df1.to_csv(path_or_buf=None,index=False))

def parse_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", help="CSV file")
  parser.add_argument("column_names", help="Column names")
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  arguments = parse_arguments()
  main(arguments)

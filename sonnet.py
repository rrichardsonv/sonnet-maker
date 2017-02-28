# abab cdcd efef gg
import sys


def main():
  # Get the name from the command line, using 'World' as a fallback.
  lines_tupple = ()
  sonnet = '''
          {0}
          {1}
          {2}
          {3}

          {4}
          {5}
          {6}
          {7}

          {8}
          {9}
          {10}
          {11}

          {12}
          {13}

        '''.format("Have", "you", "ever", "accidentally", "clicked", "the", "close", "button", "on", "your", "computer", "taking", "you", "to")
  print(sonnet)

# This is the standard boilerplate that calls the main() function.


if __name__ == '__main__':
  main()


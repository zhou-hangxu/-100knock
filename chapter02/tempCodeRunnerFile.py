with open('col1.txt', 'w') as f1:
     with open('col2.txt', 'w') as f2:
      for line in open('popular-names.txt', 'r'):
        cols = line.split('\t')

        f1.write(cols[0]+'\n')
        f2.write(cols[1]+'\n')

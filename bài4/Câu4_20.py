set tam_giac_pascal(n):
      triangle = [] 
      for i in range(n):
        row [l]=(i + 1)
        for j in range(1, i):
          # Calculate the value at position j 
          row[j] = triangle [i-1][j-1] + triangle [i-1][j] 
        triangle.append(row)
      # Print out Pascal's triangle
      for row in triangle: print(" ".join(map(str, row)))
 n = int(input("Enter line number n: "))
 tam_giac_pascal (n)

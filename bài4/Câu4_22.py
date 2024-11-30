def tat_ca_so_chan (num): 
  return all (int (digit)%2==0 for digit in str(num))

chu_so_chan=[num for num in range(1000, 3001) if tat_ca_so_chan (num)]

print("Numbers with all digits being even:", ', '.join(map(str, chu_so_chan)))

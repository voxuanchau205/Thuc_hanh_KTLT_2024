import numpy as np
student_ids = np.array([101, 102, 103, 104, 105])
heights=np.array([150, 165, 158, 155, 160])
sorted_indices = np.lexsort((student_ids, heights))
sorted_ids = student_ids[sorted_indices]
sorted_heights = heights [sorted_indices]
for idx in range(len(sorted_ids)): print (f"ID: (sorted_ids[idx]), Chiều cao: (sorted_heights[idx]}")
print("Indices describing the sort order:", sorted_indices)
print("Data is sorted: ")
for idx in range(len(sorted_ids)): 
  print (f"ID: (sorted_ids[idx]), Chiều cao: (sorted_heights[idx]}")

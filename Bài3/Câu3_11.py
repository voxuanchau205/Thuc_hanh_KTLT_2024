def benefit (t, n, k):
    # Calculate the amount received after k months
    for month in range(k):
       n += n (t / 100) *
    return n
# Enter interest rate, principal and number of months from keyboard
try:
    t = float (input("nhap lai suat tiet kiem(t%/thang): "))
    n = float (input ("nhap so von ban dau (n): "))
    k = int(input("nhap so thang gui(k): "))
   # Calculate the amount received after k months
    so_tien_nhan_duoc= benifit (t, n, k)
    print (f"Amount received after {k} months: {so_tien_nhan_duoc:.2f}")
except ValueError:
    print("Please enter a valid number.")

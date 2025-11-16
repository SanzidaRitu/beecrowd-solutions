import struct
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    A_s, B_s = line.split()
    C_s, D_s = sys.stdin.readline().split()

    A = struct.unpack('f', struct.pack('f', float(A_s)))[0]
    B = struct.unpack('f', struct.pack('f', float(B_s)))[0]

    C = float(C_s)
    D = float(D_s)

    print(f"A = {A:.6f}, B = {B:.6f}")
    print(f"C = {C:.6f}, D = {D:.6f}")

    print(f"A = {A:.1f}, B = {B:.1f}")
    print(f"C = {C:.1f}, D = {D:.1f}")

    print(f"A = {A:.2f}, B = {B:.2f}")
    print(f"C = {C:.2f}, D = {D:.2f}")

    print(f"A = {A:.3f}, B = {B:.3f}")
    print(f"C = {C:.3f}, D = {D:.3f}")

    print(f"A = {A:.3E}, B = {B:.3E}")
    print(f"C = {C:.3E}, D = {D:.3E}")

    print(f"A = {round(A)}, B = {round(B)}")
    print(f"C = {round(C)}, D = {round(D)}")
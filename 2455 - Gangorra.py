P1, C1, P2, C2 = map(int, input().split())

left_torque = P1 * C1
right_torque = P2 * C2

if left_torque == right_torque:
    print(0)
elif left_torque > right_torque:
    print(-1)
else:
    print(1)
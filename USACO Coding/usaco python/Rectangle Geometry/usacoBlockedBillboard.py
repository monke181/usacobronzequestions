ax1, ay1, ax2, ay2 = 1, 2, 3, 5
gx1, gy1, gx2, gy2 = 6, 0, 10, 4
sx1, sy1, sx2, sy2 = 2, 1, 8, 3

alex_billboard_area = (ax2 - ax1) * (ay2 - ay1)
greg_billboard_area = (gx2 - gx1) * (gy2 - gy1)
alex_and_truck_overlap_area = max(0, min(ax2, sx2) - max(ax1, sx1)) * max(0, min(ay2, sy2) - max(ay1, sy1))
greg_and_truck_overlap_area = max(0, min(gx2, sx2) - max(gx1, sx1)) * max(0, min(gy2, sy2) - max(gy1, sy1))


visible_area = alex_billboard_area + greg_billboard_area - alex_and_truck_overlap_area - greg_and_truck_overlap_area
print(visible_area)
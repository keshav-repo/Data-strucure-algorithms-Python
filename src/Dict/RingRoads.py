rings = "B0B6G0R6R0R6G9"
# rings = "B0R6G9"

ring = ""
rodLevel = None
rodRings = {}
for idx in range(0, len(rings)):
    if idx % 2 == 0:
        ring = rings[idx]
    else:
        rodLevel = rings[idx]
        if rodLevel in rodRings.keys():
            ringInrod = rodRings[rodLevel]
            ringInrod.add(ring)
            rodRings[rodLevel] = ringInrod
        else:
            rodRings[rodLevel] = {ring}

count = 0
for rodRing in rodRings.values():
    if len(rodRing) == 3:
        count = count + 1

print(count)


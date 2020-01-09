class orbiter:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


with open('input') as file:
    orbits = {}
    for line in file:
        o = line.split(')')
        orb = orbiter(o[1].strip(), o[0])
        orbits[orb.name] = orb

def build_orbit_chain(orbit, orbit_list):
    if orbit.parent == 'COM':
        return ['COM']
    else:
        extend_with = build_orbit_chain(orbit_list[orbit.parent], orbit_list)
        return [orbit.name] + extend_with

san = build_orbit_chain(orbits['SAN'], orbits)
you = build_orbit_chain(orbits['YOU'], orbits)
san.reverse()
you.reverse()
for idx, orb in enumerate(san):
    if orb == you[idx]:
        print(orb)
        continue
    else:
        print("From {} to SAN: {}".format(san[idx], len(san[idx:])-1))
        print("From {} to YOU: {}".format(you[idx], len(you[idx:])-1))
        print(len(san[idx-1:] + you[idx-1:]))
        break

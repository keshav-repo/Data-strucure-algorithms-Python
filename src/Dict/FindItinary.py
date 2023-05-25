tickets = ["Chennai->Banglore", "Bombay->Delhi", "Goa->Chennai", "Delhi->Goa"]

airportFreq = {}
ticketsDict={}
for ticket in tickets:
    airport = ticket.split("->")
    ticketsDict[airport[0]] = airport[1]
    if airport[0] in airportFreq.keys():
        airportFreq[airport[0]] = airportFreq[airport[0]] + 1
    else:
        airportFreq[airport[0]] = 1
    if airport[1] in airportFreq.keys():
        airportFreq[airport[1]] = airportFreq[airport[1]] - 1
    else:
        airportFreq[airport[1]] = -1

startingAirport=""
endingAirport=""
for airport, freq in airportFreq.items():
    if freq == 1:
        startingAirport = airport
    elif freq == -1:
        endingAirport = airport

orderedTicket = []
currentairport = startingAirport
while currentairport != endingAirport:
     dest = ticketsDict[currentairport]
     orderedTicket.append(currentairport+"->"+dest)
     currentairport = dest

print(orderedTicket)

tickets = ["Chennai->Banglore", "Bombay->Delhi", "Goa->Chennai", "Delhi->Goa"]

"""
"""
airportFreq={}
itinaryInfo={}
for ticket in tickets:
    ticketSplitted = ticket.split("->")
    deprAirport=ticketSplitted[0]
    arrAirport=ticketSplitted[1]
    itinaryInfo[deprAirport] = arrAirport
    if arrAirport in airportFreq.keys():
        airportFreq[arrAirport] = airportFreq[arrAirport] - 1
    else:
        airportFreq[arrAirport] = -1
    if deprAirport in airportFreq.keys():
        airportFreq[deprAirport] = airportFreq[deprAirport]+1
    else:
        airportFreq[deprAirport] = + 1
print(airportFreq)

startingAirport=""
endAirport=""
for airport, freq in airportFreq.items():
    if freq == 1:
        startingAirport = airport
    elif freq == -1:
        endAirport = airport

print(startingAirport)
print(endAirport)
print(itinaryInfo)

currentAirport=startingAirport

resultTicket=[]
while currentAirport != endAirport:
    arrAirport=itinaryInfo[currentAirport]
    resultTicket.append(currentAirport+"->"+arrAirport)
    currentAirport = arrAirport

print(resultTicket)

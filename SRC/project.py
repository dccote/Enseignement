import experiment as Exp

# La classe DataFile permet de rapidement lire des données .csv
data = Exp.DataFile('ampoules.csv', columnId='x0 y0 y1 y2 y3 y4 y5 y6 y7')

labels = ["Lampe #0","Lampe #1","Lampe #2","Lampe #3","Lampe #4","Lampe #5","Lampe #6","Lampe #7"]
for i,curve in enumerate(data.curves):
    curve.connectPoints = True
    curve.label = labels[i]

# La classe Graph permet de rapidement faire un graphique raisonnable
graph = Exp.XYGraph(data)
graph.useColors = True
graph.xlabel = "Wavelength [nm]"
graph.ylabel = "Intensité [arb. u]"
graph.xlim = (350, 900)
graph.show()
graph.save('test.pdf')
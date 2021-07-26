import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.stats.stats import pearsonr
import matplotlib.gridspec as gridspec

fortnights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# transport cost for each fortnight
transport = [265, 193, 248, 255, 212, 206, 266, 243, 222, 246, 203, 239, 208, 131, 273, 199, 264, 264, 234, 127, 267,
             231, 328, 337]
# takeout cost for each fortnight
takeout = [192, 272, 272, 295, 391, 298, 252, 127, 107, 225, 349, 321, 248, 189, 25, 48, 29, 75, 27, 100, 116, 176, 91,
           191]
# groceries cost for each fortnight
groceries = [122, 120, 118, 150, 134, 139, 131, 143, 224, 130, 160, 173, 170, 157, 205, 175, 223, 185, 266, 187, 210,
             174, 86, 256]

plt.style.use('dark_background')

figure = plt.figure(num=1,figsize=(10,200))
figure.suptitle('An analysis of our fortnight Budget', fontsize=14, fontweight='bold')

gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[2, 2, 2,], hspace=1.1)

transportAndGroceriesLineGraph = figure.add_subplot(gs[0, 0])
transportAndGroceriesLineGraph.set_ylabel('cost')
transportAndGroceriesLineGraph.set_xlabel('fortnight')
transportAndGroceriesLineGraph.set_title('Transport vs Groceries')

line1, = transportAndGroceriesLineGraph.plot(fortnights, transport, color='red', marker='o', label='transport')
line2, = transportAndGroceriesLineGraph.plot(fortnights, groceries, color='yellow', marker='o', label='groceries')

transportAndGroceriesLineGraph.legend()
transportAndGroceriesLineGraph.grid(True)

plt.xticks(np.arange(1, len(fortnights) + 1, 1), color='green')
plt.yticks(np.arange(0, max(takeout), 20), color='green')


def animate(i):
    line1.set_data(fortnights[:i], transport[:i])
    line2.set_data(fortnights[:i], groceries[:i])
    return line1, line2


ani = FuncAnimation(fig=figure, func=animate, interval=2)

takeoutAndGroceriesLineGraph = figure.add_subplot(gs[0, 1])
line3, = takeoutAndGroceriesLineGraph.plot(fortnights, takeout, marker='o', label='takeout')
line4, = takeoutAndGroceriesLineGraph.plot(fortnights, groceries, color='green', marker='o', label='groceries')
takeoutAndGroceriesLineGraph.set_ylabel('cost')
takeoutAndGroceriesLineGraph.set_xlabel('fortnight')
takeoutAndGroceriesLineGraph.set_title('Takeout vs Groceries')
takeoutAndGroceriesLineGraph.grid(True)
takeoutAndGroceriesLineGraph.legend()

plt.xticks(np.arange(1, len(fortnights) + 1, 1), color='green')
plt.yticks(np.arange(0, max(takeout), 20), color='green')


def animate(i):
    line3.set_data(fortnights[:i], takeout[:i])
    line4.set_data(fortnights[:i], groceries[:i])
    return line3, line4


ani2 = FuncAnimation(fig=figure, func=animate, interval=2)

transportAndTakeoutScatterPlot = figure.add_subplot(gs[1, 0])
transportAndTakeoutScatterPlot.scatter(fortnights, transport, color='red', marker='o', label='transport')
transportAndTakeoutScatterPlot.scatter(fortnights, takeout, color='yellow', marker='o', label='groceries')

plt.xticks(np.arange(1, len(fortnights) + 1, 1), color='green')
plt.yticks(np.arange(0, max(takeout), 20), color='green')

transportAndTakeoutScatterPlot.set_ylabel('cost')
transportAndTakeoutScatterPlot.set_xlabel('fortnight')
transportAndTakeoutScatterPlot.set_title('Transport vs take_out')
transportAndTakeoutScatterPlot.legend()

scatterPlot1Explanation = figure.add_subplot(gs[1, 1])
scatterPlot1Explanation.axes.xaxis.set_visible(False)
scatterPlot1Explanation.axes.yaxis.set_visible(False)
scatterPlot1Explanation.text(0.1, 0.35,
         'I expected zero correlation between groceries and transport however\n'
         'According to pearsons correlation:\n'
         'There is a weak negative correlation between groceries and takeout of:\n'
         '-0.17717388056215955, 0.40754712482189326',
                             fontsize=8,
                             )

groceriesAndTakeoutScatterPlot = figure.add_subplot(gs[2, 0])
groceriesAndTakeoutScatterPlot.scatter(fortnights, groceries, color='red', marker='o', label='transport')
groceriesAndTakeoutScatterPlot.scatter(fortnights, takeout, color='yellow', marker='o', label='groceries')
groceriesAndTakeoutScatterPlot.set_title('Groceries vs take_out')
groceriesAndTakeoutScatterPlot.set_xlabel('fortnight')
groceriesAndTakeoutScatterPlot.set_ylabel('cost')
groceriesAndTakeoutScatterPlot.legend()

plt.xticks(np.arange(1, len(fortnights) + 1, 1), color='green')
plt.yticks(np.arange(0, max(takeout), 20), color='green')

scatterPlot2Explanation = figure.add_subplot(gs[2, 1])
scatterPlot2Explanation.axes.xaxis.set_visible(False)
scatterPlot2Explanation.axes.yaxis.set_visible(False)
scatterPlot2Explanation.text(0.1, 0.35,
         'I expected a stronger negative correlation of -0.8 or 0.9 because;\n'
         'I thought the more groceries we orded the less takeout we would order\n'
         'According to pearsons correlation:\n'
         'There is a strong  negative correlation between groceries and takeout of:\n '
         '-0.5085343629640278, 0.011165467950515167',
                             fontsize=8,
                             )

figure2= plt.figure(num=2)
figure2.suptitle('An analysis of our fortnight Budget', fontsize=14, fontweight='bold')

totalTransportCost=sum(transport)
totalTakeoutCost= sum(takeout)
totalGroceriesCost=sum(groceries)

fortnightPieChart = figure2.add_subplot()
fortnightTotalCost=[totalGroceriesCost,totalTakeoutCost,totalTransportCost]
myLabels=["groceries","takeout","transport"]
myexplode = [0, 0.2, 0]
fortnightPieChart.pie(fortnightTotalCost,labels=myLabels,startangle=90,explode=myexplode,shadow=True)
fortnightPieChart.legend(title="Total fortnight cost")



print(pearsonr(transport, takeout))
print(pearsonr(groceries, takeout))

plt.show()

#!/usr/bin/python3

import plotly.graph_objs as go

day = 0
blockheight = 0
currentCoins = 0

coinbase = 5000000000 # sats

era = 1
eraLength = 210000 # blocks between halvings

coin_history = []
inflation_rate = []
blockheight_history = []

bitcoin_monetary_inflation = open("bitcoin_monetary_inflation.csv", 'w+')

# Generate coin minting schedule
while coinbase > 0:

    for each in range(0,eraLength):
        blockheight += 1
        currentCoins += coinbase
        inflation = coinbase*52500/currentCoins*100 # assuming 52500 blocks per year
        inflation = format(inflation, '.10f')
        if blockheight % 1440 == 0: # using 1440 instead of 144 for 10-day ticks instead of 1-day ticks, to reduce density
            day += 1
            bitcoin_monetary_inflation.write("{}, {}, {}, {}, {}\n".format(day, blockheight, coinbase, currentCoins, inflation))

            blockheight_history.append(blockheight)
            coin_history.append(currentCoins/100000000)
            inflation_rate.append(inflation)

    era += 1
    coinbase = int(coinbase/2)


bitcoin_monetary_inflation.close()


trace1 = go.Scatter(name="bitcoins", x=blockheight_history, y=coin_history, line=dict(color='rgb(31, 119, 180)'))
trace2 = go.Scatter(name="% inflation", x=blockheight_history, y=inflation_rate, yaxis="y2", line=dict(color='rgb(255, 127, 14)'))

data = [trace1, trace2]

layout = go.Layout(title="Bitcoin Monetary Inflation",
                        dragmode="pan",
                        plot_bgcolor='rgba(0,0,0,0)',
                        legend=dict(
                            x = 0.85,
                            y = -0.15,
                            traceorder = 'normal',
                            xanchor = 'auto',
                            yanchor = 'auto'
                        ),
                        annotations = [
                            dict(
                                x = 628000,
                                y = 0.603249290398,
                                arrowhead = 3,
                                arrowsize = 1,
                                ax = 50,
                                ay = -35,
                                bgcolor = 'rgb(255, 255, 255)',
                                borderpad = 1.8,
                                text = 'you are here',
                                xref = 'x',
                                yref = 'y2'
                            ),
                            dict(
                                x = -0.0459662288931,
                                y = -0.122251655629,
                                ax = -544,
                                ay = 280,
                                showarrow = False,
                                text = 'inflation = coinbase x blocksPerYear / existingCoins',
                                xref = 'paper',
                                yref = 'paper'
                            ),

                            dict(
                                x=0,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='2009',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=210000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='2012',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=420000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='2016',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=630000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='2020',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=840000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2024',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1050000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2028',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1260000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2032',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1470000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2036',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1680000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2040',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1890000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2044',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=2100000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2048',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=2310000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2052',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=2520000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2056',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=2730000,
                                y=22000000,
                                font=dict(size=10),
                                showarrow=False,
                                text='~2060',
                                xanchor='left',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=105000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='50',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=315000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='25',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=525000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='12.5',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=735000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='6.25',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=945000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='3.125',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1155000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='1.5625',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1365000,
                                y=-0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.78125',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1575000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.390625',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1785000,
                                y=-0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.1953125',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=1995000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.09765625',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=2205000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.04882812',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=2415000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.02441406',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=2625000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.01220703',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=2835000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00610351',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=3045000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00305175',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=3255000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00152587',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=3465000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00076293',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=3675000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00038146',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=3885000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00019073',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=4095000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00009536',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=4305000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00004768',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=4515000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00002384',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=4725000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00001192',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=4935000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000596',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=5145000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000298',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=5355000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000149',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=5565000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000074',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=5775000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000037',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=5985000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000018',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=6195000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000009',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=6405000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000004',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=6615000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000002',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=6825000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='0.00000001',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=7035000,
                                y=0,
                                font=dict(size=8),
                                showarrow=False,
                                text='.00000000',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y'
                            ),
                            dict(
                                x=5045000,
                                y=-6,
                                font=dict(size=4),
                                showarrow=False,
                                text='plotly gets weird with numbers this small',
                                xanchor='center',
                                xref='x',
                                yanchor='bottom',
                                yref='y2'
                            )

                        ],
                        xaxis=dict(
                            title="block height",
                            dtick="210000",
                            exponentformat = "none",
                            range=(0,3000000),
                            side="bottom"
                        ),
                        yaxis=dict(
                            title="bitcoins",
                            tickfont=dict(color='rgb(31, 119, 180)'),
                            titlefont = dict(color='rgb(31, 119, 180)'),
                            dtick="3000000",
                            range=(0,22000000),
                            zeroline=False
                        ),
                        yaxis2=dict(
                            title="% monetary inflation",
                            tickfont=dict(color='rgb(255, 127, 14)'),
                            titlefont = dict(color='rgb(255, 127, 14)'),
                            type="log",
                            showgrid=False,
                            showline=False,
                            overlaying='y',
                            side="right",
                            range=(-5,4),
                            exponentformat="none"

                        )

                   )


fig = go.Figure(data=data, layout=layout)
fig.update_xaxes(showgrid=True, ticks="inside", tick0=210000, gridcolor='lightgray')
fig.update_layout(title={
        'text': "Bitcoin Monetary Inflation",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        hovermode='x')

fig.write_html('index.html', auto_open=True, full_html=True, include_plotlyjs='cdn')

# This adds the twitter logo to the layout after the HTML is generated, so that it can be included in the bitmaps
fig.layout.images = [dict(
        source="images/logo.png",
        xref="paper", yref="paper",
        x=1.05, y=-0.15,
        sizex=0.1, sizey=0.1,
        xanchor="right", yanchor="bottom",
      )]


# The `write_image` function requires orca and a couple other dependencies to generate bitmaps
fig.write_image("images/Bitcoin_Monetary_Inflation.png", format="png", width=1200, height=764, scale=1)
fig.write_image("images/Bitcoin_Monetary_Inflation_10x.png", format="png", width=1200, height=764, scale=10)

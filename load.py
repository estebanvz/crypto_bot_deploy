import plotly.graph_objects as go
from plotly.subplots import make_subplots


def build_img(dataset, cripto):
    fig = make_subplots(rows=2, cols=1, row_heights=[0.8, 0.2], shared_xaxes=True)
    clr = []
    for i, e in enumerate(dataset["lr"].values):
        if i == 0:
            if dataset["lr"].values[i + 1] >= dataset["lr"].values[i]:
                clr.append("#00ff00")
            else:
                clr.append("#ff0000")
        else:
            if dataset["lr"].values[i] >= dataset["lr"].values[i - 1]:
                clr.append("#00ff00")
            else:
                clr.append("#ff0000")
    cadx = []
    for i, e in enumerate(dataset["adx"].values):
        if i == 0:
            if dataset["adx"].values[i + 1] >= dataset["adx"].values[i]:
                if dataset["mdm"].values[i] < dataset["pdm"].values[i]:
                    cadx.append("#00ff00")
                else:
                    cadx.append("#ff0000")
            else:
                if dataset["mdm"].values[i] < dataset["pdm"].values[i]:
                    cadx.append("#004400")
                else:
                    cadx.append("#8B0000")
        else:
            if dataset["adx"].values[i] >= dataset["adx"].values[i - 1]:
                if dataset["mdm"].values[i] < dataset["pdm"].values[i]:
                    cadx.append("#00ff00")
                else:
                    cadx.append("#ff0000")
            else:
                if dataset["mdm"].values[i] < dataset["pdm"].values[i]:
                    cadx.append("#004400")
                else:
                    cadx.append("#8B0000")
    fig.add_trace(
        go.Candlestick(
            name="Precio",
            x=dataset.index,
            open=dataset.Open,
            close=dataset.Close,
            high=dataset.High,
            low=dataset.Low,
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Bar(
            name="Regresión",
            x=dataset.index,
            y=dataset.lr,
            opacity=0.5,
            marker={"color": clr},
        ),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            name="EMA55",
            x=dataset.index,
            y=dataset["55"],
            mode="lines",
            marker={"color": "#dddddd"},
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            name="ADX",
            mode="lines+markers",
            x=dataset.index,
            y=dataset["adx"],
            marker=dict(size=6, color=cadx),
            marker_symbol="diamond",
            marker_line_width=1,
            marker_line_color="gray",
        ),
        row=2,
        col=1,
    )

    fig.update_layout(height=600, width=800, title_text=cripto)
    fig.update_layout(
        template="plotly_dark", xaxis=dict(rangeslider=dict(visible=False))
    )
    fig.write_image("./img/{}.jpg".format(cripto))
    return "./img/{}.jpg".format(cripto)

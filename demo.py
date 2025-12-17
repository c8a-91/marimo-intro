import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    import seaborn as sns

    return mo, pd, px, sns


@app.cell
def _(sns):
    titanic_data = sns.load_dataset("titanic")
    return (titanic_data,)


@app.cell
def _(mo):
    age_min = mo.ui.slider(start=0, stop=80, value=0, label="年齢（下限）")
    age_max = mo.ui.slider(start=0, stop=80, value=80, label="年齢（上限）")
    mo.hstack([age_min, age_max])
    return age_min, age_max


@app.cell
def _(age_max, age_min, mo, px, titanic_data):
    filtered = titanic_data[
        (titanic_data["age"] >= age_min.value) & (titanic_data["age"] < age_max.value)
    ].dropna(subset=["age", "pclass", "survived"])

    survival = (
        filtered.groupby("pclass")["survived"].agg(["sum", "count"]).reset_index()
    )
    survival["rate"] = (survival["sum"] / survival["count"] * 100).round(1)
    survival["pclass"] = survival["pclass"].map({1: "1等", 2: "2等", 3: "3等"})
    survival["label"] = survival.apply(
        lambda r: f"{r['rate']}% ({int(r['sum'])}/{int(r['count'])}人)", axis=1
    )

    fig = px.bar(
        survival,
        x="pclass",
        y="rate",
        color="pclass",
        title=f"客室クラス別 生存率（{age_min.value}歳以上 {age_max.value}歳未満）",
        labels={"rate": "生存率 (%)", "pclass": "客室クラス"},
        text="label",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(showlegend=False)

    mo.vstack(
        [mo.md(f"**対象: {len(filtered)}人** / 全体: {len(titanic_data)}人"), fig]
    )
    return filtered, fig, survival


if __name__ == "__main__":
    app.run()

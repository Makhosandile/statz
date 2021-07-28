import pandas as pd

confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
            '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv '
recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
            '/csse_covid_19_time_series/time_series_covid19_recovered_global.csv '
deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
         '/csse_covid_19_time_series/time_series_covid19_deaths_global.csv '

deaths = pd.read_csv(deaths)
recovered = pd.read_csv(recovered)
confirmed = pd.read_csv(confirmed)

recovered = recovered.drop(columns=['Province/State'])
deaths = deaths.drop(columns=['Province/State'])
confirmed = confirmed.drop(columns=['Province/State'])

recovered = recovered.rename(columns={'Country/Region': 'Country'})
deaths = deaths.rename(columns={'Country/Region': 'Country'})
confirmed = confirmed.rename(columns={'Country/Region': 'Country'})


class GlobalCases:
    def confirmed(self):
        df = confirmed.iloc[:, 4:].sum().max()
        df = {'Confirmed': int(df)}
        return df

    def deaths(self):
        df = deaths.iloc[:, 4:].sum().max()
        df = {'Deaths': int(df)}
        return df

    def recovered(self):
        df = recovered.iloc[:, 4:].sum().max()
        df = {'Recovered': int(df)}
        return df

    def active(self):
        df = GlobalCases.confirmed(self)['Confirmed'] - GlobalCases.deaths(self)['Deaths'] \
             - GlobalCases.recovered(self)['Recovered']
        df = {'Active': int(df)}
        return df

    def complete_world(self):
        df = {
            'Confirmed': GlobalCases.confirmed(self),
            'Deaths': GlobalCases.deaths(self),
            'Recovered': GlobalCases.recovered(self),
            'Active': GlobalCases.active(self)
        }
        return df

    def death_rate(self=None):
        df = GlobalCases.deaths(self)['Deaths'] / GlobalCases.confirmed(self)['Confirmed'] * 100
        df = {'Death Rate': float(df)}
        return df

    def recovery_rate(self):
        df = GlobalCases.recovered(self)['Recovered'] / GlobalCases.confirmed(self)['Confirmed'] * 100
        df = {'Recovery Rate': float(df)}
        return df

    def active_perc(self):
        df = GlobalCases.active(self)['Active'] / GlobalCases.confirmed(self)['Confirmed'] * 100
        df = {'Active Percantage': float(df)}
        return df

    def daily_confirmed(self):
        df = confirmed.iloc[:, 3:].sum(axis=0)
        df.index = pd.to_datetime(df.index)
        df = pd.DataFrame(df).reset_index()
        df.columns = ['Date', 'Confirmed']
        #df["Confirmed"].astype(int)
        return df.to_dict()

    def daily_deaths(self):
        df = deaths.iloc[:, 3:].sum(axis=0)
        df.index = pd.to_datetime(df.index)
        df = pd.DataFrame(df).reset_index()
        df.columns = ['Date', 'Deaths']
        # df['7 Day Change'] = df['Deaths'].pct_change(periods=7)
        # df /= 1_000_000
        return df.to_dict()

    def daily_recovered(self):
        df = recovered.iloc[:, 3:].sum(axis=0)
        df.index = pd.to_datetime(df.index)
        df = pd.DataFrame(df).reset_index()
        df.columns = ['Date', 'Recovered']
        # df['7 Day Change'] = df['Recovered'].pct_change(periods=7)
        # df /= 1_000_000
        return df.to_dict()

    def daily_active(self):
        df = (confirmed.iloc[:, 3:].sum(axis=0)) - (deaths.iloc[:, 3:].sum(axis=0)) - (
            recovered.iloc[:, 3:].sum(axis=0))
        df.index = pd.to_datetime(df.index)
        df = pd.DataFrame(df).reset_index()
        df.columns = ['Date', 'Active']
        # df['7 Day Change'] = df.rolling(window=7).mean()
        # df['7 Day Change'] = df['Active'].pct_change(periods=7)
        return df.to_dict()


df_confirmed = confirmed.groupby('Country').sum().reset_index()
df_recovered = recovered.groupby('Country').sum().reset_index()
df_deaths = deaths.groupby('Country').sum().reset_index()

df_confirmed.loc[:, ['Lat', 'Long']] = confirmed.groupby('Country').mean().reset_index().loc[:, ['Lat', 'Long']]
df_deaths.loc[:, ['Lat', 'Long']] = deaths.groupby('Country').mean().reset_index().loc[:, ['Lat', 'Long']]
df_recovered.loc[:, ['Lat', 'Long']] = recovered.groupby('Country').mean().reset_index().loc[:, ['Lat', 'Long']]


class Countries:

    def confirmed(self):
        data = pd.melt(df_confirmed,
                       id_vars=df_confirmed.iloc[:, :3],
                       var_name='Date',
                       value_vars=df_confirmed.iloc[:, 3:],
                       value_name='Confirmed')
        return data

    def recovered(self):
        df = pd.melt(df_recovered,
                     id_vars=df_recovered.iloc[:, :3],
                     var_name='Date',
                     value_vars=df_recovered.iloc[:, 3:],
                     value_name='Confirmed')
        return df

    def deaths(self):
        df = pd.melt(df_deaths,
                     id_vars=df_deaths.iloc[:, :3],
                     var_name='Date',
                     value_vars=df_deaths.iloc[:, 3:],
                     value_name='Deaths')
        return df

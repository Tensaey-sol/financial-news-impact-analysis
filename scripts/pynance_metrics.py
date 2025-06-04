def get_returns(stock_df):
    stock_df = stock_df.copy()
    stock_df['returns'] = stock_df['close'].pct_change()
    return stock_df[['date', 'returns']].dropna()

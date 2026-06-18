
def running_peak(values):
    current_peak = values[0]
    peaks = []

    for value in values:
        current_peak = max(current_peak, value)
        peaks.append(current_peak)
    return peaks

def drawdown_series(pnl_history):
    peaks = running_peak(pnl_history)
    drawdowns = []
    for i in range(len(pnl_history)):
        pnl = 
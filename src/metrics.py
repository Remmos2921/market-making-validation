
def running_peak(values):
    if len(values) == 0:
        raise ValueError (
            "input must have a length of more than 0"
        )
    current_peak = values[0]
    peaks = []

    for value in values:
        current_peak = max(current_peak, value)
        peaks.append(current_peak)
    return peaks

def drawdown_series(pnl_history):
    if len(pnl_history) == 0:
        raise ValueError (
            "input must have a length of more than 0"
        )
    peaks = running_peak(pnl_history)
    drawdowns = []
    for i in range(len(pnl_history)):
        pnl = pnl_history[i]
        peak = peaks[i]
        drawdowns.append(pnl - peak)
    return drawdowns

def max_drawdown(pnl_history):
    if len(pnl_history) == 0:
        raise ValueError (
            "input must have a length of more than 0"
        )
    drawdowns = drawdown_series(pnl_history)
    return min(drawdowns)

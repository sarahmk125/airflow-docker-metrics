from datetime import datetime, time, timedelta


# NOTE: This is over-abstracted on purpose to showcase with the /lib/ folder is for.
class EpochManipulate(object):
    def __init__(self):
        pass

    def _get_current_epoch(self):
        current = datetime.combine(datetime.today(), time.min)
        return int(current.timestamp())

    def _get_previous_epoch_days(self, days):
        current_datetime = datetime.combine(datetime.today(), time.min)
        prev_datetime = current_datetime - timedelta(days=days)
        return int(prev_datetime.timestamp())

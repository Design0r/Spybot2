from django import template
from datetime import datetime, timezone

register = template.Library()


@register.filter
def is_string(val):
    return isinstance(val, str)


# from https://gist.github.com/jonlabelle/7d306575cbbd34b154f87b1853d532cc
@register.filter
def relative_time(date):
    """Take a datetime and return its "age" as a string.
    The age can be in second, minute, hour, day, month or year. Only the
    biggest unit is considered, e.g. if it's 2 days and 3 hours, "2 days" will
    be returned.
    Make sure date is not in the future, or else it won't work.
    Original Gist by 'zhangsen' @ https://gist.github.com/zhangsen/1199964
    """

    def formatn(n, s):
        """Add "s" if it's plural"""

        if n == 1:
            return "1 %s" % s
        elif n > 1:
            return "%d %ss" % (n, s)

    def qnr(a, b):
        """Return quotient and remaining"""

        return a / b, a % b

    class FormatDelta:

        def __init__(self, dt):
            now = datetime.now(timezone.utc)
            delta = now - dt
            self.day = delta.days
            self.second = delta.seconds
            self.year, self.day = qnr(self.day, 365)
            self.month, self.day = qnr(self.day, 30)
            self.hour, self.second = qnr(self.second, 3600)
            self.minute, self.second = qnr(self.second, 60)

        def format(self):
            for period in ['year', 'month', 'day', 'hour', 'minute', 'second']:
                n = getattr(self, period)
                if n >= 1:
                    return '{0} ago'.format(formatn(n, period))
            return "just now"

    return FormatDelta(date).format()

@register.filter
def duration_format(td):

    total_seconds = td

    days = total_seconds // 86400
    remaining_hours = total_seconds % 86400
    remaining_minutes = remaining_hours % 3600
    hours = remaining_hours // 3600
    minutes = remaining_minutes // 60
    seconds = remaining_minutes % 60

    days_str = f'{days}d ' if days else ''
    hours_str = f'{hours}h ' if hours else ''
    minutes_str = f'{minutes}m ' if minutes else ''
    seconds_str = f'{seconds}s' if seconds and not hours_str else ''

    return f'{days_str}{hours_str}{minutes_str}{seconds_str}'
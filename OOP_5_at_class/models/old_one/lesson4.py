import datetime
import traceback

try:
    1 / 0
except ZeroDivisionError as err:
    with open('logs.txt', 'a') as file:
        message = '{}   {}:\n {} \n\n'.format(
            datetime.datetime.now(), err.__class__.__name__, traceback.format_exc())
        file.write
finally:
    print('Exception was handled. Check the logs for additional info.')

from pprint import pprint

from googleapiclient import discovery

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/drive.readonly'
#     'https://www.googleapis.com/auth/spreadsheets'
#     'https://www.googleapis.com/auth/spreadsheets.readonly'
credentials = None

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to retrieve data from.
spreadsheet_id = '1ep-DLPCGoOqS8E6PSVngpnW5nzDcakESRUew57alkMk'  # TODO: Update placeholder value.

# The A1 notation of the values to retrieve.
range_ = 'A1:Z100'  # TODO: Update placeholder value.

# How values should be represented in the output.
# The default render option is ValueRenderOption.FORMATTED_VALUE.
value_render_option = ''  # TODO: Update placeholder value.

# How dates, times, and durations should be represented in the output.
# This is ignored if value_render_option is
# FORMATTED_VALUE.
# The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].
date_time_render_option = ''  # TODO: Update placeholder value.

request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_, valueRenderOption=value_render_option, dateTimeRenderOption=date_time_render_option)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
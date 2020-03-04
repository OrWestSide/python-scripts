import openpyxl
import requests


def initExcelSheet():
    """
    Initializes an empty excel sheet, with corresponding
    column names. The column names will be
    1. Order number
    2. Date the order was placed
    3. Customer name
    4. Customer address
    5. Delivery type
    6. Items ordered

    Args: None
    Output: The excel sheet created
    """
    column_color = openpyxl.styles.PatternFill(start_color='00B7EB', end_color='00B7EB', fill_type='solid')
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Orders'

    ws.column_dimensions['A'].width = 50
    ws['A1'].fill = column_color
    ws['A1'] = 'Order Number'

    ws.column_dimensions['B'].width = 50
    ws['B1'].fill = column_color
    ws['B1'] = 'Date Placed'

    ws.column_dimensions['C'].width = 50
    ws['C1'].fill = column_color
    ws['C1'] = 'Customer Name'

    ws.column_dimensions['D'].width = 50
    ws['D1'].fill = column_color
    ws['D1'] = 'Customer Address'

    ws.column_dimensions['F'].width = 50
    ws['F1'].fill = column_color
    ws['F1'] = 'Delivery Type'

    ws.column_dimensions['E'].width = 50
    ws['E1'].fill = column_color
    ws['E1'] = 'Items'

    wb.save('orders.xlsx')

    return wb


def fetchData():
    token_url = 'https://pa-restaurang.starwebserver.se/api/v2/token'
    body = {
        'grant_type':  'client_credentials',
        'client_id': 'automatiseramera.automatiseramera',
        'client_secret': '37cc6lqfoj2e2xzsvhlpyqgo92jz5nzesvsfln7e3cf6nadnydxqro2q'
    }
    r = requests.post(token_url, data=body)
    print(r.json())

    # orders_url = 'https://pa-restaurang.starwebserver.se/api/v2/orders?sortBy=orderId&sortOrder=DESC&include=items'

    # r = requests.get(orders_url)
    # print(r)
    # print(r.text)
    print('Here, I will get the data. It will return a list of dictionaries')


def fillExcelSheet():
    print('Here, I will fill the excel sheet with the data fetched')

if __name__ == '__main__':
    wb = initExcelSheet()
    fetchData()
    fillExcelSheet()

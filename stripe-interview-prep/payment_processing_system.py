class Status:
    AUTHORIZED = "AUTHORIZED"
    CAPTURED = "CAPTURED"
    REFUNDED = "REFUNDED"
    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"

class Response:
    OK = "OK"
    ERROR = "ERROR"

class Payment:
    def __init__(self, merchant_id, amount):
        self.merchant_id = merchant_id
        self.amount = amount
        self.refunded_amount = 0
        self.status = Status.AUTHORIZED

payments = {}

def get_payment(payment_id):
    return payments.get(payment_id)

def create_payment(payment_id, merchant_id, amount):
    if payment_id in payments:
        return Response.ERROR
    if amount <= 0:
        return Response.ERROR
    payments[payment_id] = Payment(merchant_id, amount)
    return Response.OK

def capture_payment(payment_id):

    payment = payments.get(payment_id)
    if payment and payment.status == Status.AUTHORIZED:
        payment.status = Status.CAPTURED
        return Response.OK
    else:
        return Response.ERROR

def get_payment_status(payment_id):
    if payments.get(payment_id) is None:
        return Response.ERROR
    return payments.get(payment_id).status

def refund_payment(payment_id, amount):
    payment = get_payment(payment_id)
    if payment is None:
        return Response.ERROR
    if payment.status not in [Status.CAPTURED, Status.PARTIALLY_REFUNDED]:
        return Response.ERROR
    if amount <= 0:
        return Response.ERROR
    refund = payment.amount - payment.refunded_amount
    if refund - amount < 0:
        return Response.ERROR
    elif refund - amount == 0:
        payment.status = Status.REFUNDED
    else:
        payment.status = Status.PARTIALLY_REFUNDED
    payment.refunded_amount += amount
    return Response.OK

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        continue

    line = line.split()
    command = line[0]
    if command == "CREATE_PAYMENT":
        payment_id = line[1]
        merchant_id = line[2]
        amount = int(line[3])
        print(create_payment(payment_id, merchant_id, amount))
    elif command == "CAPTURE":
        payment_id = line[1]
        print(capture_payment(payment_id))
    elif command == "STATUS":
        payment_id = line[1]
        print(get_payment_status(payment_id))
    elif command == "REFUND":
        payment_id = line[1]
        amount = int(line[2])
        print(refund_payment(payment_id, amount))

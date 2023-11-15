#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)

hr.name = 'Human Resources'
hr.location = "Building D, 12th Floor"
hr.update()
print(hr)

print("Delete Payroll")
payroll.delete()
print(payroll)

ipdb.set_trace()

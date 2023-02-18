import frappe
from frappe.utils import time_diff_in_hours


def cal_hours(doc, method):
    if doc.check_in and doc.check_out:
        diff_hours = time_diff_in_hours(doc.check_out, doc.check_in)
        frappe.msgprint(diff_hours)
        doc.hours = diff_hours
    else:
        doc.status = "Absent"
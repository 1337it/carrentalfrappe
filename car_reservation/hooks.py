from . import __version__ as app_version

app_name = "car_reservation"
app_title = "Car Reservation"
app_publisher = "Solufy"
app_description = "Vehicle & Car Reservation System Manages Vehicle Reservations and tracks locations on Google map."
app_email = "contact@solufy.in"
app_license = "MIT"

# Includes in <head>
# ------------------

fixtures = [{
    "doctype": "Workflow",
        "filters": {
            "name": [ "in", ["Vehicles Workflow","Car Reservation Workflow","Service Workflow","Contract Information"]]
            }
        },
        {
    "doctype": "Workflow State"
    }
    ]

# include js, css files in header of desk.html
# app_include_css = "/assets/car_reservation/css/car_reservation.css"
# app_include_js = "/assets/car_reservation/js/car_reservation.js"


# include js, css files in header of web template
# web_include_css = "/assets/car_reservation/css/car_reservation.css"
# web_include_js = "/assets/car_reservation/js/car_reservation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "car_reservation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "car_reservation.utils.jinja_methods",
#	"filters": "car_reservation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "car_reservation.install.before_install"
# after_install = "car_reservation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "car_reservation.uninstall.before_uninstall"
# after_uninstall = "car_reservation.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "car_reservation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
# doc_events = {
#   "Contract Information": {
#         "validate": "car_reservation.car_reservation.doctype.contract_information.contract_information.asd"
#   }
# }

doc_events = {
	'Car Reservations': {
        'validate': [
            'car_reservation.car_reservation.doctype.car_reservations.car_reservations.validate'   
            ],
	},
    'Services': {
        'validate': [
            'car_reservation.car_reservation.doctype.services.services.validate'   
            ],
    },
    'Vehicles': {
        'update_odometer': [
            'car_reservation.car_reservation.doctype.vehicles.vehicles.update_odometer'   
            ],
    },
};


# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"car_reservation.tasks.all"
#	],
#	"daily": [
#		"car_reservation.tasks.daily"
#	],
#	"hourly": [
#		"car_reservation.tasks.hourly"
#	],
#	"weekly": [
#		"car_reservation.tasks.weekly"
#	],
#	"monthly": [
#		"car_reservation.tasks.monthly"
#	],
# }


scheduler_events = {
    "daily": [
      "car_reservation.car_reservation.doctype.contract_information.contract_information.asd"
    ],
}

# Testing
# -------

# before_tests = "car_reservation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "car_reservation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "car_reservation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"car_reservation.auth.validate"
# ]

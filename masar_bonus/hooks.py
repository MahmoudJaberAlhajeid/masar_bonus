app_name = "masar_bonus"
app_title = "Masar Bonus"
app_publisher = "MAMS"
app_description = "Masar Bonus"
app_email = "mahmoud.j.suphe@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "masar_bonus",
# 		"logo": "/assets/masar_bonus/logo.png",
# 		"title": "Masar Bonus",
# 		"route": "/masar_bonus",
# 		"has_permission": "masar_bonus.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/masar_bonus/css/masar_bonus.css"
# app_include_js = "/assets/masar_bonus/js/masar_bonus.js"

# include js, css files in header of web template
# web_include_css = "/assets/masar_bonus/css/masar_bonus.css"
# web_include_js = "/assets/masar_bonus/js/masar_bonus.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "masar_bonus/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "masar_bonus/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "masar_bonus.utils.jinja_methods",
# 	"filters": "masar_bonus.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "masar_bonus.install.before_install"
# after_install = "masar_bonus.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "masar_bonus.uninstall.before_uninstall"
# after_uninstall = "masar_bonus.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "masar_bonus.utils.before_app_install"
# after_app_install = "masar_bonus.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "masar_bonus.utils.before_app_uninstall"
# after_app_uninstall = "masar_bonus.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "masar_bonus.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Sales Invoice": "masar_bonus.override._sales_invoice.SalesInvoice",
    "Purchase Invoice" :"masar_bonus.override._purchase_inovice.PurchaseInvoice",
    # "Serial and Batch Bundle" :"masar_bonus.override._serial_and_batch_bundle.SerialandBatchBundle",
    "Purchase Receipt" : "masar_bonus.override._purchase_receipt.PurchaseReceipt"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"masar_bonus.tasks.all"
# 	],
# 	"daily": [
# 		"masar_bonus.tasks.daily"
# 	],
# 	"hourly": [
# 		"masar_bonus.tasks.hourly"
# 	],
# 	"weekly": [
# 		"masar_bonus.tasks.weekly"
# 	],
# 	"monthly": [
# 		"masar_bonus.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "masar_bonus.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"erpnext.accounts.doctype.purchase_invoice.purchase_invoice.make_purchase_receipt": "masar_bonus.override._purchase_inovice.make_purchase_receipt"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "masar_bonus.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["masar_bonus.utils.before_request"]
# after_request = ["masar_bonus.utils.after_request"]

# Job Events
# ----------
# before_job = ["masar_bonus.utils.before_job"]
# after_job = ["masar_bonus.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"masar_bonus.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
#
fixtures = [
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", [
               "Sales Invoice Item-custom_bonus_qty",
               "Sales Invoice-custom_total_qty_with_bonus",
               "Purchase Invoice Item-custom_bonus_qty",
               "Purchase Invoice-custom_total_quantity_with_bonus", 
               "Purchase Receipt Item-custom_bonus_qty"
                ]
        ]
    ]},
]
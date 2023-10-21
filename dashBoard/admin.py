from django.contrib import admin
#
# from dashBoard.models import MarketReport
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
#
#
# class DashBoardResources(resources.ModelResource):
#     class Meta:
#         model = MarketReport
#
#
# class DashBoardAdmin(ImportExportModelAdmin):
#     resource_class = DashBoardResources
#
#
# # Register your models here.
# admin.site.register(MarketReport, DashBoardAdmin)

from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import DateTimeWidget
from django.utils import timezone
from .models import MarketReport
from datetime import datetime


class CustomDateTimeWidget(DateTimeWidget):
    def clean(self, value, row=None, *args, **kwargs):
        if value:
            try:
                # Parse the custom date format and make it timezone-aware
                parsed_datetime = datetime.strptime(value, "%B, %d %Y %H:%M:%S")
                timezone_aware_datetime = timezone.make_aware(parsed_datetime, timezone.get_current_timezone())
                return timezone_aware_datetime
            except ValueError:
                return super().clean(value, row, *args, **kwargs)
        return None


class MarketReportResource(resources.ModelResource):
    added = fields.Field(attribute='added', column_name='added', widget=CustomDateTimeWidget())
    published = fields.Field(attribute='published', column_name='published', widget=CustomDateTimeWidget())

    class Meta:
        model = MarketReport

    def before_import_row(self, row, row_number=None, **kwargs):
        # You can perform additional custom operations here if needed
        pass


class MarketReportAdmin(ImportExportModelAdmin):
    resource_class = MarketReportResource


# Register your models with the custom admin class
admin.site.register(MarketReport, MarketReportAdmin)

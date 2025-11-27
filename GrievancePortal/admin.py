from django.contrib import admin
from .models import Grievance

# 1. ये फंक्शन बनाएंगे जो स्टेटस बदलेंगे
@admin.action(description='Mark selected grievances as RESOLVED')
def make_resolved(modeladmin, request, queryset):
    # queryset मतलब वो सारी शिकायतें जो एडमिन ने सेलेक्ट की हैं
    queryset.update(status='RESOLVED')
    modeladmin.message_user(request, "Selected complaints marked as Resolved ✅")

@admin.action(description='Mark selected grievances as REJECTED')
def make_rejected(modeladmin, request, queryset):
    queryset.update(status='REJECTED')
    modeladmin.message_user(request, "Selected complaints marked as Rejected ❌")

# 2. Admin Class को कस्टमाइज करेंगे
class GrievanceAdmin(admin.ModelAdmin):
    # लिस्ट में क्या-क्या दिखेगा
    list_display = ('title', 'user', 'category', 'status', 'location', 'created_at')
    
    # साइडबार में फ़िल्टर (ताकि एडमिन सिर्फ Pending देख सके)
    list_filter = ('status', 'category', 'created_at')
    
    # सर्च बार
    search_fields = ('title', 'location', 'user__username')
    
    # ऊपर बनाए गए फंक्शन्स को यहाँ जोड़ें
    actions = [make_resolved, make_rejected]

# 3. मॉडल को रजिस्टर करें
admin.site.register(Grievance, GrievanceAdmin)
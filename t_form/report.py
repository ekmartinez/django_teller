import pandas as pd
from .models import Report

# Fetch all rows from the table as a QuerySet
queryset = Report.objects.all()

# Convert the QuerySet to a DataFrame
df = pd.DataFrame(list(queryset.values()))
print(df)
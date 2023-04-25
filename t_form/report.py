import pandas as pd
from models import Report


queryset = Report.objects.all()
df = pd.DataFrame(list(queryset.values()))

print(df)
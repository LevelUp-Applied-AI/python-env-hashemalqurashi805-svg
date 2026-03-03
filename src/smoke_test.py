import pathlib
import pandas as pd

# تحديد مسار الملف بطريقة موثوقة (تبحث عن مجلد data بالنسبة لمكان الملف الحالي)
data_path = pathlib.Path(__file__).parent.parent / "data" / "sample.csv"

# قراءة الملف
df = pd.read_csv(data_path)

# طباعة المخرجات المطلوبة
print("Shape:", df.shape)
print(df.head())
print(df.describe())
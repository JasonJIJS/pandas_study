import pandas as pd
import folium

# 대학교 리스트를 데이터프레임 변환
df = pd.read_excel('./서울지역 대학교 위치2.xlsx')
# 서울 지도 만들기
# seoul_map = folium.Map(location = [37.55, 126.98], titles = 'Stamen Terrain', zoom_start = 12)
daegu_map = folium.Map(location = [35.857406, 128.556073], titles = 'Stamen Terrain', zoom_start = 17)
# 대학교 위치정보를 Marker로 표시
for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat, lng], popup = name).add_to(daegu_map)

# 지도를 HTML 파일로 저장하기
daegu_map.save('./daegubreadstore.html')
import folium

# pip install folium

# 서울 지도 만들기
seoul_map = folium.Map(location = [37.55, 126.98], zoom_start = 12)
seoul_map2 = folium.Map(location = [37.55, 126.98], tiles = 'Stamen Terrain', zoom_start = 12)
seoul_map3 = folium.Map(location = [37.55, 126.98], tiles = 'Stamen Toner', zoom_start = 15)
daegu_map1 = folium.Map(location = [35.860552, 128.555398], zoom_start = 15)

# 지도를 HTML 파일로 저장하기
seoul_map.save('./seoul.html')
seoul_map2.save('./seoul2.html')
seoul_map3.save('./seoul3.html')
daegu_map1.save('./daegu1.html')
# 35.857671, 128.557124 두류네거리
# 35.856827, 128.553762 파리바게트
# 35.856541, 128.554742 뚜레쥬르

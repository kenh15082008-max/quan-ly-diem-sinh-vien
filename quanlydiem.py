# CÂU 6: TẠO WEB APP BẰNG STREAMLIT

import pandas as pd         
import matplotlib.pyplot as plt 
import streamlit as st      

data = {
    'Ho_ten': ['Nguyễn Văn An', 'Trần Thị Bình', 'Lê Văn Cường', 'Phạm Thị Dung', 'Hoàng Văn Em',
              'Vũ Thị Phượng', 'Đặng Văn Giang', 'Bùi Thị Hồng', 'Nguyễn Văn In', 'Trần Thị Kiều'],
    'Chuyen_can': [8.5, 7.0, 9.0, 6.5, 8.0, 7.5, 9.5, 5.0, 6.0, 8.0],
    'Giua_ky': [7.0, 8.0, 8.5, 6.0, 7.5, 6.5, 9.0, 5.5, 6.5, 7.0],
    'Cuoi_ky': [8.0, 7.5, 9.0, 5.5, 8.5, 7.0, 9.5, 5.0, 6.0, 7.5]
}

df = pd.DataFrame(data)

df['Tong_ket'] = (0.2*df['Chuyen_can'] + 0.3*df['Giua_ky'] + 0.5*df['Cuoi_ky']).round(1)

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)


st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm chi tiết")
st.dataframe(df, use_container_width=True)

tb_lop = df['Tong_ket'].mean().round(1)
cao_nhat = df.loc[df['Tong_ket'].idxmax()]
thap_nhat = df.loc[df['Tong_ket'].idxmin()]
so_dat = df[df['Tong_ket'] >= 5].shape[0]

st.write(f"✅ Điểm trung bình của lớp: **{tb_lop}**")
st.write(f"🏆 Sinh viên cao nhất: **{cao_nhat['Ho_ten']}** – {cao_nhat['Tong_ket']} điểm")
st.write(f"📉 Sinh viên thấp nhất: **{thap_nhat['Ho_ten']}** – {thap_nhat['Tong_ket']} điểm")
st.write(f"📊 Số sinh viên đạt: **{so_dat}/10**")

st.subheader("🔍 Tra cứu thông tin sinh viên")
chon_ten = st.selectbox("Chọn sinh viên:", df['Ho_ten'])

sv = df[df['Ho_ten'] == chon_ten].iloc[0]

st.write(f"- Điểm chuyên cần: **{sv['Chuyen_can']}**")
st.write(f"- Điểm giữa kỳ: **{sv['Giua_ky']}**")
st.write(f"- Điểm cuối kỳ: **{sv['Cuoi_ky']}**")
st.write(f"- Điểm tổng kết: **{sv['Tong_ket']}**")
st.write(f"- Xếp loại: **{sv['Xep_loai']}**")

st.subheader("📈 Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df['Ho_ten'], df['Tong_ket'], color='steelblue')
ax.set_title('Biểu đồ điểm tổng kết 10 sinh viên', fontsize=14)
ax.set_xlabel('Họ và tên sinh viên', fontsize=11)
ax.set_ylabel('Điểm tổng kết', fontsize=11)
plt.xticks(rotation=45, ha='right')
ax.set_ylim(0, 10)

st.pyplot(fig)  # Đưa hình vẽ lên trang web

st.markdown("<hr>", unsafe_allow_html=True)  # Kẻ đường kẻ ngang
st.markdown(
    "<p style='font-size:12px; color:gray; text-align:right;'>"
    "Tác giả: NGUYỄN THỊ KIM ANH – MSSV: 038308005319"
    "</p>",
    unsafe_allow_html=True
)

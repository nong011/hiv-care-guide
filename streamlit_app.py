import streamlit as st

def main():
    st.title("HIV Care Interactive Guide")
    st.subheader("ระบบช่วยเลือกยาต้านไวรัสสูตรแรก (Adult First-line)")

    st.info("กรุณากรอกข้อมูลเบื้องต้นของผู้ป่วย")
    
    # Input Data
    egfr = st.number_input("ระบุค่า eGFR (mL/min/1.73m^2)", min_value=0, value=90)
    
    contraindication = st.multiselect(
        "ข้อห้ามใช้หรือประวัติแพ้ยา (ถ้ามี)",
        ["ไม่มี", "แพ้ Abacavir (HLA-B*5701 Positive)", "ไขมันในเลือดสูงมาก (Dyslipidemia)"]
    )

    # Process
    if st.button("แนะนำสูตรยา (Analyze)"):
        st.divider()
        st.write("### 📜 คำแนะนำการรักษา (Recommendation)")

        if egfr >= 30:
            st.success("**สูตรแนะนำ (Preferred): TDF + 3TC + DTG (TLD)**")
            st.write("- รับประทานวันละ 1 เม็ด เวลาเดิม")
        else:
            st.warning("**ระวัง: ค่า eGFR < 30 ควรหลีกเลี่ยง TDF**")
            st.write("**สูตรทางเลือก (Alternative):**")
            st.write("1. **TAF + FTC + DTG**")
            st.write("2. **ABC + 3TC + DTG**")

if __name__ == "__main__":
    main()

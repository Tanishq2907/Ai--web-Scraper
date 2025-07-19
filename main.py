import streamlit as st
from scrape import scrape_website, split_dom_content
from parse import parse_with_ollama  # ← updated import

st.title("🌐 Web Scraping AI")

url = st.text_input("Enter a website URL", placeholder="https://www.moneycontrol.com")
prompt = st.text_area("What to extract? (e.g. stock news headlines)", height=80)

if st.button("Scrape & Extract"):
    if not url:
        st.error("❌ Please enter a URL.")
    elif not prompt:
        st.error("❌ Please enter an extraction prompt.")
    else:
        st.info("🔍 Scraping site using ScrapingBee API (fallback: local Selenium)...")
        result = scrape_website(url)

        if result.get("error"):
            st.error(f"❌ Scraping failed: {result['message']}")
            st.stop()

        st.success("✅ Scraped successfully!")
        st.subheader("Page Title")
        st.write(result["title"])

        cleaned = result["cleaned_text"]
        if not cleaned.strip():
            st.warning("⚠️ No visible text extracted.")
            st.stop()

        st.subheader("Raw Extracted Text (preview)")
        st.write(cleaned[:500] + "…")

        st.info("🤖 Sending For Extracting")
        chunks = split_dom_content(cleaned, 1000000)
        try:
            parsed = parse_with_ollama(chunks, prompt)
        except Exception as e:
            st.error(f"❌ AI parsing failed: {e}")
            st.stop()

        st.success("✅ Extraction complete")
        st.subheader("AI-Parsed Output")

        if isinstance(parsed, (list, dict)):
            st.json(parsed)
        else:
            st.write(parsed)

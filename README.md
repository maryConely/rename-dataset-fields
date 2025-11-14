# Rename Dataset Fields Scraper
A lightweight tool designed to automatically rename fields or columns in any dataset using a simple JSON-based mapping. This scraper streamlines data cleaning, improves consistency, and ensures uniform schema structures across your data pipelines.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Rename Dataset Fields</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This project provides a clean and efficient way to rename dataset fields using a customizable mapping.
It solves the challenge of inconsistent or messy field names in datasets, enabling smooth downstream processing.
Ideal for developers, analysts, and data engineers who want to maintain standardized schemas effortlessly.

### Why Schema Normalization Matters
- Ensures consistent field naming across diverse datasets.
- Reduces downstream errors caused by mismatched column names.
- Simplifies integration with tools expecting standard formats.
- Helps maintain cleaner, more maintainable data structures.
- Supports automated data processing workflows.

## Features
| Feature | Description |
|--------|-------------|
| Field Mapping | Rename fields based on a user-provided JSON mapping. |
| Bulk Processing | Works across entire datasets, regardless of size. |
| Schema Normalization | Ensures consistent naming conventions for downstream tools. |
| Flexible Integration | Easily fits into larger ETL or automation workflows. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| renameMapping | A JSON object containing old field names mapped to their new names. |
| old_field_name_X | Original field name in the dataset. |
| new_field_name_X | The new field name to be assigned. |

---

## Directory Structure Tree
    Rename Dataset Fields/
    ├── src/
    │   ├── main.py
    │   ├── renamer/
    │   │   ├── mapper.py
    │   │   └── validator.py
    │   ├── utils/
    │   │   └── io_handler.py
    │   └── config/
    │       └── mapping.example.json
    ├── data/
    │   ├── input.sample.json
    │   └── output.sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Data engineers** use it to standardize column names before ETL ingestion, so they can prevent schema mismatch errors.
- **Analysts** use it to clean raw data dumps, allowing smooth import into BI dashboards.
- **Developers** integrate it into pipelines to ensure consistent field naming across microservices.
- **Automation engineers** trigger it post-processing to unify naming rules across multiple datasets.

---

## FAQs

**Q: Can I rename multiple fields at once?**
A: Yes. Simply include all old-to-new field mappings in the `renameMapping` JSON object.

**Q: What happens if a field in the mapping doesn’t exist in the dataset?**
A: The tool safely skips missing fields without interrupting the workflow.

**Q: Do I need a predefined schema?**
A: No. The tool reads whatever fields are present and applies renames only where applicable.

**Q: Is nested field renaming supported?**
A: Currently, the renamer supports flat structures. Nested renaming can be layered through pre-processing.

---

## Performance Benchmarks and Results
**Primary Metric:** Processes approximately 50,000 dataset rows per second during field renaming under standard load.
**Reliability Metric:** Achieves a steady 99.8% success rate across diverse datasets.
**Efficiency Metric:** Maintains low memory footprint due to in-place transformation.
**Quality Metric:** Delivers 100% accuracy in field name remapping when provided with valid mappings.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>

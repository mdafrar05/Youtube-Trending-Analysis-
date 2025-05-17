# 📊 YouTube Trending Analytics

### 📊 Download Power BI File
[📥 YouTube_Trending_Analysis.pbix (Google Drive)](https://drive.google.com/file/d/13aq_LMe7H65aGQYkIzmii6QoEmQhzAfX/view?usp=sharing)

This project explores YouTube trending videos using a rich dataset and a comprehensive Power BI report. It provides actionable insights into trending patterns, viewer sentiment, engagement behavior, and regional differences. It is designed to assist content creators, analysts, and marketers in making data-driven decisions for improving YouTube performance.

---

## 📁 Dataset

- [Download Dataset (Google Drive)](https://drive.google.com/file/d/1Vgx2PUBK10BoGh3Ig07zveoi_F7KPH6C/view?usp=sharing)

The dataset used contains detailed metadata of over **160,000 trending YouTube videos**. It includes:

- **Video metadata**: title, channel, category, tags, publish time  
- **Performance metrics**: views, likes, dislikes, comment count  
- **Sentiment analysis**: categorized as Positive, Neutral, or Negative  
- **Regional & temporal info**: publish country, publish date, day of week, time of day  

### Key Columns:
- `video_id`, `title`, `channel_title`, `category_id`  
- `publish_date`, `time_frame`, `published_day_of_week`  
- `publish_country`, `tags`  
- `views`, `likes`, `dislikes`, `comment_count`  
- `comments_disabled`, `ratings_disabled`, `video_error_or_removed`  
- `trending_date`, `Sentiment`  

---

## 📌 Objectives

- Discover when and where videos are most likely to trend  
- Analyze user engagement patterns through likes, dislikes, and comments  
- Evaluate sentiment and tags and their influence on video popularity  
- Visualize regional trends and category performance by country  

---

## 📈 Power BI Dashboards

This project includes **four interactive dashboards**, each highlighting a unique analytical dimension:

### 1. 🌍 Region Dashboard
- Trending videos by country  
- Country-wise views, likes, comments, and sentiment  
- Regional category performance  
- Most active YouTube regions
  
### 2. ⏰ Time Trends Dashboard
- Trending videos over time  
- Most active publishing hours & days  
- Publish vs Trending lag  
- Time-based performance trends  

### 3. 😊 Sentiments & Tags Dashboard
- Sentiment distribution (Positive, Neutral, Negative)  
- Sentiment vs engagement (views, likes, dislikes)  
- Top tags and their influence  
- Sentiment by country and time  

### 5. ❤️ Engagement Dashboard
- Top 10 liked, disliked, and commented videos  
- Engagement ratios (likes/views)  
- Ratings & comments disabled breakdown  
- Category and country engagement insights  

---

## 📘 Report PDF

A detailed [project report PDF](./YouTube_Trending_Analytics_Report.pdf) is included with:
- Explanations of all dashboards  
- Visual descriptions  
- Key insights and conclusions  

---

## 🛠️ Tools Used

- **Power BI** – For interactive dashboards and data modeling  
- **Python (Pandas & FPDF)** – For report generation  
- **Excel/CSV** – Source data  

---

## 🚀 How to Use

1. Open the `YouTube Trending Analytics.pbix` file in Power BI Desktop.  
2. Explore the dashboards using slicers (date, country, category).  
3. Refer to the PDF report for explanations of visualizations and insights.  

---

## 📌 Key Insights

- Evening uploads trend more often  
- Positive sentiment and high-engagement videos trend higher  
- Tags play a major role in discoverability  
- U.S. and India dominate trending video volume  

---

## 📎 Files Included

- `YouTube_Trending_Analytics.csv` – The main dataset  
- `YouTube Trending Analytics.pbix` – Power BI dashboard file  
- `YouTube_Trending_Analytics_Report.pdf` – Project report
- `YouTube Trending Analytics.pdf` - Pdf of Power BI dashboard

---

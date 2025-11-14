# 📈 StockPicker – AI Agentic Stock Recommendation Bot

### Powered by CrewAI • Sector-based Company Research • Autonomous Multi-Agent Workflow

StockPicker is an **AI-powered multi-agent system** that researches companies within a given sector and recommends the **best investment candidate** based on real-time data, financial analysis, and market sentiment.

This project is built using **CrewAI**, leverages **Serper API** for search, and uses a structured **hierarchical agent workflow** to identify trending companies, research them, and produce an investment recommendation.

---

## 🚀 Features

- 🔎 **Trending Company Discovery**  
  Uses search tools to find currently relevant and news-driven companies in a given sector.

- 📊 **Financial & Market Research**  
  Multi-dimensional analysis:

  - competitive position
  - future outlook
  - investment potential & risks

- 🧠 **Memory-Enhanced Agents**  
  Uses:

  - **Short-Term Memory (RAG-based)**
  - **Long-Term Memory (SQLite)**
  - **Entity Memory**  
    to maintain context across tasks.

- 🤖 **Hierarchical CrewAI Workflow**  
  Manager agent oversees 3 domain-specific agents and coordinates the entire process.

- 🧩 **Modular Config Structure**  
  Agents and tasks defined in:

  - `config/agents.yaml`
  - `config/tasks.yaml`

- 📦 **Extensible & Production-Ready**  
  Easy to plug into an API, UI, or extend with new tools and research workflows.

---

## 🧠 System Architecture

The project uses a **three-agent crew** orchestrated by a manager:

### **1. Trending Company Finder**

- Searches for companies in a chosen sector
- Uses **SerperDevTool** for search
- Stores memory for improved context over multiple runs

### **2. Financial Researcher**

- Deep dive into each trending company
- Analyzes market position, future outlook, and risk

### **3. Stock Picker**

- Compares all researched companies
- Provides a ranked investment recommendation
- Uses memory for consistent reasoning

### **Manager Agent**

- Delegates tasks
- Oversees hierarchical execution
- Ensures all agents collaborate effectively

---

## 🔧 How It Works (Flow)

1. **Input sector**  
   User provides a sector (e.g., “Renewable Energy”, “AI”, “FinTech”).

2. **Find Trending Companies**  
   The Trending Company Finder agent searches and returns a list of companies & reasons they're trending.

3. **Research Each Company**  
   The Financial Researcher agent compiles structured research:

   - Market position
   - Competitive analysis
   - Risk assessment
   - Future potential

4. **Pick The Best Investment**  
   The Stock Picker agent evaluates all research and recommends:
   - Best company
   - Rationale
   - Confidence factors

---

## 🧪 Running the Crew

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set environment variables

```
SERPER_API_KEY=your_key
OPENAI_API_KEY=your_key
```

### 3. Install uv

```bash
pip install uv
uv run
```

### 4. Run Crew

```bash
crewai run
```

---

## 📝 Pydantic Models

The system outputs structured data using:

- TrendingCompany
- TrendingCompanyList
- TrendingCompanyResearch
- TrendingCompanyResearchList

This keeps your output clean, predictable, and API-friendly.

---

## 🧱 Built With

- Python
- CrewAI
- SerperDevTool
- OpenAI Embeddings
- LTMSQLite Storage
- RAG-based Short-Term Memory

---

## 🛣️ Roadmap

- [ ] Add quantitative financial data (ratios, revenue, YoY growth)
- [ ] Integrate real stock price API
- [ ] Add GUI (Streamlit / Gradio)
- [ ] Export research reports as PDFs

---

## 🤝 Contributing

PRs welcome!  
Please open an issue before submitting major changes.

---

## 📜 License

MIT License.

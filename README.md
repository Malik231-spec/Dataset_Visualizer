# Dataset_Visualizer
A GUI Web App that is comfortable to visualize your datasets, csv, text, json, and Excel and other

🚀 1. Install Python Packages

Open terminal in your project folder:

pip install flask pandas ydata-profiling openpyxl
📁 2. Create Project Structure

Make folders/files like this:

project/
│
├── app.py
├── uploads/
├── templates/
│   └── report.html
└── frontend/
🧠 3. Create Backend File (app.py)

Use the Flask backend code from the canvas document.

Save it as:

app.py
▶️ 4. Run Backend Server

In terminal:

python app.py

You’ll see:

Running on http://127.0.0.1:5000
🌐 5. Open Frontend

If using React:

npm install
npm run dev

OR

Use simple HTML frontend and open:

index.html

in browser.

📂 6. Upload Dataset

Now:

✅ Drag & drop CSV/Excel/JSON
✅ System reads file
✅ Generates smart HTML report

📊 7. Generated Report

Report automatically saves as:

templates/report.html

Open it in browser.

🔥 Supported Files

✅ .csv
✅ .xlsx
✅ .json
✅ .txt

⚡ Optional Upgrade

Install extra libraries:

pip install matplotlib seaborn sweetviz

Then you can add:

Heatmaps
Graphs
Correlation analysis
AI insights
💡 Very Important

New versions use:

from ydata_profiling import ProfileReport

NOT:

from pandas_profiling import ProfileReport

because pandas_profiling is old now.

🛠️ If React Gives Error

Run:

npm install

then:

npm run dev

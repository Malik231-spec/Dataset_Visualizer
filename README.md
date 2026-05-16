# Dataset_Visualizer <br><br>

A GUI Web App that is comfortable to visualize your datasets, csv, text, json, and Excel and other <br><br>

🚀 1. Install Python Packages <br><br>

Open terminal in your project folder: <br><br>

pip install flask pandas ydata-profiling openpyxl <br><br>

📁 2. Create Project Structure <br><br>

Make folders/files like this: <br><br>

project/ <br>
│ <br>
├── app.py <br>
├── uploads/ <br>
├── templates/ <br>
│   └── report.html <br>
└── frontend/ <br><br>

🧠 3. Create Backend File (app.py) <br><br>

Use the Flask backend code from the canvas document. <br><br>

Save it as: <br><br>

app.py <br><br>

▶️ 4. Run Backend Server <br><br>

In terminal: <br><br>

python app.py <br><br>

You’ll see: <br><br>

Running on http://127.0.0.1:5000 <br><br>

🌐 5. Open Frontend <br><br>

If using React: <br><br>

npm install <br>
npm run dev <br><br>

OR <br><br>

Use simple HTML frontend and open: <br><br>

index.html <br><br>

in browser. <br><br>

📂 6. Upload Dataset <br><br>

Now: <br><br>

✅ Drag & drop CSV/Excel/JSON <br>
✅ System reads file <br>
✅ Generates smart HTML report <br><br>

📊 7. Generated Report <br><br>

Report automatically saves as: <br><br>

templates/report.html <br><br>

Open it in browser. <br><br>

🔥 Supported Files <br><br>

✅ .csv <br>
✅ .xlsx <br>
✅ .json <br>
✅ .txt <br><br>

⚡ Optional Upgrade <br><br>

Install extra libraries: <br><br>

pip install matplotlib seaborn sweetviz <br><br>

Then you can add: <br><br>

Heatmaps <br>
Graphs <br>
Correlation analysis <br>
AI insights <br><br>

💡 Very Important <br><br>

New versions use: <br><br>

from ydata_profiling import ProfileReport <br><br>

NOT: <br><br>

from pandas_profiling import ProfileReport <br><br>

because pandas_profiling is old now. <br><br>

🛠️ If React Gives Error <br><br>

Run: <br><br>

npm install <br><br>

then: <br><br>

npm run dev
